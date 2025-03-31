#-პროექტი 77 - Testing my Twttr 
import sys

def main():
    greetings = ["hello there", "hi", "goodbye", "exit"]
    for greeting in greetings:
        print(f"Input: {greeting} -> Value: ${value(greeting)}")

def value(greeting):
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()


#-პროექტი 78 - Back to the Bank
def main():
    greetings = ["hello there", "hi", "goodbye", "exit"]
    for greeting in greetings:
        if greeting.lower() == "exit":
            break
        print(f"Input: {greeting} -> Value: ${value(greeting)}")

def value(greeting):
    greeting = greeting.lower().strip()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()


#-პროექტი 80 - Refueling
def main():
    fractions = ["1/4", "3/4", "1/2", "E", "F"]
    for fraction in fractions:
        percentage = convert(fraction)
        print(gauge(percentage))

def convert(fraction):
    try:
        numerator, denominator = fraction.split('/')
        percentage = (int(numerator) / int(denominator)) * 100
        return percentage
    except ValueError:
        return -1

def gauge(percentage):
    if percentage == -1:
        return "Invalid input."
    elif percentage <= 0:
        return "E"
    elif percentage >= 100:
        return "F"
    else:
        return f"{round(percentage)}%"

if __name__ == "__main__":
    main()

#- პროექტი 81 - Paint Calculator
def main():
    test_input = [
        (12, 30),  # First room: length=12, width=30
        (10, 15),  # Second room: length=10, width=15
        (20, 20)   # Third room: length=20, width=20
    ]
    
    for length, width in test_input:
        area = (length, width)
        gallons_needed =(area)
        print(f"You will need to purchase {gallons_needed} gallons of paint to cover {round(area)} square feet.")

if __name__ == "__main__":
    main()

#- პროექტი 82 - Self-Checkout
def calculate_item_total(price, quantity):
    return price * quantity

def calculate_subtotal(item_totals):
    return sum(item_totals)

def calculate_tax(subtotal, tax_rate=5.5):
    return (subtotal * tax_rate) / 100

def calculate_total(subtotal, tax):
    return subtotal + tax

def main():
    item_totals = []
    items = [
        {'price': 25, 'quantity': 2},
        {'price': 10, 'quantity': 1},
        {'price': 4, 'quantity': 1}
    ]

    for item in items:
        price = item['price']
        quantity = item['quantity']
        item_total = calculate_item_total(price, quantity)
        item_totals.append(item_total)

    subtotal = calculate_subtotal(item_totals)
    tax = calculate_tax(subtotal)
    total = calculate_total(subtotal, tax)

    print(f"Subtotal: ${subtotal:.2f}")
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")

if __name__ == "__main__":
    main()

#-პროექტი 83 - Currency Conversion
   import requests

def main():
    amount_from = float(input("How many euros are you exchanging? "))
    rate_from = get_exchange_rate()
    
    amount_to = convert_to_dollars(amount_from, rate_from)
    
    print(f"{amount_from} euros at an exchange rate of {rate_from} is\n$ {amount_to:.2f} U.S. dollars.")

def get_exchange_rate():
    url = "https://api.exchangerate-api.com/v4/latest/EUR"
    response = requests.get(url)
    data = response.json()
    return data["rates"]["USD"]

def convert_to_dollars(amount_from, rate_from):
    return round(amount_from * rate_from, 2)

if __name__ == "__main__":
    main()

#-პროექტი 85 - Determining Compound Interest
def main():
    P = float(input("What is the principal amount? "))
    r = float(input("What is the rate? ")) / 100
    t = float(input("What is the number of years? "))
    n = int(input("What is the number of times the interest is compounded per year? "))

    A = compound_interest(P, r, t, n)
    
    print(f"${P} invested at {r*100}% for {t} years compounded {n} times per year is ${A:.2f}.")

def compound_interest(P, r, t, n):
    return round(P * (1 + r/n) ** (n * t), 2)

if __name__ == "__main__":
    main() 
