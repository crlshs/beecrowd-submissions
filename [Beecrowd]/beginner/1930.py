v = list(map(int, input().split()))
v.sort()

total = ((v[0]-1) + v[3])-2 + v[1] + v[2]

print(total)
