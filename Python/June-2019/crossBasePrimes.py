# Check if a number is prime in the given base.

# First, create the function that verifies if any number is prime
def isPrime(num):
    isPrime = True
    for i in range(num,0,-1):
        if i == num or i == 1:
            continue
        if num % i == 0:
            isPrime = False
            break
    return isPrime    

def crossBaseNum(num,base):
    # Convert num to string or iteration purposes
    numStr = str(num)
    # Initialize exponent variable
    ind = len(numStr) - 1
    # Initialize converted number variable
    numInBase = 0
    # Convert given number to given base
    for d in numStr:
        numInBase += (int(d)*(base**ind))
        ind -= 1
    # Check if converted number is prime
    print("Original number:",num)
    print(num,"in base",base,":",numInBase)
    if isPrime(numInBase):
        print(num,"in base",base,"("+str(numInBase)+")","is prime.")
    else:
        print(num,"in base",base,"("+str(numInBase)+")","is not prime.")    

crossBaseNum(137,16)