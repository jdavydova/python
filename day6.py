#🗓️ День 6: Практика и задачи
#Сочетание всех изученных тем.
#Попробуй решить задачи:
#Калькулятор: программа для выполнения математических операций.
#Игра "Угадай число": компьютер загадывает число, а пользователь пытается его угадать.

def calculator():
    print("Hello! I'm calculator! Welcome.\n")
    print("Choose an operation:\n")
    print("  1. Addition       (+)\n")
    print("  2. Difference     (-)\n")
    print("  3. Multiplication (*)\n")
    print("  4. Division       (/)\n")

    try:
        ops = int(input("Please enter number of operation: "))
        numb_one = float(input("Please enter the number one:"))
        numb_two = float(input("Please enter the number two:"))

        if ops == 1:
            print(f"The result of addition: {numb_one + numb_two}")
        elif ops == 2:
            print (f"The result of difference {numb_one - numb_two}")
        elif ops == 3:
            print(f"The result of multiplication {numb_one * numb_two}")
        elif ops == 4:
            if numb_two != 0:
                print(f"The result of substraction {numb_one / numb_two:.2f}")
            else:
                print("ERROR! Division by zero is not allowed")
        else: 
            print("Invalid operation selected")

    except:
        print("ERROR! Please enter valide number.")

#calculator()


#Игра "Угадай число": компьютер загадывает число, а пользователь пытается его угадать.
import random

# Компьютер загадывает случайное число от 1 до 100
number = random.randint(1,100)
attempts = 3
count = 1

while count <= attempts:
    try:
        guess_number = int(input("Welcome!\nPlease guesse number from 1 to 100"))
        count += 1  
        if guess_number > number:
            print (f"It's wrong. The number gussed is less. Please try again! You have {attempts} attempts.")
        if guess_number < number:
            print (f"It's wrong. The number gussed is higher. Please try again! You have {attempts} attempts.")
        else:
            print ("You guessed it. Well done! 🎉 ")
            break
    except:
        print ("Wrong number!")