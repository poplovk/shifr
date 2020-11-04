import os
import time

# print(type(choose))

truecode = ["390erjsm9-0d()dm", "123125", "123123"]
message = ["Сообщение", "Сообщение1", "Сообщение2"]
while True:
    print("---------------------------Выберите опцию------------------------------------")
    print()
    print("[---           1. Ввести код")
    print("[---           2. Загрузить данные")
    print("[---           3. Что это такое?")
    print("[---           4. Выйти")
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
                print("┬─┬")
                time.sleep(1)
                print("─┬")
                time.sleep(1)
                print("┬")
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
        print("Q: Что-это?")
        print("A: Своеобразная программа для хранения файлов. Анонимная.")
        print()
        print("Q: Как это работает?")
        print("A: Вы можетете загружать любые данные (кроме файлов напрямую) и присваивать им код, ")
        print("зная который любой может получить к ним доступ")
    if choose == 4:
        print("Завершили работу >_<")
        break
