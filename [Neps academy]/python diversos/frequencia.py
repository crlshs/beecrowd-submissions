alunos = {-1}
n = int(input())

for _ in range(n):
    aluno = int(input())
    alunos.add(aluno)

print(len(alunos)-1)