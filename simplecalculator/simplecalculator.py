
# using if else statement (conditional statement)
# operator = input("Enter an operator(+, -, *, /, **, %, // ): ")
# num1 = float(input("Enter the 1st number: "))
# num2 = float(input("Enter the 2nd number: "))

# # if operator == "+":
# #     result = num1 + num2
# #     print(round(result, 3))
# # elif operator == "-":
# #     result = num1 - num2
# #     print(round(result, 3))
# # elif operator == "/":
# #     result = num1 / num2
# #     print(round(result, 3))
# # elif operator == "*":
# #     result = num1 * num2
# #     print(round(result, 3))
# # else:
# #     print(f"{operator} is not a valid operator")


# # using the match
# match operator:
#     case "+":
#         result = num1 + num2
#         print(f"Result: {round(result, 3)}")
#     case "-":
#         result = num1 - num2
#         print(f"Result: {round(result, 3)}")
#     case "/":
#         if num2 != 0:
#             result = num1 / num2
#             print(f"Result: {round(result, 3)}")
#         else:
#             print("Error: Not divisible by zero")
#         # try:
#         #     if num2 != 0:
#         #         result = num1 / num2
#         #         print(round(result, 3))
#         # except:
#         #     print("Error: Not divisible by zero")
#     case "*":
#         result = num1 * num2
#         print(f"Result: {round(result, 3)}")
#     case "**":
#         result = num1 ** num2
#         print(f"Result: {round(result, 3)}")
#     case "%":
#         if num2 != 0:
#             result = num1 % num2
#             print(f"Result: {round(result, 3)}")
#         else:
#             print(f"Error: Modulo by zero")
#     case "//":
#         if num2 != 0:
#             result = num1 // num2
#             print(f"Result: {round(result, 3)}")
#         else:
#             print("Error: Zero Division")
#     case _:
#         print(f"{operator} is not a valid python operator")


# retry until its true - using function, match and while loop
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("❌ invalid number. Please enter a valid number")


def calculator():
    while True:
        operator = input("Enter an operator(+, -, *, /, **, %, // ): ")
        num1 = get_number("Enter the 1st number: ")
        num2 = get_number("Enter the 2nd number: ")

        match operator:
            case "+":
                result = num1 + num2

            case "-":
                result = num1 - num2

            case "/":
                if num2 == 0:
                    print(f"❌Error: Division by zero.")
                    continue
                result = num1 / num2
            case "*":
                result = num1 * num2

            case "**":
                result = num1 ** num2

            case "%":
                if num2 == 0:
                    print(f"❌Error: Modulo by zero.")
                    continue
                result = num1 % num2

            case "//":
                if num2 == 0:
                    print(f"❌Error: Floor division by zero")
                    continue
                result = num1 // num2

            case _:
                print(f"{operator} is not a valid python operator")
                continue
        print(f"Result: {round(result, 3)}")

        again = input(
            "Do you want to perform another calculation? (yes/no); ").lower()
        if again not in ("yes", "y"):
            print("👋 Goodbye!")
            break


calculator()
