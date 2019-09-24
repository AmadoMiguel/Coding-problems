package com.union_intersection;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class UnionIntersection {

	public static void main(String[] args) {
		int[] arr1 = {1,2,3,5,2,7,5,9,0,6,14}; int[] arr2 = {8,10,3,6,2,7,5,9,0};
		List<Integer> l1 = Arrays.stream(arr1).boxed().collect(Collectors.toList());
		List<Integer> l2 = Arrays.stream(arr2).boxed().collect(Collectors.toList());
		System.out.println(getUnionAndIntersectionOfArrays(l1, l2));
	}
	
	public static List<List<Integer>> getUnionAndIntersectionOfArrays(List<Integer> l1, List<Integer> l2) {
		List<List<Integer>> unionAndIntersection = new ArrayList<List<Integer>>();
//		Prepare lists inside the outer list
		unionAndIntersection.add(new ArrayList<Integer>()); // Union list
		unionAndIntersection.add(new ArrayList<Integer>()); // Intersection list
//		Iterate over all the elements and add elements to each internal list
		l1.addAll(l2);
		for (Integer n: l1) {
			if (!unionAndIntersection.get(0).contains(n)) {
				unionAndIntersection.get(0).add(n);
			}
			
			if (l2.contains(n)) {
				if (!unionAndIntersection.get(1).contains(n)) {
					unionAndIntersection.get(1).add(n);
				}
			}
		}
		return unionAndIntersection;
	}

}
