from typing import Callable, Dict

# Визначення функції

def add(a: int, b: int) -> int:
    return a + b

def multiply(a: int, b: int) -> int:
    return a * b

def power(exponent: int) -> Callable[[int],int]:
    def inner(base: int) -> int:
        return base ** exponent
    return inner

# Використання power для створення функцій square та cube
square = power(2)
cube = power(3)

operations: Dict[str, Callable] = {
    'add': add,
    'multiply': multiply,
    'square': square,
    'cube': cube
}

result_add = operations['add'](20, 30)  # 30
result_square = operations['square'](10)  # 25

print(result_add)  
print(result_square)  