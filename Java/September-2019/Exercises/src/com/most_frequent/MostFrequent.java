package com.most_frequent;

import java.util.Collections;
import java.util.HashMap;
import java.util.Map;

public class MostFrequent {

	public static void main(String[] args) {
		int[] nums = {1,2,2,3,3,4,5,6,6,6,6,2,7,3,7,5};
		System.out.println(mostFrequentNumber(nums));
	}
	
	public static String mostFrequentNumber(int[] nums) {
		int mostRepeated = 0;
		Map<Integer, Integer> histogram = new HashMap<Integer, Integer>();
//		Iterate over the numbers
		for (int i = 0; i < nums.length; i++) {
			if (!histogram.containsKey(nums[i])) {
				histogram.put(nums[i], 1);
			} else {
				int numOfTimes = histogram.get(nums[i]);
				numOfTimes += 1;
				histogram.put(nums[i], numOfTimes);
			}
		}
		int maxNumOfTimes = Collections.max(histogram.values());
		for (Integer k:histogram.keySet()) {
			if (histogram.get(k) == maxNumOfTimes) {
				mostRepeated = k;
				break;
			}
		}
		return "The most repeated number is: "+mostRepeated;
	}

}
