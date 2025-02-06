N = int(input())

list = list(map(int, input().split()))
print(list)

for i in range(len(list)):
    for j in range(2, list[i]):
        if list[i] % j != 0:
            break
        