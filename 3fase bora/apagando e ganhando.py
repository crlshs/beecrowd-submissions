res = []
while True:
    nd = list(map(int, input().split()))
    if nd == [0, 0]: break

    numeros = list(input())

    apagar = nd[1]
    resultado = []

    for i in numeros:
        while apagar > 0 and resultado and resultado[-1] < i:
            resultado.pop()
            apagar -= 1
        resultado.append(i)
    
    resultado = resultado[:nd[0] - apagar]

    res.append("".join(str(i)for i in resultado))

for i in res: print(i)