N = int(input())
long_num = int(N/4)
for i in range(long_num):
    if i == long_num-1:
        print ("long int")
    else:
        print("long", end=" ")