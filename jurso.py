ask = 's'

while ask == 's':
    mont1 = float(input("Informe o montante mensal: "))
    taxa = float(input("Informe a taxa mensal: "))
    mont = mont1

    for i in range(1, 12):
        mont = mont + (mont * (taxa / 100))
        mont = mont + mont1
        print(f"Após {i + 1} meses, o montante é: {mont:.2f}")
        
    print(f"Após 1 ano, o montante é: {mont:.2f}")
    
    ask = input("Deseja continuar? (s/n): ").lower()
    while ask != 's' and ask != 'n':
        print("Opção inválida. Tente novamente.")
        ask = input("Deseja continuar? (s/n): ").lower()
        if ask == 'n':
            print("Programa encerrado.")

