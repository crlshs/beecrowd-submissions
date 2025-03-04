n = int(input())
fila = list(map(int, input().split()))
m = int(input())
desistentes = set(map(int, input().split()))

res = [str(i) for i in fila if i not in desistentes]

print(" ".join(res))