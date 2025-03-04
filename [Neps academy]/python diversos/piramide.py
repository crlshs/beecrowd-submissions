dimensao = int(input(""))

matriz = []

for i in range(dimensao):
    linha = list(map(int, input("").split()))
    matriz.append(linha)

print(matriz)