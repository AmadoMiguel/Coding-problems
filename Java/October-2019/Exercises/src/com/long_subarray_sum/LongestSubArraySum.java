package com.long_subarray_sum;


public class LongestSubArraySum {

	public static void main(String[] args) {
		int[] result = findLongestSubarrayBySum(
				15,new int[] {1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10});
		System.out.println(String.valueOf(result[0])+", "+String.valueOf(result[1]));
	}

	public static int[] findLongestSubarrayBySum(int s, int[] arr) {
	//		Initialize array pointers and other required variables
			int ptr1 = 0;
			int ptr2 = 0;
			Integer maxRange = null;
			int[] indexesOfSubArray = new int[2];
	//		Start traversing and slice using the pointers until the end of the array is reached.
	//	    The final condition is that ptr1 is equal to length of array - 1
			while (ptr1 <= arr.length && ptr2 <= arr.length + 1) {
	//			Find current sum for the range between ptr1 and ptr2
				int currSum = 0;
				for (int i = ptr1; i < ptr2; i++) {
					if (i < arr.length) {
						currSum += arr[i];
					}
				}
				if (currSum == s) {
					if (maxRange == null || (ptr2 + 1 - (ptr1 + 1)) > maxRange) {
						maxRange = (ptr2 + 1 - (ptr1 + 1));
						indexesOfSubArray[0] = ptr1+1;
						indexesOfSubArray[1] = ptr2;
					}
					if (ptr2 == arr.length) {
						break;
					} else {
						ptr2 += 1;
					}
				} else {
	//				Change pointers accordingly
					if (currSum <= s) {
						ptr2 += 1;
					} else {
						ptr1 += 1;
					}
	//				If pointers cross, reset
					if (ptr1 > ptr2) {
						ptr1 = ptr2;
						ptr2 += 1;
					}
				}
			}
			if (maxRange != null) {
				return indexesOfSubArray;
			} else {
				return new int[]{-1};
			}
	}

}