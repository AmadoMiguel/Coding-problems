package com.anagram_strings;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class AnagramStrings {

	public static void main(String[] args) {
		System.out.println(checkAnagramStrings("Mother In Law","Hitler Woman"));
	}
	
	public static boolean checkAnagramStrings(String str1, String str2) {
//		Remove white spaces
		String s1 = str1.replaceAll("\\s+","").toLowerCase();
		String s2 = str2.replaceAll("\\s+", "").toLowerCase();
//		Transform each string into a list with each character on them
		List<String> str1Chars = Arrays.asList(s1.split(""));
		List<String> str2Chars = Arrays.asList(s2.split(""));
//		Sort each list of characters
		Collections.sort(str1Chars);
		Collections.sort(str2Chars);
//		Check if lists are equivalent
		System.out.println(str1Chars);
		System.out.println(str2Chars);
		if (str1Chars.equals(str2Chars)) {
			return true;
		} else {
			return false;
		}
	}

}
