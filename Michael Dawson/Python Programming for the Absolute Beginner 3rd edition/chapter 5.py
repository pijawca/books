#-*- coding: utf-8 -*-


import random


def first():
    '''
    Создайте программу, которая будет выводить список слов в случайном порядке. На экране должны печататься 
    без повторений все слова из представленного списка.
    '''
    words = ['Зима', 'Осень', 'Весна', 'Лето']
    random.shuffle(words)
    separator = ', '
    result = separator.join(words)
    print(result)


'''
Напишите программу "Генератор персонажей" для ролевой игры. Пользователю должно быть представлено
30 пунктов, которые можно распределить между четырьмя характеристиками: Сила, Здоровье, Мудрость
и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего "пула", но и воз-
вращать их туда из характеристик, которые он решит присвоить другие значения.
'''
points = 30
ticks = 3
strength = 0
hp = 0
wisdom = 0
dex = 0

while True:
    ticks -= 1
    put_strength = input(f'У вас осталось {points} очков. Сколько вы вложите в силу?\n')
    result = points - int(put_strength)
    ticks -= 1
    put_hp = input(f'У вас осталось {result} очков. Сколько вы вложите в здоровье?\n')
    result = result - int(put_hp)
    ticks -= 1
    put_wisdom = input(f'У вас осталось {result} очков. Сколько вы вложите в мудрость?\n')
    result = result - int(put_wisdom)
    ticks -= 1
    put_dex = input(f'У вас осталось {result} очков. Сколько вы вложите в ловкость?\n')
    result = result - int(put_dex)
    ticks -= 1
    print (ticks)
    
    if points <= 0:
        break
    if ticks <= 0:
        break
