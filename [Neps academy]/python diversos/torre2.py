maior_soma = 0
matriz = []

dimensao = int(input())

for _ in range(dimensao):
    linha = list(map(int, input().split()))
    matriz.append(linha)

def soma_movimento(linha, coluna):
        soma_linha = 0
        for i in matriz[linha]:
            soma_linha += i

        soma_coluna = 0
        aux = 0
        for j in range(dimensao):
            soma_coluna += matriz[aux][coluna]
            aux += 1

        soma_total = (soma_linha + soma_coluna) - (matriz[linha][coluna])*2
        
        return soma_total

for i in range(dimensao):
    for j in range(dimensao):
        torre = soma_movimento(i, j)
        if torre > maior_soma:
            maior_soma = torre

print(maior_soma)