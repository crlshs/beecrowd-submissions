sal_tun = list(map(int, input("").split()))

matriz = [[0] * (sal_tun[0]+1) for _ in range(sal_tun[0]+1)]

for _ in range(sal_tun[1]):
    conexao = list(map(int, input("").split()))
    matriz[conexao[0]][conexao[1]] = 1
    matriz[conexao[1]][conexao[0]] = 1

qntpasseios = int(input(""))
passeios = []

for _ in range(qntpasseios):
    passeio = list(map(int, input("").split()))
    passeios.append(passeio)

impossivel = 0

for p in passeios:
    pos = 0
    for i in p:
        pos += 1
        if pos == (p[0]):
            break

        dupla = [p[pos], p[pos+1]]
        
        if matriz[dupla[0]][dupla[1]] == 0:
            impossivel += 1
            break

print(qntpasseios - impossivel)