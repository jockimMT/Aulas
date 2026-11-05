mes = int(input("Qual o mês: "))

while mes < 1 or mes > 12:
    mes = int(input("Valor inválido tente novamente: "))

if (mes == 2):
    ano = int(input("Qual ano? "))

    if (ano % 4 == 0) and (ano % 100 != 0) or (ano % 400 == 0):
        print(f"O mês {mes} do ano {ano} tem 29 dias")

    else:
        print(f"O mês {mes} do ano {ano} tem 28 dias")

elif (mes == 1) or (mes == 3) or (mes == 5) or (mes == 7) or (mes == 8) or (mes == 10) or (mes == 12):
    print(f"O mês {mes} tem 31 dias")

else:
    print(f"O mês {mes} tem 30 dias")


