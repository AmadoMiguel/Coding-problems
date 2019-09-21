package com.string_rotations;

public class StringRotations {

	public static void main(String[] args) {
//		Create a thread for the first example (verify rotation of first string)
		RotationOfStringThread rotationThread1 = new RotationOfStringThread();
		RotationOfStringThread rotationThread2 = new RotationOfStringThread();
//		Create a thread for the second example (reverse words of string)
		ReverseWordsThread reverseThread = new ReverseWordsThread();
		
//		Begin threads
		rotationThread1.start();
		try {
//			Wait for rotation threads to finish before going to the reverse thread
			rotationThread1.join();
			rotationThread2.start();
			rotationThread2.join();
			reverseThread.start();
		} catch (InterruptedException e) {
			e.printStackTrace();
		}
	}

}
