total = 0
Creditcount = 0
for i in range(20):
    userinput = input()
    arr = userinput.split(" ")
    arr[1] = float(arr[1])
    #print (arr[0])
    if arr[2] == "A+":
        Creditcount += arr[1]
        total += arr[1] * 4.5
    elif arr[2] == "A0":
        Creditcount += arr[1]
        total += arr[1] * 4.0
    elif arr[2] == "B+":
        Creditcount += arr[1]
        total += arr[1] * 3.5        
    elif arr[2] == "B0":
        Creditcount += arr[1]
        total += arr[1] * 3.0
    elif arr[2] == "C+":
        Creditcount += arr[1]
        total += arr[1] * 2.5
    elif arr[2] == "C0":
        Creditcount += arr[1]
        total += arr[1] * 2.0
    elif arr[2] == "D+":
        Creditcount += arr[1]
        total += arr[1] * 1.5
    elif arr[2] == "D0":
        Creditcount += arr[1]
        total += arr[1] * 1.0
    elif arr[2] == "F":
        Creditcount += arr[1]
        total += arr[1] * 0.0
    
print(total/Creditcount)