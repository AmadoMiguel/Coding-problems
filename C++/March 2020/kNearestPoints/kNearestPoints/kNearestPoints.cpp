// kNearestPoints.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <time.h>
#include <iostream>
#include <vector>

using namespace std;

struct point {
	float x, y;
};

float calculateDistance(point &p1, point &p2) {
	return sqrt(pow(p2.x - p1.x, 2) + pow(p2.y - p1.y, 2));
}

int comparePoints(point &ref, point &p1, point &p2) {
	if (calculateDistance(ref, p1) < calculateDistance(ref, p2)) return -1;
	if (calculateDistance(ref, p1) > calculateDistance(ref, p2)) return 1;
	return 0;
}

void showPoints(vector<point> &points, point &ref) {
	for (point &p : points) {
		cout << "{" << p.x << ", " << p.y << "}, ";
		cout << "Distance to reference point: " << calculateDistance(p, ref) << endl;
		cout << endl;
	}
}

void swapPoints(point &p1, point &p2) {
	point temp = p1;
	p1 = p2;
	p2 = temp;
}

void bubbleDown(int fromIndex, point newPoint, vector<point> &points) {
	for (int i = points.size() - 1; i > fromIndex; i--) {
		swapPoints(points[i], points[i-1]);
	}
	points[fromIndex] = newPoint;
}

void insertPoint(point &newPoint, point &refPoint, vector<point> &points) {
	// Only insert new point if is closer to reference point than any of the already
	// stored points
	for (int i = 0; i < points.size(); i++) {
		if (comparePoints(refPoint, newPoint, points[i]) == -1) {
			if (points[i].x == LONG_MAX && points[i].y == LONG_MAX) {
				points[i] = newPoint;
			}
			else {
				bubbleDown(i, newPoint, points);
			}
			return;
		}
	}
	
}

vector<point> findKClosestPoints(vector<point> &pts, point &p, int k) {
	vector<point> closestPoints(k);
	// Initialize closest points vector
	for (int i = 0; i < closestPoints.size(); i++) {
		closestPoints[i].x = LONG_MAX;
		closestPoints[i].y = LONG_MAX;
	}

	for (point pt : pts) {
		insertPoint(pt, p, closestPoints);
	}

	return closestPoints;
}

int main()
{
	srand(time(NULL));

	int numPoints = 30;
	vector<point> allPoints(numPoints);
	point refPoint;
	refPoint.x = rand() % numPoints - 5;
	refPoint.y = rand() % numPoints - 5;

	point p;
	for (int i = 0; i < numPoints; i++) {
		p.x = rand() % numPoints - 5;
		p.y = rand() % numPoints - 5;
		allPoints[i] = p;
	}

	cout << "----------------All Points---------------" << endl;
	showPoints(allPoints, refPoint);
	int k = 5;
	vector<point> closePoints = findKClosestPoints(allPoints, refPoint, k);
	cout << "----------------Closest points-----------" << endl;
	cout << "Reference point " << refPoint.x << ", " << refPoint.y << endl;
	showPoints(closePoints, refPoint);
}
