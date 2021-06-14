# -*- coding: utf-8 -*-

import os
import sys
import random
import time
from random import randint
from effects import *
from minigames import *
#from places import *


import sqlite3
import getpass




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
    CheckLogin = ""
p = Player()


def start_game(p):
    logging(p)




    os.system('cls||clear')

    time.sleep(3)
######################

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
░▀▄▐▒▀▀▀▀▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒█      2. Деревянная_палка (+3 урона) 5$
░░░▀▌▒▄██▄▄▄▄████▄▒▒▒▒█▀       3. Дешевый_меч (+5 урона) 10$
░░░░▄██████████████▒▒▐▌        4. Обычный_меч (+9 урона) 40$
░░░▀███▀▀████▀█████▀▒▌         5. Легендарный_меч(+15 урона) 90$
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
                p.wearphone = "Деревянная_палка"
                p.wearphone_damage =  3
            else: print("Нехватает денег")
            time.sleep(1)
            os.system('cls||clear')
        if n == "3":
            if p.money >= 10:
                p.money -=10
                p.wearphone = "Дешевый_меч"
                p.wearphone_damage =  5
            else: print("Нехватает денег")
            time.sleep(1)
            os.system('cls||clear')
        if n == "4":
            if p.money >= 40:
                p.money -=40
                p.wearphone = "Обычный_меч"
                p.wearphone_damage =  9
            else: print("Нехватает денег")
            time.sleep(1)
            os.system('cls||clear')
        if n == "5":
            if p.money >= 90:
                p.money -=90
                p.wearphone = "Легендарный_меч"
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


#global db
#global sql


###################################

def logging(p):
    CreateDB(p)
    print("""
    1 Зарегестрироваться
    2 Войти
    """)
    des=int(input())
    if des == 1:
        InputUser(p)
    elif des == 2:
        LogIner(p)
    else:
        print("Incorrect choice")


def CreateDB(p):
    db = sqlite3.connect('users.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS SteelGeorge(
    login TEXT,
    password TEXT
    ) """)
# тут пихать поля
    db.commit()


def InputUser(p):
    os.system('cls||clear')
    db = sqlite3.connect('users.db')
    sql = db.cursor()
    ULogin = input('Придумайте логин: ')
    UPassword = getpass.getpass('Придумайте пароль: ')
    os.system('cls||clear')
    UPass = getpass.getpass('Подтвердите пароль: ')
    if UPass == UPassword:
        sql.execute(f"SELECT login FROM SteelGeorge  WHERE login = '{ULogin}'")
        if sql.fetchone() is None:
            #sql.execute(f"INSERT INTO SteelGeorge VALUES ('{user_id}'),{0},'{user_nickname}'")
            sql.execute(f"INSERT INTO SteelGeorge VALUES (?,?)", (ULogin, UPassword ))
            print('Зарагастрировано')
            db.commit()
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
        else:
            print("""Такой логин уже зарегестрирован, хочешь войти?

            1. Да
            2. Нет
            """)
            a = int(input())
            if a == 1:
                LogIner(p)
            else:
                exit()
    else:
        print("пароли не совпадают, попробуйте еще раз")
        time.sleep(3)
        InputUser(p)


def ShovTable(p):
    db = sqlite3.connect('users.db')
    sql = db.cursor()
    for value in sql.execute("SELECT * FROM SteelGeorge"):
        print(value[0],'   ',value[1])

def LogIner(p):
    os.system('cls||clear')
    db = sqlite3.connect('users.db')
    sql = db.cursor()
    p.CheckLogin = input('Введите логин: ')
    СheckPassword = getpass.getpass('Введите пароль: ')
    sql.execute(f"SELECT login FROM SteelGeorge  WHERE login = '{p.CheckLogin}'")
    if sql.fetchone() is None:
        print("""Такой логин не зарегестрирован, хотите создать?

        1. Да
        2. Нет
        """)
        a = int(input())
        if a == 1:
            InputUser(p)
        else:
            exit()
    else:
        sql.execute(f"SELECT password FROM SteelGeorge  WHERE password = '{СheckPassword}'")
        if sql.fetchone() is None:
            print('пароли не совпадают')
        else:
            print('пароли совпадают')


def saveload(p):
    os.system('cls||clear')
    deside=input("  save/load/back    ")
    if deside == "save":   #нормас сохраняет Spisok
        # Spisok это мписок параметров, через который реализуем сохранялку
        Spisok = [p.hp,p.max_xp,p.pw,p.level,p.q,p.money,p.xp,p.max_xp,p.medcine,p.wearphone,p.wearphone_damage,p.name]
        print("Список характеристик",Spisok)
        open('player_{}_save.txt'.format(p.CheckLogin), 'w').close() # сначала очищаем
        with open('player_{}_save.txt'.format(p.CheckLogin), 'w') as f:  # теперь пишем
            for Spisok in Spisok:
                f.write("%s\n" % Spisok)
        os.system('cls||clear')
        menu_simple(p)
    elif deside == "load":
        sp = [] #создаем список
        with open('player_{}_save.txt'.format(p.CheckLogin), 'r') as file:
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
