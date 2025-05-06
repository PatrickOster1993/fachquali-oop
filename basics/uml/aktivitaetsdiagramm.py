import random

def zahlen_raten_iterativ(zahl):
    versuch = 0

    while versuch < 3:
        eingabe = int(input("Bitte Zahl eingeben (1 - 10): "))

        if eingabe < zahl:
            print("Zahl zu niedrig!")
        elif eingabe > zahl:
            print("Zahl zu groß!")
        else:
            print("Glückwunsch, Zahl erraten!!!")
            return
        
        versuch += 1

def zahlen_raten_rekursiv(zahl, versuch=0):
    if versuch >= 3:
        return
    eingabe = int(input("Bitte Zahl eingeben (1 - 10): "))
    if eingabe < zahl:
        print("Zahl zu niedrig!")
        zahlen_raten_rekursiv(zahl, versuch + 1)
    elif eingabe > zahl:
        print("Zahl zu groß!")
        zahlen_raten_rekursiv(zahl, versuch + 1)
    else:
        print("Glückwunsch, Zahl erraten!!!")
        return

def print_something(wert):
    print(wert)

def main():
    zahl = random.randint(1, 10)
    print("ITERATIV:")
    zahlen_raten_iterativ(zahl)
    print("REKURSIV:")
    zahlen_raten_rekursiv(zahl)

main()
