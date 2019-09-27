# Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y
# are integers and returns x^y


exponent = 1
result = 1


# Use recursion to power a number to an exponential
def integerExponent(num, power):
    global exponent
    global result

    if exponent <= power:
        result = result * num
        exponent += 1
        integerExponent(num, power)
    return result


print(integerExponent(2, 10))
