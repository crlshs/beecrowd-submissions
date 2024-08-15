# olimpiada japonesa 2017
n = int(input(""))
sequencia = str(input(""))

atual = 1
vezes = 0
for i in sequencia:
    if i == "L" and atual != 1: atual -= 1
    elif i == "R" and atual != 3: atual += 1

    if atual == 3: vezes += 1

print(vezes)

