lista = []
matriz = []
médias = []


NQ = int(input("Quantas notas de cada aluno deseja colocar? "))

while True:
    for i in range(1):
        lista = []
        lista.append(input("Nome: "))
        soma = 0
        
        for j in range(NQ):
            n = float(input("Digite a nota: "))
            lista.append(n)
            
            soma = soma + n
            
        médias.append(soma/NQ)
        matriz.append(lista)
        
    R = input("Deseja Continuar S/N: ").upper()
    
    if R == 'N':
        break



for i in range(len(matriz)):
    print(f"A média do aluno {matriz[i][0]} foi {médias[i]}")
