M = int(input())
N = int(input())

list = []
for i in range(M, N + 1):
    isPrime = True
    for j in range(2, i):
        if i % j == 0:
            isPrime = False
    if i == 1:
        isPrime = False
    if isPrime == True:
        list.append(i)

#print(list)
if len(list) == 0:
    print('-1')
else:
    print(sum(list), min(list))