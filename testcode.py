
# # # # # create a simple calcular using any methods you know
# # # # def input_function(prompt):
# # # #     try:
# # # #         return float(input(prompt))
# # # #     except ValueError as ve:
# # # #         print(ve)


# # # # def math_calculations():
# # # #     while True:
# # # #         operator = input("Enter an operator (+, -, *, /); ")
# # # #         first_value = input_function("Enter the first value: ")
# # # #         second_value = input_function("Enter the second value: ")

# # # #         if operator == "+":
# # # #             result = first_value + second_value
# # # #         elif operator == "-":
# # # #             result = first_value - second_value
# # # #         elif operator == "*":
# # # #             result = first_value * second_value
# # # #         elif operator == "/":
# # # #             if second_value == 0:
# # # #                 print("❌Error: not divisible by zero")
# # # #                 continue
# # # #             result = first_value / second_value
# # # #         else:
# # # #             print("Value invalid or not requested")
# # # #         print(round(result, 2))

# # # #         again = input("Do you want to perform another calculations? (yes/no)")
# # # #         if again.lower() not in ("yes", "y"):
# # # #             print("Bye bye")
# # # #             break


# # # # math_calculations()

# # # for x in range(1, 11, 2):
# # #     if x == 6:
# # #         continue
# # #     else:
# # #         print(f"Welcome back number {x}")

# # # import time
# # # import platform

# # # # time.sleep(3)
# # # # print("Time's up")
# # # x = platform.system()
# # # x = dir(platform)
# # # print(x)

# # import testcode as td
# # from math import factorial, sqrt
# # import sys
# # import random

# # # td.add(3, 5)
# # # td.subtract(68, 33)
# # # print(sys.path)
# # # print(factorial(6))
# # # print(1*2*3*4*5*6)
# # # print(random.randint(0, 10))
# # print(random.random())

# import random
# import datetime
# import time

# x = random.random() * 100
# y = random.randint(2, 10)
# List = [1, 4, True, 800, "python", 27, "Hello"]

# print(x)
# print(y)
# print(random.choice(List))

# print(time.time())
# print(datetime.date.fromtimestamp(454554))

# for x in range(3):
#     for y in range(1, 10+1):
#         print(y, end=" ")
#     print()

# rows = int(input("Enter the number of rows: "))
# columns = int(input("Enter the number of columns: "))
# symbol = input("Enter the symbol to use: ")

# for x in range(rows):
#     for y in range(columns):
#         print(symbol, end="")
#     print()

fruits = ["Apple", "Banana", "Coconut", "Orange"]
fruits_tuple = ("Apple", "Banana", "Coconut", "Orange")
fruits_sets = {"Apple", "Banana", "Coconut", "Orange"}

# print(dir(fruits))
print(help(fruits))
# print(dir(fruits_tuple))
# print(dir(fruits_sets))
# for fruit in fruits:
#     print(fruit)
