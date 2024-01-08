def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def classification(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal Weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    print("Welcome to the BMI Calculator!")

    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))

    # Calculate BMI
    bmi_result = calculate_bmi(weight, height)

    # Interpret BMI and provide classification
    bmi_classification = classification(bmi_result)

    # Display the results
    print(f"\nYour BMI is: {bmi_result:.2f}")
    print(f"You are classified as: {bmi_classification}")

if __name__ == "__main__":
    main()
