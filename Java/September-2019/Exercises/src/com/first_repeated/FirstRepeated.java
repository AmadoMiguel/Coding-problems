package com.first_repeated;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class FirstRepeated {

	public static void main(String[] args) {
		System.out.println(firstRepAndNoRepLetters("JavaConceptOfTheDay"));
	}
	
	public static Map<String, String> firstRepAndNoRepLetters(String str) {
		List<String> letters = Arrays.asList(str.split(""));
		int currentIndex = 0;
		Map<String, String> firstRepAndFirstNoRep = new HashMap<String, String>();
		for (String l : letters) {
			if (letters.subList(currentIndex + 1, letters.size()).contains(l)) {
				if (!firstRepAndFirstNoRep.containsKey("First repeated letter")) {
					firstRepAndFirstNoRep.put("First repeated letter", l);
				}
			}
			if (!letters.subList(currentIndex + 1, letters.size()).contains(l)) {
				if (!firstRepAndFirstNoRep.containsKey("First not repeated letter")) {
					firstRepAndFirstNoRep.put("First not repeated letter", l);
				}
			}
//			If both of the letters were found, stop iterating over the letters
			if (firstRepAndFirstNoRep.size() == 2) {
				break;
			}
			currentIndex += 1;
		}
		return firstRepAndFirstNoRep;
	}

}
