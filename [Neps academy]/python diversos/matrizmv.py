matriz = []

maior_valor = -9999
for i in range(0, 3):
    x = int(input())
    if x > maior_valor: maior_valor = x

    y = int(input())
    if y > maior_valor: maior_valor = y

    z = int(input())
    if z > maior_valor: maior_valor = z

    linha = [x, y, z]
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz)):
        if matriz[i][j] == maior_valor: matriz[i][j] = -1

for linha in matriz:
    for coluna in linha:
        print(coluna, end=" ")
    print()
