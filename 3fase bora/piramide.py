# tarefa "pirâmide" obi 2023 fase 3 - por Carlos Henrique Silveira

pesos = list(map(int, input().split()))
pesos.sort(reverse=True)

def resposta(lista):
    # topo é o maior elemento dos pesos
    topo = lista[0]
    duplas = []

    # verifica todas as duplas possíveis, isto é, as que possuem soma igual ao peso do topo
    for i in range(1, len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] + lista[j] == topo:
                duplas.append((lista[i], lista[j]))

    # se não há duplas com peso igual ao topo
    if not duplas: return "N"

    # cria uma cópia da lista original, sem as possíveis duplas, deixando apenas um trio restante para a base
    for dupla in duplas:
        restante = lista[1:].copy() # uma cópia da lista original, sem o topo
        restante.remove(dupla[0])
        restante.remove(dupla[1])

    if sum(restante) == topo: return "S"

    return "N"

print(resposta(pesos))