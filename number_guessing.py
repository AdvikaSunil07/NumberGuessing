#The number guessing game (using random module)

import random as r

print("Welcome to the game!!\nLet's see how many attempts you'll take to guess.")

a = input("Enter the upper limit: ")


if a.isdigit():
    a = int(a)
    print("OKAY!! YOU'RE READY TO BEGIN")
    random_num = r.randint(0, a)  
else:
    print("Enter a valid number next time")
    quit()

attempts = 0

while True:
    user_guess = input("Enter your guess: ")

    if user_guess.isdigit():
        user_guess = int(user_guess)
        attempts += 1

        if user_guess < random_num:
            print("Too low! Try again.")
        elif user_guess > random_num:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congrats! You guessed the number in {attempts} attempts.")
            break  
    else:
        print("Please enter a valid number.")
