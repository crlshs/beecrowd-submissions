def atribuir(valor, t1, t2, a1, a2, a3):
    if (valor < t1): return a1
    elif (valor >= t1 and valor < t2): return a2
    return a3

while(True):
    try:
        n = int(input())
    except (ValueError): break
    except (EOFError): break

    graph = {i : [] for i in range(1, n+1)}
    atributos = {i : [] for i in range(1, n+1)}

    for i in range(1, n+1):
        try:
            amigos = list(map(int, input().split()))
        except(ValueError): break
        except(EOFError): break

        amigos.insert(-1,i)
        graph[i] = amigos[:-1]

    while (True):
        try:
            linha = input()
            if not linha: break
        
            p, t1, t2, a1, a2, a3 = linha.split()
        except(ValueError):break
        except(EOFError): break

        p, t1, t2 = int(p), int(t1), int(t2)

        # a1 < t1 < a2 < t3 < a3
        fila = set(graph[p])
        visitados = set()
        while fila:
            i = fila.pop()
            if i not in visitados:
                valor = len(graph[i])-1

                atributos[i].append(atribuir(valor, t1, t2, a1, a2, a3))

                visitados.add(i)
                fila.update(graph[i])
        if visitados != set(graph.keys()):
            for i in visitados.symmetric_difference(set(graph.keys())):
                atributos[i].append(a1+" ")

    for j in range(1, n+1):
        nome = input()
        print(f"{nome}: {' '.join(atributos[j])}")