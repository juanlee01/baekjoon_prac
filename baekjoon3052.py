arr = []

for i in range(42):
    arr.append(0)

for i in range(10):
    n = int(input())
    arr[n % 42] += 1

count = 0
for i in range(42):
    if arr[i] != 0:
        count += 1

print(count)
