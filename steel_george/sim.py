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
#    dep = 0
    xp = int(0)       # Очки опыта  experience
    max_xp = int(10)  #
    medcine = int(7)
    heal_hp = int(5)   #Сила аптечки
    wearphone = "Hends"  #оружие
    wearphone_damage = int(0)
p = Player()

###################################
#ДОПОЛНИТЛЬНЫЕ ЭФФЕКТЫ
def Loading():
    os.system('cls||clear')
    print("Loading")
    time.sleep(0.3)
    os.system('cls||clear')
    print("Loading.")
    time.sleep(0.3)
    os.system('cls||clear')
    print("Loading..")
    time.sleep(0.3)
    os.system('cls||clear')
    print("Loading...")
    time.sleep(0.3)
    os.system('cls||clear')
    print("Loading")
    time.sleep(0.3)
    os.system('cls||clear')
    print("Loading.")
    time.sleep(0.3)
    os.system('cls||clear')
    print("Loading..")
    time.sleep(0.5)
    os.system('cls||clear')
    print("Loading...")
    time.sleep(0.3)
    os.system('cls||clear')
    print("Loading")
    time.sleep(0.5)
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
    █▒═▒█
    █▒═▒█
    █▒═▒█
    █▒═▒█
    █▒═▒█
    █▒═▒█
     █▒█
      █
""")
 #заставка
def Game_Ower():
    os.system('cls||clear')
    print("""

    КОНЕЦ ИГРЫ

    """)
    time.sleep(3)
    sys.exit()   #Конец игры (с завершением работы)

###################################

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
        print("""
1. Специальные задания
2. Работа
3. Назад
        """)
        wer = input("")
        if wer == "1":
            barplace(p)
            os.system('cls||clear')
        if wer == "2":
            job(p)
            os.system('cls||clear')
        if wer == "3":
            taverna(p)
            os.system('cls||clear')

    if k == "2":
        os.system('cls||clear')
        print("""
        Готов ли ты поиграть в очко?
        Правила просты, наберешь 20 или 21 очко и я утрою твой депозит
        """)
        blackjack(p)
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
    else:
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
7. Банк

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
            bank_menu(p)
        if n == "givememoney":
            p.money += 1000
            os.system('cls||clear')
            menu_simple(p)
        else:
            os.system('cls||clear')
            menu_simple(p)
    os.system('cls||clear')

def menu_fight(p):
    os.system('cls||clear')             #Бой с противником
    ehp = 2 * randint(4,20)
    epw = p.pw + randint(-5,5)
    while ehp>0:
        print("Здоровье врага: {}  Сила врага:{}".format(ehp, epw))
        print("Твое здоровье: {} из {}, Твоя сила: {}".format(p.hp, p.max_hp, p.pw))
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
    p.money += epw            #даём опыта
    if p.xp >= p.max_xp:
        p.xp = 0
        p.max_xp += 5
        p.level +=1
    os.system('cls||clear')

def job(p):
    print("Просто бери")
    p.money += 10
    taverna(p)

def bank_menu(p):
    os.system('cls||clear')
    time.sleep(1)
    print("""
    Добро пожаловать в банк
-------------------------------
Твой баланс {}$
Твой депозит {}$
Здесь ты можешь открыть депозит
Процентная ставка 2% в минуту с капитализацией каждые 25 минут

1. Вложить
2. Снять (все)
    """.format(p.money, p.deposit))
    b = input("Ввод: ")
    if b == "1":
        dep = int(input("Сколько вкладываем?"))
        if dep <= p.money:
            p.money -= dep
            p.deposit += dep
            while p.deposit > 0:
                z = 0
                for z in 7:
                    dep *= 1.02

                    time.sleep(3)
                    print("suck")
                p.deposit += dep
                dep = p.deposit
                print("some dick")
        else:
            print("нет столько денег")
            time.sleep(2)
    if b == "2":
        p.money += p.deposit
        p.deposit = 0
    os.system('cls||clear')
    menu_simple(p)



def blackjack(p):

    qaz = input("y/n\n")
    if qaz == "y":
        stavka = int(input("Ваша ставка  "))
        if p.money >= stavka:
            p.money -= stavka
            koloda = [6,7,8,9,10,1,2,3,4,11] * 4
            random.shuffle(koloda)
            count = 0
            while True:
                choice = input('Будете брать карту? y/n\n')
                if choice == 'y':
                    current = koloda.pop()
                    print('Вам попалась карта достоинством %d' %current)
                    count += current
                    if count > 21:
                        print('Извините, но вы проиграли')
                        print("Хотите повторить?  y/n  ")
                        t = input("")
                        if t == "y":
                            print("Вы уверены?")
                            blackjack(p)
                        else:
                            print('До новых встреч!')
                            break
                        break
                    elif 20 <= count <= 21:
                        p.money += (3*stavka)
                        print('Поздравляю, вы выиграли!')
                        time.sleep(2)
                        os.system('cls||clear')
                        print("Хотите повторить?   ")
                        t = input("")
                        if t == "y":
                            blackjack(p)
                        else:
                            print('До новых встреч!')
                            break
                        break
                    else:
                        print('У вас %d очков.' %count)
                elif choice == 'n':
                    print('У вас %d очков и вы закончили игру.' %count)
                    break

        else:
#            print("Ну как до встречи тогда")
            print('До новых встреч!')
        time.sleep(3)

#########################
#Квесты
def barplace(p):
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

def quest_3(p):
    os.system('cls||clear')
    time.sleep(1)
    print("""
Ну чтож, вижу ты готов к своему третьему заданию
    """)
    time.sleep(2)
    os.system('cls||clear')

def final_quest(p):
    os.system('cls||clear')
    time.sleep(1)
    print("""
Ну чтож, вижу ты готов к своему последнему заданию
    """)
    time.sleep(2)
    os.system('cls||clear')


    BossHp = 2* randint(4,20)
    BossPower = 3* randint(1,5)
    while BossHp > 0:
        print("""
Здоровье главного боса: {}  Сила:{}
Твое здоровье: {} из {}, Твоя сила: {}
~~~~~~
1. Ударить с силой {}
2. У тебя {} аптечек которые востанавливают по {}ед. здоровья
3. Сбежать
        """).format(BossHp, BossPower, p.hp, p.max_hp, p.pw, p.pw + p.wearphone_damage, p.medcine, p.heal_hp)

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
                    print("Ты помер")
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
    p.xp += epw
    p.money += epw            #даём опыта
    if p.xp >= p.max_xp:
        p.xp = 0
        p.max_xp += 5
        p.level +=1
    os.system('cls||clear')



#########################



#######################
#
# ЗАПУСК ИГРЫ
#
########################
os.system('cls||clear')
Loading()
os.system('cls||clear')
logo()
time.sleep(3)
menu_simple(p)
Game_Ower()
