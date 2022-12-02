#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

from decimal import Decimal

def input_float():
    while True:
        try:
            user_number = input('Введите вещественное число ')
            user_number = float(user_number)
            return user_number
        except ValueError:
            print('Введено не вещественное число.')


def get_sum_of_digits_math(user_number):
    user_sum = 0
    user_number = abs(user_number)
    while round(user_number, 4) - int(user_number) != 0:
        user_number *= 10
        
    while user_number > 0:
        user_sum = user_number % 10 + user_sum
        user_number = user_number // 10
    return user_sum

num = input_float()
sum = int(get_sum_of_digits_math(num))
print(f'{num} -> {sum}')


