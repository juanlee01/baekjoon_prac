N = int(input())

x = []
y = []
for i in range(N):
    a, b = map(int, input().split())
    x.append(a) 
    y.append(b)
size = (max(y) - min(y)) * (max(x) - min(x))

print(size)