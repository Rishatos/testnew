# -*- coding: utf-8 -*-
import random
n = random.randint(0, 10)
print u"Я загадал число от 0 до 10."
print u"Отгадайте"
pop = 3
one = 1
while n != True:
    number = int(input(u"Введите число "))
    if pop < 1:
        print u"Вы проиграли:"
        print u"********************"
        print u"*******LOSE*********"
        print u"********************"
        n = False
        break 
    if number < n:
        print u"------------"
        print u"Число больше"
        print u"------------"
        n == n
        pop = pop - one
        print (u"Увы. Вы не откадали число. Осталось попыток "),pop
        continue
    elif number > n:
        print u"------------"
        print u"Число меньше"
        print u"------------"
        pop = pop - one
        print (u"Увы. Вы не отгадали число. Осталось попыток "),pop
        n == n
        continue
    elif number == n:
        print u"*********************"
        print u"Вы отгадали число! :)"
        print u"********************"
        print u"*********WIN**********"
        print u"**********************"
        n = True
        print (u"Осталось попыток "),pop
        break
    else:
        print u"Что-то не так..."
        n = False
