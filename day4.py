#🗓️ День 4: Циклы (for, while)
##📚 Что изучить:
#Цикл for для перебора элементов.
#Цикл while для повторений до выполнения условия.
#Функция range().

#💻 Примеры кода:

# Цикл for
for i in range(5):
    print(f"Iteration {i}")

# Цикл while
count = 0
while count < 5:
    print(f"Counter : {count}")
    count += 1

#✅ Задача:
#Напиши программу, которая выводит таблицу умножения для числа, введённого пользователем.
try:
    number = int(input("Enter the number: "))

    print(f"\nMultiplication table for {number}:\n")
    for i in range(1, 11):
        print(f"{i} x {number} = {i * number}") 
except ValueError:
    print("Error! Please enter a valid integer number.")

#✅ Задачи для практики
#Сумма чисел от 1 до 100
#Напиши программу, которая вычисляет сумму всех чисел от 1 до 100.

total_sum = 0
for i in range(1, 101):
    total_sum += i
#   print (sum)

print (f"\nThe sum of all numbers from 1 to 100 is {total_sum}.")

total_sum = sum(range(1, 1001))
print (f"\nThe sum of all numbers from 1 to 1000 is {total_sum}.")

#Поиск чётных чисел
#Выведи все чётные числа от 1 до 20 с использованием цикла for.
print ("\nEven numbers:" )
for i in range(1, 21):
    # Проверка, является ли число чётным
    if i % 2 == 0:
        print(i, end=" ")

#Отгадай число
#Напиши программу, в которой компьютер загадывает число, а пользователь пытается его угадать. Используй цикл while
import random

# Компьютер загадывает случайное число от 1 до 10
number = random.randint(1,10)

try:
    guess_number = int(input("\nGuess the number (between 1 and 10): "))
    
    while number != guess_number:
        if guess_number > number:
            print("Wrong! The number is lower.")
        else:
            print("Wrong! The number is higher.")
    
        print ("Try again !")
                
        # Запрос следующей попытки
        guess_number = int(input("Gess the number: "))
            
    print("You guessed it. Well done! 🎉 " )
    
except ValueError:
    print("Error! Please enter a valid integer number.")
