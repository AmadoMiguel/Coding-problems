package com.bishops_attack;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class BishopsAttack {

	public static void main(String[] args) {
//		Create a list of bishop points
		List<List<Integer>> allBishops = new ArrayList<List<Integer>>();
		int[] b1Arr = {0,0}; int[] b2Arr = {1,2};
		int[] b3Arr = {2,2}; int[] b4Arr = {4,0};
		List<Integer> bishop1 = Arrays.stream(b1Arr).boxed().collect(Collectors.toList());
		List<Integer> bishop2 = Arrays.stream(b2Arr).boxed().collect(Collectors.toList());
		List<Integer> bishop3 = Arrays.stream(b3Arr).boxed().collect(Collectors.toList());
		List<Integer> bishop4 = Arrays.stream(b4Arr).boxed().collect(Collectors.toList());
		allBishops.add(bishop1); allBishops.add(bishop2); 
		allBishops.add(bishop3); allBishops.add(bishop4);
		System.out.println(numberOfBishopsAttacking(allBishops, 5));
	}
//	Conditions to find out that two points share the same diagonal in a 2D matrix
//	1. x1 == y1 && x2 == y2
//	2. x1 + y1 == M - 1 && x2 + y2 == M -1
//	3.  (x1 != y1 && x2 != y2) && ...
//		3.1 (x1 + y1 == x2 + y2)
//		3.2 (x1 + y1 % 2 == 0 && x2 + y2 % 2 == 0)
//		3.3 (x1 + y1 % 2 != 0 && x2 + y2 % 2 != 0)
	public static String numberOfBishopsAttacking(List<List<Integer>> bishops, int M) {
//		Iterate over the bishops location
		int indexOfCurrentBishop = 0;
		int numberOfBishopsAttacking = 0;
		while (indexOfCurrentBishop < bishops.size() - 1) {
			List<Integer> currBishop = bishops.get(indexOfCurrentBishop);
			for (List<Integer> b: bishops.subList(indexOfCurrentBishop+1, bishops.size())) {
//				Main diagonal
				if (currBishop.get(0) == currBishop.get(1) &&
						b.get(0) == b.get(1)) {
					numberOfBishopsAttacking += 1;
				}
//				Second main diagonal
				else if (currBishop.get(0) + currBishop.get(1) == M - 1 &&
						b.get(0) + b.get(1) == M - 1) {
					numberOfBishopsAttacking += 1;
//					Other diagonals
				} else if (currBishop.get(0) != currBishop.get(1) &&
						b.get(0) != b.get(1)) {
					if (currBishop.get(0)+currBishop.get(1)==b.get(0)+b.get(1)) {
						numberOfBishopsAttacking += 1;
					} else if (((currBishop.get(0)+currBishop.get(1))%2==0) &&
							((b.get(0)+b.get(1))%2==0)) {
						numberOfBishopsAttacking += 1;
					} else if (((currBishop.get(0)+currBishop.get(1))%2!=0) &&
							((b.get(0)+b.get(1))%2!=0)) {
						numberOfBishopsAttacking += 1;
					}
				}
			}
			indexOfCurrentBishop += 1;
		}
		return "Number of attacks between bishops: "+numberOfBishopsAttacking;
	}
}
