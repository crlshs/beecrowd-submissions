def analisa(lista):
    if lista.count("{") != lista.count("}") or len(lista) % 2 != 0:
        return "N"

    stack = []
    for i in lista:
        if i == "{":
            stack.append(i)

        elif i == "}":
            if not stack or stack[-1] != "{":
                return "N"
            stack.pop()
    return "S" if not stack else "N"

n = int(input())

lista = []
for _ in range(n):
    linha = list(input())
    lista.extend(i for i in linha if i == "{" or i == "}")

print(analisa(lista))
