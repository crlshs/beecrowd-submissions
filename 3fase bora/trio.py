n, k = map(int, input().split())
b = list(map(int, input().split()))
b.sort()

# a <= b <= c
# 1 5 7 8 11 15 16
res = []
limite = 0

for i in range(0, len(b)):
    for j in range(i+1, len(b)-1):

        for l in range(j+1, len(b)-2):
            trio = [b[i], b[j], b[l]]
            balanceamento = (b[i] - b[j])**2

            if balanceamento in res: break

            # print(i,j,l,trio,balanceamento)

            if limite != k:
                res.append(balanceamento)
                limite += 1
                print(res, k, "ãia")
            else:
                res.sort()
                if balanceamento < res[-1]:
                    print(res, balanceamento, trio)
                    res.pop()
                    res.append(balanceamento)

print(res)