package com.goldbach_conjecture;

import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GoldbachConjecture {
	public static void main(String[] args) {
		Map<Integer, List<Integer>> primesSumNum = primesThatSumEvenNumber(20); 
		System.out.println(primesSumNum);
	}
	
	public static Map<Integer, List<Integer>> primesThatSumEvenNumber(int num) {
//		Get primes number from 1 to num
		List<Integer> primes = primeNumbers(num);
		Map<Integer, List<Integer>> solutions = new HashMap<Integer, List<Integer>>();
		int numOfSolution = 0;
//		Start iterating over the list of primes
		for(Integer n : primes) {
			if (primes.contains(num - n)) {
//				Add the solution to the list
				numOfSolution += 1;
				List<Integer> solution = new ArrayList<Integer>();
				solution.add(n);
				solution.add(num - n);
				Collections.sort(solution);
				if (!solutions.containsValue(solution)) {
					solutions.put(numOfSolution, solution);
				}
			}
		}
		return solutions;
	}
	
	public static List<Integer> primeNumbers(int num) {
//		Iterate from 2 to num to get prime numbers
		List<Integer> primes = new ArrayList<Integer>();
		primes.add(1);
		primes.add(2);
		for (int i = 3; i <= num; i++) {
			if (isPrime(i)) {
				primes.add(i);
			}
		}
		return primes;
	}
	
	public static boolean isPrime(int num) {
		boolean isPrime = true;
		for (int i = 2; i < num; i++) {
			if (num % i == 0) {
				isPrime = false;
				break;
			}
			else {
				continue;
			}
		}
		return isPrime;
	}
}
