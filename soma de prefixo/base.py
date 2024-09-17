lista_original = list(map(int, input().split()))

# cria uma lista com n 0's
s_prefixo = [0] * len(lista_original)

# o primeiro elemento é igual
s_prefixo[0] = lista_original[0]

# na lista s_prefixo, na posicao i, eu tenho a soma dos elementos da lista_original da posicao 0 até a posição i

# 1 2 3 4 5
# 1 3 (1 + 2)
# 1 3 6 (1 + 2 + 3)
# 1 3 6 10 (1 + 2 + 3 + 4) e etc

for i in range(1, len(lista_original)):
    s_prefixo[i] = s_prefixo[i-1] + lista_original[i]

left = 2
right = 6

# para somar um intervalo da lista, basta pegar o elemento s_prefixo[right] (elemento da direita) - s_prefixo[left-1]

print(f"{lista_original}\n{s_prefixo}")

print(s_prefixo[right] - s_prefixo[left-1])