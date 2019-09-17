package com.shortest_substring;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ShortestSubstringInString {

	public static void main(String[] args) {
		List<String> shortestSubstring = shortestSubstringInString("armariakhuoheasilo",
				Arrays.asList("aio".split("")), new ArrayList<List<String>>(), 0);
		System.out.println(shortestSubstring);
	}
	
	public static List<String> shortestSubstringInString(String str, List<String> chars,
			List<List<String>> allSubstringsWithChars, int index) {
//		Create new list that is supposed to contain the substring with chars
		List<String> subStr = new ArrayList<String>();
//		Define array of the string from the current index
		List<String> charsFromString = Arrays.asList(str.split("")).subList(index, str.length());
//		Iterate over the str as array
		if (index < str.length()-chars.size()) {
			for (String l : charsFromString) {
				subStr.add(l);
				if (subStr.containsAll(chars)) {
					allSubstringsWithChars.add(subStr);
					break;
				}
			}
			shortestSubstringInString(str, chars, allSubstringsWithChars, index + 1);
		}
//		Find the shortest substring
		if (allSubstringsWithChars.size() > 0) {
			int lengthOfShortest = -1;
			List<String> shortest = new ArrayList<String>();
			for (List<String> subString : allSubstringsWithChars) {
				if ((subString.size() < shortest.size()) || lengthOfShortest == -1) {
					shortest = subString;
					lengthOfShortest = shortest.size();
				}
			}
			return shortest;
		} else {
			subStr.clear();
			return subStr;
		}
	}

}
