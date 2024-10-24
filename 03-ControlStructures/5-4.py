###
# A simple number guessing game
#
import random

# Randomly chosen number to be guessed from 1 to 100
number_to_guess = random.randint(1, 100)
user_guess = 0

print("Zgadnij numer od 1 do 100!")

while user_guess != number_to_guess:
    user_guess = int(input("Zgaduj: "))

    if user_guess < number_to_guess:
        print("Za mało! Spróbuj jeszcze raz.")
    elif user_guess > number_to_guess:
        print("Za wysoko! Spróbuj jeszcze raz.")
    else:
        print("Gratulacje! Zgadłaś!!!!")