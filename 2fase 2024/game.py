n = int(input())
sequencia = list(str(input()))

atual = 1

for i, j in enumerate(sequencia):
    if j == "E":
        atual = 2 * atual

    elif j == "D":
        atual = 2 * atual + 1

print(atual)