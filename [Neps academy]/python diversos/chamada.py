nk = list(map(int, input().split()))
nomes = []

for _ in range(nk[0]):
    nomes.append(input())

nomes.sort()
print(nomes[nk[1]-1])