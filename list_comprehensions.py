# compehensions - [new_item for item in iterable if condition]

sq = [x**2 for x in range(1, 6)]
print(sq) # вивід квадратів всіх чисел в діапазоні range(1, 6)
# тобто Створення списку квадратів чисел від 1 до 5:

even_squares = [x**2 for x in range(1, 10) if x % 2 == 0]
print(even_squares)