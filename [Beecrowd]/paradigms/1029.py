def fibonacci(n,c=0):
    if (n==0): 
        return 0,c+1
    if (n==1):
        return 1,c+1

    f1,c1 = fibonacci(n-1,c+1)
    f2,c2 = fibonacci(n-2,c+1)
    return f1+f2,c1+c2

x = int(input())
for _ in range(x):
    n = int(input())
    c, f = fibonacci(n,0)
    print(f"fib({n}) = {c-1} calls = {f}")