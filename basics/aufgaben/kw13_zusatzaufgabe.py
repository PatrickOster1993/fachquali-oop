#Ein Spieler steuert eine Schlange in einem 10×10-Spielfeld. Ziel ist es, Essen zu fressen ohne
#gegen die Wände oder sich selbst zu stoßen. Die Schlange wächst mit jeder Mahlzeit. Folgende Implementierungen sind vorzunehmen:

    #Erstellen Sie ein 10×10-Spielfeld mit '.' für leere Felder.
    #Die Schlange startet mit einer Länge von 2 Feldern und wird durch 'S' dargestellt. Platzieren Sie zufällig ein Essen auf dem Spielfeld.

#Der Spieler gibt Bewegungen ein:
    #- W (hoch), S (runter), A (links), D (rechts).
    #- Die Schlange bewegt sich in die gewählte Richtung.
    #- Falls sie das Essen erreicht, wächst sie.

#Regeln für das Spiel:
    #- Die Schlange kann sich nicht durch Wände bewegen (führt zum Game Over).
    #- Wenn die Schlange sich selbst berührt, verliert der Spieler.
    #- Nach dem Fressen erscheint das nächste Essen an einer zufälligen Position.
    #Nach jedem Zug wird das Spielfeld aktualisiert und ausgegeben. Das Spiel endet, wenn:
    #- Die Schlange gegen eine Wand oder sich selbst stößt (= verloren).

#- Optional: Der Spieler eine bestimmte Länge (z. B. 10 Felder) erreicht (= gewonnen).

import random

def print_spielfeld(spielfeld):
    for zeile in spielfeld:
        for spalte in zeile:
            print(spalte, end = "")
        print()

def init_spielfeld():
    spielfeld = []
    for _ in range(10):
        zeile = []
        for _ in range(10):
            zeile.append(" . ")
        spielfeld.append(zeile)
    return spielfeld

def setze_schlange(spielfeld, schlange):
    # neuer Code für beliebig viele Glieder der Schlange
    for koerperteil in schlange:
        koerperteil_zeile = koerperteil[0]
        koerperteil_spalte = koerperteil[1]
        spielfeld[koerperteil_zeile][koerperteil_spalte] = ' S '

    # Legacy-Code für 2 Glieder der Schlange (Kopf & Schwanz)
    #                    Kopf   Schwanz
    # meine_schlange = [[5, 4], [5, 5],]
    # kopf_zeile = schlange[0][0]
    # kopf_spalte = schlange[0][1]
    # schwanz_zeile = schlange[1][0]
    # schwanz_spalte = schlange[1][1]

    # spielfeld[kopf_zeile][kopf_spalte] = ' S '
    # spielfeld[schwanz_zeile][schwanz_spalte] = ' S '


def bewege_schlange(schlange, richtung):

    kopf = schlange[0]
    neuer_kopf = [kopf[0], kopf[1]]

    if richtung == 'w':
        neuer_kopf[0] -= 1

    elif richtung == 's':
        neuer_kopf[0] += 1

    elif richtung == 'a':
        neuer_kopf[1] -= 1

    elif richtung == 'd':
        neuer_kopf[1] += 1

    schlange.insert(0, neuer_kopf)
    return schlange

def setze_essen(spielfeld, schlange):
    while True:
        zeile = random.randint(0, 9)
        spalte = random.randint(0, 9)
        essen = [zeile, spalte]
        if essen not in schlange:
            spielfeld[zeile][spalte] = ' O '
            return essen

def game_over(schlange):
    # [[zeile0, spalte0], [zeile1, spalte1], ..., [zeile n, spalte n]]
    kopf = schlange[0]
    for n in range(len(schlange) - 1):
        n += 1
        glied = schlange[n]
        if glied == kopf:
            return True
    if kopf[0] < 0 or kopf[0] > 9 or kopf[1] < 0 or kopf[1] > 9:
        return True
    return False

def player_won(schlange):
    laenge_schlange = len(schlange)
    if laenge_schlange >= 10:
        return True
    return False

mein_spielfeld = init_spielfeld()
print_spielfeld(mein_spielfeld)

print("#############################")

meine_schlange = [[5, 4], [5, 5]]
setze_schlange(mein_spielfeld, meine_schlange)
mein_essen = setze_essen(mein_spielfeld, meine_schlange)
print_spielfeld(mein_spielfeld)

print("#############################")

while True:
    mein_spielfeld = init_spielfeld()
    mein_spielfeld[mein_essen[0]][mein_essen[1]] = ' O '
    # mein_essen = setze_essen(mein_spielfeld, meine_schlange)
    meine_richtung = input("Bitte Richtung eingeben (WASD): ")
    meine_neue_schlange = bewege_schlange(meine_schlange, meine_richtung)
    if player_won(meine_neue_schlange):
        print("Glückwunsch, du hast gewonnen!")
        break
    if game_over(meine_neue_schlange):
        print("Du hast veroren!")
        break
    if meine_neue_schlange[0] == mein_essen:
        mein_essen = setze_essen(mein_spielfeld, meine_neue_schlange)
    else:
        meine_neue_schlange.pop()
    setze_schlange(mein_spielfeld, meine_neue_schlange)
    print_spielfeld(mein_spielfeld)
    meine_schlange = meine_neue_schlange







