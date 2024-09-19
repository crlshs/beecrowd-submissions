n = int(input())

res = []

def analisa(caracteres):

    if caracteres.count("]") != caracteres.count("[") or \
    caracteres.count("(") != caracteres.count(")") or \
    caracteres.count("{") != caracteres.count("}") or \
    len(caracteres) % 2 != 0:
        return "N"

    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}

    for char in caracteres:
        if char in "({[":
            pilha.append(char)
        elif char in ")}]":
            if not pilha or pilha[-1] != pares[char]:
                return "N"
            pilha.pop()

    return "S" if not pilha else "N"

for _ in range(n):
    caracteres = list(input())
    res.append(analisa(caracteres))

for i in res:
    print(i)
