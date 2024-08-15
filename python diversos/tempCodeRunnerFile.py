n = int(input())

numeros = []

for i in range(n):
    y = int(input())

    if y == 0:
        numeros.pop()
    else:
        numeros.append(y)

print(sum(numeros))
