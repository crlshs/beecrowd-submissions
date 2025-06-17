while(True):
    n = int(input())
    if (n == 0): break
    for _ in range(n):
        respostas = list(map(int,input().split()))

        achou = False
        res = -1

        for i,j in enumerate(respostas):
            if (j<=127):
                if (not achou):
                    res = i
                    achou = True
                else:
                    res = -1
                    break
        match res:
            case 0: print("A")
            case 1: print("B")
            case 2: print("C")
            case 3: print("D")
            case 4: print("E")
            case -1: print("*")