n = int(input())
alturas = list(map(int, input().split()))

maiorAchado = -1
visiveis = 0
for i in range(n-1,-1,-1):
    if (alturas[i]>maiorAchado):
        visiveis+=1

print(n-visiveis)