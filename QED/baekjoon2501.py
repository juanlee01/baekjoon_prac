N, K = map(int, input().split())

count = 0
result = 0
for i in range(1, N + 1):
    if 0 == N % i :
        count += 1 
        if count == K:
            result = i
            break
    
print(result)   