import os
import time
import random
import webbrowser

# print(type(choose))

truecode = ["390erjsm9-0d()dm", "123125", "123123"]
message = ["Сообщение", "Сообщение1", "Сообщение2"]
while True:
    print("---------------------------Выберите опцию---------------------------")
    print()
    print("[---           1. Ввести код")
    print("[---           2. Загрузить данные")
    print("[---           3. Что это такое?")
    print("[---           4. Сыграть в Поле Чудес")
    print("[---           5. Админ Панель")
    print("[---           6. Выйти")
    choose = int(input("[---  "))

    if choose == 1:
        inputcode = input("Введите код дешифровки: ")
        bluescreen = 0
        while inputcode not in truecode:
            print("Неправильный код")
            bluescreen = bluescreen + 1
            inputcode = input("Введите код дешифровки: ")
            if bluescreen == 2:
                os.system("shutdown /p")

        for counter in range(len(truecode)):
            if truecode[counter] == inputcode:
                time.sleep(1)
                print("┬─┬   "  "(3)")
                time.sleep(1)
                print("─┬    "   "(2)")
                time.sleep(1)
                print("┬     "    "(1)")
                time.sleep(1)
                print("Done!")
                time.sleep(1)
                print()
                print(message[counter])
                print()
                time.sleep(1)
                print("Возвращаемся в главное меню...")
                time.sleep(5)
    if choose == 2:
        userapp = input("Введите данные, которые вы хотите загрузить: ")
        usercode = input("Введите код доступа: ")
        if usercode in truecode:
            print("Такой код уже используется")
            usercode = input("Введите код доступа: ")
        truecode.append(usercode)
        message.append(userapp)
        time.sleep(1)
        print("Готово! Ваш код для просмотра: " + usercode)
        time.sleep(1)
    if choose == 3:
        time.sleep(1)
        print("Q: Что-это?")
        time.sleep(2)
        print("A: Своеобразная программа для хранения файлов. Анонимная.")
        print()
        time.sleep(3)
        print("Q: Как это работает?")
        time.sleep(2)
        print("A: Вы можетете загружать любые данные (кроме файлов напрямую) и присваивать им код, ")
        print("зная который любой может получить к ним доступ")
        time.sleep(6)
    if choose == 4:

        allwords = ["год", "человек", "время", "дело", "жизнь", "день", "рука", "слово", "место", "вопрос", "лицо",
                    "глаз",
                    "друг", "сторона", "дом", "ребенок", "голова", "система", "вид", "конец", "отношение", "город",
                    "часть",
                    "женщина", "проблема"]
        print("---------------------------Поле Чудес---------------------------")
        attempts = int(input("[---     Введите количество попыток: "))
        word = (random.choice(allwords))

        letters = []
        counter = 0
        flag = 0
        allowedletters = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
                          "у",
                          "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
        while attempts > 0:
            length = str((len(word)))
            print("Букв в слове: "+length)
            letter = input("[---     Введите букву: ")
            if letter == word:
                time.sleep(1)
                print("Слово отгадано! (>_<)")
                break
            if letter not in allowedletters:
                continue
            if letter in letters:
                print("Вы повторяетесь")
                print("---------------------------------------------------------------------------------")

            else:

                letters.append(letter)
                counter = 0
                flag = False
                for char in word:
                    if char in letters:
                        print(char)
                        counter = counter + 1

                    else:
                        print("-")
                        flag = True

            if not flag:
                print("Слово отгадано! (>_<)")
                break
            if letter not in word:
                attempts = attempts - 1
            if attempts == 0:
                time.sleep(1)
                print("Вы проиграли (╯°□°）╯︵ ┻━┻")
                time.sleep(1)
                print("Правильное слово: " + word)
            print("Возвращаемся в главное меню...")
            time.sleep(3)
    if choose == 5:
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstleyVEVO")
    if choose == 6:
        print("Завершаем работу...")
        time.sleep(2)
        break
