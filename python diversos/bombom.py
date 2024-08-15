#A = Ás, J = Valete, Q = Dama, K = Rei
#C = Copas, E = Espadas, O = Ouros, P = Paus

# tabela = {"A":10, "J":11, "Q":12, "K":13}

dominante = list(str(input("")))
luana = []
edu = []
pluana = 0
pedu = 0

for _ in range(3):
    par = list(str(input("")))
    luana.append(par)

for _ in range(3):
    par = list(str(input("")))
    edu.append(par)

for lista in luana:
    if lista[0] == "A": pluana += 10
    elif lista[0] == "J": pluana += 11
    elif lista[0] == "Q": pluana += 12
    elif lista[0] == "K": pluana += 13
    if lista[1] == dominante[1]: pluana += 4 

for lista in edu:
    if lista[0] == "A": pedu += 10
    elif lista[0] == "J": pedu += 11
    elif lista[0] == "Q": pedu += 12
    elif lista[0] == "K": pedu += 13
    if lista[1] == dominante[1]: pedu += 4 

if pluana == pedu: 
    vencedor = "empate"
elif pedu > pluana: 
    vencedor = "Edu"
else: 
    vencedor = "Luana"

print(vencedor)