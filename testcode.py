
# # # # # # # # # # create a simple calcular using any methods you know
# # # # # # # # # def input_function(prompt):
# # # # # # # # #     try:
# # # # # # # # #         return float(input(prompt))
# # # # # # # # #     except ValueError as ve:
# # # # # # # # #         print(ve)


# # # # # # # # # def math_calculations():
# # # # # # # # #     while True:
# # # # # # # # #         operator = input("Enter an operator (+, -, *, /); ")
# # # # # # # # #         first_value = input_function("Enter the first value: ")
# # # # # # # # #         second_value = input_function("Enter the second value: ")

# # # # # # # # #         if operator == "+":
# # # # # # # # #             result = first_value + second_value
# # # # # # # # #         elif operator == "-":
# # # # # # # # #             result = first_value - second_value
# # # # # # # # #         elif operator == "*":
# # # # # # # # #             result = first_value * second_value
# # # # # # # # #         elif operator == "/":
# # # # # # # # #             if second_value == 0:
# # # # # # # # #                 print("❌Error: not divisible by zero")
# # # # # # # # #                 continue
# # # # # # # # #             result = first_value / second_value
# # # # # # # # #         else:
# # # # # # # # #             print("Value invalid or not requested")
# # # # # # # # #         print(round(result, 2))

# # # # # # # # #         again = input("Do you want to perform another calculations? (yes/no)")
# # # # # # # # #         if again.lower() not in ("yes", "y"):
# # # # # # # # #             print("Bye bye")
# # # # # # # # #             break


# # # # # # # # # math_calculations()

# # # # # # # # for x in range(1, 11, 2):
# # # # # # # #     if x == 6:
# # # # # # # #         continue
# # # # # # # #     else:
# # # # # # # #         print(f"Welcome back number {x}")

# # # # # # # # import time
# # # # # # # # import platform

# # # # # # # # # time.sleep(3)
# # # # # # # # # print("Time's up")
# # # # # # # # x = platform.system()
# # # # # # # # x = dir(platform)
# # # # # # # # print(x)

# # # # # # # import testcode as td
# # # # # # # from math import factorial, sqrt
# # # # # # # import sys
# # # # # # # import random

# # # # # # # # td.add(3, 5)
# # # # # # # # td.subtract(68, 33)
# # # # # # # # print(sys.path)
# # # # # # # # print(factorial(6))
# # # # # # # # print(1*2*3*4*5*6)
# # # # # # # # print(random.randint(0, 10))
# # # # # # # print(random.random())

# # # # # # import random
# # # # # # import datetime
# # # # # # import time

# # # # # # x = random.random() * 100
# # # # # # y = random.randint(2, 10)
# # # # # # List = [1, 4, True, 800, "python", 27, "Hello"]

# # # # # # print(x)
# # # # # # print(y)
# # # # # # print(random.choice(List))

# # # # # # print(time.time())
# # # # # # print(datetime.date.fromtimestamp(454554))

# # # # # # for x in range(3):
# # # # # #     for y in range(1, 10+1):
# # # # # #         print(y, end=" ")
# # # # # #     print()

# # # # # # rows = int(input("Enter the number of rows: "))
# # # # # # columns = int(input("Enter the number of columns: "))
# # # # # # symbol = input("Enter the symbol to use: ")

# # # # # # for x in range(rows):
# # # # # #     for y in range(columns):
# # # # # #         print(symbol, end="")
# # # # # #     print()

# # # # # fruits = ["Apple", "Banana", "Coconut", "Orange"]
# # # # # fruits_tuple = ("Apple", "Banana", "Coconut", "Orange")
# # # # # fruits_sets = {"Apple", "Banana", "Coconut", "Orange"}

# # # # # # print(dir(fruits))
# # # # # print(help(fruits))
# # # # # # print(dir(fruits_tuple))
# # # # # # print(dir(fruits_sets))
# # # # # # for fruit in fruits:
# # # # # #     print(fruit)

# # # # # python quiz
# # # # # import time
# # # # # import threading
# # # # # import os
# # # # # import sys


# # # # # def beep():
# # # # #     if sys.platform == "win32":
# # # # #         import winsound
# # # # #         winsound.Beep(1000, 500)  # frequency, duration
# # # # #     else:
# # # # #         print("\a")  # fallback beep for linux/macos


# # # # # def countdown(seconds, stop_event):
# # # # #     for remaining in range(seconds, 0, -1):
# # # # #         if stop_event.is_set():
# # # # #             return
# # # # #         print(f"⌛{remaining} seconds left...", end="\r")
# # # # #         time.sleep(1)
# # # # #     print("\n⏰ Time's up!")
# # # # #     beep()


# # # # # def input_with_timeer(prompt, timeout=10):
# # # # #     result = [None]
# # # # #     stop_event = threading.Event()

# # # # #     def get_input():
# # # # #         result[0] = input(prompt).lower()
# # # # #         stop_event.set()

# # # # #     input_thread = threading.Thread(target=get_input)
# # # # #     timer_thread = threading.Thread(
# # # # #         target=countdown, args=(timeout, stop_event))

# # # # #     input_thread.start()
# # # # #     timer_thread.start()

# # # # #     timer_thread.join(timeout)
# # # # #     stop_event.set()

# # # # #     if input_thread.is_alive():
# # # # #         return None
# # # # #     return result[0]


# # # # # def quiz_game():
# # # # #     questions = ("How many elements are in the periodic table?: ", "Which animal lays the largest egg?: ",
# # # # #                  "What is the most abundant gas in Earth's atmosphere?: ", "How many bones are in the human body?: ", "Which planet in the solar system is the hottest?: ")

# # # # #     options = (("A. 116", "B. 117", "C. 118", "D. 119"),
# # # # #                ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
# # # # #                ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
# # # # #                ("A. 206", "B. 207", "C. 208", "D. 209"),
# # # # #                ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

# # # # #     answers = ("C", "D", "A", "A", "B")
# # # # #     guesses = []
# # # # #     score = 0
# # # # #     question_num = 0

# # # # #     while True:
# # # # #         for question in questions:
# # # # #             print("-----------------------------")
# # # # #             print(f"Question {question_num + 1}: {question}")
# # # # #             for option in options[question_num]:
# # # # #                 print(option)
# # # # #             guess = input_with_timeer("Enter (A, B, C or D): ", timeout=10)
# # # # #             if guess is None:
# # # # #                 guess = "X"
# # # # #             else:
# # # # #                 guess = guess.upper()
# # # # #             # guesses.append(guess)

# # # # #                 while guess not in ("A", "B", "C", "D"):
# # # # #                     print("❌invalid value!!!")
# # # # #                     guess = input("Please enter (A, B, C, D): ").upper()
# # # # #                     print(guess)

# # # # #             guesses.append(guess)

# # # # #             if guess == answers[question_num]:
# # # # #                 score += 1
# # # # #                 print("✅Correct! ")
# # # # #             elif guess == "X":
# # # # #                 print("🚫You skipped this question")
# # # # #                 print(f"The correct answer is {answers[question_num]}")
# # # # #             else:
# # # # #                 print("❌INCORRECT!")
# # # # #                 print(f"The correct answer is {answers[question_num]}")

# # # # #             question_num = question_num + 1

# # # # #         print("-------------------------------")
# # # # #         print("     RESULT      ")
# # # # #         print("-------------------------------")

# # # # #         print("answer: ", end="")
# # # # #         for answer in answers:
# # # # #             print(answer, end=" ")
# # # # #         print()

# # # # #         print("guesses: ", end="")
# # # # #         for guess in guesses:
# # # # #             print(guess, end=" ")
# # # # #         print()

# # # # #         score = int(score / len(questions) * 100)
# # # # #         print(f"Your score is: {score}%")

# # # # #         try_again = input("Do you want to try again? (yes/no): ")
# # # # #         if try_again not in ("yes", "y"):
# # # # #             print("👋Goodbye")
# # # # #             break
# # # # #         question_num = 0
# # # # #         score = 0
# # # # #         guesses = []


# # # # # quiz_game()

# # # # name = "Anna"
# # # # age = 65
# # # # win_rate = 0.6765567
# # # # weight = 23567890098766
# # # # net_worth = 77119293883
# # # # day = 7
# # # # month = 6
# # # # # print(f"{name} is {win_rate:.2%} and she is {age:x} years old. netwoth is ${net_worth:,}")
# # # # print(
# # # #     f"The month is {month:03} and the day is {day:03} {age:07x} weight: {weight:_b}")


# # # sentence = "Each column has a width of 10"
# # # items = {
# # #     "name": "Jane Odey",
# # #     "age": 20,
# # #     "occupation": "Backend engineer"
# # # }

# # # for key, value in items.items():
# # #     output = f"{key.title():.20}: {value}"
# # #     print(output)
# # # # table = " "
# # # # for x in sentence.split(" "):
# # # #     table += f"{x:^50}"
# # # # print(f"{table}")

# # import datetime

# # current_time = datetime.datetime.now()
# # print(f"{current_time:%Y-%m-%d %H:%M:%S}")

# # using equals to see a full expression that is in the bracket
# print(f"Here is a calculation of 20 + 40 = {20+40}")
# print(f"Here is a calcualtion of {20 + 40=} ")
# f_name = "Jane"
# print(
#     f"Dear Lord, thank you for the gift of life, your daughter {f_name=} is grateful")
# calcilate the total
# total = []

# for key, value in menu.items():
#     total += value
# print(f"The total item is: {total}")

# for key, value in menu.items():
#     total.append(value)
# print(sum(total))
