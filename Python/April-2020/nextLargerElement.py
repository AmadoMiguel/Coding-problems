# Given a list of numbers, for each element find the next element that is larger than the current element.
# Return the answer as a list of indices. If there are no elements larger than the current element, then use
# -1 instead.


def largerNumber(nums):
    lN=len(nums)
    a=nums[:]
    inds=[-1 for _ in range(lN)]
    for i in range(lN):
        for j in range(lN):
            if nums[i] > nums[j]:
                if a[j] == nums[j] or nums[i] < a[j]:
                    a[j],inds[j] = nums[i],i
    return inds


print(largerNumber([3, 2, 5, 6, 9, 8]))
