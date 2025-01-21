a, b = map(int, input().split())

arr = []
basket = []
for i in range(a):
    basket.append(0)

for i in range(b):
    arr = list(map(int, input().split()))

    for j in range(arr[0]-1, arr[1]):
        basket[j] = arr[2]

for i in range(len(basket)):
    print(basket[i], end=" ")