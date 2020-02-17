# Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ",
# "AAA", "AAB", ....
#
# Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".


def getColumnId(num, alphabet):
    base = len(alphabet)
    id = []
    # Get num % 26 to get the last character, and then divide it by 26
    while True:
        if num > base:
            # If number is multiple of 26, means that a sub-alphabet end is reached
            if num % base == 0:
                id += ["Z"]
                num = int(num / base) - 1
            else:
                id += [alphabet[num % base]]
                num = int(num / base)
        else:
            id += [alphabet[num]]
            break
    return "".join(id[::-1])


alphabetMap = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L",
               13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W",
               24: "X", 25: "Y", 26: "Z"}

print(getColumnId(40, alphabetMap))
