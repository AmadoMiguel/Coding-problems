def canScramble(word1,word2):
    if sorted(word1) == sorted(word2):
        return True
    else:
        return False    

print( canScramble("aab", "bba") )        