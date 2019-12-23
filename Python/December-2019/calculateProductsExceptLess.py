# You are given an array of integers. Return an array of the same size where the element at each index is the
# product of all the elements in the original array except for the element at that index.
#
# For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].
#
# You cannot use division in this problem.


def getRunningProducts(nums):
    normRunningProd, invRunningProd = nums[:], nums[:]
    ptr1, ptr2, = 0, len(nums) - 1
    cumProdNorm, cumProdInv = 1, 1
    while ptr1 < len(nums) and ptr2 >= 0:
        cumProdNorm *= nums[ptr1]
        cumProdInv *= nums[ptr2]
        normRunningProd[ptr1] = cumProdNorm
        invRunningProd[ptr2] = cumProdInv
        ptr1, ptr2 = ptr1 + 1, ptr2 - 1
    return normRunningProd, invRunningProd


def getProductForEachNum(nums):
    prodForEachNum = nums
    normProdRun, invProdRun = getRunningProducts(nums)
    for i in range(len(nums)):
        if i == 0:
            prodForEachNum[i] = invProdRun[1]
        elif i == len(nums) - 1:
            prodForEachNum[i] = normProdRun[-2]
        else:
            prodForEachNum[i] = normProdRun[i - 1] * invProdRun[i + 1]
    return prodForEachNum


nums = [1, 2, 3, 4, 5]
print(getProductForEachNum(nums))
