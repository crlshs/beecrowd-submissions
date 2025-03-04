lista = list(map(int, input("").split()))

passou = False
if lista[0] == lista[2] and lista[1] != lista[3]:
    passou = True
elif lista[0] != lista[2] and lista[1] == lista[3]:
    passou = True

print("V" if passou else "F")