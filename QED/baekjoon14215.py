triple = list(map(int, input().split()))

trisum = sum(triple)
answer = 0
if max(triple) >= trisum - max(triple):
    answer = 2 * (trisum - max(triple)) - 1
else:
    answer = sum(triple)
    
print(answer)