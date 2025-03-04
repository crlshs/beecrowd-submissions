n = int(input())
matriz = []

for i in range(n):
    linha = list(map(int, input().split()))
    matriz.append(linha)

res = 0
somasl = []
somasc = []
somasd = []

# soma diagonais

somad = 0
for i in range(n):
    somad += matriz[i][i]
somasd.append(somad)

somad = 0
aux = n - 1
for i in range(n):
    somad += matriz[i][aux]
    aux -= 1
somasd.append(somad)

if somasd[0] != somasd[1]: 
    res = -1
else:
    res = somasd[0]

if res != -1:
    # soma linhas
    for i in matriz:
        somal = 0
        for j in i:
            somal += j
        somasl.append(somal)

    for i in range(n):
        if somasl[i] != res: 
            res = -1
            break

if res != -1:
    # soma colunas
    aux = 0
    for j in range(n):
        somac = 0
        for i in range(n):
            somac += matriz[i][aux]
        somasc.append(somac)
        aux += 1

    for i in range(n):
        if somasc[i] != res: 
            res = -1
            break

print(res)

