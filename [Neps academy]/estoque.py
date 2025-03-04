dimensao = list(map(int,input("").split()))

matriz = []
for _ in range(dimensao[0]):
    linha = list(map(int, input("").split()))
    matriz.append(linha)

numvendas = int(input(""))
vendas = 0
for i in range(numvendas):
    venda = list(map(int, input("").split()))
    if matriz[venda[0]-1][venda[1]-1] > 0:
        matriz[venda[0]-1][venda[1]-1] -= 1
        vendas += 1

print(vendas)