aero_voos = list(map(int,input("").split()))

matriz = [[0] * aero_voos[0] for _ in range(aero_voos[0])]

for i in range(aero_voos[1]):
    voo = list(map(int,input("").split()))
    matriz[voo[0]-1][voo[1]-1] = 1

S = False

for j in matriz:
    qnt = 0
    for i in j:
        if i == 1:
            qnt += 1
    if qnt == (aero_voos[0] - 1):
        S = True
        break

if S: print("S")
else: print("N")

