package com.string_rotations;

import java.util.Arrays;
import java.util.List;

public class RotationOfStringThread extends Thread {
	
	@Override
	public void run() {
		System.out.println(isRotationOfString( "JavaJ2eeStrutsHibernate","HibernateJavaJ2eeStruts"));
	}
	
	public static synchronized boolean isRotationOfString(String str1, String str2) {
//		Since each string is in pascal case, split each string in words by capital letters
//		The ?= symbols make it possible to include the capital letters		
		List<String> wordsOfFirstString = Arrays.asList(str1.split("(?=[A-Z])"));
		List<String> wordsOfSecondString = Arrays.asList(str2.split("(?=[A-Z])"));
		try {
//			Sleep this thread 300 ms in order to practice the join() method in the main file
			Thread.sleep(300);
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
		return wordsOfSecondString.containsAll(wordsOfFirstString);
	}
}
