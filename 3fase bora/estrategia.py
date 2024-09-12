jr = tuple(map(int, input().split()))
pontos = list(map(int, input().split()))

total = [0] * jr[0]

for indice, j in enumerate(pontos):
    atual = indice % jr[0]
    total[atual] += j

maior_participante = 0
maior_pontos = total[0]

for i in range(len(total)):
    if total[i] >= maior_pontos:
        maior_pontos = total[i]
        maior_participante = i

print(maior_participante + 1)
