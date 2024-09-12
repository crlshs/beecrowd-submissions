lista_de_inteiros = map(int, input().split())

resultado = [i * 2 if i % 2 == 0 else i * 3 for i in lista_de_inteiros]

print(resultado)