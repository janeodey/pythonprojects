# # python quiz
# import time
# import threading
# import os
# import sys

# def input_with_timeout(prompt, timeout=10):
#     result = [None]

#     def ask():
#         result[0] = input(prompt).lower()

#     t = threading.Thread(target=ask)
#     t.start()
#     t.join(timeout)
#     if t.is_alive():
#         print(f"\n⏰ Time's up! Moving to the next question.")
#         t.join()
#     return result[0]


# def quiz_game():
#     questions = ("How many elements are in the periodic table?: ", "Which animal lays the largest egg?: ",
#                  "What is the most abundant gas in Earth's atmosphere?: ", "How many bones are in the human body?: ", "Which planet in the solar system is the hottest?: ")

#     options = (("A. 116", "B. 117", "C. 118", "D. 119"),
#                ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
#                ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
#                ("A. 206", "B. 207", "C. 208", "D. 209"),
#                ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

#     answers = ("C", "D", "A", "A", "B")
#     guesses = []
#     score = 0
#     question_num = 0

#     while True:
#         for question in questions:
#             print("-----------------------------")
#             print(f"Question {question_num + 1}: {question}")
#             for option in options[question_num]:
#                 print(option)
#             guess = input_with_timeout("Enter (A, B, C or D): ", timeout=10)
#             if guess is None:
#                 guess = "X"
#             else:
#                 guess = guess.upper()
#             # guesses.append(guess)

#                 while guess not in ("A", "B", "C", "D"):
#                     print("❌invalid value!!!")
#                     guess = input("Please enter (A, B, C, D): ").upper()
#                     print(guess)

#             guesses.append(guess)

#             if guess == answers[question_num]:
#                 score += 1
#                 print("✅Correct! ")
#             elif guess == "X":
#                 print("🚫You skipped this question")
#                 print(f"The correct answer is {answers[question_num]}")
#             else:
#                 print("❌INCORRECT!")
#                 print(f"The correct answer is {answers[question_num]}")

#             question_num = question_num + 1

#         print("-------------------------------")
#         print("     RESULT      ")
#         print("-------------------------------")

#         print("answer: ", end="")
#         for answer in answers:
#             print(answer, end=" ")
#         print()

#         print("guesses: ", end="")
#         for guess in guesses:
#             print(guess, end=" ")
#         print()

#         score = int(score / len(questions) * 100)
#         print(f"Your score is: {score}%")

#         try_again = input("Do you want to try again? (yes/no): ")
#         if try_again not in ("yes", "y"):
#             print("👋Goodbye")
#             break
#         question_num = 0
#         score = 0
#         guesses = []


# quiz_game()

import time
import threading
import os
import sys


def beep():
    if sys.platform == "win32":
        import winsound
        winsound.Beep(1000, 500)  # frequency, duration
    else:
        print("\a")  # fallback beep for linux/macos


def countdown(seconds, stop_event):
    for remaining in range(seconds, 0, -1):
        if stop_event.is_set():
            return
        print(f"⌛{remaining} seconds left...", end="\r")
        time.sleep(1)
    print("\n⏰ Time's up!")
    beep()


def input_with_timeer(prompt, timeout=10):
    result = [None]
    stop_event = threading.Event()

    def get_input():
        result[0] = input(prompt).lower()
        stop_event.set()

    input_thread = threading.Thread(target=get_input)
    timer_thread = threading.Thread(
        target=countdown, args=(timeout, stop_event))

    input_thread.start()
    timer_thread.start()

    timer_thread.join(timeout)
    stop_event.set()

    if input_thread.is_alive():
        return None
    return result[0]


def quiz_game():
    questions = ("How many elements are in the periodic table?: ", "Which animal lays the largest egg?: ",
                 "What is the most abundant gas in Earth's atmosphere?: ", "How many bones are in the human body?: ", "Which planet in the solar system is the hottest?: ")

    options = (("A. 116", "B. 117", "C. 118", "D. 119"),
               ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
               ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"),
               ("A. 206", "B. 207", "C. 208", "D. 209"),
               ("A. Mercury", "B. Venus", "C. Earth", "D. Mars"))

    answers = ("C", "D", "A", "A", "B")
    guesses = []
    score = 0
    question_num = 0

    while True:
        for question in questions:
            print("-----------------------------")
            print(f"Question {question_num + 1}: {question}")
            for option in options[question_num]:
                print(option)
            guess = input_with_timeer("Enter (A, B, C or D): ", timeout=10)
            if guess is None:
                guess = "X"
            else:
                guess = guess.upper()
            # guesses.append(guess)

                while guess not in ("A", "B", "C", "D"):
                    print("❌invalid value!!!")
                    guess = input("Please enter (A, B, C, D): ").upper()
                    print(guess)

            guesses.append(guess)

            if guess == answers[question_num]:
                score += 1
                print("✅Correct! ")
            elif guess == "X":
                print("🚫You skipped this question")
                print(f"The correct answer is {answers[question_num]}")
            else:
                print("❌INCORRECT!")
                print(f"The correct answer is {answers[question_num]}")

            question_num = question_num + 1

        print("-------------------------------")
        print("     RESULT      ")
        print("-------------------------------")

        print("answer: ", end="")
        for answer in answers:
            print(answer, end=" ")
        print()

        print("guesses: ", end="")
        for guess in guesses:
            print(guess, end=" ")
        print()

        score = int(score / len(questions) * 100)
        print(f"Your score is: {score}%")

        try_again = input("Do you want to try again? (yes/no): ")
        if try_again not in ("yes", "y"):
            print("👋Goodbye")
            break
        question_num = 0
        score = 0
        guesses = []


quiz_game()
