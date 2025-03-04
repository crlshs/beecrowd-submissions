n, k = map(int, input().split())
lista = list(map(int, input().split()))

somaprefixo = [0] * n
somaprefixo[0] = lista[0]

for i in range(1, n):
    somaprefixo[i] = somaprefixo[i-1] + lista[i]

def contar_sequencias(n, k, lista):
    soma_atual = 0
    quantidade = 0
    # soma : quantidade que ela aparece;
    soma_prefixo_count = {0: 1}

    for i in lista:
        soma_atual += i

        if soma_atual - k in soma_prefixo_count:
            quantidade += soma_prefixo_count[soma_atual - k]

        if soma_atual in soma_prefixo_count:
            soma_prefixo_count[soma_atual] += 1
        else:
            soma_prefixo_count[soma_atual] = 1

    return quantidade

print(contar_sequencias(n, k, lista))