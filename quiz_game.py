# python quiz

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
            guess = input("Enter (A, B, C or D): ").upper()
            guesses.append(guess)

            while guess not in ("A", "B", "C", "D"):
                print("❌invalid value!!!")
                guess = input("Please enter (A, B, C, D): ").upper()
                print(guess)

            if guess == answers[question_num]:
                score += 1
                print("🥳Correct! ")
            else:
                print("INCORRECT!")
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


quiz_game()
