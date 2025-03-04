n = int(input())
s = [100, 50, 25, 10, 5, 1]

contador = 0

for i in s:
    if n >= i:
        contador += 1 * int(n / i)
        n -= i * int(n / i)

print(contador)