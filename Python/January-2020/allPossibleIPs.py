# Given a string of digits, generate all possible valid IP address combinations.
#
# IP addresses must follow the format A.B.C.D, where A, B, C, and D are numbers between 0 and 255. Zero-prefixed
# numbers, such as 01 and 065, are not allowed, except for 0 itself.
#
# For example, given "2542540123", you should return ['254.25.40.123', '254.254.0.123'].


def isValidNum(num):
    if len(num):
        if num[0] == 0 or int(num) > 255:
            return False
        return True
    return False


def isValidIP(IPAddress):
    nums = IPAddress.split(".")
    if len(nums) == 4:
        for n in nums:
            if not isValidNum(n):
                return False
        return True
    return False


def findIPPossibilities(numsStr, currentNum, currentIP, allIPs):
    if not len(numsStr):
        return allIPs
    if isValidNum(currentNum):
        currentIP += currentNum
        if isValidIP(currentIP):
            allIPs += [currentIP]
        else:
            currentIP += "."
    allIPs = findIPPossibilities(numsStr[1:], currentNum + numsStr[0], currentIP, allIPs)
    allIPs = findIPPossibilities(numsStr[1:], currentNum, currentIP, allIPs)
    return allIPs


print(findIPPossibilities("2542540123", "", "", []))
