n = int(input())

count = 0
for i in range(n):
    str = input()
    used = []
    usedFlag = False

    # 글자수가 1개 일 때 이하 알고리즘의 문제 발생 
    # 다른 케이스로 정리함
    if len(str) == 1:
        usedFlag = False
    else:
        used.append(str[0])
        
        for i in range(1, len(str)):
            for k in range(len(used)):
                # 이미 사용된 적이 있는 문자
                if str[i] == used[k]:
                    # 사용됐지만 연속 사용이 아닐 때 문자 탐색
                    if str[i] != str[i-1]:
                        usedFlag = True
                        break
            if usedFlag == True:
                break
            used.append(str[i])
    if usedFlag == False:
        count += 1

print(count)