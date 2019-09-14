import time

def printSomething():
    print("Hello")

def jobSched(func,nMilis):
    time.sleep(nMilis / 1000)
    func()

jobSched(printSomething,1000)        