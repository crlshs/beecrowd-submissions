nm = list(map(int, input().split()))

matriz = []

for _ in range(nm[0]):
    linha = list(map(int, input().split()))

    matriz.append(linha)

poderes = []
possibilidades = nm[0] * nm[1]

def menor_vizinha(m, linha, coluna):
    direita = m[linha][coluna+1]
    esquerda = m[linha][coluna-1]
    baixo = m[linha+1][coluna]
    cima = m[linha-1][coluna]

for i in range(nm[0]):
    for j in range(nm[1]):
        print(menor_vizinha(matriz, i, j))
