package com.rotate_array;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

public class RotateArray {

	public static void main(String[] args) {
		int[] numbers = {1, 2, 3, 4, 5, 6, 7};
		List<Integer> numsList = Arrays.stream(numbers).boxed().collect(Collectors.toList());
		System.out.println(numsList);
		System.out.println(rotateNPositions(numsList, 5));
	}
	
	public static List<Integer> rotateNPositions(List<Integer> numbers, int n) {
		List<Integer> rotatedVersion = numbers;
		if (n < numbers.size() && n > 0) {
			for (int i = 0; i < n; i++) {
//				Remove the current number and add it to the tail of the list
				int actual = rotatedVersion.get(0);
				rotatedVersion.remove(0); rotatedVersion.add(actual);
			}
			return rotatedVersion;
		} else if(n == numbers.size() || n == 0) {
//			If the number of rotations is equal to the length of the list 
			return numbers;
		} else {
			return null;
		}
	}

}
