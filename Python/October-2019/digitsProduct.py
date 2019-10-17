# Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose
# digits is equal to product. If there is no such integer, return -1 instead.


def digitsProduct(product):
    if product == 0:
        return 10
    if product == 1:
        return 1
    factors = numDescomp(product)
    if len(factors) == 0 or len(factors) < len(str(product)):
        return -1
    return int("".join([str(d) for d in factors]))


def numDescomp(num):
    factors = []
    currFactor = 9
    while num != 1 and currFactor > 1:
        if num % currFactor == 0:
            num //= currFactor
            factors.append(currFactor)
        else:
            currFactor -= 1
    return list(sorted(factors))


print(digitsProduct(12))
