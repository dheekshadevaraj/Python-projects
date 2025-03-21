def calculate_bmi(weight, height):
    """
    Calculate BMI using the formula: BMI = weight (kg) / height^2 (m^2)
    """
    try:
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ZeroDivisionError:
        return "Height cannot be zero."

def bmi_category(bmi):
    """
    Determine the BMI category.
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    """
    Main function to take user input and display BMI & category.
    """
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        bmi = calculate_bmi(weight, height)
        if isinstance(bmi, str):
            print(bmi)
        else:
            print(f"Your BMI is: {bmi}")
            print(f"Category: {bmi_category(bmi)}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    main()
