N = int(input())

list = list(map(int, input().split()))
#print(list)
primeCount = 0
for i in range(len(list)):
    isPrime = True
    for j in range(2, list[i]):
        if list[i] % j == 0:
            isPrime = False
            break
    if list[i] == 1:
        isPrime = False
    if isPrime == True:
        primeCount += 1
        
print(primeCount)