equipes = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]

def fase(equipes, num_jogos):
    novas_equipes = []
    for i in range(num_jogos):
        jogo = list(map(int, input().split()))
        if jogo[0] > jogo[1]:
            novas_equipes.append(equipes[2 * i])
        else:
            novas_equipes.append(equipes[2 * i + 1])
    return novas_equipes

equipes = fase(equipes, 8)
equipes = fase(equipes, 4)
equipes = fase(equipes, 2)
equipes = fase(equipes, 1)

print(equipes[0].title())