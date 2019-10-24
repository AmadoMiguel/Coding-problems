# Find the minimum number of coins required to make n cents.
#
# You can use standard American denominations, that is, 1¢, 5¢, 10¢, and 25¢.
#
# For example, given n = 16, return 3 since we can make it with a 10¢, a 5¢, and a 1¢.


def findMinNumCoins(qty):
    # Define coins denomination
    coins = {'pickle': 1, 'penny': 5, 'dime': 10, 'quarter': 25}
    return calculateNumCoins(coins, qty, 0)


def calculateNumCoins(denoms, usdQty, totalNumCoins):
    if usdQty >= denoms['quarter']:
        usdQty -= denoms['quarter']
        totalNumCoins += 1
        totalNumCoins = calculateNumCoins(denoms, usdQty, totalNumCoins)
    elif usdQty >= denoms['dime']:
        usdQty -= denoms['dime']
        totalNumCoins += 1
        totalNumCoins = calculateNumCoins(denoms, usdQty, totalNumCoins)
    elif usdQty >= denoms['penny']:
        usdQty -= denoms['penny']
        totalNumCoins += 1
        totalNumCoins = calculateNumCoins(denoms, usdQty, totalNumCoins)
    elif usdQty >= denoms['pickle']:
        usdQty -= denoms['pickle']
        totalNumCoins += 1
        totalNumCoins = calculateNumCoins(denoms, usdQty, totalNumCoins)
    return totalNumCoins


print(findMinNumCoins(16))
