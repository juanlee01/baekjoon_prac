import math

A, B, V = map(int, input().split())

n = math.ceil((V - B)/(A - B))

print(n)


# 시간초과된 버전

# current = 0
# day = 0
# while True:
#     day += 1
#     current += A
#     if current >= V:
#         break
#     else:
#         current += - B

# print(day)