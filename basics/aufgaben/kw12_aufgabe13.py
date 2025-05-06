# Schreiben Sie ein Tic-Tac-Toe-Spiel für zwei Spieler.
# 1. Verwenden Sie eine 3×3-Liste, die zu Beginn mit leeren Zeichen gefüllt ist.
# 2. Die Spieler geben abwechselnd die Zeilen- und Spaltennummer ein, um ein 'X' oder 'O' zu
# setzen.
# 3. Nach jedem Zug soll das Spielfeld aktualisiert und ausgegeben werden.
# 4. Überprüfen Sie nach jedem Zug, ob ein Spieler gewonnen hat oder das Spielfeld voll ist.

# 1. Leeres Spielfeld initialisieren:

spielfeld = []

def init_spielfeld():
    for _ in range(3):
        zeilen = []
        for _ in range(3):
            zeilen.append('.')
        spielfeld.append(zeilen)
    print(spielfeld)

print("###### Spielfeld initialisieren ######")
init_spielfeld()
print("######################################")

# Algorithmus:

def update_spielfeld(x_or_o, zeilenindex, spaltenindex):
    spielfeld[zeilenindex][spaltenindex] = x_or_o
    for zeilen_index in range(3):
        for spalten_index in range(3):
            print(spielfeld[zeilen_index][spalten_index], end = ' ')
        print()

def check_zeilen_sieg(x_or_o):
    for zeile in spielfeld:
        if zeile[0] == x_or_o and zeile[1] == x_or_o and zeile[2] == x_or_o:
            return True
    return False

def check_spalten_sieg(x_or_o):
    if (spielfeld[0][0] == x_or_o and spielfeld[1][0] == x_or_o and spielfeld[2][0] == x_or_o) or (spielfeld[0][1] == x_or_o and spielfeld[1][1] == x_or_o and spielfeld[2][1] == x_or_o) or (spielfeld[0][2] == x_or_o and spielfeld[1][2] == x_or_o and spielfeld[2][2] == x_or_o):
        return True
    return False

def check_diagonal_sieg(x_or_o):
    if (spielfeld[0][0] == x_or_o and spielfeld[1][1] == x_or_o and spielfeld[2][2] == x_or_o) or (spielfeld[0][2] == x_or_o and spielfeld[1][1] == x_or_o and spielfeld[2][0] == x_or_o):
        return True
    return False

def check_spielfeld_voll():
    counter = 0
    for zeile in spielfeld:
        for spalte in zeile:
            if spalte != '.':
                counter += 1
    if counter == 9:
        return True
    return False

def is_feld_belegt(zeilenindex, spaltenindex):
    if spielfeld[zeilenindex][spaltenindex] != '.':
        return True
    return False

# Könnte man noch zusätzlich machen...
# def eingabe_gueltig(index):
#     if index < 3 and index >= 0:
#         return True

while True:
    try:
        print("Spieler 1 (X) ist am Zug!")
        print("*************************")

        x_zeilenindex = int(input("Bitte Zeilenindex eingeben: "))
        x_spaltenindex = int(input("Bitte Spaltenindex eingeben: "))
    
        while is_feld_belegt(x_zeilenindex, x_spaltenindex):
            print("Feld bereits belegt!")
            x_zeilenindex = int(input("Bitte Zeilenindex eingeben: "))
            x_spaltenindex = int(input("Bitte Spaltenindex eingeben: "))
    
        update_spielfeld('X', x_zeilenindex, x_spaltenindex)

        if check_zeilen_sieg('X') or check_spalten_sieg('X') or check_diagonal_sieg('X'):
            print("Spieler 1 (X) gewonnen!")
            break

        print("Spieler 2 (0) ist am Zug!")
        print("*************************")
        o_zeilenindex = int(input("Bitte Zeilenindex eingeben: "))
        o_spaltenindex = int(input("Bitte Spaltenindex eingeben: "))

        while is_feld_belegt(o_zeilenindex, o_spaltenindex):
            print("Feld bereits belegt!")
            o_zeilenindex = int(input("Bitte Zeilenindex eingeben: "))
            o_spaltenindex = int(input("Bitte Spaltenindex eingeben: "))
    
        update_spielfeld('O', o_zeilenindex, o_spaltenindex)

        if check_zeilen_sieg('O') or check_spalten_sieg('O') or check_diagonal_sieg('O'):
            print("Spieler 2 (O) gewonnen!")
            break

        if check_spielfeld_voll():
            print("Unentschieden!")
            break
    
    except:
        print("Irgendein Fehler aufgetreten!")
        continue

# ToDo: State zwischenspeichern, falls Fehler auftritt (Wer ist dran?) --> tipp: globale State-Variable!
# Refactoring: Sich wiederholender Code in entsprechende Funktionen auslagern
# Feel free: Anwendung ganz nach eigenem Belieben anpassen / erweitern (gern auch vereinfachte, python-spezifische Syntax)