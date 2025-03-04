n = int(input())
corredor = list(map(int, input().split()))

somaprefixo = [0] * n
somaprefixo[0] = corredor[0]

for i in range(1, n):
    somaprefixo[i] = somaprefixo[i-1] + corredor[i]

left = 1
right = 0
maior = somaprefixo[0]

while left != n:
    right += 1
    if right != n:
        satual = somaprefixo[right] - somaprefixo[left-1]
        if satual > maior: 
            maior = satual
    else:
        right = left + 0
        left += 1

print(maior)