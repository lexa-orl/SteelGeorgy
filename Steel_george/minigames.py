import os
import sys
import random
import time
from random import randint
from effects import *
from main import *



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
