package com.percentage_of_symbols;

import java.util.Arrays;
import java.util.List;

public class PercentageOfSymbols {

	public static void main(String[] args) {
		System.out.println(findPercentagesOfSymbols("Hello!% 1 I @ 3 am Miguel*"));
	}
	
	public static String findPercentagesOfSymbols(String str) {
//		Prepare the string that will contain the percentages information
		String info = "";
//		Convert the string into list
		List<String> symbols = Arrays.asList(str.split(""));
//		# of uppercases
		int upperCases = 0;
//		# of lowercases
		int lowerCases = 0;
//		# of digits
		int digits = 0;
//		# of other characters
		int otherChars = 0;
//		Recollect information using regex
		for (String s : symbols) {
			if (s.matches("[A-Z]")) {
				upperCases += 1;
			} else if (s.matches("[a-z]")) {
				lowerCases += 1;
			} else if (s.matches("[0-9]")) {
				digits += 1;
			} else {
				otherChars += 1;
			}
		}
//		Get length of string
		int totalLength = str.length();
//		Percentage of uppercases
		double perUpp = (upperCases * 100) / totalLength;
//		Percentage of lowercases
		double perLow = (lowerCases * 100) / totalLength;
//		Percentage of digits
		double perDig = (digits * 100) / totalLength;
//		Percentage of other characters
		double perOther = (otherChars * 100) / totalLength;
		info += "Percentage of upper case words: "+perUpp+"\n";
		info += "Percentage of lower case words: "+perLow+"\n";
		info += "Percentage of digits: "+perDig+"\n";
		info += "Percentage of other characters: "+perOther+"\n";
		return info;
	}

}
