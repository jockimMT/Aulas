alunos = int(input("Digite a quantidade de alunos: "))

nomes = [input("Digite os nomes dos alunos: ") for i in range(alunos)]
notas = [float(input("Digite as notas dos alunos: ")) for i in range(alunos)]

for i in range(alunos):
    print("Nome do aluno: ", nomes[i], "Nota: ", notas[i])

maior = max(notas)
menor = min(notas)
media = sum(notas) / alunos

print("A media da turma é: ", media)
print("A maior nota é: ", maior)
print("A menor nota é: ", menor)

for i in range(alunos):
    if notas[i] < media:
        print(f"A média da turma é: {media:.2f} A nota do aluno: {nomes[i]} é menor que a média")
    elif notas[i] == media:
        print(f"A média da turma é: {media:.2f} A nota do aluno: {nomes[i]} é igual a média")
    else:
        print(f"A média da turma é: {media:.2f} A nota do aluno: {nomes[i]} é maior que a média")




