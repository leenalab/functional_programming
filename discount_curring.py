def apply_discount(price: float, discount_percentage: int) -> float:
    return price * (1 - discount_percentage / 100)

# Використання
discounted_price = apply_discount(500, 10)  # Знижка 10% на ціну 500
print(discounted_price)

discounted_price = apply_discount(500, 20)  # Знижка 20% на ціну 500
print(discounted_price)