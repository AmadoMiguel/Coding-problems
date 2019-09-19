package com.lfu_cache;

public class LeastFrequentlyUsedTest {

	public static void main(String[] args) {
//		Create a new lfu cache
		LFUCache cache = new LFUCache(5);
//		Add 5 elements
		cache.set(1, "Hello");
		cache.set(2, "How");
		cache.set(3, "Are");
		cache.set(4, "You");
		cache.set(5, "Today");
//		Retrieve some of the values
		String v1 = cache.get(5);
		String v2 = cache.get(5);
		String v3 = cache.get(3);
		String v4 = cache.get(4);
		String v5 = cache.get(1);
		System.out.println(v1+" "+v2+" "+v3+" "+v4+" "+v5);
//		Add a new element
		cache.set(6, "?");
//		View memory information
		System.out.println(cache.getCacheMemory());
	}

}
