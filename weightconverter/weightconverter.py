# python weight converter

def weight_converter():
    while True:
        try:
            weight = float(input("Enter your weight: "))
            unit = input("Kilograms or Pounds? (K or L): ")

            if unit.lower() == "k":
                weight = weight * 2.205
                unit = "lbs"
                print(f"your weight is {round(weight, 1)} {unit}")
            elif unit.lower() == "l":
                weight = weight / 2.205
                unit = "kgs"
                print(f"Your weight is: {round(weight, 1)} {unit}")
        except ValueError as e:
            # print(f"{unit} is not valid")
            print(e)

        again = input("Do you want to check another weight? (yes/no): ")
        if again not in ("yes", "y"):
            print("Goodbye 👋")
            break


weight_converter()
