k, n, m = map(int, input().split())
ordematual = []

matrizadj = [[0] * (n+2)] * (n+2)

for _ in range(m):
    x, y = map(int, input().split())
    matrizadj[x][y] = 1
    # 0 1 1 1 0
    if matrizadj[x].count(1) == k and matrizadj[x] not in ordematual:
        print(matrizadj[x])
        ordematual.append(x)

print(ordematual)