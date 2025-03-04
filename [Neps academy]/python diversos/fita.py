n = int(input(""))
lista = list(map(int, input("").split()))

posicoes = [i for i,j in enumerate(lista) if j == 0]

resposta = []

for i in range(n):
    menor = n
    for j in posicoes:
        dist = abs(j - i)
        if dist < menor: menor = dist
    
    resposta.append(menor if menor <= 9 else 9)

print(" ".join(map(str, resposta)))