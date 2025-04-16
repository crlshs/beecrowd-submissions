while(True):
    try:
        c, n = list(map(int, input().split())) 
        estacionados = [(0, 0)]
        valor = 0
    except ValueError: break
    except EOFError: break

    for _ in range(n):
        xpq = list(map(str, input().split()))
        x, p = xpq[0], int(xpq[1])
        if (xpq[-1] != p): q = int(xpq[-1])
        #########
        if (x == "C"):
            if (q <= c):
                estacionados.append((p, q))
                c -= q
                valor += 10
        else:
            for i, j in enumerate(estacionados):
                if (j[0] == p):
                    c += j[1]
                    del estacionados[i]
                    break
    print(valor)