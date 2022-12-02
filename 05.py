#Реализуйте алгоритм генерации случайного числа.(Не используя библиотеки связанные с рандомом)

import time

#генерация целых положительных чисел
#start = int(input('Введите начало отрезка: '))
#end = int(input('Введите конец отрезка: '))
start = 1
end = 100
decimal = len(str(end-1))


def random_generation(start, end, decimal):
    ran_dom = (int(time.time()*1000000)) * 5829 + 6231
    random_num = ran_dom % 10**decimal
    if start < random_num < end:
        return random_num
    else:
        return random_generation(start, end, decimal)

print(random_generation(start, end, decimal))
