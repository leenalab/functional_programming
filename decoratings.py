# Дуже складна функція))) complicated

def complicated(x: int, y: int) -> int:
    return x + y

# Пам'ятаючи про те, що функція — це об'єкт першого класу, можна зробити щось подібне:

def complicated(x: int, y: int) -> int:
    return x + y

def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

complicated = logger(complicated)
print(complicated(2, 3))

""" Декоратор logger приймає функцію як аргумент і повертає нову функцію complicated = logger(complicated). Декорована функція зберігає свою оригінальну функціональність, але додатково отримує нову поведінку або модифікації.
"""
# Використувуємо декоратор @

def logger(func):
    def inner(x: int, y: int) -> int:
        print(f"Викликається функція: {func.__name__}: {x}, {y}")
        result = func(x, y)
        print(f"Функція {func.__name__} завершила виконання: {result}")
        return result

    return inner

@logger
def complicated(x: int, y: int) -> int:
    return x * y

print(complicated(4, 5))
