arr = [0,1,2,3,4,5,6,4]
num = 6

for m in range(0,len(arr)-1):
    initNum = arr[m]
    for n in arr[m+1:]:
        if initNum + n == num:
            print(initNum,"+",n,"=",num)       