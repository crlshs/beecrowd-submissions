n = int(input())
alturas = list(map(int, input().split()))

m = max(alturas)
s = 0
maiorAchado = alturas[-1]
# 180 180 170 190 150

# 1 1 2 1 1
# 999 10 9 777 8 3 1
if n > 2:
    for i in range(n-1,-1,-2):
        atual = alturas[i]
        anterior = alturas[i-1]

        if (i<n-1):
            prox = alturas[i+1]
        else: prox = -11

        if (atual > maiorAchado):
            maiorAchado = atual
            # print("a")
        if (prox > maiorAchado):
            maiorAchado=prox
            # print("b")

        if (atual == m):
            s+=i
            break
        elif (anterior == m):
            s+=i-1
            break

        if (atual <= maiorAchado):
            if (i != n-1):
                s+=1

        if (anterior <= maiorAchado):
            s+=1

        # if (prox>= atual):
        #     s+=1
        # 10 9 8 7 6 5 4 3 5 1
        # if (anterior <= atual):
        #     s+=1

elif n ==2:
    if alturas[0] <= alturas[1]:
        s+=1
print(s)