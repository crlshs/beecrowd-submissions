a = int(input())
b = int(input())
c = int(input())
d = int(input())

while(True):
    c-=d
    if (c >= a and c<=b):
        print("S")
        break
    elif (c<a):
        print("N")
        break