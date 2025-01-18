a = int(input())
arr = []
arr = list(map(int, input().split()))

max = arr[0]
min = arr[0]

for i in range(1, a):
    if arr[i]>max:
        max = arr[i]
    if arr[i]< min:
        min = arr[i]
print(min, max)