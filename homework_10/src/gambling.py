import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 5
    
    print("Guess the number from 1 to 100. You have 5 attempts")
    
    for _ in range(attempts):
        try:
            guess = int(input("Write a number "))
            
            if guess == secret_number:
                print("Congratulation!")
                return
            elif guess < secret_number:
                print("Too low. Try again.")
            else:
                print("Too high. Try again.")
        except ValueError:
            print("This number does not fit.")
    
    print(f"Sorry, you've run out of attempts. The correct number was {secret_number}.")


guess_the_number()