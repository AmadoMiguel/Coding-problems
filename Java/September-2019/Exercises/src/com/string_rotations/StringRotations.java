package com.string_rotations;

import java.util.Arrays;
import java.util.List;

public class StringRotations {

	public static void main(String[] args) {
		boolean result = isRotationOfString( "JavaJ2eeStrutsHibernate","HibernateJavaJ2eeStruts");
		System.out.println(result);
		String reversedWords = reverseWords("Java Concept Of The Day");
		System.out.println(reversedWords);
	}
	
	public static boolean isRotationOfString(String str1, String str2) {
//		Since each string is in pascal case, split each string in words by capital letters
//		The ?= symbols make it possible to include the capital letters		
		List<String> wordsOfFirstString = Arrays.asList(str1.split("(?=[A-Z])"));
		List<String> wordsOfSecondString = Arrays.asList(str2.split("(?=[A-Z])"));
		return wordsOfSecondString.containsAll(wordsOfFirstString);
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
			if (w == words.get(words.size()-1)) {
				reversedWords += " ";
			}
		}
		return reversedWords;
	}

}
