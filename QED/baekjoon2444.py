n = int(input())

for i in range(1, n):
    for j in range(1, n - i + 1):
        print(" ", end = "")
    for k in range(1, i * 2):
        print("*", end = "")
    print("")

for i in range(0, n):
    for j in range(0, i):
        print(" ", end = "")
    for k in range(0, n * 2 - 1 - i * 2):
        print("*", end = "")
    print("")