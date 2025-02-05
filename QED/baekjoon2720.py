Test_count =  int(input())


for i in range(Test_count):
    q, d, n, p = 0, 0, 0, 0
    change = int(input())

    q = change // 25
    change = change % 25

    d = change // 10
    change = change % 10

    n = change // 5
    change = change % 5

    p = change 

    print(q, d, n, p)

