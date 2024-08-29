n = int(input())
numeros = list(map(int, input().split()))
numeros.sort()

possiveis = 0

for i in range(len(numeros)):
    for j in range(i+1, len(numeros)):
        for k in range(j+1, len(numeros)):
            possiveis += (1 if (numeros[i] + numeros[j] > numeros[k] and numeros[i] + numeros[k] > numeros[j] and numeros[j] + numeros[k] > numeros[i]) else 0)

print(possiveis)
