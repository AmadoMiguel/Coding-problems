package com.cont_sub_array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class ContinuousSubArray {

	public static void main(String[] args) {
		int[] numsArray = {12, 5, 31, 9, 21, 8};
		List<Integer> listOfNums = Arrays.stream(numsArray).boxed().collect(Collectors.toList());
		System.out.println(findContinuousSubArrayThatSumNum(listOfNums, 45, 0));
	}
	
	public static List<Integer> findContinuousSubArrayThatSumNum(List<Integer> nums, 
			int num, int index) {
//		Create new list to store the numbers that will add to num
		List<Integer> subList = new ArrayList<Integer>();
		int sumTotal = 0;
		boolean subListFound = false;
//		Iterate over the list of numbers
		if (index < nums.size() - 1) {
			for (int n : nums.subList(index, nums.size())) {
				sumTotal += n;
				System.out.println(sumTotal);
				if (sumTotal < num) {
					subList.add(n);
				} 
				if (sumTotal == num) {
					subList.add(n);
					subListFound = true;
					break;
				} 
				if (sumTotal > num) {
					break;
				}
			}
			if (!subListFound) {
				findContinuousSubArrayThatSumNum(nums, num, index + 1);
			}
		}
		return subList;
	}

}
