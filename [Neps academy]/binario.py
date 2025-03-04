n = int(input())
res = []

while True:
    if n == 0: 
        break

    resto = n % 2
    n = int(n/2)
    res.append(resto)

    if n == 1: 
        res.append(1)
        break

while True:
    if not res: break
    if res[-1] == 0: res.pop()
    else: break

if n != 0:
    for i in range(len(res)-1, -1, -1):
        print(res[i], end="")
else:
    print(0)