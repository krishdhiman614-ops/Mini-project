import random
a = random.randint(1, 100)
attempts = 0
print("===== Number Guessing Game =====")
print("I have selected a number between 1 and 100.")
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < a:
        print("Too Low! Try Again.")
    elif guess > a:
        print("Too High! Try Again.")
    else:
        print("Congratulations! You guessed the correct number:",a)
        print("Total Attempts:", attempts)
        break