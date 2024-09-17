# 2 4 6 8 10
# 2 6 12 20 30

def inverte(x: int, y: int, lista: list):
    lista[x:y+1] = lista[x:y+1][::-1]

for i in range(2, len(lista) + 1):
    soma_prefixo[i] = soma_prefixo[i - 1] + lista[i]