while (True):
    n = int(input())
    if n == 0: break
    pilha = []
    pilha.extend(i for i in range(1, n+1))
    descarte = []
    # tira a do topo, e move a prox para a base
    while (len(pilha)>1):
        descarte.append(pilha.pop(0))

        prox = pilha.pop(0)
        pilha.append(prox)

    print(f"Discarded cards: {', '.join(map(str, descarte))}")
    print(f"Remaining card: {pilha[0]}")
