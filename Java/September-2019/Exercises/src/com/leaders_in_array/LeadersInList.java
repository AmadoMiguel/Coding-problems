package com.leaders_in_array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class LeadersInList {

	public static void main(String[] args) {
		int[] numsArray = {14, 9, 11, 7, 8, 5, 3, 6, 7, 3, 8, 9};
		List<Integer> nums = Arrays.stream(numsArray).boxed().collect(Collectors.toList());
		System.out.println(findLeadersInList(nums, 0, new ArrayList<Integer>()));
	}
	
	public static List<Integer> findLeadersInList(List<Integer> numsList, int index,
			List<Integer> leadersList) {
		boolean currentNumIsLeader = true;
		int currentNum = numsList.get(index);
		if (index < numsList.size() - 1) {
			for (int n : numsList.subList(index + 1, numsList.size())) {
				if (currentNum > n) {
					continue;
				} else {
					currentNumIsLeader = false;
					break;
				}
			}
			if (currentNumIsLeader) {
				leadersList.add(currentNum);
			}
			findLeadersInList(numsList, index + 1, leadersList);
		}
		return leadersList;
	}

}
