#Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

def input_float():
    while True:
        try:
            user_number = input('Введите вещественное число: ')
            user_number = float(user_number)
            return user_number
        except ValueError:
            print('Введено не вещественное число.')

def get_sum_of_digits_str(user_number):
    user_sum = 0
    for i in str(user_number):
        if i.isdigit() == True:
            user_sum += int(i)
    return user_sum

num = input_float()
sum = int(get_sum_of_digits_str(num))
print(f'{num} -> {sum}')




