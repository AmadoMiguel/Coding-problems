import re

alNumStr = "Hola123hayalguien56PorAHI"

lowerLetts = sorted(re.findall('[a-z]',alNumStr))
upperLetts = sorted(re.findall('[A-Z]',alNumStr))
nums = sorted(re.findall('[0-9]',alNumStr))

evenNums = (num for num in nums if int(num)%2 == 0)
oddNums = (num for num in nums if int(num)%2 != 0)
newSortNums = ("".join(evenNums),"".join(oddNums))

print( "".join(lowerLetts),"".join(upperLetts),"".join(newSortNums) )