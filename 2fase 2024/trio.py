n = int(input())
numeros = list(map(int, input().split()))
numeros.sort()

possiveis = 0

for i in range(n - 2):
    k = i + 2
    for j in range(i+1, n-1):
        k = max(k, j+1)
        while k < n and numeros[i] + numeros[j] > numeros[k]:
            k += 1
        possiveis += (k - 1) - j

print(possiveis)
