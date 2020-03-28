package com.largest_no_digit;

import java.util.Arrays;
import java.util.List;

public class LargestNumWithoutDigit {

	public static void main(String[] args) {
		System.out.println(largestNumNoDigit(22222,2));
	}
	
	public static int largestNumNoDigit(int num, int digit) {
////		Convert number to string and turn it into an array
//		List<String> numAsString = Arrays.asList(String.valueOf(num).split(""));
////		Substract 1 on each digit of num that is equal to the digit parameter
//		for (String d : numAsString) {
//			if (d.equals(String.valueOf(digit))) {
//				int index = numAsString.indexOf(d);
//				int digitInNum = Integer.valueOf(d);
//				digitInNum -= 1;
//				numAsString.set(index, String.valueOf(digitInNum));
//				System.out.println(numAsString);
//			}
//		}
//		String numString = String.join("", numAsString);
//		int n = Integer.valueOf(numString);
		for (int i = num; i > 0; i--) {
//			If the digit is not in the number, return the current i value
			if (String.valueOf(i).indexOf(String.valueOf(digit)) == -1) {
				return i;
			}
		}
		return -1;
	}

}
