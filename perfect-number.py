# This function receives any number and determines if a perfect number (its digits sum to ten) can
# be conformed from it by adding a last digit or not
def conformPerfect(n):
    # Convert the number into string
    stringNum = str(n)
    # Determine the sum of its digits
    digitsSum = 0
    for d in stringNum:
        digitsSum += int(d)
    # Determine the difference between 10 and the number
    difference = 10 - digitsSum
    # Check if difference is equals of less than 0, or equals to 10
    # Return corresponding result/message
    if (difference <= 0 or difference == 10):
        return "The number cannot be converted to perfect"
    else:
        perfectNumber = stringNum + str(difference)
        return "The perfect number should be",int(perfectNumber)
    
print(conformPerfect(5))