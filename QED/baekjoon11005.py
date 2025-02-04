def inttochar(ten):
    if  10 <= ten <= 35:
        result = chr(ten + 55)
    else:
        result = int(ten)

    return result

def __main__():
    userinput, N = map(int, input().split())

    result = []

    while 1:

        result.append(inttochar(userinput % N))
        userinput = userinput // N 

        if userinput == 0:
            break

    result.reverse()

    for i in range(len(result)):
        print(result[i], end = "")

__main__()