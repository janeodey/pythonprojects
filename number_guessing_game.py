# python guessing game
import random

print("Python number guessing game")
print("Select a number between 1 and 100")

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True
max_guessing = 7

while is_running:
    guess = input(
        f"Please select a number between {lowest_num} and {highest_num} (please x to cancel): ")

    if guess.lower() == "x":
        print("Thank you for playing with us!")
        break

    if guess.isdigit():
        guess = int(guess)

        if guess < lowest_num or guess > highest_num:
            print("❌ That number is out of range...")
            print(
                f"Please select a valid number between {lowest_num} and {highest_num}")
            continue

        guesses += 1

        if guess == answer:
            print(f"✅ Correct guess! Well done 🎉 Your answer was {answer}")
            print(f"📊 Number of guesses: {guesses}")
            # break or
            is_running = False

        elif guess < answer:
            print("⬇️Too low! Try again!")
        elif guess > answer:
            print("⬆️Too high! Try again!")

        if guesses == max_guessing:
            print("❌ You've exceeded the number of free tries!")
            print(f"🎯 The correct answer was {answer}")
            # break or
            is_running = False
    else:
        print("Invalid")
        print(
            f"Please select a valid number between {lowest_num} and {highest_num}")
