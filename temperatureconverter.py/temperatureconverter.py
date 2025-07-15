
# def temeperature_converter():
#     while True:
#         unit = input("Is this temperature in celsius or fahrenheit (C/F/K): ")
#         try:
#             temp = float(input("Enter the temperature: "))
#         except ValueError:
#             print("❌Please enter a valid number")
#             continue

#         if unit.lower() == "c":
#             temp = round((9 * temp)/5 + 32, 1)
#             print(f"The temperature in Fahrenheit is: {temp}")
#         elif unit.lower() == "f":
#             temp = round((temp - 32) * 5 / 9, 1)
#             print(f"The temperature in Celsius is {temp}")
#         else:
#             print(f"{unit} is an invalid unit of environment")

#         again = input(
#             f"Do you want to perform another operation? (yes/no)").lower()
#         if again not in ("yes", "y"):
#             print("Thank you for using our app")
#             break


# temeperature_converter()


def convert_temperature(value, from_unit, to_unit):
    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    # convert from original unit to Celsius
    if from_unit == "C":
        temp_c = value
    elif from_unit == "F":
        temp_c = (value - 32) * 5/9
    elif from_unit == "K":
        temp_c = value - 273.15
    else:
        raise ValueError(f"❌ unsupported from_unit {from_unit}")

    # convert from celsius to target unit
    if to_unit == "C":
        return temp_c
    elif to_unit == "F":
        return temp_c * 9 / 5 + 32
    elif to_unit == "K":
        return temp_c + 273.15
    else:
        raise ValueError(f"❌ unsupported to_unit {to_unit}")


def run_converter():
    print("🌡 Smart Temperature Converter")
    print("Supported units: C (Celsius), F (Fahrenheit), K (Kelvin)\n")

    while True:
        try:
            from_unit = input("Convert FROM (C/F/K): ").strip().upper()
            to_unit = input("Convert to (C/F/K): ").strip().upper()
            if from_unit not in {"C", "F", "K"} or to_unit not in {"C", "F", "K"}:
                print("❌ Please enter valid units (C, F or K).\n")
                continue

            value = float(input(f"Enter temperature in {from_unit}: "))
            result = convert_temperature(value, from_unit, to_unit)
            print(f"✅ {value}°{from_unit} = {round(result, 2)}°{to_unit} ")
        except ValueError as ve:
            print(ve)
            continue

        again = input(
            "Do you want to convert another temeperature? (yes/no)").lower()
        if again not in ("yes", "y"):
            print("Thank you")
            break


run_converter()
