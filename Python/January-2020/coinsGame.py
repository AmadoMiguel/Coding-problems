# In front of you is a row of N coins, with values v1, v1, ..., vn.
#
# You are asked to play the following game. You and an opponent take turns choosing either the first or last coin
# from the row, removing it from the row, and receiving the value of the coin.
#
# Write a program that returns the maximum amount of money you can win with certainty, if you move first,
# assuming your opponent plays optimally.


def getMaxScore(coins):
    yourScore, otherPlayerScore = 0, 0
    while len(coins):
        # Make optimal first player move
        print(coins)
        if coins[0] > coins[-1]:
            yourScore += coins[0]
            del coins[0]
            # Simulate 2nd player optimal move
            if len(coins):
                if coins[0] > coins[-1]:
                    otherPlayerScore += coins[0]
                    del coins[0]
                else:
                    otherPlayerScore += coins[-1]
                    del coins[-1]
        else:
            yourScore += coins[-1]
            del coins[-1]
            # Simulate 2nd player optimal move
            if len(coins):
                if coins[0] > coins[-1]:
                    otherPlayerScore += coins[0]
                    del coins[0]
                else:
                    otherPlayerScore += coins[-1]
                    del coins[-1]
    return yourScore, otherPlayerScore


coins = [3, 4, 6, 7, 8, 9, 20, 1]
print(getMaxScore(coins))
