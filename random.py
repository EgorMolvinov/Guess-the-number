#Guess the number invented by the computer
 
 
import random
 
print("The computer thought of a 3-digit number")
print("Guess it with the fewest attempts")
print("The computer will prompt you with every attempt.")
z = 0
x=random.randint(100, 999)
while True :
    n=int(input("Enter the number that the computer suggested to you: "))
 
    if n>x :
        print("Less ")
        z += 1
 
    elif n<x :
        print("More ")
        z += 1
 
    else:
        z += 1
        print("Congratulations, you guessed the number with ",z," tries")
        break
input()
