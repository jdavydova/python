#🗓️ День 3: Условные операторы (if, else, elif)
#📚 Что изучить:
#Условия if, else, elif.
#Операторы сравнения (==, !=, >, <, >=, <=).
#Логические операторы (and, or, not).
#💻 Примеры кода:

#Проверка пароля
#Запроси пароль у пользователя и проверь, соответствует ли он заранее заданному паролю.

import getpass

password = "Mishka123"
attempts = 3

while attempts > 0:
    # Скрытый ввод пароля
    enter_passw = getpass.getpass("Enter your password: ")

    # Проверка пароля (без учёта регистра)
    if password.lower() == enter_passw.lower():
        print("The password is correct ✅")
        break
    else:
        attempts -= 1 
        print(f"The password is not correct ❌. Attempts left {attempts}")

age = int(input("Enter youe age: "))

if age >= 18:
    print("You are full grown")
elif(age > 12):
    print("You are teenager ")
else:
    print("You are baby! ")

#✅ Задача:
#Напиши программу, которая проверяет, является ли введённое число положительным, отрицательным или нулём.



try: 
    x = int(input("Enter the number: "))
    if x > 0:
        print("Your number is positive!")
    elif x == 0:
        print ("Your number equal zero!")
    else:
        print("Your number is negative")
except ValueError:
    print("Error! This is not valid number!")


#✅ Задачи для практики
#Проверка температуры
#Напиши программу, которая запрашивает температуру и сообщает, холодно ли, тепло или жарко:

#Меньше 10°C: "It's cold."
#От 10°C до 25°C: "It's warm."
#Больше 25°C: "It's hot."

try:
    temperature = float(input("Enter the temperature in Celsius: "))
    
    if temperature < 10:
        print ("It's cold.")
    elif 10 <= temperature <= 25:
        print("It's warm.")
    else:
        print("It's hot.")
except ValueError:
    print("Error! This is not valid number!")

# Определение наибольшего из трёх чисел
# Запроси три числа у пользователя и выведи наибольшее из них
try:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    z = int(input("Enter the third number: "))
    if ((x >=  y) and (x >= z)):
        print(f"The largest number is {x}")
    elif ((y >= x) and (y >= z)):
        print(f"The largest number is {y}")
    else:
        print(f"The largest number is  {z}")
except ValueError:
    print("Error! This is not valid number!")




