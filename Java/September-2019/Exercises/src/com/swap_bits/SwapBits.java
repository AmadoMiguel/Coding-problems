package com.swap_bits;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SwapBits {

	public static void main(String[] args) {
		System.out.println(swapOddEvenBits("10101010"));
	}
	
	public static List<String> swapOddEvenBits(String bitStream) {
		List<String> stream = Arrays.asList(bitStream.split(""));
		List<String> swappedStream = new ArrayList<String>();
		for (int i = 0; i <= stream.size()-2; i += 2) {
			String current = stream.get(i);
			swappedStream.add(stream.get(i+1));
			swappedStream.add(current);
		}
		return swappedStream;
	}

}
