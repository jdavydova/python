#День 1: Введение и основы синтаксиса
#📚 Что изучить:
#Как писать и запускать Python-код.
#Правила синтаксиса Python (отступы, комментарии).
#Функция print() для вывода данных.
#Ввод данных с помощью input().

print("Hello World !")

# name = input("Enter Your name : ")
# print ("Hello " + name )

#Напиши программу, которая запрашивает имя и возраст пользователя и выводит их на экран

name = input("What is Your name ")
age = input("How old are You? ")

print("Hello ", name)
print("Your age is ", age)

# Улучшенный вариант

name = input ("What is your name? ")
age = int(input("How old are You? "))
print(f"Hello, {name}!")
print(f"Your age is {age} years old")

# Добавим что будет в следующем году

print(f"Next year you will be {age + 1} years old")

# Что ты можешь ещё добавить?
# Проверку на корректность ввода:
try:
    age = int(input("How old are You? "))
    if age < 18:
        print("You're still a teenager!")
    else:
        print("You're an adult!")
except ValueError:
    print("Please enter valid number for age ")

# Условие для персонализированного ответа:



