# -*- coding: utf-8 -*-

import os
import sys
import random
import time
from random import randint

class Player:  #описываем персонажа
    """docstring for Player;."""
    hp = int(20)       # Heal point
    max_hp = int(20)   #
    pw = int(5)        #Power
    level = int(0)    #уровень
    q = int(1)         #квесты
    money = int(1000)        # money
    deposit = int(0)
    xp = int(0)       # Очки опыта  experience
    max_xp = int(10)  #
    medcine = int(7)
    heal_hp = int(5)   #Сила аптечки
    wearphone = "Руки"  #оружие
    wearphone_damage = int(0)
    name = "Джорж"

p = Player()

###################################
#ДОПОЛНИТЛЬНЫЕ ЭФФЕКТЫ
#загрузка готово
def Loading():
    i=11
    popka=0
    while i > 0:
        os.system('cls||clear')

        print("""


            ---------------------
            |                   |
                 Loading {}%
            |                   |
            ----------------------
            """.format(popka))
        popka += 10
        i-=1
        time.sleep(0.3)
#лого готово
def logo():
    print("""

     █████
     █═══█
      ███
      ███
 ████═███═████
    ███████
     █▒═▒█  ▄▀▀ ▀█▀ █▀▀ █▀▀ █      ▄▀▀  █▀▀ ▄▀▄ █▀▀▄ ▄▀▀  █▀▀
     █▒═▒█  ▀▄   █  █▀▀ █▀▀ █ ▄    █ ▀▌ █▀▀ █ █ ██▀  █ ▀▌ █▀▀
     █▒═▒█  ▀▀   ▀  ▀▀▀ ▀▀▀ ▀▀▀    ▀▀▀  ▀▀▀  ▀  ▀ ▀▀ ▀▀▀  ▀▀▀
     █▒═▒█
     █▒═▒█
     █▒═▒█
     █▒═▒█
     █▒═▒█
      █▒█
       █
""")
    time.sleep(3)
# готово
def Game_Ower():
    os.system('cls||clear')
    print("""



              КОНЕЦ ИГРЫ

    """)
    time.sleep(3)
    sys.exit()   #Конец игры (с завершением работы)
#  готово
def win_game(p):
    print("""
                       ▄▄
                     ▄▀░░▌
                   ▄▀▐░░░▌  Оказалось никакой принцессы нет
                ▄▀▀▒▐▒░░░▌  Ну ничего, в другой игре спасешь принцессу
     ▄▀▀▄   ▄▄▀▀▒▒▒▒▌▒▒░░▌
    ▐▒░░░▀▄▀▒▒▒▒▒▒▒▒▒▒▒▒▒█  Спасибо за игру {}
    ▌▒░░░░▒▀▄▒▒▒▒▒▒▒▒▒▒▒▒▒▀▄
    ▐▒░░░░░▒▒▒▒▒▒▒▒▒▌▒▐▒▒▒▒▒▀▄
    ▌▀▄░░▒▒▒▒▒▒▒▒▐▒▒▒▌▒▌▒▄▄▒▒▐
   ▌▌▒▒▀▒▒▒▒▒▒▒▒▒▒▐▒▒▒▒▒█▄█▌▒▒▌
 ▄▀▒▐▒▒▒▒▒▒▒▒▒▒▒▄▀█▌▒▒▒▒▒▀▀▒▒▐░░░▄
▀▒▒▒▒▌▒▒▒▒▒▒▒▄▒▐███▌▄▒▒▒▒▒▒▒▄▀▀▀▀
▒▒▒▒▒▐▒▒▒▒▒▄▀▒▒▒▀▀▀▒▒▒▒▄█▀░░▒▌▀▀▄▄
▒▒▒▒▒▒█▒▄▄▀▒▒▒▒▒▒▒▒▒▒▒░░▐▒▀▄▀▄░░░░▀
▒▒▒▒▒▒▒█▒▒▒▒▒▒▒▒▒▄▒▒▒▒▄▀▒▒▒▌░░▀▄
▒▒▒▒▒▒▒▒▀▄▒▒▒▒▒▒▒▒▀▀▀▀▒▒▒▄▀
▒▒▒▒▒▒▒▒▒▒▀▄▄▒▒▒▒▒▒▒▒▒▒▒▐
▒▒▒▒▒▒▒▒▒▒▒▒▒▀▀▄▄▄▒▒▒▒▒▒▌
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐
    """.format(p.name))
#готово
def start_game(p):
    os.system('cls||clear')
    print("""

                   Приветствую тебя храбрец!

          Тебе предстоит пройти трудный путь и только
    пройдя его полностью возможно ты сможешь найти принцессу

                Так же не забывай про Достижения*

               Но для начала скажи как тебя зовут?


""")
    p.name = str(input("      "))
    time.sleep(3)
# тестируем
def saveload(p):
    deside=input("save/load/back    ")
    if deside == "save":   #нормас сохраняет Spisok
        # Spisok это мписок параметров, через который реализуем сохранялку
        Spisok = [p.hp,p.max_xp,p.pw,p.level,p.q,p.money,p.xp,p.max_xp,p.medcine,p.wearphone,p.wearphone_damage,p.name]
        print("Список характеристик",Spisok)
        open('soxranenie.txt', 'w').close() # сначала очищаем
        with open('soxranenie.txt', 'w') as f:  # теперь пишем
            for Spisok in Spisok:
                f.write("%s\n" % Spisok)                
        os.system('cls||clear')
        menu_simple(p)
    elif deside == "load":
        sp = [] #создаем список
        with open('soxranenie.txt', 'r') as file:
            #Получаем все строки из файла
            lines = file.readlines()
        for line in lines:
            # каждую строку разбиваем по пробелу
            temp = line.split()
            # добавляем через extend, чтобы получить список, а не список списков
            sp.extend(temp)
        p.hp = sp[0]
        p.max_hp = sp[1]
        p.pw = sp[2]
        p.level = sp[3]
        p.q = sp[4]
        p.money = sp[5]
        p.xp = sp[6]
        p.max_xp = sp[7]
        p.medcine = sp[8]
        p.wearphone = sp[9]
        p.wearphone_damage = sp[10]
        p.name = sp[11]
        print("Готово, загружено!")
        time.sleep(1)
        os.system('cls||clear')
        menu_simple(p)
    elif deside == "back":
        os.system('cls||clear')
        menu_simple(p)
    else:
        print("Давай по новой, ты что то не то написал")
        time.sleep(1)
        os.system('cls||clear')
        saveload(p)
###################################

#Таверно готово
def taverna(p):
    os.system('cls||clear')
    print("""
        Ты вошел в таверну.
        1. Специальные задания.
        2. Пойти поиграть в очко.
        3. Уйти
    """)
    k = input("")
    if k == "1":
        barplace(p)
        os.system('cls||clear')
    if k == "2":
        os.system('cls||clear')
        blackjack(p)
    if k == "3":
        os.system('cls||clear')
        menu_simple(p)
    os.system('cls||clear')
#инвентарь готово
def inventary(p):
    os.system('cls||clear')
    print("""

   _____ИНВЕНТАРЬ_______
    """)
    print("У тебя {} Аптечек".format(p.medcine))
    print("Тво оружие: {}".format(p.wearphone))
    print("1. Назад.")
    n = input("")
    if n == "1":
        os.system('cls||clear')
        menu_simple(p)
    else:
        os.system('cls||clear')
        menu_simple(p)
#
def menu_upgrade(p):
    while p.money > 0:
        print("Выбирай прокачку!             Баланс: {}$".format(p.money))
        print("----------------------------------------------")
        print("1. Здоровье {}/{}  20$".format(p.hp, p.max_hp))
        print("2. Сила {}  35$".format(p.pw))
        print("3. Вернуться")
        n = input("Номер:")
        if n =="1":
            if p.money >= 20:
                p.money -=20
                p.hp +=4
                p.max_hp = p.max_hp+5
            else: print("Нехватает денег")
            time.sleep(0.1)
            os.system('cls||clear')
        if n == "2":
            if p.money >= 35:
                p.pw +=2
                p.money -=35  #меню прокачки
            else: print("Нехватает денег")
            time.sleep(0.1)
            os.system('cls||clear')
        if n == "3":
            break
    os.system('cls||clear')
#магазин готово
def menu_market(p):
    while p.money > 0:
        print("____У {}______{}$ ________".format(p.name, p.money))
        print("""

░░▄███████▀▀▀▀▀▀███████▄
░▐████▀▒▒▒▒▒▒▒▒▒▒▀██████▄
░███▀▒▒▒▒▒▒▒▒▒▒▒▒▒▒▀█████
░▐██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▌   Добро пожаловать в мой магазин!
░▐█▌▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒████▌
░░█▒▄▀▀▀▀▀▄▒▒▄▀▀▀▀▀▄▒▐███▌ Тут ты можешь купить следующие товары:
░░░▐░░░▄▄░░▌▐░░░▄▄░░▌▐███▌
░▄▀▌░░░▀▀░░▌▐░░░▀▀░░▌▒▀▒█▌
░▌▒▀▄░░░░▄▀▒▒▀▄░░░▄▀▒▒▄▀▒▌     1. Аптечка  1$
░▀▄▐▒▀▀▀▀▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒█      2. Деревянная палка (+3 урона) 5$
░░░▀▌▒▄██▄▄▄▄████▄▒▒▒▒█▀       3. Дешевый меч (+5 урона) 10$
░░░░▄██████████████▒▒▐▌        4. Обычный меч (+9 урона) 40$
░░░▀███▀▀████▀█████▀▒▌         5. Легендарный меч(+15 урона) 90$
░░░░░▌▒▒▒▄▒▒▒▄▒▒▒▒▒▒▐          6. Вернуться
░░░░░▌▒▒▒▒▀▀▀▒▒▒▒▒▒▒▐
""")
        n = input("Номер:")

        if n == "1":
            p.medcine +=1
            p.money -=1
            os.system('cls||clear')
        if n == "2":
            if p.money >= 5:
                p.money -=5
                p.wearphone = "Деревянная палка"
                p.wearphone_damage =  3
            else: print("Нехватает денег")
            time.sleep(1)
            os.system('cls||clear')
        if n == "3":
            if p.money >= 10:
                p.money -=10
                p.wearphone = "Дешевый меч"
                p.wearphone_damage =  5
            else: print("Нехватает денег")
            time.sleep(1)
            os.system('cls||clear')
        if n == "4":
            if p.money >= 40:
                p.money -=40
                p.wearphone = "Обычный меч"
                p.wearphone_damage =  9
            else: print("Нехватает денег")
            time.sleep(1)
            os.system('cls||clear')
        if n == "5":
            if p.money >= 90:
                p.money -=90
                p.wearphone = "Легендарный меч"
                p.wearphone_damage =  15
            else: print("Нехватает денег")
            time.sleep(1)
            os.system('cls||clear')
        if n == "6":
            break
    os.system('cls||clear')
#готово
def menu_stats(p):
    print("""
____________________________Статус {}___________
            ▄▄▀▀▀▀▀▀▀▄▄
         ▄▀▀░░░░░░░░░░░▀▄
        ▄▀░░░░░░░░░░░░░░░░▀▄
       ▌░░░░░░░░░░░░░░░░░░░▌    Здоровье {}/{}
      ▌░░░░░░░░░░░░░░░░░░░░▐    Сила {}
      ▌░▄█████▄░░░░░▄████▄░▐    Лечение {}
     ▐░▌░▄▄▄▄▄░░░░░░▄▄▄▄▄░░▌    Уровень {}
     ▌░▌░░░██░░░▐░▌░░██░░░█     Опыт {}
     ▀▄▐░░░░░░░░▐░▌░░░░░░░▌     Баланс {}$
       █░░░░░░░░▌░▐░░░░░░▐      Оружие {}
       █░░░░░░░▀▄▄▄▀░░░░░▌
        █░░░░▄░░░░░░▄░░░█
    ▄▄▄▄█░░░░░▀▀▀▀▀▀░░░█
▄▄▀▀▒▒▒▌░▀▄░░░░░░░░░░░█
▒▒▒▒▒▒▐░░░░▀▀▄░░░░░▄▄▀▀▄
▒▒▒▒▒▒▌░░░░░░░▀▀▀▀▀░░▐▒▒▀▄
▒▒▒▒▒▒▐░░░░░░░░░░░░░░▐▒▒▒▒▀▄
▒▒▒▒▒▒▒▐░░░░░░░░░░░░▐▒▒▒▒▒▒▒▀▄
""".format(p.name, p.hp, p.max_hp, p.pw, p.heal_hp, p.level, p.xp, p.money, p.wearphone))
    input("Enter чтобы продолжить.")
    os.system('cls||clear')   #Cтатистика персонажа

#Стартовое меню (главное)
def menu_simple(p):
    os.system('cls||clear')
    while True:
        print("""

        Выбери действие...
    1. Пойти сражаться
    2. Посмотреть статистику персонажа
    3. Прокачать навыки
    4. Пойти в магазин
    5. Пойти в таверну
    6. Инвентарь
    7. Сохранения


Для выхода из игры напиши 'exit'.

""")

        n = input("Номер:")
        if n == "1":
            os.system('cls||clear')
            menu_fight(p)
        if n == "2":
            os.system('cls||clear')
            menu_stats(p)
        if n == "3":
            os.system('cls||clear')
            menu_upgrade(p)
        if n == "4":
            os.system('cls||clear')
            menu_market(p)
        if n == "5":
            os.system('cls||clear')
            taverna(p)
        if n == "6":
            os.system('cls||clear')
            inventary(p)
        if n == "7":
            os.system('cls||clear')
            saveload(p)
        if n == "exit":
            os.system('cls||clear')
            print("Выход из игры")
            time.sleep(2)
            os.system('cls||clear')
            sys.exit()
        if n == "givememoney":
            p.money += 1000
            os.system('cls||clear')
            menu_simple(p)
        else:
            os.system('cls||clear')
            menu_simple(p)
    os.system('cls||clear')
#готово
def menu_fight(p):
    os.system('cls||clear')             #Бой с противником
    ehp = 2 * randint(4,20)
    epw = p.pw + randint(-5,5)
    while ehp>0:
        print("""
_________Твое здоровье: {} из {}, Твоя сила: {}____
░░░░░░░▄▄▄▄▄▓▓▓▄▄▄░░░░░
░░░░▄▄▓▀▀▀▀▀▀▓▓▓▓▓▓▄░░░
░░▄▄▓▀▀░░░░░░░░░░░░▀▓▄░     Твой враг - циклоп!
░▐▓▓▌░░░░░░▄▄▄▄▄░░░░░▓▌
░▐▓▒░░░░░░█░▒◐▒░█░░░░░▓
░▓▓▌░░░░░░░▀▀▀▀▀░░░░░▒▓      Здоровье врага: {}
░▐▓░░░░░░░░░░░░░░░░▒▒▒▓      Сила врага:{}
█░▀▄░█▄█▀▄▄░▀░▀▄▄▀░░█░█
░█░░░▀▄█▄█░█▀▄▄▄▄▄▀██░█
░░█░░░░█░███▄█▄█▄███░░█
░░░█░░░▀▀█░█▀█▀█▀███░█
░░░░▀▄░░░░▀▀▄█▄█▄█▄▀░█
░░░░░░▀▄▄░▒▒▒░░░░░░░░░█
░░░░░░░░░▀▀▄▄▄▄▄▄▄▄▄▄▀

    1. Ударить с силой {}".format
    2. У тебя {} аптечек которые востанавливают по {}ед. здоровья
    3. Сбежать""".format( p.hp, p.max_hp, p.pw, ehp, epw, p.pw + p.wearphone_damage , p.medcine, p.heal_hp))
        n = input("Номер:")
        os.system('cls||clear')

        if n == "1":
            r=randint(1,2)
            if r == 1:
                ehp -= (p.pw + p.wearphone_damage)
                print("Ты наносишь удар")
            if r == 2:
                p.hp -= epw
                print("Твой враг наносит удар")
                if p.hp <= 0:
                    print("Ты умер")
                    time.sleep(2)
                    Game_Ower()

        if n == "2":
            if p.medcine > 0:
                p.medcine -= 1
                p.hp += p.heal_hp
                if p.hp > p.max_hp:
                    p.hp = p.max_hp

                    print("Лечение...{}".format(p.hp))
            else: print("Аптечки кончились!")

        if n == "3":
            r = randint(1,2)
            if r == 2:
                print("Ты сбежал")
                return True
            else:
                p.hp -= 1
                print("Ты не смог сбежать и потерял 1 ед здоровья")

    os.system('cls||clear')
    p.xp += epw
    p.killed +=1
    p.money += epw            #даём опыта
    if p.xp >= p.max_xp:
        p.xp = 0
        p.max_xp += 5
        p.level +=1
    os.system('cls||clear')
#

#готово

def blackjack(p):
    while True:
        start = input('Нажмите Enter что бы начать, для выхода введите Exit \n')
        start = start.lower()
        if start != 'exit':
            stavka = int(input("Сколько будешь ставить?"))
            if p.money >= stavka:
                p.money -= stavka
            else:
                print("Куда столько ставишь, у тебя всего {}$".format(p.money))
                time.sleep(3)
                taverna(p)
            deck = [6, 7, 8, 9, 10, 10, 10, 10, 11] * 4
            count = 0
            croupier_count = 0
            # перемешали колоду
            random.shuffle(deck)
            # переменные для крупье
            croupier_current = deck.pop()
            croupier_count += croupier_current
            print('У крупье {} очков'.format(croupier_current))
            print('Добро пожаловать в игру 21!: ')

            while True:
                os.system('cls||clear')
                choise = input("""____У вас {} очков_____

Что бы взять карту нажмите y или n что бы остановиться: """.format(count))
                choise = choise.lower()

                if choise == 'y':
                    current = deck.pop()
                    print('Вам попалась карта достоинством {}'.format(current))
                    count += current
                    if count > 21:
                        print('У вас перебор')
                        break
                    elif count == 21:
                        print('Вы выиграли')
                        p.money += (stavka*3)
                        break
                    else:
                        print('')
                else:
                    print('У вас {} очков, крупье берет карту: '.format(count))
                    # блок добора и сравнения карт крупье
                    while True:
                        if croupier_count >= 17:
                            if count <= croupier_count <= 21:
                                print('Вы проиграли!, у вас {} у крупье {}'.format(count, croupier_count))
                                break
                            else:
                                print('Вы выиграли, набрав {} очков'.format(count))
                                p.money += (stavka*3)
                                break
                        else:
                            if croupier_count < 17:
                                croupier_current = deck.pop()
                                croupier_count += croupier_current
                                print(
                                    'Крупье взял еще и ему выпало {}, у крупье {}'.format(croupier_current, croupier_count))
                    break
        else:
            taverna(p)

#Квесты
def barplace(p):
    os.system('cls||clear')
    print("""

Ты подошел к барной стойке, тут можно взять задание, ты готов?
        """)
    n = input("y/n")
    if n == "y":
        if p.q == 1:
            if p.level >=25:
                 time.sleep(1)
                 os.system('cls||clear')
                 quest_1(p)
            else:
                print("Тебе надо получить 25 уровень!")
                time.sleep(1)
                taverna(p)
        elif p.q == 2:
            if p.level >=50:
                time.sleep(1)
                os.system('cls||clear')
                quest_2(p)
            else:
                print("Тебе надо получить 50 уровень!")
                time.sleep(1)
                taverna(p)
        elif p.q == 3:
            if p.level >=75:
                time.sleep(1)
                os.system('cls||clear')
                quest_3(p)
            else:
                print("Тебе надо получить 75 уровень!")
                time.sleep(1)
                taverna(p)
        elif p.q == 4:
            if p.level >=100:
                time.sleep(1)
                os.system('cls||clear')
                final_quest(p)
            else:
                print("Тебе надо получить 100 уровень!")
                time.sleep(1)
                taverna(p)
    else:
        time.sleep(1)
        os.system('cls||clear')
        taverna(p)
#готово
def quest_1(p):
    os.system('cls||clear')
    time.sleep(1)
    print("""
Ну чтож, вижу ты готов к своему первому заданию
    """)
    x1 = 1
    x2 = 100
    x3 = 10   #попыток
    w = True
    a = (random.randint(x1, x2))
    os.system('cls||clear')
    print ("Угадай число от {} до {}".format(x1,x2))
    while w :
    	if x3>=0:
    		print ("                    ")
    		print("попыток",x3)
    		s = input ("Введите число : ")
    		os.system('cls||clear')
    		print ("                    ")
    		x3 -= 1
    		if (int(a) == int(s)):
    			print ("У вас получилось")
    			print("p/q",p.q)
    			p.q+=1
    			print("p/q",p.q)
    			w = False;
    		else :
    			if (int(a) > int(s)):
    				print("СЛИШКОМ МАЛО")
    			if (int(a) < int(s)):
    				print("СЛИШКОМ МНОГО")
    	else:
    		w = False
    		print("проиграли")
    		time.sleep(0.3)
    time.sleep(2)
    os.system('cls||clear')
#готово
def quest_2(p):
    os.system('cls||clear')
    time.sleep(1)
    print("""
Ну чтож, вижу ты готов к своему второму заданию
    """)
    time.sleep(2)
    os.system('cls||clear')
    words = ["аист", "акула", "бабуин", "баран", "барсук", "бобр", "бык", "варан", "верблюд", "волк", "вомбат", "воробей", "ворон", "выдра",
    "голубь", "гусь", "додо", "дятел", "енот", "ехидна", "еж", "жаба", "жираф", "журавль", "заяц", "зебра", "землеройка", "зяблик",
    "игуана", "кабан", "казуар", "кайман", "какаду", "кальмар", "камбала", "канарейка", "каракатица", "карп", "кенгуру",
    "киви", "кит", "лама", "ламантин", "ласка", "ласточка", "лебедь", "лев", "лемур", "ленивец", "леопард", "лиса", "лягушка",
    "мотылек", "муравьед", "муравей", "мангуст", "медведь", "морж", "муха", "мышь", "медуза", "нарвал", "носорог", "орел", "омар", "олень", "овцебык",
    "осьминог", "орел", "осел", "оса", "овца", "опоссум", "обезьяна", "паук", "пескарь", "пингвин", "пиранья", "попугай",
    "пчела", "рысь", "рыба", "росомаха", "страус", "сурок", "стрекоза", "сорока", "сова", "снегирь", "сокол", "собака", "слон",
    "слон", "скорпион", "скворец", "скат", "сельдь", "свинья", "сурикат", "скунс", "слизень", "светлячок", "тюлень", "тукан", "тигр",
    "трясогуска", "термит", "тетерев", "тунец", "тритон", "тарантул", "таракан", "тля", "утконос", "уж", "устрица", "улитка", "угорь", "фазан", "фламинго",
    "форель", "хорек", "хомяк", "хамелеон", "цапля", "цесарка", "цикада", "черепаха", "червь", "чайка", "шимпанзе", "шиншилла",
    "щука", "эму", "ящерица", "ястреб", "як", "ягуар"]
    word=words[random.randrange(5)]
    len_word=len(word)
    health = 10
    test=False
    used_letters=""
    win_word=[]
    # заполнение массива для слова в игре
    for i in range(len(word)):
        win_word+="_"

    while len_word != 0 and health != 0:
        test = False
        # ввод буквы и проверка на повтор
        while True:
            letter = input("\nвведите букву ")
            if letter in used_letters or len(letter)>1:
                print("\nНе больше одного символа, попробуйте снова!")
            else:
                used_letters+=letter
                break
        count=0
        for i in word:
            if letter in i:
                len_word -= 1
                test=True
                win_word[count]=letter
            count+=1
        if not test:
            os.system('cls||clear')
            health -= 1
            print("Неверно")
            print(win_word)
        else:
            os.system('cls||clear')
            print("Верно")
            print(win_word)
        print("Ваше здоровье = ", health)
    if(len_word == 0):
        p.q+=1
        print("\nВы выиграли! Слово было", word.upper())
    else:
        print("\nВЫ ПРОИГРАЛИ! ПОПРОБУЙТЕ СНОВА!")
# готово
def quest_3(p):
    os.system('cls||clear')
    time.sleep(1)
    print("""
Ну чтож, вижу ты готов к своему третьему заданию
    """)
    time.sleep(2)
    os.system('cls||clear')
    listnum = [random.randint(0,9) for n in range(num_digits)]
    count=0
    pops=100
    while True:
        count+=1
        os.system('cls||clear')
        print("~~~ Попытка: " + str(count) + " ~~~")
        print("Попробуй угадать " + str(num_digits) + "-х значное число: ")
        # transform input string (e.g. "1234") to list of integers (e.g. [1,2,3,4])
        guess = [int(i) for i in str(input())]
        if guess == listnum:
            print("Ты Победил!")
            print("Тебе потребовалось "+str(count)+" попыток.")
            if count <= pops:
                print("Ты прошел испытание, ждем дебя на следующем уровне(тут это типа + уровень написать)")
            else:
                print("Тебе потребовалось более попыток, тебе придется перепройти",pops)
            break
        else:
            cow=0
            bull=0
            for x in range(0,num_digits):
                if guess[x]==listnum[x]:
                    cow += 1
                elif guess[x] in listnum: # look if digit is somewhere else in the solution key (might already be a cow)
                    bull += 1
        print("Коров: "+str(cow)+" Быков: "+str(bull))
        print("++++++++++++++++")
#готово
def final_quest(p):
    os.system('cls||clear')
    time.sleep(1)
    print("""
Ну чтож, вижу ты готов к своему последнему заданию
    """)
    time.sleep(2)
    os.system('cls||clear')


    BossHp = 1* randint(4,20)
    BossPower = 1* randint(1,5)
    while BossHp > 0:
        print("""  Твое здоровье: {} из {}, Твоя сила: {}

░░░░░░░░░░░░░▄▐░░░░
░░░░░░░▄▄▄░░▄██▄░░░  А вот и главный босс
░░░░░░▐▀█▀▌░░░░▀█▄░
░░░░░░▐█▄█▌░░░░░░▀█▄  Здоровье босса {}
░░░░░░░▀▄▀░░░▄▄▄▄▄▀▀  Сила босса {}
░░░░░▄▄▄██▀▀▀▀░░░░░
░░░░█▀▄▄▄█░▀▀░░░░░░
░░░░▌░▄▄▄▐▌▀▀▀░░░░░
░▄░▐░░░▄▄░█░▀▀░░░░░
░▀█▌░░░▄░▀█▀░▀░░░░░
░░░░░░░░▄▄▐▌▄▄░░░░░
░░░░░░░░▀███▀█░▄░░░
░░░░░░░▐▌▀▄▀▄▀▐▄░░░
░░░░░░░▐▀░░░░░░▐▌░░
░░░░░░░█░░░░░░░░█░░
░░░░░░▐▌░░░░░░░░░█░

    1. Ударить с силой {}
    2. У тебя {} аптечек которые востанавливают по {}ед. здоровья
    3. Сбежать
        """).format(p.hp, p.max_hp, p.pw, BossHp, BossPower, p.pw + p.wearphone_damage, p.medcine, p.heal_hp)

        n = input("Номер:")
        os.system('cls||clear')

        if n == "1":
            r=randint(1,2)
            if r == 1:
                BossHp -= (p.pw + p.wearphone_damage)
                print("Ты наносишь удар")
            if r == 2:
                p.hp -= BossPower
                print("Твой враг наносит удар")
                if p.hp <= 0:
                    print("Ты умер")
                    time.sleep(2)
                    Game_Ower()

        if n == "2":
            if p.medcine > 0:
                p.medcine -= 1
                p.hp += p.heal_hp
                if p.hp > p.max_hp:
                    p.hp = p.max_hp

                    print("Лечение...{}".format(p.hp))
            else: print("Аптечки кончились!")

        if n == "3":
            r = randint(1,50)
            if r == 6:
                print("Ты сбежал")
                return True
            else:
                p.hp -= 1
                print("Ты не смог сбежать и потерял 1 ед здоровья")

    os.system('cls||clear')
    win_game(p)
    os.system('cls||clear')

#########################

#######################
#
# ЗАПУСК ИГРЫ
#
########################
os.system("mode con cols=65 lines=23")
os.system('cls||clear')
logo()
os.system('cls||clear')
Loading()
time.sleep(3)
start_game(p)
menu_simple(p)
Game_Ower()
