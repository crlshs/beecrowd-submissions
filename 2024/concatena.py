digitos_perguntas = list(map(int, input().split()))

lista = list(map(int,input().split()))
respostas = []

for _ in range(digitos_perguntas[1]):
    intervalo = list(map(int, input().split()))
    somas = 0

    lista_intervalo = lista[intervalo[0]-1:intervalo[1]]

    for e in lista_intervalo:
        indice = lista_intervalo.index(e)
        somas += int(str(e) + str(lista_intervalo[i] for i in range(len(lista_intervalo)) if i != indice))

    respostas.append(somas)

print(*respostas, sep='\n')
