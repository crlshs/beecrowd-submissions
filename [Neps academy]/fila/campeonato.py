times = list(map(int, input().split()))
novos_times = []
fases = 0

def jogo(lista, fases):
    novos_times = []
    for i in range(0, len(lista), 2):
        partida = [lista[i], lista[i+1]]
        if 1 in partida and 9 in partida:
            return [[0, 0], fases]

        if 1 in partida and 9 not in partida:
            novos_times.append(1)
        elif 9 in partida and 1 not in partida:
            novos_times.append(9)
        else:
            novos_times.append(partida[0])
    fases += 1
    return [novos_times, fases]

resultado = jogo(times, fases)
novos_times = resultado[0]
fases = resultado[1]

while novos_times != [0, 0]:
    resultado = jogo(novos_times, fases)
    novos_times = resultado[0]
    fases = resultado[1]

    if novos_times == [0, 0]: break

if fases == 0: print("oitavas")
if fases == 1: print("quartas")
if fases == 2: print("semifinal")
if fases == 3: print("final")
