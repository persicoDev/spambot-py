# little spam bot in python
import time
import pyautogui
choice = 0
list = []
while(choice != 1 and choice != 2):
    choice = int(input("\nvuoi inserire da input il messaggio o da file?\n\t1)da file\t2)da input\n"))
    if(choice == 1):
        list = open("spam.txt","r")
    elif(choice == 2):
        n = int(input("quanti messaggi vuoi inserire? "))
        for i in range(0, n):
            msg = str(input("messaggio " + str(i + 1) +":"))
            list.append(msg)
    else:
        print("inserisci un valore corretto")
time.sleep(5)
for char in list:
    pyautogui.typewrite(char + "\n")

