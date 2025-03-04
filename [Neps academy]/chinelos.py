n = int(input())
estoque = []
estoque.extend(int(input()) for _ in range(n))

vendas = 0

p = int(input())

for _ in range(p):
    compra = int(input())

    if estoque[compra - 1] > 0:
        vendas += 1
        estoque[compra - 1] -= 1
    else:
        pass

print(vendas)