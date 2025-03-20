#დაწერეთ პროგრამა სადაც მომხმარებელს შეეძლება შემოიყვანოსტ წილადი, მაგალითად 1/4 ანდ 2/7 და ა.შ.
#შემოტანილი მონაცემებიდან წილადი გადაიყვანეთ პროცენტებში, მაგალითად თუ შემოვიდა 1/4 ეს არის 25%, რადგან 1 / 4 * 100 = 25
#იმ შემთხვევაში თუ მიღებული შედეგი 1-ზე ნაკლებია ან ტოლია მაშინ გამოპრინტეთ E, იმ შემთხვევაში თუ შედეგი 99 ტოლია ან მეტია გამოპრინტეთ F, სხვა შემთხვევაში შედეგის რიცხვითი მნიშვნელობა % ნიშანთან ერთად. 
from fractions import Fraction

def fraction_to_percentage():
    while True:
        try:
            fraction_input = input("fraction: ")
            numerator, denominator = fraction_input.split("/")
            
            # Convert words to numbers if necessary
            if not numerator.isdigit() or not denominator.isdigit():
                raise ValueError
            
            numerator, denominator = int(numerator), int(denominator)
            
            if denominator == 0:
                raise ZeroDivisionError
            
            if numerator > denominator:
                raise ValueError
            
            percentage = (numerator / denominator) * 100
            
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{int(percentage)}%")
            
            break
        except (ValueError, ZeroDivisionError):
            pass  # If there's an error, re-prompt the user

fraction_to_percentage()

 #- პროექტი 55 - Felipe's Taqueria

MENU = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
    total = 0.0
    try:
        while True:
            item = input("Item: ").title()
            if item in MENU:
                total += MENU[item]
                print(f"Total: ${total:.2f}")
    except EOFError:
        print("\nGoodbye!")

if __name__ == "__main__":
    main()

 #დაწერეთ პროგრამა სადაც მომხმარებელს ექნება საშუალება შეიყვანოს თითოეულ ხაზზე სასურსათო სია მას შემდეგ რაც ამუშავდება EOFError მაშინ თქვენ უნდა გამოიტანოთ უნიკალური დასახელებული სურსათის დასახელებები მათი რაოდენობის მიხედვით, გაითვალისწინეთ რომ გამოტანილი სია უნდა იყოს მაღალი რეგისტრის ასოებით, სორტირებული ალფავიტის მიხედვით და წინ უნდა ეწეროს რაოდენობა თუ რამდენჯერ აკრიფა კონკრეტული სურსათის დასახელება
from collections import defaultdict

def main():
    grocery_list = defaultdict(int)
    try:
        while True:
            item = input("Item: ").strip().upper()
            grocery_list[item] += 1
    except EOFError:
        print()
        for item in sorted(grocery_list.keys()):
            print(f"{grocery_list[item]} {item}")

if __name__ == "__main__":
    main()
   #დაწერეთ პროგრამა სადაც მომხმარებელს შეეძლება შემოიყვანოს 2 ტიპის თარიღის ფორმატი: m/d/yyyy ან m d, yyyy

def parse_date():
    months = {"January": "01", "February": "02", "March": "03", "April": "04", "May": "05", "June": "06", "July": "07", "August": "08", "September": "09", "October": "10", "November": "11", "December": "12"}
    
    while True:
        try:
            date_str = input("Date: ").strip()
            
            if "/" in date_str:
                month, day, year = map(int, date_str.split("/"))
            else:
                parts = date_str.replace(",", "").split()
                month = months[parts[0]]
                day = int(parts[1])
                year = int(parts[2])
            
            if not (1 <= int(month) <= 12 and 1 <= day <= 31):
                raise ValueError
            
            formatted_date = f"{year:04d}-{int(month):02d}-{day:02d}"
            return formatted_date
        except (ValueError, KeyError, IndexError):
            pass  # If input is invalid, ask again.

def main():
    print(parse_date())

if __name__ == "__main__":
    main()

#-პროექტი 58 - Blood Alcohol Calculator
def validate_input(prompt, valid_options=None, convert_func=None):
    while True:
        try:
            value = input(prompt).strip()
            if convert_func:
                value = convert_func(value)
            if valid_options and value not in valid_options:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please try again.")

def calculate_bac(weight, gender, drinks, alcohol_per_drink, hours):
    r = 0.73 if gender.lower() == "male" else 0.66
    total_alcohol = drinks * alcohol_per_drink
    bac = (total_alcohol * 5.14 / weight * r) - (0.015 * hours)
    return bac

def main():
    weight = validate_input("What is your weight (in pounds)? ", convert_func=float)
    gender = validate_input("Male or Female? ", valid_options=["Male", "Female"])
    drinks = validate_input("Number of drinks? ", convert_func=int)
    alcohol_per_drink = validate_input("Amount of alcohol in one drink (oz)? ", convert_func=float)
    hours = validate_input("Hours since your last drink? ", convert_func=float)
    
    bac = calculate_bac(weight, gender, drinks, alcohol_per_drink, hours)
    print(f"Your BAC is {bac:.2f}")
    
    if bac >= 0.08:
        print("It is not legal for you to drive.")
    else:
        print("It is legal for you to drive.")

if __name__ == "__main__":
    main()

#- პროექტი 59 - Anagram Checker
def is_anagram(word1, word2):
    return sorted(word1.lower()) == sorted(word2.lower())

def validate_input(prompt):
    while True:
        try:
            value = input(prompt).strip()
            if not value.isalpha():
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a valid word.")

def main():
    print("Enter two strings and I'll tell you if they are anagrams:")
    word1 = validate_input("Enter the first string: ")
    word2 = validate_input("Enter the second string: ")
    
    if len(word1) != len(word2):
        print(f'"{word1}" and "{word2}" are not anagrams.')
    elif is_anagram(word1, word2):
        print(f'"{word1}" and "{word2}" are anagrams.')
    else:
        print(f'"{word1}" and "{word2}" are not anagrams.')

if __name__ == "__main__":
    main()

#- პროექტი 60 - Password Strength Indicator
import re

def password_validator(password):
    if len(password) < 8:
        if password.isdigit():
            return "very weak password"
        elif password.isalpha():
            return "weak password"
    elif any(char.isdigit() for char in password) and any(char.isalpha() for char in password):
        if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return "very strong password"
        return "strong password"
    return "weak password"


def main():
    password = input("Enter a password to check its strength: ")
    result = password_validator(password)
    print(f"The password '{password}' is a {result}.")


if __name__ == "__main__":
    main()

#- პროექტი 61 - Validating Inputs
import re

def validate_name(name, field_name):
    if len(name) == 0:
        return f"The {field_name} must be filled in."
    elif len(name) < 2:
        return f'"{name}" is not a valid {field_name}. It is too short.'
    return ""

def validate_zip(zip_code):
    if not zip_code.isdigit():
        return "The ZIP code must be numeric."
    return ""

def validate_employee_id(emp_id):
    if not re.match(r"^[A-Z]{2}-\d{4}$", emp_id):
        return f"{emp_id} is not a valid ID."
    return ""

def main():
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    zip_code = input("Enter the ZIP code: ")
    emp_id = input("Enter an employee ID: ")
    
    errors = []
    errors.append(validate_name(first_name, "first name"))
    errors.append(validate_name(last_name, "last name"))
    errors.append(validate_zip(zip_code))
    errors.append(validate_employee_id(emp_id))
    
    errors = [error for error in errors if error]
    
    if errors:
        for error in errors:
            print(error)
    else:
        print("There were no errors found.")

if __name__ == "__main__":
    main()

#-პროექტი 62 - Weekly Exercise Log
def main():
    exercises = []
    total_time = 0
    total_calories = 0

    while True:
        exercise_name = input("Enter the type of exercise (or type 'done' to finish): ")
        if exercise_name.lower() == 'done':
            break
        
        try:
            duration = float(input("Enter the duration in minutes: "))
            calories = float(input("Enter the calories burned: "))
            
            if duration <= 0 or calories <= 0:
                print("Duration and calories must be positive numbers. Please try again.")
                continue
            
            exercises.append({'exercise': exercise_name, 'duration': duration, 'calories': calories})
            total_time += duration
            total_calories += calories
        
        except ValueError:
            print("Invalid input. Please enter a number for duration and calories.")
    
    print("\nWeekly Exercise Log:")
    for exercise in exercises:
        print(f"Exercise: {exercise['exercise']}, Duration: {exercise['duration']} minutes, Calories: {exercise['calories']} calories")
    
    print(f"Total exercise time: {total_time} minutes")
    print(f"Total calories burned: {total_calories} calories")

if __name__ == "__main__":
    main()

#-პროექტი 63 - Weather Logger
def main():
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weather_data = {}

    while True:
        day = input("Enter a day of the week (or 'done' to finish): ").capitalize()
        
        if day == 'Done':
            break
        
        if day not in days_of_week:
            print("Invalid day. Please enter a valid day of the week.")
            continue
        
        while True:
            try:
                temperature = float(input(f"Enter temperature for {day} in °C: "))
                break
            except ValueError:
                print("Invalid input. Please enter a valid number for temperature.")
        
        weather_condition = input(f"Enter weather condition for {day} (e.g., sunny, rainy): ").lower()
        
        weather_data[day] = {'temperature': temperature, 'condition': weather_condition}

    print("\nWeekly Weather Log:")
    for day in days_of_week:
        if day in weather_data:
            print(f"{day}: {weather_data[day]['temperature']}°C, {weather_data[day]['condition']}")
        else:
            print(f"{day}: No data available")

if __name__ == "__main__":
    main()
