# lambda arguments: expression

add = lambda x, y: x + y
print(add(5, 3))  # Виведе 8

print((lambda x, y: x * y)(10, 20))


students = [
    ("Олена", 90),
    ("Андрій", 75),
    ("Марія", 90),
    ("Ігор", 85)
]

# Сортуємо за балами (спаданням), а при рівності — за іменем (зростанням)
sorted(students, key=lambda s: (-s[1], s[0]))

students_sorted = sorted(students, key=lambda s: (-s[1], s[0]))

print(students_sorted)
