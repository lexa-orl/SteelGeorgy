# -*- coding: utf-8 -*-
import os #For clear cls
import sys
import time
from random import randint

class Player:  #описываем персонажа
    """docstring for Player;."""
    hp = 80       # Heal point
    max_hp = 80   #
    pw = 5        #Power
    level = 0     #уровень
    money = 5        # money
    xp = 0        # Очки опыта  experience
    max_xp = 10  #
    medcine = 5
    heal_hp = 10   #Сила аптечки
    wearphone = "Hends"  #оружие
    wearphone_damage = 0
p = Player()

#тут кароче обозначение констант
#инвентарь
def inventary(p):
    os.system('cls||clear')
    print("You have {} medcine".format(p.medcine))
    print("Your wearphone: {}".format(p.wearphone))
    print("1. Go back.")
    n = input("")
    if n == "1":
        os.system('cls||clear')
        menu_simple(p)


def menu_upgrade(p):
    while p.money > 0:
        print("Choose your upgrades! Money: {}$".format(p.money))
        print("-----")
        print("1. HP {}/{}  10$".format(p.hp, p.max_hp))
        print("2. Power {}  15$".format(p.pw))
        print("3. Go to main menu")
        n = input("Number:")
        if n =="1":
            p.hp +=5
            p.money -=10
            p.max_xp +=5
            os.system('cls||clear')
        if n == "2":
            p.pw +=2
            p.money -=15  #меню прокачки
            os.system('cls||clear')
        if n == "3":
            break
            os.system('cls||clear')
#магазин
def menu_market(p):
    while p.money > 0:
        print("You have {}$ ".format(p.money))
        print("Welcome to market")
        print("1. medcine  1$")
        print("2. Wooden stick (+3 heat) 5$")
        print("3. Cheep sword (+5 heat) 10$")
        print("4. Usual sword (+9 heat) 40$")
        print("5. Legendary sword(+15 heat) 90$")
        print("6. Go back")
        n = input("Number:")

        if n == "1":
            p.medcine +=1
            p.money -=1
            os.system('cls||clear')
        if n == "2":
            if p.money >= 5:
                p.money -=5
                p.wearphone = "Wooden stick"
                p.wearphone_damage =  3
            else: print("You haven't enough money")
            time.sleep(3)
            os.system('cls||clear')
        if n == "3":
            if p.money >= 10:
                p.money -=10
                p.wearphone = "Cheep sword"
                p.wearphone_damage =  5
            else: print("You haven't enough money")
            time.sleep(3)
            os.system('cls||clear')
        if n == "4":
            if p.money >= 40:
                p.money -=40
                p.wearphone = "Usual sword"
                p.wearphone_damage =  9
            else: print("You haven't enough money")
            time.sleep(3)
            os.system('cls||clear')
        if n == "5":
            if p.money >= 90:
                p.money -=90
                p.wearphone = "Legendary sword"
                p.wearphone_damage =  15
            else: print("You haven't enough money")
            time.sleep(3)
            os.system('cls||clear')
        if n == "6":
            break
            os.system('cls||clear')

def menu_stats(p):
    print("Player stats")
    print("-----")
    print("HP {}/{}".format(p.hp, p.max_hp))
    print("Power {}".format(p.pw))
    print("Healing {}".format(p.heal_hp))
    print("Level {}".format(p.level))
    print("experience {}".format(p.xp))
    print("skillpoint {}".format(p.sp))
    input("Enter to continue.")
    os.system('cls||clear')   #Cтатистика персонажа

def Game_Ower():
    os.system('cls||clear')
    print("Game Ower")
    time.sleep(3)
    sys.exit()   #Конец игры (с завершением работы)



#Стартовое меню (главное)
def menu_simple(p):
    while True:
        print("Choose what to do")
        print("1. Go Fight")
        print("2. Check your stats")
        print("3. To Upgrade")
        print("4. Market")
        print("5. Inventary")
        n = input("Number:")
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
            inventary(p)


def menu_fight(p):
    os.system('cls||clear')             #Бой с противником
    ehp = 2* randint(4,20)
    epw = 3* randint(1,5)
    while ehp>0:
        print("Enemy: {}  Power:{}".format(ehp, epw))
        print("You: {} of {}, Power: {}".format(p.hp, p.max_hp, p.pw))
        print("~~~~~~" )
        print("1. Punch with power {}".format(p.pw))
        print("2. Medcine {} Heal (+{}) ".format(p.medcine, p.heal_hp))
        print("3. Run away")
        n = input("Number:")
        os.system('cls||clear')
        if n == "1":

            r=randint(1,2)
            if r == 1:
                ehp -= p.pw
                print("you hit the enemy")
            if r == 2:
                p.hp -= epw
                print("enemy hit you")
                if p.hp <= 0:
                    print("ypu loose")
                    Game_Ower()

        if n == "2":
            if p.medcine > 0:
                p.hp += p.heal_hp
                if p.hp > p.max_hp:
                    p.hp = p.max_hp
                    p.medcine -= 1
                    print("Healing...{}".format(p.hp))
            else: print("You haven't medcine")

        if n == "3":

            r = randint(1,3)
            if r == 3:
                print("You ran away")
                return True
            else:
                print("you can't run")

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
    █▒═▒█  █▀▄ █░█ ▄▀▀ █░░     █░▄▀ █▀▀ ▀▄░▄▀     ▀█▀ ▄▀▄     ▄▀▀ ▀█▀ ▄▀▄ █▀▀▄ ▀█▀
    █▒═▒█  █░█ █░█ ░▀▄ █▀▄     █▀▄░ █▀▀ ░░█░░     ░█░ █░█     ░▀▄ ░█░ █▀█ █▐█▀ ░█░
    █▒═▒█  █▀░ ░▀░ ▀▀░ ▀░▀     ▀░▀▀ ▀▀▀ ░░▀░░     ░▀░ ░▀░     ▀▀░ ░▀░ ▀░▀ ▀░▀▀ ░▀░
    █▒═▒█
    █▒═▒█
    █▒═▒█
     █▒█
      █
""")
logo()
time.sleep(3)
print("Loading.")
time.sleep(0.5)
os.system('cls||clear')
print("Loading..")
time.sleep(0.5)
os.system('cls||clear')
print("Loading...")
time.sleep(0.5)
os.system('cls||clear')
print("Loading.")
time.sleep(0.5)
os.system('cls||clear')
print("Loading..")
time.sleep(0.5)
os.system('cls||clear')

menu_simple(p)
Game_Ower()
