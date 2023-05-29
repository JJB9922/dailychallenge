#9. Write a guessing game where the user has to guess a secret number. After ever guess, the program tells the user whether
#their number was too large or too small. At the end the number of tries needed should be printed. It counts only as one try if they
#input the same number multiple times consecutively.

import random

secretNumber = int(random.randint(0, 100))
#print(f"Secret Number = {secretNumber}")
guess = -1
counter = 1

while secretNumber != guess:
    prevGuess = guess
    print("---")
    guess = input("Guess the secret number between 0 and 100\n")
    if prevGuess == guess:
        if int(secretNumber) < int(guess):
            print("Too big - try again\n")
        elif int(secretNumber) > int(guess):
            print("Too small - try again\n")
    elif prevGuess != guess:
        if int(secretNumber) < int(guess):
            print("Too big - try again\n")
            counter = counter + 1
        elif int(secretNumber) > int(guess):
            print("Too small - try again\n")
            counter = counter +1
        elif int(secretNumber) == int(guess):
            print("---")
            print("Correct\n")
            print(f"The secret number was {guess}\n")
                        
            print(f"You guessed in {counter} tries.")
            break