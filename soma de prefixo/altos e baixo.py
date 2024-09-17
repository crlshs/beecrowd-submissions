n = int(input())
seq = list(input())
precos = [0] * n

for i in range(1, n):
    if seq[i-1] == "A":
        precos[i] = precos[i-1] + 1

    if seq[i-1] == "B":
        precos[i] = precos[i-1] - 1

menor = min(precos)
ajuste = 0 - menor
precos = [i + ajuste for i in precos]

print(" ".join(map(str, precos)))