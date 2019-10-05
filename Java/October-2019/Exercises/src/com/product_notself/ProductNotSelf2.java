package com.product_notself;

import java.math.BigInteger;

public class ProductNotSelf2 {

	public static void main(String[] args) {
		System.out.println(productExceptSelf(new int[]{37, 50, 50, 6, 8, 54, 7, 64, 2, 64, 67, 59, 22, 73, 33, 53, 43, 77, 56, 76, 59, 96, 64, 100, 89, 38, 64, 73, 85, 96, 65, 50, 62, 4, 82, 57, 98, 61, 92, 1, 80, 53, 80, 55, 94, 9, 73, 89, 83, 80}
		, 67));
	}
	
	public static int productExceptSelf(int[] nums, int m) {
		BigInteger result = new BigInteger("0");
		BigInteger g = new BigInteger("0");
		
	    BigInteger prodCumLR = new BigInteger("1");
	    BigInteger[] runProdLR = new BigInteger[nums.length];
	    BigInteger prodCumRL = new BigInteger("1");
	    BigInteger[] runProdRL = new BigInteger[nums.length];
	    int indexBeg = 0;
	    int indexEnd = nums.length - 1;
	    
	    while(indexBeg < nums.length && indexEnd >= 0) {
	    	prodCumLR = prodCumLR.multiply(BigInteger.valueOf(nums[indexBeg]));
	    	runProdLR[indexBeg] = prodCumLR;
	    	indexBeg += 1;
	    	prodCumRL = prodCumRL.multiply(BigInteger.valueOf(nums[indexEnd]));
	    	runProdRL[indexEnd] = prodCumRL;
	    	indexEnd -= 1;
	    }
	    
	    for (int i = 0; i < nums.length; i++) {
	    	if (i == 0) {
	    		g = g.add(runProdRL[i + 1]);
	    	} else if (i == nums.length - 1) {
	    		g = g.add(runProdLR[i - 1]);
	    	} else {
	    		g = g.add(runProdRL[i + 1].multiply(runProdLR[i - 1]));
	    	}
	    }
	    result = g.mod(BigInteger.valueOf(m));
	    return result.intValue();
	} 

}
