n = int(input())

vezes = 0

while n > 0:
    nstr = list(str(n))
    atual = int(max(nstr))
    n -= atual
    vezes += 1

print(vezes)
