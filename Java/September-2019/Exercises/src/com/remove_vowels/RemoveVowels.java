package com.remove_vowels;

public class RemoveVowels {

	public static void main(String[] args) {
		System.out.println(withoutVowels("Hello world"));
	}
	
	public static String withoutVowels(String str) {
		return str.replaceAll("[a,e,i,o,u]", "_");
	}

}
