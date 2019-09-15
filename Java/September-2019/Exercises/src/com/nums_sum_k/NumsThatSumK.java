package com.nums_sum_k;

import java.util.ArrayList;
import java.util.List;

public class NumsThatSumK {

	public static void main(String[] args) {
		List<Integer> numsList = new ArrayList<Integer>();
		numsList.add(1); numsList.add(2); numsList.add(3); numsList.add(4);
		numsList.add(5); numsList.add(6);
		List<List<Integer>> listOfOptionsThatSumK = findContiguousNums(numsList, 9, 0, 
																	 new ArrayList<List<Integer>>());
		System.out.println(listOfOptionsThatSumK);
	}
	
	public static List<List<Integer>> findContiguousNums(List<Integer> listOfNums, 
														 int K, int currentIndx,
														 List<List<Integer>> numsThatSumK) {
//		Create the list that is going to store every time the numbers that sum K
		List<Integer> contiguousNumsThatSumK = new ArrayList<Integer>();
//		Iterate over the list from the current index to the end of the list
		int currentSum = 0;
		if (currentIndx < listOfNums.size()) {
			for(Integer n : listOfNums.subList(currentIndx, listOfNums.size())) {
//				Add n to the sum of the traversed numbers
				currentSum += n;
				if (currentSum > K) {
					findContiguousNums(listOfNums, K, currentIndx + 1, numsThatSumK);
				} else if (currentSum < K) {
					contiguousNumsThatSumK.add(n);
				}
//				Add the list of contiguous numbers in case they sum to K
				if (currentSum == K) {
					contiguousNumsThatSumK.add(n);
					if (!numsThatSumK.contains(contiguousNumsThatSumK)) {
						numsThatSumK.add(contiguousNumsThatSumK);
					}
					findContiguousNums(listOfNums, K, currentIndx + 1, numsThatSumK);
				}
			}
		}
		return numsThatSumK;
	}

}
