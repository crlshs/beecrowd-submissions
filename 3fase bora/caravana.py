n = int(input())
pesos = []
pesos.extend(int(input()) for _ in range(n))

meio = int(sum(pesos) / n)

for i in pesos:
    print((meio - i))