package com.roman_equivalent;

import java.util.ArrayList;
import java.util.List;

public class RomanNumberEquivalent {

	public static void main(String[] args) {
		System.out.println(getRomanRepresentationOfNum(145));
	}
	
	public static String getRomanRepresentationOfNum(int num) {
		String romanNumber = "";
		String[] romans = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
		int[] numbersOfRomans = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
		int currentIndexRoman = 0;
		while (num > 0) {
			if (num >= numbersOfRomans[currentIndexRoman]) {
				num -= numbersOfRomans[currentIndexRoman];
				romanNumber += romans[currentIndexRoman];
			} else {
				currentIndexRoman += 1;
			}
		}
		return romanNumber;
	}

}
