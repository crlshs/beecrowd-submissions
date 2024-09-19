c, n = map(int, input().split())
caixas = [0] * c

fila = []
t, d = 0, 0

for i in range(n):
    # momento a partir da abertura
    # tempo necessario para atender
    t, d = map(int, input().split())
    caixas[i] += d
    fila.append(t)