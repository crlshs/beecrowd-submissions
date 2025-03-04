n, q = map(int, input().split())

matriz = []
valores = []

for _ in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

def vizinhos(i, j, matriz):
    direita = matriz[i][j+1]
    esquerda = matriz[i][j-1]
    cima = matriz[i-1][j]
    baixo = matriz[i+1][j]

    vizinhas = []
    if j+1 != q: vizinhas.append([direita, (i, j+1)])
    if j-1 > 0: vizinhas.append([esquerda, (i, -1)])
    if i-1 > 0: vizinhas.append([cima, (i-1, j)])
    if i+1 != n: vizinhas.append([baixo, (i+1, j)])

    return vizinhas

matrizresposta = []

linha = 0
coluna = 0
while linha != n and coluna != q:
    atual = matriz[linha][coluna]
    soma = atual + 0

    vizinhas = vizinhos(linha, coluna, matriz)
    matrizcopy = matriz.copy()

    while True:
        if min(vizinhas[0]) > atual:
            matrizresposta[linha][coluna] = soma
            break
