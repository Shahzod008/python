# name = input("Привет! Как тебя зовут? ")
# print("Приятно познакомиться,", name)


# a = int(input("Ведите целое число: "))
# b = a * a
# print("квадрат числа", a, "равен", b)


# a = int(input("Ведите длину основания: "))
# b = int(input("Ведите высоту треугольника: "))
# c = (a * b) / 2
# print("Площадь треугольника равна", c)


# a = int(input("Ведите первое число: "))
# b = int(input("Ведите второе число: "))
# print("Сумма:", a + b)
# print("Разность:", a - b)
# print("Произведение:,", a * b)
# print("Частное:", a / b)


# a = input("У вас RUB или USD ")
# if a == "RUB":
#     b = int(input("Сколько RUB?"))
#     print("у вас", b * 0.011, "USD")
# elif a == "USD":
#     c = int(input("Сколько USD?"))
#     print("У вас", c * 91.25, "RUB")
# else:
#     print("Некорректный ответ")


# a = input("Какое величина вам известно метр или сантиметр? ")
# if a == "метр" and "Метр":
#     b = int(input("Ведите сколько метров: "))
#     print(b, "метр равен", b*100, "сантиметр")
# elif a == "сантиметр" and "см" and "Сантиметр":
#     c = int(input("Ведите сколько сантиметров: "))
#     print(c, "см равен", c/100, "метров")
# else:
#     print("Ведите правильное название величины")


# from tkinter import*
# root = Tk()
# root.title("Tk")
# root.geometry("400x400")
# root.mainloop()


# a = int(input("Ведите длину: "))
# b = int(input("Ведите ширину: "))
# print(a*b)


# a = int(input("Ведите радиус круга: "))
# print("Площадь круга ровна", a*3.14)


# a = float(input("Ведите рост: "))
# b = int(input("Ведите свой вес: "))
# c = b/(a*a)
# c = int(c)
# if c <= 18.5:
#     print("Ваш индекс маccы тела равна", c )
#     print("У вас недостаточный вес")
# elif 18.5 <= c < 25:
#     print("Ваш индекс маccы тела равна", c )
#     print("У вас нормальный вес")
# elif 25 <= c < 30:
#     print("Ваш индекс маccы тела равна", c )
#     print("У вас избыточный вес")
# elif c >30:
#     print("Ваш индекс маccы тела равна", c )
#     print("У вас ожирение")


# a = int(input("Ведите первое число: "))
# b = int(input("Ведите первое число: "))
# c = input("Ведите тип операции если умножение ведите (*) если деление ведите (/) если вычитание то (-) если сложение то (+): ")
# if c == '*':
#     print(a*b)
# elif c == '+':
#     print(a+b)
# elif c == '-':
#     print(a-b)
# elif c == '/':
#     print(a/b)
# else:
#     print("Вы ввели не правильно")


# a = int(input("Ведите число: "))
# if 2 % a:
#     print("Вы ввели четное число")
# else:
#     print("Вы ввели нечетное число")


# a = int(input("Ведите число: "))
# print(f"{a} в двоичной системе равна {a:0b}")


# a = int(input("Введите ваш возраст: "))
# if a<18:
#     print("Иди учи уроки бро!")
# elif a>=18:
#     print("Welcome Бро!")


# from pyfiglet import Figlet
# preview_text = Figlet(font='slant')
# print(preview_text.renderText('HELLO, WORLD'))


# a = input()
# print(a[::-1])


# print('нечет' if int(input('> ')) % 2 else 'чет')


# import schedule
# import time
# from plyer import notification
# def remind_1():
#     title = 'Напоминание 1'
#     message = 'Время выполнить важную задачу 1!'
#     timeout = 10
#     notification.notify(
#         title=title,
#         message=message,
#         timeout=timeout
#     )
# def remind_2():
#     title = 'Напоминание 2'
#     message = 'Время выполнить важную задачу 2!'
#     timeout = 10
#     notification.notify(
#         title=title,
#         message=message,
#         timeout=timeout
#     )
# reminder_time_1 = "02:45"
# reminder_time_2 = "02:44"
# schedule.every().day.at(reminder_time_1).do(remind_1)
# schedule.every().day.at(reminder_time_2).do(remind_2)

# while True:
#     schedule.run_pending()
#     time.sleep(60) 


# a = input("Есть ли у вас первоначальная сумма? ").lower()
# if a == "да" or a == "есть":
#     b = int(input("Первоначальная сумма: "))
# dav = 0
# dyv = 0
# f = 0
# c = input("Какая периодичность пополнения?(Каждый месяц/Каждый день/Каждый год): ").lower()
# if c == "каждый месяц" or c == "месяц" or c == "месячная":
#     d = int(input("Сумма: "))
#     dyv = d*12
# elif c == "каждый день" or c == "день" or c == "дневная":
#     g = int(input("Сумма: "))
#     dav = g*365
# elif c == "каждый год" or c == "год" or c == "годовая":
#     f = int(input("Сумма: "))
# else:
#     print("Некорректный ввод. Пожалуйста, выберите один из вариантов: Каждый месяц, Каждый день, Каждый год.")
# lol = [dav, dyv, f]
# dev = 0
# div = 0
# y = 0
# s = input("Начисление процентной ставки?(Каждый месяц/Каждый день/Каждый год): ").lower()
# if s == "каждый месяц" or s == "месяц" or s == "месячная":
#     r = int(input("Процент: "))
#     dev = r*12
# elif s == "каждый день" or c == "день" or c == "дневная":
#     t = int(input("Процент: "))
#     div = t*365
# elif s == "каждый год" or c == "год" or c == "годовая":
#     y = int(input("Процент: "))
# else:
#     print("Некорректный ввод. Пожалуйста, выберите один из вариантов: Каждый месяц, Каждый день, Каждый год.")
# prs = [dev, div, y]
# z = int(input("Количесто лет инвестиции: "))
# if s in ["каждый месяц", "месяц", "месячная"]:
#     selected_prs = b * (1 + dev) ** (z * 12) 
# elif s in ["каждый день", "день", "дневная"]:
#     selected_prs = b * (1 + div) ** (z * 365)
# elif s in ["каждый год", "год", "годовая"]:
#     selected_prs = b * (1 + y/100) ** z
# print(selected_prs)


# import random

# number1 = random.randint(1, 10)
# number2 = random.randint(1, 10)

# user_input = int(input(number1* number2))
# if user_input == number1 * number2:
#     print("Правильно!")
# else:
#     print("Неправильно!")


# a = input("Что вам известно: стороны или диагональ? ").lower()
# d = input("Отлично! Пожалуйста, введите длину диагонали (d): ").lower()
# if a == "сторона" or a == "стороны" or a == "первое":
#     c = int(input("Прекрасно! Вы выбрали прямоугольник. Пожалуйста, введите длину стороны a:"))


# from pytube import YouTube
# link = "Ссылка в видео"
# yt = YouTube(link)
# yt.streams.get_highest_resolution().download()
# print("Видео скачан! ")


# vopros = input("Что вы хотите узнать? \n1) узнать значение дробей \n2) узнать правильность дроби \nВежите номер: ")
# a = int(input("Ведите числитель: "))
# b = int(input("Ведите знаменатель: "))
# print(a/b)


# from math import sqrt
# a = int(input("Ведите зночение а: "))
# b = int(input("Ведите зночение b: "))
# c = int(input("Ведите зночение c: "))
# d = int(input("Ведите зночение =: "))
# # 10x^2+30x+20=0
# # a=10, b=30, c=20
# diskr = b**2-4*a*c
# if diskr > 0:
#     x1 = -b+sqrt(diskr)
#     x2 = x1/(2*a)
#     x3 = -b-sqrt(diskr)
#     x4 = x3/(2*a)
#     print(x2,x4)
# elif diskr < 0:
#     print("Корней нет")
# elif diskr == 0:
#     x3 = -b/2*a
#     print(x3)





# from math import sqrt
# v = input("Какая сторона треугольника вам не известно?\nc или a или b?\nответ дайте одной буквой: ")
# if v == "c":
#     a = int(input("Ведите сторону a"))
#     b = int(input("Ведите сторону b"))
#     if a > b:
#         c = (a*a)+(b*b)
#         print(int(sqrt(c)))
#     if a < b:
#         c = (b*b)+(a*a)
#         print(int(sqrt(c)))
# elif v == "a":
#     b = int(input("Ведите сторону b"))
#     c = int(input("Ведите сторону с"))
#     if b<c:
#         a=(c*c-b*b)
#         print(int(sqrt(a)))
#     if b>c:
#         a = (b*b-c*c)
#         print(int(sqrt(a)))
# elif v == "b":
#     a = int(input("Ведите сторону a"))
#     c = int(input("Ведите сторону с"))
#     if a<c:
#         b=(c*c-a*a)
#         print(int(sqrt(b)))
#     if a>c:
#         b = (a*a-c*c)
#         print(int(sqrt(b)))
# else:
#     print("Некорректный ввод. Введите 'c', 'a' или 'b'.")


# print("Hello, World")