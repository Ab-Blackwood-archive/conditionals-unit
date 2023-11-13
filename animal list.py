"""""
guess the animal the proram repeats until the correct animal is guessed when the correct animal is guessed 
then the program outputs the amount of correct ansewers out of the total attempts
"""""
#posible animals
l= "leopard"  
z= "zebra"  
e= "elephant"  
f= "fennic fox"  
o= "ostrich" 
c= "crocodile" 
 # secret animal
secrt = e

#boolian loop and answer counter
x = 0
y = 0
play = True
#code
while play :
    ani = input ("what is the secret animal? ")
    if ani == secrt:
        print("Congratulations! You guessed the animal!")
        y = y + 1
        x = x + 1
        q = y / x
        print("you got the answer right " + str(y) + "/" + str(x) + " times.")
        print("that's " + str(q) + ".")
        # continue game or no
        print("play again? yes or no")
        if "yes":
            x = 0
            y = 0
            play == True
        else:
            play == False
            break
    else:
        x = x + 1
        print("Wrong animal, try again.")