#🗓️ День 5: Функции
#📚 Что изучить:
#Определение функций с def.
#Аргументы и возвращаемые значения (return).

#💻 Примеры кода:
def greet(name):
    return f"Hello, {name}!"

print(greet("Anna"))

#✅ Задача:
#Создай функцию, которая принимает два числа и возвращает их сумму, разность, произведение и частное.

def math_ops(numb_one, numb_two):
    sum_result = numb_one + numb_two
    diff = numb_one - numb_two
    mult = numb_one * numb_two

    if numb_two != 0:
        div = numb_one / numb_two
    else:
        div = "undefined (division by zero)"

    return (
        f"\nThe sum is {sum_result}\n"
        f"Difference is {diff}\n"
        f"The multiplication is {mult}\n"
        f"The division is {div:.2f}")

print (math_ops(5,6))