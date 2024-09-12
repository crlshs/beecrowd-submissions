n = int(input())
precos = []

for _ in range(n):
    precos.append(int(input()))

precos.sort()

precos = precos[(len(precos) % 3):]

print(precos)

print(sum(precos))
