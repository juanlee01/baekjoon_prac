str = input()

count = 0

for i in range (len(str)):
    count += 1
    if str[i] == "=":
        if str[i - 1] == "z":
            if str[i - 2] == "d":
                count += -2
            else:
                count += -1
        else:
            count += -1
    elif str[i] == "-":
        count += -1
    elif str[i] == "j":
        if(str[i - 1] == "l" or str[i - 1] == "n"):
            count += -1
    
print(count)