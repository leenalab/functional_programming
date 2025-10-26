# filter(function, iterable)

even_nums = filter(lambda x: x % 2 == 0, range(1, 11))

print(list(even_nums))