alunos = int(input("Digite a quantidade de alunos: "))

nomes = []
N = []
notas = []
for i in range(alunos):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nomes.append(nome)
    nota = float(input(f"Digite a nota do aluno {nomes[i]}: "))
    notas.append(nota)
    N.append((nomes[i], notas[i]))
    
for i in range(alunos):
    if notas[i] < 7:
        print("Nome do aluno: ", N[i][0], " Nota: ", N[i][1], " Reprovado")
    elif notas[i] == 7:
        print("Nome do aluno: ", N[i][0], " Nota: ", N[i][1], " Aprovado")
    else:
        print("Nome do aluno: ", N[i][0], " Nota: ", N[i][1], " Aprovado com louvor")
     