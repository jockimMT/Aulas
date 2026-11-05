nomes = []
N = []
notas = []
i = 0

while True:
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nomes.append(nome)
    nota = float(input(f"Digite a nota do aluno {nomes[i]}: "))
    notas.append(nota)
    N.append((nomes[i], notas[i]))
    i += 1
    
    R = input("Deseja Continuar S/N: ").upper()
    
    if R == 'N':
        break

print(N)
    