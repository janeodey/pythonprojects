# python compound interest calculator

principle = 0
rate = 0
time = 0

# while principle <= 0:
#     principle = float(input("Enter the principal amount: "))
#     if principle <= 0:
#         print("prinicipal cannot be less than zero")

# while rate <= 0:
#     rate = float(input("Input your rate: "))
#     if rate <= 0:
#         print("rate cannot be zero")

# while time <= 0:
#     time = float(input("Enter the time: "))
#     if time <= 0:
#         print("Time cannot be zero")

# # formula for calculating compund interest
# total = principle * (pow((1 + rate / 100), time))

# print(f"Balance after {time} {'years' if time > 1 else "year"}: ${total:.2f}")

while True:
    try:
        principle = float(input("Enter the principal amount: "))
        if principle < 0:
            print("prinicipal cannot be less than zero")
        else:
            break
    except ValueError:
        print("❌ please enter a valid number for principal")
while True:
    try:
        rate = float(input("Input your rate: "))
        if rate < 0:
            print("rate cannot be zero")
        else:
            break
    except ValueError as ve:
        print(ve)

while True:
    try:
        time = float(input("Enter the time: "))
        if time < 0:
            print("Time cannot be less than zero")
        else:
            break
    except:
        print("Please input the correct value for time")

# formula for calculating compund interest
total = principle * (pow((1 + rate / 100), time))

print(f"Balance after {time} {'years' if time > 1 else "year"}: ${total:.2f}")
