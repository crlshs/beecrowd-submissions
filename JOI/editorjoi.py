n = int(input(""))
palavra = str(input(""))
palavra = list(palavra)

for i in range(0, n):
    if i != n-1:
        if palavra[i] == palavra[i+1]:
            palavra[i] = palavra[i].upper()
            palavra[i+1] = palavra[i+1].upper()

print("".join(map(str, palavra)))