p, r = map(int, input().split())
# participantes - rodadas

vencedores = []

while r != 0:
    fila = list(map(int, input().split()))
    for _ in range(r):
        instrucao = list(map(int, input().split()))
        ordem = instrucao[1]
        acoes = instrucao[2:]
        fila = [j for i, j in enumerate(fila) if acoes[i] == ordem]

    vencedores.append(fila[0])
    p, r = map(int, input().split())

for i in range(0, len(vencedores)):
    print(f"Teste {i+1}")
    print(vencedores[i])
    print()