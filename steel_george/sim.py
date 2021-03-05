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
    sp = 0        # skill point
    xp = 0        # Очки опыта  experience
    max_xp = 10  #
    heal_hp = 10   #Сила аптечки
p = Player()

#тут кароче обозначение констант

def menu_upgrade(p):
    if p.sp > 0:
        print("Choose your upgrades! Skill points: {}".format(p.sp))
        print("-----")
        print("1. HP {}/{}".format(p.hp, p.max_hp))
        print("2. Power {}".format(p.pw))
        n = input("Number:")
        if n =="1":
            p.hp +=5
            p.sp -=1
            p.max_xp +=5
        if n == "2":
            p.pw +=1
            p.sp -=1  #меню прокачки
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


def menu_fight(p):
    os.system('cls||clear')             #Бой с противником
    ehp = 2* randint(4,20)
    epw = 3* randint(1,5)
    while ehp>0:
        print("Enemy: {}  Power:{}".format(ehp, epw))
        print("You: {} of {}, Power: {}".format(p.hp,p.max_hp, p.pw))
        print("~~~~~~" )
        print("1. Punch with power {}".format(p.pw))
        print("2. Heal (+{})".format(p.heal_hp))
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

            p.hp += p.heal_hp
            if p.hp > p.max_hp:
                p.hp = p.max_hp
            print("Healing...{}".format(p.hp))
        if n == "3":

            r = randint(1,3)
            if r == 3:
                print("You ran away")
                return True
            else:
                print("you can't run")

    os.system('cls||clear')
    p.xp += epw
    p.sp += epw            #даём опыта
    if p.xp >= p.max_xp:
        p.xp = 0
        p.max_xp += 5
        p.level +=1
    os.system('cls||clear')
    menu_upgrade(p)

#######################
#
# ЗАПУСК ИГРЫ
#
########################

os.system('cls||clear')
menu_simple(p)
Game_Ower()
