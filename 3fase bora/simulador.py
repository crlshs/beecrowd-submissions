nm = list(map(int, input().split()))

lista = []
lista.extend(i for i in range(1,(nm[0]+1)))

def inverte(x: int, y: int, lista: list):
    x -= 1
    y -= 1

    while x < y:
        lista[x], lista[y] = lista[y], lista[x]
        x += 1
        y -= 1
    return lista

def construir_sprefixo(lista):
    soma_prefixo = [0] * (len(lista) + 1)
    for i in range(1, len(lista) + 1):
        soma_prefixo[i] = soma_prefixo[i - 1] + lista[i - 1]
    return soma_prefixo

def soma(x: int, y: int, soma_prefixo: list):
    return soma_prefixo[y] - soma_prefixo[x - 1]

#
somas = []

for _ in range(nm[1]):
    instrucao = list(str(input()).split())
    x = int(instrucao[1])
    y = int(instrucao[2])
    op = instrucao[0]

    if op == "I":
        lista = inverte(x, y, lista)
    elif op == "S":
        soma_prefixo = construir_sprefixo(lista)
        somas.append(soma(x, y, soma_prefixo))

for i in somas:
    print(i)