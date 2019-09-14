package com.armstrong_number;

public class ArmstrongNumber {

	public static void main(String[] args) {
		String result = isArmstrongNumber(153);
		System.out.println(result);
	}
	
	public static String isArmstrongNumber(int num) {
//		Convert the number to string
		String numAsString = String.valueOf(num);
//		Split the number and pass it to an array
		String[] digitsAsString = numAsString.split("");
//		Iterate over each digit and check if the sum of the cube of each one
//		is equal to the number
		int sumOfCubes = 0;
		for (String d : digitsAsString) {
			int digit = Integer.valueOf(d);
			sumOfCubes += Math.pow((double) digit, 3);
		}
		if (sumOfCubes == num) {
			return num+" is an Armstrong number";
		} else {
			return num+" is not an Armstrong number";
		}
	}

}
