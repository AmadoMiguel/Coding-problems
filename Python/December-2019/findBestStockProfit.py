# Given a array of numbers representing the stock prices of a company in chronological order, write a function
# that calculates the maximum profit you could have made from buying and selling that stock. You're also given a '
# number fee that represents a transaction fee for each buy and sell transaction.
#
# You must buy before you can sell the stock, but you can make as many transactions as you like.
#
# For example, given [1, 3, 2, 8, 4, 10] and fee = 2, you should return 9, since you could buy the stock at 1 dollar,
# and sell at 8 dollars, and then buy it at 4 dollars and sell it at 10 dollars. Since we did two transactions, there
# is a 4 dollar fee, so we have 7 + 6 = 13 profit minus 4 dollars of fees.


def findMaxProfit(currentTransactions, remainingPrices, maxProfit):
    if not len(remainingPrices):
        if len(currentTransactions) % 2 != 0:
            del currentTransactions[-1]
        print("Current transactions", currentTransactions)
        return True, maxProfit, currentTransactions
    else:
        for i in range(len(remainingPrices)):
            transac = currentTransactions + [remainingPrices[i]]
            status, maxProfit, transac = findMaxProfit(transac, remainingPrices[i+1:], maxProfit)
            if status:
                if len(transac) >= 2:
                    # Calculate current transactions profit and compare to maxProfit
                    subPtr1, subPtr2 = 0, 1
                    currentProfit = 0
                    while subPtr2 < len(transac):
                        currentProfit += (transac[subPtr2] - transac[subPtr1]) - 2
                        subPtr1 = subPtr2 + 1
                        subPtr2 = subPtr1 + 1
                    if maxProfit is None or currentProfit > maxProfit:
                        maxProfit = currentProfit
                        print("Max profit so far", transac, maxProfit)

    return False, maxProfit, currentTransactions


stockPrices = [1, 3, 2, 8, 4, 10]
print(findMaxProfit([], stockPrices, None))
