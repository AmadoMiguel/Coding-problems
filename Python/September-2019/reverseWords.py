# Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here",
# return "here world hello"


def reverseWords(str):
    # split words from str by blank-spaces, reverse the array and join it back with blank-spaces
    return " ".join(w for w in reversed(str.split(" ")))


st = "hello world here"
print(st)
print(reverseWords(st))
