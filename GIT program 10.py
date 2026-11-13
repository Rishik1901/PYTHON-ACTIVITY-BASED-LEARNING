secret_number = 42
attempts = 0

print("Guess the secret number between 1 and 50!")
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == secret_number:
        print(f"Correct! You found it in {attempts} attempts.")
        break
    elif guess < secret_number:
        print("Too low! Try a higher number.")
    else:
        print("Too high! Try a lower number.")




