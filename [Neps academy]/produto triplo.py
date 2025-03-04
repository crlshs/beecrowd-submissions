n = int(input())
lista = list(map(int, input().split()))

maior = max(
    lista[-1] * lista[-2] * lista[-3],
    lista[0] * lista[1] * lista[-1]
)
print(maior)