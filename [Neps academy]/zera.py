n = int(input())

numeros = []

for _ in range(n):
    x = int(input())
    if x != 0:
        numeros.append(x)
    else:
        numeros.pop()

print(sum(numeros))