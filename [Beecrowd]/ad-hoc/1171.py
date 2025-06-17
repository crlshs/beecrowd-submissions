n = int(input())
frequencia = {}
for _ in range(n):
    x = int(input())
    try:
        frequencia[x] +=1
    except KeyError:
        frequencia[x] = 1
ordem = list(frequencia.keys())
ordem.sort()

for c in ordem:
    print(f"{c} aparece {frequencia[c]} vez(es)")