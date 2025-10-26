def outer_function(msg):
    message = msg

    def inner_function():
        print(message)

    return inner_function

# Створення замикання
my_func = outer_function("Hello, world!")
my_func()

"""
У цьому прикладі функція outer_function визначена таким чином, що приймає аргумент msg і 
створює внутрішню змінну message, значення якої ініціалізується переданим аргументом. 
Усередині outer_function розміщена інша функція, inner_function, яка призначена для виведення 
на екран значення змінної message. Важливим аспектом є те, що inner_function використовує змінну 
message, яка була визначена у зовнішньому лексичному середовищі outer_function.



Після виконання outer_function, замість того, щоб безпосередньо викликати inner_function, 
outer_function повертає її як об'єкт. Це дозволяє функції inner_function зберегти зв'язок 
зі своїм лексичним середовищем, навіть після завершення виконання outer_function.



Коли виконується дія my_func = outer_function("Hello, world!"), то функція my_func становиться
 посиланням на функцію inner_function. Чому? Тому, що коли викликається функція outer_function,
   вона повертає посилання на функцію inner_function. Далі коли ми викликаємо my_func() виконується
насправді саме функція inner_function , вона успішно виводить "Hello, world!". Це відбувається завдяки 
збереженню inner_function доступу до змінної message, що була визначена в outer_function. Така поведінка
 є класичним прикладом замикання, де внутрішня функція зберігає стан змінних зі свого лексичного контексту
 . """