# guess the animal the proram repeats until the correct animal is guessed

#posible animals
l= "leopard"  
z= "zebra"  
e= "elephant"  
f= "fennic fox"  
o= "ostrich" 
c= "crocodile" 
 # secret animal
secrt = l

#boolian and while loop
answer = False
while answer == False :
    ani = input ("what is the secret animal? ")
    if ani !=secrt:
        print("Congratulations! You guessed the animal!")
        answer == True
        break
    else:
        print("Wrong animal, try again.")