jogos = 0
resultados = []

def getAdj(i,j,m,n):
    direcoes = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),           (0, 1),
        (1, -1),  (1, 0),  (1, 1)
    ]
    vizinhos = []
    for x,y in direcoes:
        x+=i
        y+=j
        if (x>=0 and x<m and y>=0 and y<n):
            vizinhos.append((x,y))
    return vizinhos


while (True):
    m,n = list(map(int, input().split()))
    if (m == 0 and n == 0):break

    jogos+=1

    campo = [[0]*n for _ in range(m)]
    dicas = []
    
    for _ in range(m):
        linha = list(input())
        dicas.append(linha)

    for i in range(m):
        for j in range(n):
            if (dicas[i][j]) == "*":
                campo[i][j] = -1
                v = getAdj(i,j,m,n)
                for x,y in v:
                    if campo[x][y] != -1:
                        campo[x][y]+=1

    saida = [f"Field #{jogos}:"]
    for i in campo:
        linha = ''.join('*' if j == -1 else str(j) for j in i)
        saida.append(linha)
    resultados.append('\n'.join(saida))

print('\n\n'.join(resultados))
