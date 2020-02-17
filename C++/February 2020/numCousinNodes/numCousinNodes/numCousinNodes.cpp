// numCousinNodes.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct Node {
	int value;
	Node *left, *right;
};

int getNumberOfCousins(Node *& root, int nodeVal) {
	// Base cases
	if (root->value == nodeVal)
		return 0;
	if (root == nullptr)
		return 0;

	int numCousins = 0;
	// Used to track the level at which the searched node is in the tree
	int nodeLevel = -1;

	queue<Node*> nodes;
	queue<int> levels;
	nodes.push(root);
	levels.push(0);
	while (!nodes.empty()) {
		Node* currNode = nodes.front();
		int currLevel = levels.front();
		nodes.pop();
		levels.pop();
		if (currNode != nullptr) {
			if (nodeLevel != -1) {
				if (currLevel == nodeLevel && currNode->value != nodeVal) {
					//cout << currNode->value << endl;
					numCousins += 1;
				}
			}

			if (currNode->left != nullptr) {
				if (currNode->left->value == nodeVal && nodeLevel == -1) {
					nodeLevel = currLevel + 1;
				}

				levels.push(currLevel + 1);
				nodes.push(currNode->left);
			}
			if (currNode->right != nullptr) {
				if (currNode->right->value == nodeVal && nodeLevel == -1) {
					nodeLevel = currLevel + 1;
				}

				levels.push(currLevel + 1);
				nodes.push(currNode->right);
			}
		}
	}
	if (numCousins == 0)
		return 0;
	return numCousins;
}

int main()
{
	Node* root = new Node;
	root->value = 1;
	root->left = new Node;
	root->left->value = 2;
	root->left->left = new Node;
	root->left->left->value = 4;
	root->left->left->left = nullptr;
	root->left->left->right = nullptr;
	root->left->right = new Node;
	root->left->right->value = 6;
	root->left->right->left = nullptr;
	root->left->right->right = nullptr;

	root->right = new Node;
	root->right->value = 3;
	root->right->left = nullptr;
	root->right->right = new Node;
	root->right->right->value = 5;
	root->right->right->left = nullptr;
	root->right->right->right = nullptr;

	cout << getNumberOfCousins(root, 5);
}

