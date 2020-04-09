# Write a function that takes a string as input and returns the string with only the vowels reversed.
# Note: The letters "a", "e", "i", "o", and "u" are vowels. The letter "y" is not a vowel.


def reverseVowelsOfString(s):
    lL = len(s)
    st=[]
    sL=[]
    if lL:
        v=["a","e","i","o","u"]
        sL=list(s)
        for l in sL:
            if l.lower() in v:
                st.append(l)
        for i in range(lL):
            if sL[i].lower() in v:
                sL[i] = st[-1]
                st.pop()
    return "".join(sL)


assert reverseVowelsOfString("hello, world") == "hollo, werld"
assert reverseVowelsOfString("eIaOyU") == "UOaIye"
