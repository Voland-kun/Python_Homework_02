#Задайте список из 2N+1 элементов, заполненных числами из промежутка [-N, N]. 
#Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

def input_int():
    while True:
        try:
            user_number = input('Введите целое число ') #4 -> -12
            user_number = int(user_number)
            return user_number
        except ValueError:
            print('Введено не целое число.')

def list_generation(user_number):
    user_list = []
    for i in range(-user_number, user_number+1):
        user_list.append(i)
    return user_list

def get_list_product(user_list):
    product = 1
    data = open('position.txt', 'r')
    for line in data:
        product *= user_list[int(line)]
    return product

num = input_int()
result_list = list_generation(num)
print(get_list_product(result_list))