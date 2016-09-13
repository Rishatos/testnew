# -*- coding: utf-8 -*-
# lol
import random
n = random.randint(0, 10)
print u"Я загадал число от 0 до 10."
print u"Отгадайте"
summ = 0
popitok = 0
one = 1
while n!= True:
    number = int(input(u"Введите предпологаемое число:"))
    print (u"Ваше количество попыток: ",summ)
    if number < n:   
        print u"Число больше"
        number = False
        summ = popitok + one
        print (u"Ваше количество попыток: ",summ)
        continue
    elif number > n:
        print u"Число меньше"
        number = False
        summ = popitok + one
        continue
    elif number == n:
        print u"Ура :)"
        number = True
        print (u"Вы отгадали число на попытки:",summ)
        break
    else:
        print u"Что-то не так..."
        number = False
    if popitok > 3:
        print u"Вы проиграли:"
        number = True
