n = int(input())

lista = list(map(int,input().split()))

op = 0

somainicio = 0
somafinal = n - 1

esquerda = lista[somainicio]
direita = lista[somafinal]

while somainicio < somafinal:

    if somainicio == somafinal:
        somainicio += 1
        somafinal -= 1
        esquerda = lista[somainicio]
        direita = lista[somafinal]

    elif somafinal < somainicio:
        op += 1
        somafinal -= 1
        direita += lista[somafinal]

    else:
        op += 1
        somainicio += 1
        esquerda += lista[somainicio]

print(op)