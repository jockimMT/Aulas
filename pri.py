n = int(input('Digite um número: '))
divisores = 0
ask = 's'

while ask == 's':
    for i in range(1,n+1):
        if n % i == 0:
            divisores += 1
            print(f"{i} é divisor de {n}")
            
    if divisores == 2:
        print(f"{n} é primo")
    else:
        print(f"{n} não é primo")
        
    ask = input("Deseja continuar? (s/n): ").lower()
    
    while ask != 's' and ask != 'n':
        print("Opção inválida. Tente novamente.")
        ask = input("Deseja continuar? (s/n): ").lower()
    
    if ask == 's':
        n = int(input("Digite um número: "))
        divisores = 0 
    elif ask == 'n':
        print("Programa encerrado.")