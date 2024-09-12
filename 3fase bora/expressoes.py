n = int(input())

res = []

def analisa(caracteres):

    if caracteres.count("]") != caracteres.count("[") or \
    caracteres.count("(") != caracteres.count(")") or \
    caracteres.count("{") != caracteres.count("}") or \
    len(caracteres) % 2 != 0:
        return "N"

    stack = []
    pares = {')': '(', ']': '[', '}': '{'}

    for char in caracteres:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack[-1] != pares[char]:
                return "N"
            stack.pop()

    return "S" if not stack else "N"

for _ in range(n):
    caracteres = list(input())
    res.append(analisa(caracteres))

for i in res:
    print(i)
