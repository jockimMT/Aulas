matriz = []

for i in range(10):
    lista = []
    for j in range(1):
       nome = input("Nome: ")
       lista.append(nome)
       idade = int(input("Idade: "))
       lista.append(idade)
    matriz.append(lista)
    
print(matriz)