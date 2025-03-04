n = int(input(""))
palavra = str(input(""))

pt1 = ""
pt2 = ""
for i in range(int(n/2)):
    pt1 += palavra[i]
    pt2 += palavra[i+(int(n/2))]

print("Yes" if pt1 == pt2 else "No")