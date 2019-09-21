package com.users_list;

import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

public class UsersInQueue {
	public static void main(String[] args) {
		List<User> users = new ArrayList<User>();
		User user1 = new User(1, "John", "Roland", 30);
		User user2 = new User(2, "Mary", "Korg", 20);
		User user3 = new User(3, "Deivid", "Gibson", 15);
		User user4 = new User(4, "Andrew", "Tama", 50);
//		Add users in any order
		users.add(user2);
		users.add(user4);
		users.add(user3);
		users.add(user1);
		System.out.println(users);
//		Users will be ordered by age (that's how is defined in the overriden compare method in the
//		UsersOrdering class which implements the Comparator interface)
		PriorityQueue<User> usersQueue = new PriorityQueue<>(new UsersOrdering());
		usersQueue.addAll(users);
		System.out.println(usersQueue);
	}
	
}
