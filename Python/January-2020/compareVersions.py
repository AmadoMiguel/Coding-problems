# Version numbers are strings that are used to identify unique states of software products. A version number is in the
# format a.b.c.d. and so on where a, b, etc. are numeric strings separated by dots. These generally represent a
# hierarchy from major to minor changes. Given two version numbers version1 and version2, conclude which is the
# latest version number. Your code should do the following:
# If version1 > version2 return 1.
# If version1 < version2 return -1.
# Otherwise return 0.
#
# Note that the numeric strings such as a, b, c, d, etc. may have leading zeroes, and that the version strings do not
# start or end with dots. Unspecified level revision numbers default to 0.
#
# Example:
# Input:
# version1 = "1.0.33"
# version2 = "1.0.27"
# Output: 1
# #version1 > version2
#
# Input:
# version1 = "0.1"
# version2 = "1.1"
# Output: -1
# #version1 < version2
#
# Input:
# version1 = "1.01"
# version2 = "1.001"
# Output: 0
# #ignore leading zeroes, 01 and 001 represent the same number.
#
# Input:
# version1 = "1.0"
# version2 = "1.0.0"
# Output: 0
# #version1 does not have a 3rd level revision number, which
# defaults to "0"


def compareVersions(v1, v2):
    v1Nums, v2Nums = v1.split("."), v2.split(".")
    ptrV1, ptrV2 = 0, 0
    while ptrV1 < len(v1Nums) and ptrV2 < len(v2Nums):
        if int(v1Nums[ptrV1]) < int(v2Nums[ptrV2]):
            return -1
        if int(v1Nums[ptrV1]) > int(v2Nums[ptrV2]):
            return 1
        ptrV1, ptrV2 = ptrV1 + 1, ptrV2 + 1
    return 0


assert compareVersions("1.01", "1.001") == 0  # Pass
assert compareVersions("1.0", "1.0.0") == 0  # Pass
assert compareVersions("1.0.33", "1.0.37") == -1  # Pass
assert compareVersions("1.0.34", "1.0.30") == 1  # Pass
