package com.repeated_in_string;

import java.util.HashMap;
import java.util.Map;

public class DuplicatesInString {

	public static void main(String[] args) {
		System.out.println(charactersInString("Better Butter"));
	}
	
	public static Map<String, Integer> charactersInString(String str) {
//		Get characters of string without white spaces
		String[] charsOfString = str.split("");
//		Create the map which will act as the histogram of string characters
		Map<String, Integer> charsHistogram = new HashMap<String, Integer>();
//		Iterate over the characters and start adding to the map
		for (String s : charsOfString) {
			if (charsHistogram.containsKey(s)) {
				int nOfTimes = charsHistogram.get(s);
				nOfTimes += 1;
				charsHistogram.put(s, nOfTimes);
			} else {
				charsHistogram.put(s, 1);
			}
		}
		return charsHistogram;
	}

}
