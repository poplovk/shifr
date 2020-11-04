import os
import time


truecode = ["390erjsm9-0d()dm", "123125", "123123"]
message = ["Сообщение", "Сообщение1", "Сообщение2"]
while True:
    print("---------------------------Выберите опцию------------------------------------")
    print()
    print("[---           1. Ввести код")
    print("[---           2. Выйти")
    print("3")
    choose = int(input("[--- "))
    if choose == 2:
        break  # print(type(choose))

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
                print(message[counter])
                time.sleep(5)
    break

