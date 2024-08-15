valor = int(input(""))
c1 = int(input(""))
c2 = int(input(""))
c3 = int(input(""))

contas = [c1, c2, c3]
contas.sort()

pagas = 0
for c in contas:
    if valor >= c:
        valor -= c
        pagas += 1

print(pagas)