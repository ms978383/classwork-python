import random

number = random.randint(1,20)

while True:
    guess = int(input("Guess a Number Between 1 to 20:"))

    if guess == number:
        print("You Guessed a Correct Number")
        break
    elif guess>number:
        print("You Guessed a Greater Number")
        
    elif guess<number:
        print("You Guessed a Lesser Number")
        

        
