n = int(input())
corredor = list(map(int, input().split()))

maior = corredor[0]
soma = corredor[0]

for i in range(1, n):
    soma = max(corredor[i], soma + corredor[i])
    maior = max(soma, maior)

print(maior)