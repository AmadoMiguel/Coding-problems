import numpy as np


# This function will conform the transition matrix based on a properly organized markov chain
def getTransitionMatrix(ch):
    currentRow, transMat = [], []
    currentLetter = ch[0][0]
    for s in ch:
        if currentLetter != s[0]:
            transMat.append(currentRow)
            currentLetter = s[0]
            currentRow = [s[2]]
        else:
            currentRow.append(s[2])
    # Insert last row
    transMat.append(currentRow)
    return transMat


def calculateNumberOfVisitTimes(transMatrix, nSteps):
    stochRow = np.linalg.matrix_power(transMatrix, nSteps)
    # From here, get the visit percentage of each state
    percVisits = []
    for i in stochRow[0, :]:
        percVisits.append(round(i, 4) * 100)
    print("Percentage of visits", percVisits)
    # Now, get the number of visits based of the number of steps
    nVisits = [(v * nSteps) / 100 for v in percVisits]
    return nVisits


chain = [
          ('a', 'a', 0.9),
          ('a', 'b', 0.075),
          ('a', 'c', 0.025),
          ('b', 'a', 0.15),
          ('b', 'b', 0.8),
          ('b', 'c', 0.05),
          ('c', 'a', 0.25),
          ('c', 'b', 0.25),
          ('c', 'c', 0.5)
        ]

transMat = getTransitionMatrix(chain)
nTimes = calculateNumberOfVisitTimes(transMat, 4000)
print(nTimes)
