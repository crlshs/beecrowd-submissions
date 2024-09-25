def minimo_balanceamento(N, K, bonecas):
    bonecas.sort()
    
    balanceamentos = []

    for i in range(N - 2):
        A = bonecas[i]
        B = bonecas[i + 1]
        balanceamento = (A - B) ** 2
        balanceamentos.append((balanceamento, i))

    balanceamentos.sort()

    usados = [False] * N
    soma_balanceamentos = 0
    trios_formados = 0

    for balanceamento, i in balanceamentos:
        if not usados[i] and not usados[i + 1] and not usados[i + 2]:
            soma_balanceamentos += balanceamento
            trios_formados += 1
            usados[i] = usados[i + 1] = usados[i + 2] = True
            if trios_formados == K:
                break

    return soma_balanceamentos

N, K = map(int, input().split())
bonecas = list(map(int, input().split()))

print(minimo_balanceamento(N, K, bonecas))
