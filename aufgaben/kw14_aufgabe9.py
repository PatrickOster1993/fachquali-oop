    # Erstellen Sie die Klasse Fach:
    # • Enthält die Attribute name (Fachname) und note (Note des Schülers in diesem Fach). 
    # •Implementieren Sie die Methode __str__(), die eine lesbare Darstellung eines Fachs
    # zurückgibt.

    # Erstellen Sie die Klasse Schüler:
    # • Enthält die Attribute name, klasse und eine Liste fächer.
    # • Definieren Sie die Klassenkonstante MAX_FAECHER = 10.
    # •Implementieren Sie eine Methode fach_hinzufuegen(fach), die ein Fach zur Liste
    # hinzufügt, falls die maximale Anzahl nicht überschritten wird.
    # • Implementieren Sie eine Methode durchschnittsnote(), die die Durchschnittsnote des
    # Schülers berechnet.
    # • Überschreiben Sie __str__(), um eine lesbare, tabellarische Darstellung des Schülers und
    # seiner Fächer zurückzugeben.

    # Erstellen Sie mehrere Schüler-Objekte:
    # • Fügen Sie verschiedene Fach-Objekte hinzu.
    # •Testen Sie die Methoden, indem Sie die Schüler-Objekte ausgeben und die
    # Durchschnittsnote berechnen.

    # Erweitern Sie das Modell um eine Operatorüberladung __eq__(): Zwei Schüler gelten als gleich (==), wenn sie denselben Namen und dieselbe Klasse haben.
    # Erstellen Sie ein Klassendiagramm, das die Beziehung zwischen Schüler und Fach verdeutlicht.
    # Optional: Erweitern Sie das System um eine Verwaltungsklasse Schule, die mehrere Schüler verwaltet. Die Klasse Schule soll eine Liste aller Schüler enthalten. Sie soll Methoden haben, um Schüler hinzuzufügen und zu entfernen. Implementieren Sie eine Methode bester_schüler(), die den Schüler mit der besten Durchschnittsnote zurückgibt. Überschreiben Sie die Methode __str__(), um eine übersichtliche Darstellung aller Schüler und ihrer Noten auszugeben und ergänzen Sie zuletzt das Klassendiagramm.

class Fach:
    
    def __init__(self, name, note):
        self.name = name
        self.note = note
    
    def __str__(self):  
        return f"Name: {self.name} | Note: {self.note}"
    
class Schueler:

    MAX_FAECHER = 10

    def __init__(self, name, klasse):
        self.name = name
        self.klasse = klasse
        self.faecher = []

    def fachHinzufuegen(self, fach):
        if len(self.faecher) < self.MAX_FAECHER:
            self.faecher.append(fach)
        else:
            print(f"Schüler belegt bereits {self.MAX_FAECHER} Fächer!")
    
    def durchschnittsnote(self):
        noten_summe = 0
        for fach in self.faecher:
            note = fach.note
            noten_summe += note
        return noten_summe / len(self.faecher)
    
    def __str__(self):
        ausgabe = "Schüler: " + self.name + " | Klasse: " + self.klasse + "\n"
        for fach in self.faecher:
            ausgabe += ("Fach: " + fach.name + " | Note: " + str(fach.note) + "\n")
        return ausgabe
    
    def __eq__(self, value):
        return (self.name == value.name and self.klasse == value.klasse)
    
class Schule:
    
    def __init__(self):
        self.schueler = []
    
    def schuelerHinzufuegen(self, schueler):
        self.schueler.append(schueler)

    def schuelerEntfernen(self, schueler):
        self.schueler.remove(schueler)

    def besterSchueler(self):
        # gibt Schüler mit bester Durchschnittsnote zurück
        bester_schueler = None
        for i in range(len(self.schueler) - 1):
            aktueller_schueler = self.schueler[i]
            naechster_schueler = self.schueler[i + 1]
            durchschnittsnote_aktueller_schueler = aktueller_schueler.durchschnittsnote()
            durchschnittsnote_naechster_schueler = naechster_schueler.durchschnittsnote()
            if durchschnittsnote_naechster_schueler < durchschnittsnote_aktueller_schueler:
                bester_schueler = naechster_schueler
            else:
                bester_schueler = aktueller_schueler
        return bester_schueler

    def __str__(self):
        ausgabe = "Schülerliste\n##################\n"
        for schueler in self.schueler:
            ausgabe += str(schueler)
            ausgabe += "-----------------\n"
        return ausgabe

# Programmablauf:
## Initialisierung
ich = Schueler("Patrick Oster", "aus der Schule")
du = Schueler("Max Mustermann", "7a")
er = Schueler("Ritter Herbert", "10c")

ich_fach1 = Fach("Mathe", 1)
ich_fach2 = Fach("Deutsch", 3)
ich_fach3 = Fach("Informatik", 5)

ich.fachHinzufuegen(ich_fach1)
ich.fachHinzufuegen(ich_fach2)
ich.fachHinzufuegen(ich_fach3)

du.fachHinzufuegen(Fach("OOP", 6))

er.fachHinzufuegen(Fach("Geschichte", 6))
er.fachHinzufuegen(Fach("Sport", 2))

## Test
# print(ich)
# print("Durchschnittsnote", ich.durchschnittsnote())

# print('########################')
# print(du)
# print(er)

# print(ich == du)

## Optionale Aufgabe testen
meine_schule = Schule()

meine_schule.schuelerHinzufuegen(ich)
meine_schule.schuelerHinzufuegen(du)
meine_schule.schuelerHinzufuegen(er)

print(meine_schule)

meine_schule.schuelerEntfernen(ich)

print(meine_schule)

print("Bester Schüler:")
print("***************")
print(meine_schule.besterSchueler())




