nm = list(map(int, input().split()))
lista = list(range(1, nm[0] + 1))
soma_prefixo = [0] * (len(lista) + 1)
atualizado = True

def inverte(x: int, y: int, lista: list):
    while x < y:
        lista[x - 1], lista[y - 1] =  lista[y - 1], lista[x - 1]
        x += 1
        y -= 1

def construir_sprefixo(lista):
    for i in range(1, len(lista) + 1):
        soma_prefixo[i] = soma_prefixo[i - 1] + lista[i - 1]

#
somas = []
construir_sprefixo(lista)

for _ in range(nm[1]):
    instrucao = list(str(input()).split())
    x = int(instrucao[1])
    y = int(instrucao[2])
    op = instrucao[0]

    if op == "I":
        inverte(x, y, lista)
        atualizado = False

    elif op == "S":
        if not atualizado:
            construir_sprefixo(lista)
            atualizado = True

        somas.append(soma_prefixo[y] - soma_prefixo[x - 1])

for i in somas:
    print(i)