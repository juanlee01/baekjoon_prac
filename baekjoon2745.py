def charto10 (inputchar):
    orded = ord(inputchar)
    result = 0
    if  ord('A') <= orded <= ord('Z'):
        result = orded - 65 + 10
    else:
        result = int(inputchar)
    
    return result
    
inputstr, N = input().split()
N = int(N)

total = 0
for i in range(len(inputstr) - 1, 0):
    total += charto10(inputstr[i]) * (N ** i)
    print(i)
    
print(total)