package com.separate_zeros;

import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class SeparateZeros {

	public static void main(String[] args) {
		int[] numsArray = {4, 0, 7, 0, 9, 13, 0, 12};
		List<Integer> listOfNums = Arrays.stream(numsArray).boxed().collect(Collectors.toList());
		System.out.println(listWithSeparatedZeros(listOfNums,0));
	}
//	For this exercise, recursion is used to avoid exception 
	public static List<Integer> listWithSeparatedZeros(List<Integer> numsList, int index) {
		if (index < numsList.size() - 1) {
//			If a zero is found, remove it from its position and add it to the end of the list
			if (numsList.get(index).equals(0)) {
				int zero = numsList.remove(index);
				numsList.add(zero);
			}
			listWithSeparatedZeros(numsList, index + 1);
		}
		return numsList;
	}

}
