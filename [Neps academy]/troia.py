n, m = map(int,input().split())

restantes = {i for i in range(1, n+1)}

dupla = tuple(map(int, input().split()))
familias = [[dupla[0], dupla[1]]]
adotados = {dupla[0], dupla[1]}

for _ in range(m-1):
    dupla = tuple(map(int, input().split()))
    esta = False
    for i in familias:
        if dupla[0] in i and dupla[1] not in i:
            i.append(dupla[1])
            adotados.add(dupla[1])
            esta = True
            break

        elif dupla[0] not in i and dupla[1] in i:
            i.append(dupla[0])
            adotados.add(dupla[0])
            esta = True
            break

        if dupla[0] in i and dupla[1] in i:
            esta = True
            break

    if not esta:
        familias.append([dupla[0], dupla[1]])
        adotados.add(dupla[0])
        adotados.add(dupla[1])

sozinhos = adotados.symmetric_difference(restantes)

print(len(familias) + len(sozinhos))