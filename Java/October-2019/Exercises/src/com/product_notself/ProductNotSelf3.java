package com.product_notself;

public class ProductNotSelf3 {

	public static void main(String[] args) {
		System.out.println(productExceptSelf(new int[]{37, 50, 50, 6, 8, 54, 7, 64, 2, 64, 67, 59, 22, 73, 33, 53, 43, 77, 56, 76, 59, 96, 64, 100, 89, 38, 64, 73, 85, 96, 65, 50, 62, 4, 82, 57, 98, 61, 92, 1, 80, 53, 80, 55, 94, 9, 73, 89, 83, 80}
		, 67));
	}
//	Solution taken from 
//	https://github.com/edyluisrey/Codefights-Algorithms/blob/master/src/CommonTechniques/ProductExceptSelf.java 
	public static int productExceptSelf(int[] nums, int m) {
		 // 1,2,3,4    - 1, 2,6,24   ---24 12 8 6  
		   int sum = 0;
		   int product = 1;
		   for (int i = 0; i < nums.length; i++) {
		        sum = (nums[i] * sum) + product;
		        sum %= m;
		        product *= nums[i];
		        product %= m;
		    }
		    return sum;
	}

}
