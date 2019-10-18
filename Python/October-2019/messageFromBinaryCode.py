# You are taking part in an Escape Room challenge designed specifically for programmers. In your efforts
# to find a clue, you've found a binary code written on the wall behind a vase, and realized that it must
# be an encrypted message. After some thought, your first guess is that each consecutive
# 8 bits of the code stand for the character with the corresponding extended ASCII code.
#
# Assuming that your hunch is correct, decode the message.


def messageFromBinaryCode(code):
    startIndex = 0
    endIndex = 8
    finalCode = ""
    while startIndex < len(code):
        finalCode += chr(binaryToDecimal(list(code)[startIndex:endIndex]))
        startIndex += 8
        endIndex += 8
    return finalCode


def binaryToDecimal(binary):
    curr2Pow = 0
    total = 0
    for d in binary[::-1]:
        total += (2 ** curr2Pow) * int(d)
        curr2Pow += 1
    return total


print(messageFromBinaryCode("010010000110010101101100011011000110111100100001"))
