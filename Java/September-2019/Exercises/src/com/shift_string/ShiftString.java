package com.shift_string;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ShiftString {

	public static void main(String[] args) {
		System.out.println(checkShiftString("abcde","cdeab"));
	}
	
	public static boolean checkShiftString(String str1, String str2) {
		boolean isShiftedString = false;
//		Convert each string into list of strings
		List<String> str1Letts = Arrays.asList(str1.split(""));
		List<String> str1LettsCopy = new ArrayList<String>(str1Letts);
		List<String> str2Letts = Arrays.asList(str2.split(""));
//		Iterate over the string, remove element on each index and add it to the end of the list
		for (int i = 0; i < str1Letts.size(); i++) {
			String firstElem = str1Letts.get(i);
			str1LettsCopy.remove(0);
			str1LettsCopy.add(firstElem);
			if (str1LettsCopy.equals(str2Letts)) {
				isShiftedString = true;
				break;
			}
		}
		return isShiftedString;
	}

}
