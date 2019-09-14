from __future__ import division

def byteRoundStr(num,nDec):
    if num <= 8:
        print(num,"=",num,"Bits")
    if num > 8 and num < 1024:
        print(num,"=",num,"Bytes")      
    if num >= 1024 and num <(1024*(10**3)):
        KB = round((num / 1024),nDec)
        print(num,"=",KB,"KB")
    if num >= (1024*(10**3)) and num < (1024*(10**6)):
        MB = round((num/(1024*(10**3))),nDec)
        print(num,"=",MB,"MB")  
    if num >= (1024*(10**6)) and num < (1024*(10**9)):
       GB = round((num/(1024*(10**6))),nDec)
       print(num,"=",GB,"GB")    
            

byteRoundStr(8101, 3)