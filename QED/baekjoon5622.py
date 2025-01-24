inputstr = input()
total = 0
for i in range(len(inputstr)):   
    if ord(inputstr[i]) >= ord('A') and ord(inputstr[i]) <= ord('C'):
        total += 3
    elif ord(inputstr[i]) >= ord('D') and ord(inputstr[i]) <= ord('F'):
        total += 4
    elif ord(inputstr[i]) >= ord('G') and ord(inputstr[i]) <= ord('I'):
        total += 5
    elif ord(inputstr[i]) >= ord('J') and ord(inputstr[i]) <= ord('L'):
        total += 6
    elif ord(inputstr[i]) >= ord('M') and ord(inputstr[i]) <= ord('O'):
        total += 7
    elif ord(inputstr[i]) >= ord('P') and ord(inputstr[i]) <= ord('S'):
        total += 8
    elif ord(inputstr[i]) >= ord('T') and ord(inputstr[i]) <= ord('V'):
        total += 9
    elif ord(inputstr[i]) >= ord('W') and ord(inputstr[i]) <= ord('Z'):
        total += 10
        
print(total)