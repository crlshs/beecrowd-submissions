n = int(input())

meio = 0
if n > 2: 
    pivo = n - 2
    meio = (pivo**2)*6

print((((pivo)**2)*pivo) if n > 2 else 0)
print(meio)
print((pivo*12)if n > 2 else 0)
print(8)