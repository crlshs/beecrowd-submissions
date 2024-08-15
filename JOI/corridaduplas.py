n = int(input(""))
lista = list(map(int, input("").split()))

res = 0
for i in lista:
    if lista.count(i) != 2:
        res = i

print(res)