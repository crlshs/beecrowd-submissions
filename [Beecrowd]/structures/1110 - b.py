from collections import deque
# menor complexidade usando o deque

while True:
    n = int(input())
    if n == 0: break

    pilha = deque(range(1, n + 1))
    descarte = []

    while len(pilha) > 1:
        descarte.append(pilha.popleft()) 
        pilha.append(pilha.popleft()) 

    print(f"Discarded cards: {', '.join(map(str, descarte))}")
    print(f"Remaining card: {pilha[0]}")
