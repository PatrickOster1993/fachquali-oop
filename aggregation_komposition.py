# Kompositions- u. Aggregationsbeziehung in Quellcode erkennen u. unterscheiden:


## Aggregation
# class Auto:

#     def __init__(self, motor):
#         self.motor = motor

#     def fahren(self):
#         self.motor.starten()
#         print("Auto fährt jetzt los!")

# class Motor:

#     def __init__(self, leistung):
#         self.leistung = leistung
    
#     def starten(self):
#         print(f"Motor mit {self.leistung} PS wird gestartet!")

## Komposition
class Auto:

    def __init__(self):
        pass

    def fahren(self):
        motor = Motor(200)
        motor.starten()
        print("Auto fährt jetzt los!")

class Motor:

    def __init__(self, leistung):
        self.leistung = leistung
    
    def starten(self):
        print(f"Motor mit {self.leistung} PS wird gestartet!")

# Programmaublauf
## Aggregation
# mein_motor = Motor(200)
# mein_motor.starten()
# mein_auto = Auto(mein_motor)
# mein_auto.fahren()

## Komposition
mein_auto = Auto()
mein_auto.fahren()

# Merksatz 0: Stellen Sie sich den Zusammenhang zwischen "Teil" und "Ganzem" bitte NICHT
# als "Reale Welt Beziehung" vor! Die Software hat ihre ganz eigenen Gesetzmäßigkeiten!
# Sie können aber den lebensweltlichen Gedanken IM NACHGANG mit der technischen Realisierung
# vergleichen --> das schult die konkreten Unterschiede und das Wissen um die softwareseitige
# Realisierung!

# Merksatz 1: Wird das "Teil" (hier Motor) in irgendeiner Weise extern dem "Ganzen" (hier Autor) übergeben,
# so MUSS davon ausgegangen werden, dass bereits eine Instanz des "Teils" unabhängig vom "Ganzen" erzeugt wurde.
# Hier läge dann immer eine Aggregationsbeziehung vor - ansonsten eine Kompositionsbeziehung!

# Merksatz 2: Eine Aggregation liegt immer dann vor, wenn die Existenz eines "Teils" in ALLEN Fällen
# unabhängig von der Existenz des "Ganzen" ist!