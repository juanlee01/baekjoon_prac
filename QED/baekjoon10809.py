inputstr = input()
countlist = []
for i in range(26):
    countlist.append(-1)
    
for i in range(len(inputstr)):
    alphanum = ord(inputstr[i]) - 97
    if countlist[alphanum] == -1:
        countlist[alphanum] = i
        
        
for i in range(len(countlist)):
    print(countlist[i], end = " ")