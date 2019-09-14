import random as rand

ways = 0
stepsDone = 0
allWays = []

def letsClimb(currSteps,totalSteps,possibleSteps):
    global ways
    global allWays
    stepOrder = []
    possibleToClimb = 1
    # Check if the steps done so far are less than the steps to go
    while currSteps < totalSteps and possibleToClimb:
        # iterate over the possible number of steps to perform
        for s in possibleSteps:
            # Count performed steps
            if currSteps+s <= totalSteps:
                currSteps = currSteps + s
                stepOrder.append(s)
                print(currSteps,possibleSteps)  
            # Check if ladder can be climbed with the given steps number options
            # Terminate program
            elif currSteps + min(possibleSteps) > totalSteps:
                possibleToClimb = 0    
                break
            # Continue scanning over the step options
            else:    
                continue                 
    if currSteps == totalSteps:
        ways=+1
        allWays.append(stepOrder)
        print("Way number: ",ways)
        print(stepOrder)        
    else:
        print("Unable to climb")

N = rand.randint(6,10)
set = []
for i in range(1,4):
    n = rand.randint(1,N-2)
    if n not in set:
        set.append(n)

print(N,set)
print('\n')
letsClimb(0,N,set)