import random
from datetime import datetime, timedelta

def generate_credit_card_number():
    # Generate a random 15-digit number (excluding the last digit)
    partial_card_number = ''.join(str(random.randint(0, 9)) for _ in range(15))
    # Append a check digit using Luhn algorithm
    check_digit = generate_check_digit(partial_card_number)
    # Return full 16-digit credit card number
    return partial_card_number + str(check_digit)

def generate_check_digit(partial_card_number):
    # Calculate check digit using Luhn algorithm
    total = 0
    for i, digit in enumerate(partial_card_number[::-1]):
        if i % 2 == 0:
            doubled_digit = int(digit) * 2
            total += doubled_digit - 9 if doubled_digit > 9 else doubled_digit
        else:
            total += int(digit)
    return (10 - (total % 10)) % 10

def generate_ccv():
    # Generate a random 3-digit CVV (Card Verification Value)
    return ''.join(str(random.randint(0, 9)) for _ in range(3))

def generate_valid_date():
    # Generate a random valid date (month and year)
    current_date = datetime.now()
    future_date = current_date + timedelta(days=random.randint(30, 365)*2)  # Valid date at least 2 years in the future
    return future_date.month, future_date.year

# Generate dummy credit card details
credit_card_number = generate_credit_card_number()
ccv = generate_ccv()
expiry_month, expiry_year = generate_valid_date()

print("Dummy Credit Card Details:")
print("Credit Card Number:", credit_card_number)
print("CVV:", ccv)
print("Expiry Date (MM/YYYY):", "{:02d}/{:04d}".format(expiry_month, expiry_year))
