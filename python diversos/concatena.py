digitos_perguntas = list(map(int, input().split()))

lista = list(map(int,input().split()))
respostas = []

for _ in range(digitos_perguntas[1]):
    intervalo = list(map(int, input().split()))
    somas = 0

    lista_intervalo = lista[intervalo[0]-1:intervalo[1]]

    for i in range(len(lista_intervalo)):
        for j in range(len(lista_intervalo)):
            if i != j:
                somas += int(str(lista_intervalo[i]) + str(lista_intervalo[j]))

    respostas.append(somas)

print(*respostas, sep='\n')
