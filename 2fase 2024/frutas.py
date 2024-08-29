rn = list(map(int, input().split()))

dinheiro = rn[0]
vezes = 0
frutas = []
fruta_preco = {}

for i in range(rn[1]):
    dupla = list(map(int, input().split()))

    if dupla[0] not in fruta_preco.keys():
        fruta_preco[dupla[0]] = dupla[1]

    else:
        if fruta_preco[dupla[0]] > dupla[1]:
            fruta_preco[dupla[0]] = dupla[1]

for f in fruta_preco.values():
    frutas.append(f)

frutas.sort()
for i in frutas:
    if dinheiro >= i: 
        dinheiro -= i
        vezes += 1
    else:
        break

print(vezes)
