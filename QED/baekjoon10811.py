n, m = map(int, input().split())

basket = []

for i in range(n):
    basket.append(i+1)

for k in range(m):
    i, j = map(int, input().split())
    i -= 1
    j -= 1
    while 1:
        if i >= j:
            break
        tmp = basket[i]
        basket[i] = basket[j]
        basket[j] = tmp
        i += 1
        j -= 1

for i in range(len(basket)):
    print(basket[i], end = " ")