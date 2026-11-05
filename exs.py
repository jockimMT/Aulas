from random import randint

f = 100
N1 = 1000
    
while f != N1:
    N1 = randint(0,10) 
    f = int(input("Advinhe um número de 0 a 10: "))
    
    if f == N1:
        print("You win")

    elif f < N1:
        print("You lost, seu número é menor")

    else:
        print("You lost, seu número é maior") 
        


    
      
