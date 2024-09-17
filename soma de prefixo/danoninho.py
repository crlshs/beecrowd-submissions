n, d = map(int, input().split())

fileira = list(map(int, input().split()))

sprefixo = [0] * n
sprefixo[0] = fileira[0]
n -= 1

for i in range(1, n):
    sprefixo[i] = sprefixo[i-1] + fileira[i]

maximo = 0
somaatual = 0
l = 0
r = 0
while True:
    if r > n:
        l += 1
        r = l + 0
    if r == n and l == n: break

    intervalo = fileira[l:r]
    somaatual = sum(intervalo)
    if somaatual <= d and maximo < len(intervalo):
        maximo = len(intervalo)

    r += 1

print(maximo)
