package com.pairs_sum_num;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class PairsThatSumNum {

	public static void main(String[] args) {
		int[] numsArray = {4, 5, 7, 11, 9, 13, 8, 12};
		List<Integer> listOfNums = Arrays.stream(numsArray).boxed().collect(Collectors.toList());
		List<List<Integer>> allPairs = findPairsThatSumNum(listOfNums, 20, 0, 
				new ArrayList<List<Integer>>());
		System.out.println(allPairs);
	}
	
	public static List<List<Integer>> findPairsThatSumNum(List<Integer> numsList, int num, int index, 
			List<List<Integer>> pairsOfNums) {
		List<Integer> currentPair = new ArrayList<Integer>();
		if (index < numsList.size() - 1) {
//			Iterate over the list to start finding pairs
			for (int n : numsList.subList(index, numsList.size())) {
				if (currentPair.size() == 0) {
//					Add the current number to the pair
					currentPair.add(n);
				} else if (n + currentPair.get(0) == num) {
//					Replace the last number of the pair in order to accept repeated numbers in list
					if (currentPair.size() == 1) {
						currentPair.add(n);
					} else {
						currentPair.set(1, n);
					}
					pairsOfNums.add(currentPair);
				}
			}
			findPairsThatSumNum(numsList, num, index + 1, pairsOfNums);
		}
		return pairsOfNums;
	}

}
