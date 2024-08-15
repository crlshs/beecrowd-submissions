diaria = int(input(""))
aumento = int(input(""))
chegada = int(input(""))

acrescimo = 0
dias = 32 - chegada

if chegada < 15:
    acrescimo = chegada - 1
    valor = dias * (diaria + acrescimo * aumento)

if chegada >= 15:
    valor = dias * (diaria + 14 * aumento)

print(valor)