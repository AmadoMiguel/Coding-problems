package com.fibonacci_series;

import java.util.ArrayList;
import java.util.List;

public class FibonacciSeries {

	public static void main(String[] args) {
		System.out.println(fibonacciSeriesUntilNum(4));
	}
	
//	How is the fibonacci series?
//	0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
//	Starts at zero and keeps adding the current one and the previous one
	public static String fibonacciSeriesUntilNum(int num) {
		int previousNum = 0;
		int currentNum = 1;
		int sumOfNums = 0;
		List<Integer> fiboSeries = new ArrayList<Integer>();
		fiboSeries.add(previousNum);
		fiboSeries.add(currentNum);
		while (sumOfNums <= num) {
//			Careful with the order of the procedures
			fiboSeries.add(sumOfNums);
			sumOfNums = previousNum + currentNum;
			previousNum = currentNum;
			currentNum = sumOfNums;
		}
		if (fiboSeries.contains(num)) {
			return "The number "+num+" is part of the Fibonacci series";
		} else {
			return "The number "+num+" is not part of the Fibonacci series";
		}
	}

}
