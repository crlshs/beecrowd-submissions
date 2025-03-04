k_n = list(map(int, input().split()))

alfabeto = input()
mensagem = input()

alfabeto = set(alfabeto)
mensagem = set(mensagem)

a = alfabeto.intersection(mensagem)

print("S" if a == mensagem else "N")