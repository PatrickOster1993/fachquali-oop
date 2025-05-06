# Schreiben Sie ein Tic-Tac-Toe-Spiel für zwei Spieler.
# 1. Verwenden Sie eine 3×3-Liste, die zu Beginn mit leeren Zeichen gefüllt ist.
# 2. Die Spieler geben abwechselnd die Zeilen- und Spaltennummer ein, um ein 'X' oder 'O' zu
# setzen.
# 3. Nach jedem Zug soll das Spielfeld aktualisiert und ausgegeben werden.
# 4. Überprüfen Sie nach jedem Zug, ob ein Spieler gewonnen hat oder das Spielfeld voll ist.

# 1. Leeres Spielfeld initialisieren:

spielfeld = []
FIELD_STRUCTURE = range(3)
player_one_turn = True

def init_spielfeld():
    for _ in FIELD_STRUCTURE:
        zeilen = []
        for _ in FIELD_STRUCTURE:
            zeilen.append('.')
        spielfeld.append(zeilen)
    print(spielfeld)

print("###### Spielfeld initialisieren ######")
init_spielfeld()
print("######################################")

# Algorithmus:

def update_spielfeld(x_or_o, zeilenindex, spaltenindex):
    spielfeld[zeilenindex][spaltenindex] = x_or_o
    for zeilen_index in FIELD_STRUCTURE:
        for spalten_index in FIELD_STRUCTURE:
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

def check_sieg(x_or_o):
    has_won = check_zeilen_sieg(x_or_o) or check_spalten_sieg(x_or_o) or check_diagonal_sieg(x_or_o)
    return has_won

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
        print("Feld bereits belegt!")
        return True
    return False

def get_player_input():
    zeilenindex = int(input("Bitte Zeilenindex eingeben: "))
    spaltenindex = int(input("Bitte Spaltenindex eingeben: "))
    return [zeilenindex, spaltenindex]

# Könnte man noch zusätzlich machen...
# def eingabe_gueltig(index):
#     if index < 3 and index >= 0:
#         return True

while True:
    try:
        if player_one_turn:
            print("Spieler 1 (X) ist am Zug!")
            print("*************************")

            player_input = get_player_input()
            x_zeilenindex, x_spaltenindex = player_input[0], player_input[1]

            while is_feld_belegt(x_zeilenindex, x_spaltenindex):
                player_input = get_player_input()
                x_zeilenindex, x_spaltenindex = player_input[0], player_input[1]
    
            update_spielfeld('X', x_zeilenindex, x_spaltenindex)

            if check_sieg('X'):
                print("Spieler 1 (X) gewonnen!")
                break
            
            player_one_turn = False
        
        else:
            print("Spieler 2 (0) ist am Zug!")
            print("*************************")

            player_input = get_player_input()
            o_zeilenindex, o_spaltenindex = player_input[0], player_input[1]

            while is_feld_belegt(o_zeilenindex, o_spaltenindex):
                player_input = get_player_input()
                o_zeilenindex, o_spaltenindex = player_input[0], player_input[1]
    
            update_spielfeld('O', o_zeilenindex, o_spaltenindex)

            if check_sieg('O'):
                print("Spieler 2 (O) gewonnen!")
                break

            player_one_turn = True

        if check_spielfeld_voll():
            print("Unentschieden!")
            break
    
    except:
        print("Irgendein Fehler aufgetreten!")
        continue

# ToDo: State zwischenspeichern, falls Fehler auftritt (Wer ist dran?) --> tipp: globale State-Variable!
# Refactoring: Sich wiederholender Code in entsprechende Funktionen auslagern
# Feel free: Anwendung ganz nach eigenem Belieben anpassen / erweitern (gern auch vereinfachte, python-spezifische Syntax)