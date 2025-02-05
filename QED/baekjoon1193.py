x = int(input())

count = 1
floor = 1
flag = False
point = []
while True:

    # 층 floor 안에서 반복
    for i in range(1, floor + 1):
        # 홀수일 경우
        if floor % 2 != 1:
            point = [i, floor - i + 1]

        # 짝수일 경우
        else:
            point = [floor - i + 1, i]
            
        # 갯수 확인
        if count == x:
            flag = True
            break

        count += 1

    floor += 1
    if flag == True:
        break

print(str(point[0]) + '/' + str(point[1]))