nl = list(map(int, input().split()))
# n = ligacoes
# l = n vendedores

vendedores = [0] * nl[0]
somas = [0] * nl[0]

somas = vendedores.copy()

tempos = [int(input()) for _ in range(nl[1])]

####

indice_tempo = 0

for indice in range(len(vendedores)):
    if indice_tempo < len(tempos):
        vendedores[indice] = tempos[indice_tempo]
        somas[indice] += 1
        indice_tempo += 1
    else: break

menor_tempo = 0

def passatempo(x):
    return x - menor_tempo

while True:
    menor_tempo = min(vendedores)
    # desconta o tempo
    vendedores = list(map(passatempo, vendedores))

    if indice_tempo < len(tempos):
        prox = tempos[indice_tempo]
    else:
        break

    menor_vendedor = vendedores.index(0)

    vendedores[menor_vendedor] = prox
    somas[menor_vendedor] += 1

    indice_tempo += 1

for i, j in enumerate(somas):
    print(f"{i+1} {j}")