e = int(input())
s = int(input())
l = int(input())

# e até s; s até l
# e até l; l até s
d1 = abs((e-s)) + abs(l-s) + abs(l-e)

print(d1)