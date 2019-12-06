# A look-and-say sequence is defined as the integer sequence beginning with a single digit in which the next
# term is obtained by describing the previous term. An example is easier to understand:
#
# Each consecutive value describes the prior value.
#
# 1      #
# 11     # one 1's
# 21     # two 1's
# 1211   # one 2, and one 1.
# 111221 # #one 1, one 2, and two 1's.
#
# Your task is, return the nth term of this sequence.

m = {"0": "zero", "1": "one", "2": "two", "3": "three", "4": "four", "5": "five",
     "6": "six", "7": "seven", "8": "eight", "9": "nine"}


def lookAndSay(sequence, description):
    if len(sequence) >= 2:
        currentCouple = sequence[0:2]
        del sequence[0:2]
        if len(description):
            if currentCouple[0] == "1":
                description += ", " + m["1"] + " " + currentCouple[1]
            else:
                description += ", " + m[currentCouple[0]] + " " + currentCouple[1] + "'s"
        else:
            if currentCouple[0] == "1":
                description += m["1"] + " " + currentCouple[1]
            else:
                description += m[currentCouple[0]] + " " + currentCouple[1] + "'s"
        description = lookAndSay(sequence, description)
    return description


s = "5112213418"
sequenceDescription = list(lookAndSay(list(s), ""))
invertedSequenceDescription = list(reversed(sequenceDescription))
indexOfLastComma = invertedSequenceDescription.index(',')
invertedSequenceDescription[indexOfLastComma] = " and"
sequenceDescription = list(reversed(invertedSequenceDescription))
print("".join(sequenceDescription))
