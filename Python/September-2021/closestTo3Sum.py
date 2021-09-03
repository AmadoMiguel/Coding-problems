# Given a list of numbers and a target number n, find 3 numbers in the list that sums closest to the target number 
# n. There may be multiple ways of creating the sum closest to the target number, you can return any combination 
# in any order.

# Here's an example and some starter code.

def find_closest_sum_recur(curr_nums,curr_sum,rem_nums,target):
    if len(curr_nums) == 3:
        curr_closest_sum = find_closest_sum_recur.closest_sum
        if curr_closest_sum is None or\
            abs(curr_sum - target) < abs(curr_closest_sum - target):
            find_closest_sum_recur.closest_sum = curr_sum
            find_closest_sum_recur.closest_sum_nums = curr_nums
        return
    for i in range(len(rem_nums)):
        next_num = rem_nums[i]
        find_closest_sum_recur(curr_nums+[next_num],curr_sum+next_num,\
            rem_nums[:i]+rem_nums[i+1:],target)

def closest_3sum(nums, target):
    find_closest_sum_recur.closest_sum = None
    find_closest_sum_recur.closest_sum_nums = None
    find_closest_sum_recur([],0,nums,target)
    return find_closest_sum_recur.closest_sum_nums

target = 3
nums = [2, 1, -5, 4, 3]
print("Given",nums)
print("A possible 3-numbers combination for which the sum is closest to",target,"is:")
print(closest_3sum(nums, target))