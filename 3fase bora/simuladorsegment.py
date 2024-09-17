class SegmentTree:
    def __init__(self, data):
        self.n = len(data)
        self.tree = [0] * (2 * self.n)
        # Constrói a árvore
        self.build(data)

    def build(self, data):
        # Inicializa as folhas da árvore
        for i in range(self.n):
            self.tree[self.n + i] = data[i]
        # Constrói a árvore interna
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[2 * i] + self.tree[2 * i + 1]

    def update(self, pos, value):
        # Atualiza o valor na posição pos
        pos += self.n
        self.tree[pos] = value
        # Atualiza os nós da árvore
        while pos > 1:
            pos //= 2
            self.tree[pos] = self.tree[2 * pos] + self.tree[2 * pos + 1]

    def query(self, l, r):
        # Retorna a soma no intervalo [l, r)
        l += self.n
        r += self.n
        result = 0
        while l < r:
            if l % 2 == 1:
                result += self.tree[l]
                l += 1
            if r % 2 == 1:
                r -= 1
                result += self.tree[r]
            l //= 2
            r //= 2
        return result

# Inicializa a lista
nm = list(map(int, input().split()))
lista = list(range(1, nm[0] + 1))
segment_tree = SegmentTree(lista)

def inverte(x, y, lista):
    # Inverte a sublista e atualiza a árvore de segmentação
    lista[x-1:y] = lista[x-1:y][::-1]
    for i in range(x-1, y):
        segment_tree.update(i, lista[i])

somas = []

for _ in range(nm[1]):
    instrucao = input().split()
    x = int(instrucao[1])
    y = int(instrucao[2])
    op = instrucao[0]

    if op == "I":
        inverte(x, y, lista)
    elif op == "S":
        somas.append(segment_tree.query(x-1, y))

# Imprime os resultados das somas
for resultado in somas:
    print(resultado)
