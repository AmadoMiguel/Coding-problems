# import random module to acces the randInt() method that returns a random integer
# within a given interval (inclusive)
import random

# Function that returns a random number between 1 and 7
def rand7():
    randNum = random.randint(1,7)
    print(randNum)
# Function that returns a random number between 1 and 5
def rand5():
    randNum = random.randint(1,5)
    print(randNum)

rand7()
rand5()