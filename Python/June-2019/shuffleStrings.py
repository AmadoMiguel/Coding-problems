import re

def isValidShuffle(str1,str2,shuffle_str):
    # Find strings into shuffle using 're' and placeholder
    # Join the list result with no spaces
    st1 = "".join(re.findall('[%s]'%(str1,),shuffle_str))
    st2 = "".join(re.findall('[%s]'%(str2,),shuffle_str))
    
    if str1 == st1 and str2 == st2:
        return True
    else:
        return False    

print( isValidShuffle("abc","def","adcbef") )    