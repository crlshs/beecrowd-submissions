n = int(input(""))
m = int(input(""))
s = int(input(""))

achou = False

for i in range(m, n, -1):
    num = str(i)
    numlista = []
    soma = 0

    for j in num:
        numlista.append(int(j))
    
    for k in numlista:
        soma += k
    
    if soma == s:
        achou = True
        break

print(num if achou else -1)