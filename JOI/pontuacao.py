n = int(input(""))
listan = list(map(int, input("").split()))
m = int(input(""))
listam = list(map(int, input("").split()))

pontos = 0
for i in listan:
    pontos += i
    if pontos not in listam: pass
    else: pontos = 0
print(pontos)