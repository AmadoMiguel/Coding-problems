package com.reverse_with_spaces;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ReverseStringWithSpaces {

	public static void main(String[] args) {
		System.out.println("I Am Not String");
		System.out.println(reversedStringWithSpaces("I Am Not String"));
	}
	
	public static String reversedStringWithSpaces(String str) {
//		Get the chars and reverse them in order
		List<String> chars = Arrays.asList(str.split(""));
		List<String> reversed = new ArrayList<String>();
//		Get reversed strings skipping spaces
		int currentIndex = 0;
		for (int i = chars.size() - 1; i >= 0; i--) {
			if (chars.get(currentIndex).equals(" ")) {
				reversed.add(" ");
			} 
			if (!chars.get(i).equals(" ")) {
				reversed.add(chars.get(i));
			}
			currentIndex += 1;
		}
		String reversedWithSpaces = "";
		for (String s : reversed) {
			reversedWithSpaces += s;
		}
		return reversedWithSpaces;
	}
}
