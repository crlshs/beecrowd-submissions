while (True):
    n = int(input())
    if n == 0: break
    ordem = list(map(int,input().split()))
    maria = ordem.count(0)
    joao = ordem.count(1)
    print(f"Mary won {maria} times and John won {joao} times")