# The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is
# to take increasingly larger prime numbers, and mark their multiples as composite.
#
# For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two),
# then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N,
# the unmarked numbers that remain will be prime.
#
# Implement this algorithm.
#
# Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).


def generatePrimeNumbers(num):
    allNumsTillNum = list(range(2, num + 1))
    allPrimes = [1]
    for n in allNumsTillNum:
        if n != -1:
            allPrimes += [n]
        currProd = 2
        while 0 <= (n * currProd) - 1 < len(allNumsTillNum):
            allNumsTillNum[(n * currProd) - 2] = -1
            currProd += 1
    print(allPrimes)


generatePrimeNumbers(121)
