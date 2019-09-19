package com.lfu_cache;

import java.util.HashMap;
import java.util.Map;

public class LFUCache {
	
//	Number of elements that can be stored in the cache
	private int cacheSize;
//	Used to store value (in this example is just a string) assigned to a key
	private Map<Integer, String> cacheMemory = new HashMap<Integer, String>();
//	Used to measure the number of times an item is being used. The first integer is the key
//	and the second one is the number of times an item with that key has being used.
	private Map<Integer, Integer> cacheInfo = new HashMap<Integer, Integer>();

//	Constructor with the cache size
	public LFUCache(int cacheSize) {
		this.cacheSize = cacheSize;
	}
	
	public int getCacheSize() {
		return cacheSize;
	}

	public void setCacheSize(int cacheSize) {
		this.cacheSize = cacheSize;
	}
	
	public Map<Integer, String> getCacheMemory() {
		return cacheMemory;
	}
	
	@Override
	public String toString() {
		return "LFUCache [cacheMemory=" + cacheMemory + "]";
	}

	//	Set a new key value pair to the cache
	public void set(int key, String value) {
//		Insert the new element, but also check the size and the least frequently used element
		if (this.cacheMemory.size() == this.cacheSize) {
//				Find the least used element
			int leastUsedElementKey = 0;
			int leastUsedElementValue = -1;
			for (Map.Entry<Integer, Integer> entry : this.cacheInfo.entrySet()) {
				if (leastUsedElementValue == -1 || entry.getValue() < leastUsedElementValue) {
					leastUsedElementKey = entry.getKey();
					leastUsedElementValue = entry.getValue();
				}
			}
//				Remove least used element
			this.cacheMemory.remove(leastUsedElementKey);
//				Add the new element
			this.cacheMemory.put(key, value);
		} else {
			this.cacheMemory.put(key, value);
//			Initialized all elements to unused
			this.cacheInfo.put(key, 0);
		}
	}
	
//	Method that returns the value for certain key. If value doesn't exist, returns null
	public String get(int key) {
		if (this.cacheMemory.containsKey(key)) {
			if (this.cacheInfo.containsKey(key)) {
//				Update the amount of times that element has been used
				int nTimesUsed = this.cacheInfo.get(key) + 1;
				this.cacheInfo.put(key, nTimesUsed);
			} else {
				this.cacheInfo.put(key, 1);
			}
			return this.cacheMemory.get(key);
		} else {
			return null;
		}
	}
	
}
