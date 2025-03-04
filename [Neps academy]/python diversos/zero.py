n = int(input())

numeros = []

for _ in range(n):
    y = int(input())

    if y:
        numeros.pop()
    else:
        numeros.append(y)

print(sum(numeros))
