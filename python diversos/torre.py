dimensao = int(input())
matriz = [list(map(int, input().split())) for _ in range(dimensao)]

soma_linhas = [sum(linha) for linha in matriz]
soma_colunas = [sum(matriz[i][j] for i in range(dimensao)) for j in range(dimensao)]

maior_soma = 0

for i in range(dimensao):
    for j in range(dimensao):
        torre = soma_linhas[i] + soma_colunas[j] - 2 * matriz[i][j]
        if torre > maior_soma:
            maior_soma = torre

print(maior_soma)
