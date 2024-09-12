class Arvore:
    def __init__(self, lista):
        self.n = len(lista)
        self.arvore = [0] * (self.n * 2)
        self.contruir(lista)

    def contruir(self, lista):
        for i in range(self.n):
            self.arvore[self.n + i] = lista[i]

        for i in range(self.n - 1, 0, -1):
            self.arvore[i] = self.arvore[2 * i] + self.arvore[2 * i + 1]

    def atualizar(self, posicao, valor):
        posicao += self.n
        self.arvore[posicao] = valor

        while posicao > 1:
            posicao //= 2
            self.arvore[posicao] = self.arvore[2 * posicao] + self.arvore[2 * posicao + 1]

    def soma_intervalo(self, esquerda, direita):
        esquerda += self.n
        direita += self.n
        soma = 0
        while esquerda < direita:
            if esquerda % 2 == 1:
                soma += self.arvore[esquerda]
                esquerda += 1
            if direita % 2 == 1:
                direita -= 1
                soma += self.arvore[direita]
            esquerda //= 2
            direita //= 2
        return soma
    
    def inverter_intervalo(self, esquerda, direita):
        esquerda += self.n
        direita += self.n
        while esquerda < direita:
            self.arvore[esquerda], self.arvore[direita - 1] = self.arvore[direita - 1], self.arvore[esquerda]
            esquerda += 1
            direita -= 1

        for i in range((esquerda + self.n) // 2, 0, -1):
            self.arvore[i] = self.arvore[2 * i] + self.arvore[2 * i + 1]

####

nm = list(map(int, input().split()))
lista = [i for i in range(1, nm[0] + 1)]

arvore_segmentada = Arvore(lista)

somas = []

for _ in range(nm[1]):
    instrucao = input().split()
    x = int(instrucao[1]) - 1
    y = int(instrucao[2])
    operacao = instrucao[0]

    if operacao == "I":
        arvore_segmentada.inverter_intervalo(x, y)
    elif operacao == "S":
        soma_atual = arvore_segmentada.soma_intervalo(x, y)
        somas.append(soma_atual)

for s in somas:
    print(s)

