class SegmentosMemoria:
    def __init__(self, n):
        self.n = n
        self.interv = [(1, n)]  # Inicializa o intervalo de memória

    def mod(self, x):
        return x if x > 0 else -x  # Retorna o valor absoluto

    def cortar(self, a):
        if a >= self.n or a <= 0:
            return
        soma = 0
        for i in range(len(self.interv)):
            qtd = self.mod(self.interv[i][0] - self.interv[i][1]) + 1
            if soma + qtd > a:
                id_ = i
                break
            soma += qtd
        meio = 0
        a -= soma
        if a == 0:
            return
        novo = None
        if self.interv[id_][0] <= self.interv[id_][1]:
            meio = self.interv[id_][0] + a
            novo = (meio, self.interv[id_][1])
            self.interv[id_] = (self.interv[id_][0], meio - 1)
        else:
            meio = self.interv[id_][0] - a
            novo = (meio, self.interv[id_][1])
            self.interv[id_] = (meio + 1, self.interv[id_][1])
        self.interv.append(novo)
        for i in range(len(self.interv) - 1, id_ + 1, -1):
            self.interv[i], self.interv[i - 1] = self.interv[i - 1], self.interv[i]

    def soma(self, a, b):
        soma = 0
        resposta = 0
        for i in range(len(self.interv)):
            qtd = self.mod(self.interv[i][0] - self.interv[i][1]) + 1
            if soma + qtd >= a and soma + qtd <= b:
                resposta += (self.interv[i][0] + self.interv[i][1]) * qtd // 2
            soma += qtd
        return resposta

    def inverter(self, a, b):
        soma = 0
        ini = fim = -1
        for i in range(len(self.interv)):
            if soma == a - 1:
                ini = i
            qtd = self.mod(self.interv[i][0] - self.interv[i][1]) + 1
            if soma + qtd == b:
                fim = i
            soma += qtd
        for i in range(ini, (ini + fim) // 2 + 1):
            self.interv[i], self.interv[fim - (i - ini)] = self.interv[fim - (i - ini)], self.interv[i]
        for i in range(ini, fim + 1):
            self.interv[i] = (self.interv[i][1], self.interv[i][0])

if __name__ == "__main__":
    n, m = map(int, input().split())  # Lê n e m
    segmentos_memoria = SegmentosMemoria(n)
    for _ in range(m):
        op, a, b = input().split()  # Lê a operação e os valores a e b
        a, b = int(a), int(b)
        segmentos_memoria.cortar(a - 1)
        segmentos_memoria.cortar(b)
        if op == 'S':
            print(segmentos_memoria.soma(a, b))
        elif op == 'I':
            segmentos_memoria.inverter(a, b)