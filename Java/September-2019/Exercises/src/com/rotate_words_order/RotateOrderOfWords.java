package com.rotate_words_order;

import java.util.Arrays;
import java.util.List;

public class RotateOrderOfWords {

	public static void main(String[] args) {
		System.out.println(wordsReversed("Java Concept Of The Day"));
	}
	
	public static String wordsReversed(String separatedWords) {
//		Initialize sb
		StringBuilder withWordsReversed = new StringBuilder("");
//		Convert str into array of words
		List<String> words = Arrays.asList(separatedWords.split(" "));
//		Start iterating words in reverse and append them to the sb
		for (int i = words.size()-1; i >= 0; i--) {
			withWordsReversed.append(words.get(i));
			if (i > 0) {
				withWordsReversed.append(" ");
			}
		}
		return withWordsReversed.toString();
	}

}
