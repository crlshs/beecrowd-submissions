t = int(input())
for _ in range(t):
    # dinheiro, ingredientes, quantidade de bolos   
    d,i,b = list(map(int, input().split()))
    precos = list(map(int, input().split()))
    bolos = []
    for j in range(b):
        # indice do ingrediente,quantidade
        entrada = list(map(int, input().split()))
        n = entrada[0]
        ingredientes = [(entrada[j], entrada[j + 1]) for j in range(1, 2 * n, 2)]
        bolos.append(ingredientes)
    maior = 0

    for x in bolos:
        custos = sum(precos[i]*q for i,q in x)
        feitos =d//custos
        
        if feitos>maior:
            maior = feitos
    print(maior)
