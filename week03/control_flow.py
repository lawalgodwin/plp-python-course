#!/usr/bin/env python3

# A discounted price calculator

def calculate_discount(price: int | float, discount_percent: int | float = 0) -> float:
    # price: The original price
    # discount_percent: the percentage discount
    if(isinstance(price, (int, float)) and isinstance(discount_percent, (int, float))):
        return price * (1 - (discount_percent / 100))

if __name__ == "__main__":
    original_price = int(input("Enter the original price: "))
    percentage_discount = float(input("Enter the discount in percentage: "))
    print(f"The discounted price is ${calculate_discount(original_price, percentage_discount):.2f}")