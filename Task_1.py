# Задача 1. Напишите программу, которая принимает на
# вход цифру, обозначающую день недели, и выводит
# название этого дня недели.


def find_day():
    week = \
        {
            1: "Понедельник",
            2: "Вторник",
            3: "Среда",
            4: "Четверг",
            5: "Пятница",
            6: "Суббота",
            7: "Воскресенье",
        }
    while True:
        user_day = int(input("Введите номер дня недели: "))
        if user_day not in week:
            print("В неделе 7 дней, введите число от 1 до 7")
        else:
            day = week.get(user_day)
            return f'День {user_day} это {day}'


print(find_day())
