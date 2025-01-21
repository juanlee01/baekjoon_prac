n = int(input())
line = 2 * n - 1

for i in range(1, n):
    for i in range(n - i, 0, -1):
        print(" ", end = "")
    for i in range(1, i * 2):
        print("*", end = "")
    print("\n")