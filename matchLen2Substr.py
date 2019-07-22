def string_match(a, b):
    i = 0
    count = 0
    for _ in range(len(a)-1):
        if a[i:i+2] in b:
            print(a[i:i+2])
            count += 1
        i += 1
    return count   

print( string_match('aabbccdd', 'abbbxxd') )