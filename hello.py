#-პროექტი 77 - Testing my Twttr 
def main():
    print(shorten(input("Enter a word: ")))


def shorten(word):
    return ''.join([char for char in word if char not in "AEIOUaeiou"])


if __name__ == "__main__":
    main()

#-პროექტი 78 - Back to the Bank
def main():
    greeting = input("Enter a greeting: ")
    print(value(greeting))


def value(greeting):
    if greeting.lower().startswith('hello'):
        return "$0"
    elif greeting.lower().startswith('h'):
        return "$20"
    else:
        return "$100"


if __name__ == "__main__":
    main()

#-პროექტი 79 - Re-requesting a Vanity Plate 
def main():
    plate = input("Enter a vanity plate: ")
    if is_valid(plate):
        print("Valid plate")
    else:
        print("Invalid plate")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if not s[0].isalpha() or not s[-1].isalpha():
        return False
    if any(char.isdigit() for char in s[:2]) or any(char.isdigit() for char in s[1:]):
        return False
    if any(char in s[2:] for char in ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]):
        return False
    return True


if __name__ == "__main__":
    main()

#-პროექტი 80 - Refueling
def main():
    fraction = input("Enter the fuel fraction (e.g., 1/4): ")
    percentage = convert(fraction)
    print(gauge(percentage))


def convert(fraction):
    numerator, denominator = fraction.split('/')
    return (int(numerator) / int(denominator)) * 100


def gauge(percentage):
    if percentage >= 90:
        return "Full"
    elif percentage >= 50:
        return "Half"
    elif percentage >= 25:
        return "Low"
    else:
        return "Empty"


if __name__ == "__main__":
    main()

 #- პროექტი 81 - Paint Calculator
def main():
    length = float(input("Length of your room: "))
    width = float(input("Width of your room: "))
    
    area = calculate_area(length, width)
    gallons_needed = calculate_gallons(area)
    
    print(f"You will need to purchase {gallons_needed} gallons of paint to cover {area} square feet.")

def calculate_area(length, width):
    return length * width

def calculate_gallons(area):
    gallon_coverage = 350
    gallons = area / gallon_coverage
    return round(gallons)

if __name__ == "__main__":
    main()


 #- პროექტი 82 - Self-Checkout
def main():
    price1, quantity1 = float(input("Enter the price of item 1: ")), int(input("Enter the quantity of item 1: "))
    price2, quantity2 = float(input("Enter the price of item 2: ")), int(input("Enter the quantity of item 2: "))
    price3, quantity3 = float(input("Enter the price of item 3: ")), int(input("Enter the quantity of item 3: "))
    
    subtotal = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)
    tax = round(subtotal * 0.055, 2)
    total = subtotal + tax
    
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

