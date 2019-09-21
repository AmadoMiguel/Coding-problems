package com.string_rotations;

import java.util.Arrays;
import java.util.List;

public class ReverseWordsThread extends Thread {
	@Override
	public void run() {
		System.out.println(reverseWords("Java Concept Of The Day"));
	}
	
	public static String reverseWords(String str) {
		List<String> words = Arrays.asList(str.split(" "));
		String reversedWords = "";
//		Iterate over each word
		for (String w : words) {
//			Reverse the string using string builder
			StringBuilder sb = new StringBuilder(w);
			String reversedWord = sb.reverse().toString();
			List<String> letters = Arrays.asList(reversedWord.split(""));
//			Start inverting it
			for (String l : letters) {
				reversedWords += l;
			}
			if (w != words.get(words.size()-1)) {
				reversedWords += " ";
			}
		}
		return reversedWords;
	}
	
}
