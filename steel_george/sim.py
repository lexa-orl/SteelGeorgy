# -*- coding: utf-8 -*-
import os
import sys
import time
from random import randint


class Player:  #описываем персонажа
    """docstring for Player;."""
    hp = 50       # Heal point
    max_hp = 50   #
    pw = 5        #Power
    level = 0     #уровень
    money = 5        # money
    xp = 0       # Очки опыта  experience
    max_xp = 10  #
    medcine = 5
    heal_hp = 8   #Сила аптечки
    wearphone = "Hends"  #оружие
    wearphone_damage = 0
p = Player()

#Настройки

#Таверно
def taverna(p):
    os.system('cls||clear')
    print("""
    Ты вошел в таверну.
1. Подойти к барной стойке.
2. Пойти поиграть в очко.
3. Уйти
    """)
    k = input("")
    if k == "1":
        os.system('cls||clear')
    if k == "2":
        os.system('cls||clear')
        import BlackJack
    if k == "3":
        os.system('cls||clear')
        menu_simple(p)
    os.system('cls||clear')




#инвентарь
def inventary(p):
    os.system('cls||clear')
    print("--Инвентарь--")
    print("У тебя {} Аптечек".format(p.medcine))
    print("Тво оружие: {}".format(p.wearphone))
    print("1. Назад.")
    n = input("")
    if n == "1":
        os.system('cls||clear')
        menu_simple(p)


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
                p.hp +=5
                p.money -=20
                p.max_xp +=5
            else: print("Нехватает денег")
            time.sleep(3)
            os.system('cls||clear')
        if n == "2":
            if p.money >= 35:
                p.pw +=2
                p.money -=35  #меню прокачки
            else: print("Нехватает денег")
            time.sleep(3)
            os.system('cls||clear')
        if n == "3":
            break
        os.system('cls||clear')
#магазин
def menu_market(p):
    while p.money > 0:
        print("У тебя {}$ ".format(p.money))
        print("""
            Добро пожаловать в магазин!
    1. Аптечка  1$
    2. Деревянная палка (+3 heat) 5$
    3. Дешевый меч (+5 heat) 10$
    4. Обычный меч (+9 heat) 40$
    5. Легендарный меч(+15 heat) 90$
    6. Вернуться
""")
        n = input("Номер:")

        if n == "1":
            p.medcine +=1
            p.money -=1
            os.system('cls||clear')
        if n == "2":
            if p.money >= 5:
                p.money -=5
                p.wearphone = "Wooden stick"
                p.wearphone_damage =  3
            else: print("Нехватает денег")
            time.sleep(3)
            os.system('cls||clear')
        if n == "3":
            if p.money >= 10:
                p.money -=10
                p.wearphone = "Cheep sword"
                p.wearphone_damage =  5
            else: print("Нехватает денег")
            time.sleep(3)
            os.system('cls||clear')
        if n == "4":
            if p.money >= 40:
                p.money -=40
                p.wearphone = "Usual sword"
                p.wearphone_damage =  9
            else: print("Нехватает денег")
            time.sleep(3)
            os.system('cls||clear')
        if n == "5":
            if p.money >= 90:
                p.money -=90
                p.wearphone = "Legendary sword"
                p.wearphone_damage =  15
            else: print("Нехватает денег")
            time.sleep(3)
            os.system('cls||clear')
        if n == "6":
            break
        os.system('cls||clear')

def menu_stats(p):
    print("  Статус игрока")
    print("----------------------")
    print("Здоровье {}/{}".format(p.hp, p.max_hp))
    print("Сила {}".format(p.pw))
    print("Лечение {}".format(p.heal_hp))
    print("Уровень {}".format(p.level))
    print("Опыт {}".format(p.xp))
    print("Баланс {}$".format(p.money))
    input("Enter чтобы продолжить.")
    os.system('cls||clear')   #Cтатистика персонажа

def Game_Ower():
    os.system('cls||clear')
    print("Конец игры")
    time.sleep(3)
    sys.exit()   #Конец игры (с завершением работы)



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
7. Настройки
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
            Settings(p)
    os.system('cls||clear')

def menu_fight(p):
    os.system('cls||clear')             #Бой с противником
    ehp = 2* randint(4,20)
    epw = 3* randint(1,5)
    while ehp>0:
        print("Здоровье врага: {}  Сила врага:{}".format(ehp, epw))
        print("Твое здоровье: {} c {}, Твоя сила: {}".format(p.hp, p.max_hp, p.pw))
        print("~~~~~~" )
        print("1. Ударить с силой {}".format(p.pw + p.wearphone_damage))
        print("2. У тебя {} аптечек которые востанавливают по {}ед. здоровья ".format(p.medcine, p.heal_hp))
        print("3. Сбежать")
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
                    print("Ты помер")
                    Game_Ower()

        if n == "2":
            if p.medcine > 0:
                p.hp += p.heal_hp
                if p.hp > p.max_hp:
                    p.hp = p.max_hp
                    p.medcine -= 1
                    print("Лечение...{}".format(p.hp))
            else: print("Аптечки кончились!")

        if n == "3":
            r = randint(1,3)
            if r == 3:
                print("Ты сбежал")
                return True
            else:
                print("Ты не смог сбежать")

    os.system('cls||clear')
    p.xp += epw
    p.money += epw            #даём опыта
    if p.xp >= p.max_xp:
        p.xp = 0
        p.max_xp += 5
        p.level +=1
    os.system('cls||clear')


#######################
#
# ЗАПУСК ИГРЫ
#
########################

os.system('cls||clear')
import loading


def logo():
    print("""
    █████
    █═══█
     ███
     ███
████═███═████
   ███████       ▄▀▀ ▀█▀ █▀▀ █▀▀ █░░     ▄▀▀░ █▀▀ ▄▀▄ █▀▀▄ ▄▀▀░ █▀▀
    █▒═▒█░        ▀▄ ░█░ █▀▀ █▀▀ █░▄     █░▀▌ █▀▀ █░█ █▐█▀ █░▀▌ █▀▀
    █▒═▒█        ▀▀░ ░▀░ ▀▀▀ ▀▀▀ ▀▀▀     ▀▀▀░ ▀▀▀ ░▀░ ▀░▀▀ ▀▀▀░ ▀▀▀
    █▒═▒█
    █▒═▒█
    █▒═▒█
    █▒═▒█
    █▒═▒█
    █▒═▒█
    █▒═▒█
    █▒═▒█
    █▒═▒█
     █▒█
      █
""")
os.system('cls||clear')
logo()
time.sleep(3)
menu_simple(p)
Game_Ower()
