res = []
while True:
    nd = list(map(int, input().split()))
    if nd == [0, 0]: break

    apagar = nd[1]
    numeros = list(input())

    for i in range(apagar):
        num = numeros.index(min(numeros))
        numeros.pop(num)
    res.append("".join(str(i)for i in numeros))

for i in res: print(i)