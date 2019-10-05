package com.product_notself;

import java.math.BigInteger;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

public class ProductNotSelf {

	public static void main(String[] args) {
		System.out.println(productExceptSelf(new int[]{37, 50, 50, 6, 8, 54, 7, 64, 2, 64, 67, 59, 22, 73, 33, 53, 43, 77, 56, 76, 59, 96, 64, 100, 89, 38, 64, 73, 85, 96, 65, 50, 62, 4, 82, 57, 98, 61, 92, 55, 80, 53, 80, 55, 94, 9, 73, 89, 83, 80}
		, 67));
	}
	
	public static int productExceptSelf(int[] nums, int m) {
	    BigInteger result = new BigInteger("0");
	    BigInteger g = new BigInteger("0");
	    BigInteger[] partial = Arrays.stream(nums)
	    		.mapToObj(BigInteger::valueOf)
	    		.toArray(BigInteger[]::new);
	    for (int i = 0; i < nums.length; i++) {
//	    	Set current index to 1 which causes it to ignore that number in the multiplication
	    	partial[i] = BigInteger.valueOf(1);
	    	Optional<BigInteger> prod = Arrays.stream(partial)
	    			.reduce((num1, num2) -> num1.multiply(num2));
	    	g = g.add(prod.get());
//	    	Set it back to the original value
	    	partial[i] = BigInteger.valueOf(nums[i]);
	    }
	    result = g.mod(BigInteger.valueOf(m));
	    return result.intValue();
	} 

}
