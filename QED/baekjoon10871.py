a, b = map(int, input().split())
arr = []
arr = list(map(int, input().split()))

cout = 0
for i in range(a):
    if arr[i]<b:
        print(arr[i], end = "")