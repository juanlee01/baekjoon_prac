a, b = map(int, input().split())

backet = []
for i in range(a):
    backet.append(i)

for i in range(b):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    tmp = backet[x]
    backet[x] = backet[y]
    backet[y] = tmp
    

for i in range(len(backet)):
    print(backet[i]+1, end=" ")

