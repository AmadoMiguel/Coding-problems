package com.users_list;

import java.util.Comparator;

public class UsersOrdering implements Comparator<User> {
	
//	Order users by age in the collection that is passed an instance of this class to specify ordering
//	of objects
	@Override
	public int compare(User arg0, User arg1) {
		if (arg0.getId() < arg1.getId()) {
			return -1;
		} else if(arg0.getId() > arg1.getId()) {
			return 1;
		} else {
			return 0;
		}
	}
	
}
