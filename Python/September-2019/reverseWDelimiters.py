# Given a string and a set of delimiters, reverse the words in the string while
# maintaining the relative order of the delimiters. For example, given
# "hello/world:here", return "here/world:hello"

import re


def reverseWordsWithDelimiters(st):
    # Use regular expressions in order to get the words and the symbols separately
    words = re.findall("[a-z]+", st)
    symbols = re.findall("[^a-z]+", st)
    reversedWords = ""
    # Join the words (in reverse order) with the symbols
    index = 0
    for w in reversed(words):
        reversedWords += w
        if index < len(symbols):
            reversedWords += symbols[index]
            index += 1
    return reversedWords


s = "hello/s/<i>o:world:here"
print(s)
print(reverseWordsWithDelimiters(s))
