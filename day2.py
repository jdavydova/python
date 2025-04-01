#🗓️ День 2: Переменные и типы данных
#📚 Что изучить:
#Типы данных: строки (str), числа (int, float), логические значения (bool).
#Переменные и присваивание значений.
#📚 Что изучить:
#Типы данных: строки (str), числа (int, float), логические значения (bool).
#Переменные и присваивание значений.

#🗓️ День 2: Переменные и типы данных в Python
#Сегодня мы разберём, что такое переменные и основные типы данных в Python.
#Это фундаментальные знания, которые помогут тебе работать с разной информацией в программах.

#📝 Что такое переменные?
#Переменная — это "контейнер" для хранения данных.
#Ты можешь присвоить переменной любое значение и использовать её для работы с этим значением позже.

#📌 Правила именования переменных:
#Имя переменной может содержать буквы, цифры и символ нижнего подчёркивания (_).
#Имя не может начинаться с цифры.
#Имена чувствительны к регистру (age и Age — разные переменные).
#Используй осмысленные имена (например, user_name, а не x).#
#🐍 Типы данных в Python
#1. Строки (str)
#Строки используются для хранения текста.

name = "Anna"
city = 'Moscow'
print(name)
print(city)

#2. Целые числа (int)
#Используются для хранения целых чисел.
age = 25
year = 2024
print(age)


#3. Числа с плавающей точкой (float)
#Используются для хранения дробных чисел.

height = 1.75
weight = 65.5
print(height)

#4. Логические значения (bool)
#Хранят только два значения: True (истина) или False (ложь).

is_student = True
has_passed = False
print(is_student)

#🔄 Преобразование типов данных
#Ты можешь изменять типы данных с помощью функций int(), float(), str() и bool().

age = "25"           # Строка
age_number = int(age)  # Преобразуем в целое число
print(age_number + 5)  # Выведет 30


# 💻 Примеры кода:
name = "Julia"
age = 36
height = 1.80
is_student = True
country = "Greece"
town = "Athens"
postal_code = 15122
student_status = "Yes" if is_student else "No"

print(f"\n Name: {name},\n Age: {age},\n Height: {height:.2f} meters,\n Student: {student_status},\n Country: {country},\n Town: {town},\n Postal Code: {postal_code}.\n")


# ✅ Задачи для практики
# Конвертер температуры
# Напиши программу, которая запрашивает температуру в градусах Цельсия и переводит её в градусы Фаренгейта по формуле:
celcius = float(input("Please enter the temperature in Celsius:"))
farenheit = float(celcius * 9/5 + 32)

print (f"The temperature in Fahrenheit: {farenheit:.2f}")

#--------------------------------------------------------------------------------------------------------------------
#Арифметические операции
#Запроси два числа у пользователя и выведи их сумму, разность, произведение и частное.

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

sum_result = x + y
difference = x - y
multiplication = x * y

# Проверка на деление на ноль

if y != 0:
    quotient = x / y
else:
    quotient = "undefined (division by zero)"

# Вывод результатов
print(f"Sum is {sum_result}")
print(f"Difference is {difference}")
print(f"Multiplication is {multiplication}")

# Проверка типа для вывода частного

#Что такое isinstance() в Python?
#Функция isinstance() используется для проверки, является ли объект экземпляром указанного типа или класса.
#Она возвращает True, если объект соответствует типу, и False в противном случае.
if isinstance(quotient,float):
    print(f"Quotient is {quotient:.2f}")
else:
    print(f"Quotient is {quotient}")

# ------------------------------------------------------------------------------------------------------------------
#   Информация о пользователе
#Запроси у пользователя его имя, возраст и город. Выведи на экран сообщение:

name = input("What is Your name? ")
age = int(input("How old are you?"))
height = float(input("How tall are you?"))
student_status = input("Are you student?\n Yes or No? ")
country = input("Which country do you live? ")
town = input("Which town dou you live? ")
postal_code = input("Which post code ?")

print(f"\n Name: {name},\n Age: {age},\n Height: {height:.2f} meters,\n Student: {student_status},\n Country: {country},\n Town: {town},\n Postal Code: {postal_code}.\n")


#Когда использовать bool()
#Для проверки ввода: Убедиться, что пользователь ввёл что-то, а не оставил поле пустым.
#Для фильтрации данных: Удалять пустые или None значения из списка.
#Для проверки условий: Проверять, содержит ли переменная ненулевое или непустое значение.
#Для явного приведения типов: Когда нужно явно преобразовать значение в True или False.
