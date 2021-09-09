# Given a sorted array arr of distinct integers, return the lowest index i for which arr[i] == i. 
# Return null if there is no such index.

# For example, given the array [-5, -3, 2, 3], return 2 since arr[2] == 2. Even though arr[3] == 3, 
# we return 2 since it's the lowest index.

def return_lowest_index_i(nums):
    for i in range(len(nums)):
        if nums[i] == i:
            return i
    return None

print(return_lowest_index_i([-5, -3, 2, 3]))