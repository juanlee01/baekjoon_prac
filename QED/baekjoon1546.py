n = int(input())

arr = list(map(int, input().split()))

max = 0 
for i in range(n):
    if arr[i] > max:
        max = arr[i]

fake = []
total = 0 
for i in range(n):
    total += arr[i]/max * 100

print(total/n)
