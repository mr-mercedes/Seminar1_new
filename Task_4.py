# Задача 4. Напишите программу, которая на вход
# принимает число (N), а на выходе показывает все чётные
# числа от 1 до N.

def print_even_item(user_input):
    user_input = abs(user_input)
    for i in range(2, user_input + 1, 2):
        print(i, end=' ')


user_number = int(input('Введите число: '))
print_even_item(user_number)
