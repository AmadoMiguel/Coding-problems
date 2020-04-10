# A top secret message containing uppercase letters from 'A' to 'Z' has been encoded as numbers using the following
# mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# You are an FBI agent and you need to determine the total number of ways that the message can be decoded.
#
# Since the answer could be very large, take it modulo 109 + 7.


def mapDecoding(message):
    lM = len(message)
    # Primary base cases
    if not lM:
        return 1
    if lM == 1:
        if message[0] == "0":
            return 0
        return 1
    waysTrack = [0 for _ in range(lM + 1)]
    waysTrack[0] = 1
    if message[0] != "0":
        waysTrack[1] = 1
    for i in range(2, lM + 1):
        pp,p=int(message[i-2:i]),int(message[i-1:i])
        if p >= 1:
            waysTrack[i] += waysTrack[i-1]
        if pp>=10 and pp<=26:
            waysTrack[i] += waysTrack[i-2]
    return waysTrack[-1] % ((10**9) + 7)


assert mapDecoding("123") == 3
assert mapDecoding("1234") == 3
assert mapDecoding("10122110") == 5
