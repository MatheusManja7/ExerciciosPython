import random

def sortearAluno(quantidade_aluno):
    alunos = []

    for i in range(quantidade_aluno):
        nome = input(f"Digite o Nome do Aluno {i+1}: ")
        alunos.append(nome)

    sortear = random.choice(alunos)

    return sortear

print()
quantidade = int(input("Digite a Quantidade: "))
print("<------------------------------------>")
primeiro_aluno = sortearAluno(quantidade)
print("<-------------------------------------------------->")
print(f"O primeiro aluno(a) a apresentar será: {primeiro_aluno}")   

