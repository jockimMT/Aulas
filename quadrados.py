tipo = input("Qual combustivel? (A/G): ").upper()
litros = float(input("Quantos litros? "))

if tipo == 'A':
    if litros <= 20:
        valor = (litros * 1.9) * 0.97
    else:
        valor = (litros * 1.9) * 0.95
elif tipo == 'G':
    if litros <= 20:
        valor = (litros * 2.5) * 0.96 
    else:
        valor = (litros * 2.5) * 0.94
        
print(f"Valor a pagar: {valor:.2f}")



