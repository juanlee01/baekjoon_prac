A = int(input()) 
B = int(input())
C = int(input())

answer = ''
if A+B+C == 180:
    if A == B or B == C or C == A:
        if A==B==C:
            answer = 'Equilateral'
        else:
            answer = 'Isosceles'
    else:
        answer = 'Scalene'
else:
    answer = 'Error'
    
print(answer)