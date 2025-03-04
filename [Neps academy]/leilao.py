numlances = int(input(""))

nomemelhor = ""
valormaior = 0

for i in range(numlances):
    nome = str(input(""))
    lance = int(input(""))

    if lance > valormaior:
        valormaior = lance
        nomemelhor = nome

print(nomemelhor)
print(valormaior)