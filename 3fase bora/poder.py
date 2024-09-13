lc = list(map(int, input().split()))
l = lc[0]
c = lc[1]

matrizoriginal = []
matrizoriginal.extend([[0]* (c + 2)])
for _ in range(l):
    linha = []
    linha = list(map(int, input().split()))
    linha.insert(0, 0)
    linha.append(0)
    matrizoriginal.append(linha)
matrizoriginal.extend([[0]* (c + 2)])

def get_ortogonal(matriz, i, j, valor):
    direita = matrizoriginal[i][j+1]
    esquerda = matrizoriginal[i][j-1]
    cima = matrizoriginal[i-1][j]
    baixo = matrizoriginal[i+1][j]

    idireita = (i, j+1)
    iesquerda = (i, j-1)
    icima = (i-1, j)
    ibaixo = (i+1, j)
    indices = [idireita, iesquerda, icima, ibaixo]

    valores = [i for i in [direita, esquerda, cima, baixo] if i != -1]

atual = matrizoriginal[1][1]
matrizpoderes = [[0] * c] * l

linha = 0
coluna = 0
restantes = l * c

while True:
    coluna += 1
    if coluna > c:
        coluna = 1
        linha += 1

    matriztemp = matrizoriginal.copy()

    viva = True
    atual = matriztemp[linha][coluna]
    while viva:
        maiorvalor = get_ortogonal[0](matriztemp, linha, coluna)
        maiorindice = get_ortogonal[1](matriztemp, linha, coluna)

        atual = matriztemp[maiorindice[0]][maiorindice[1]]
