class Fach:
    def __init__(self, name, note):
        self.name = name
        self.note = note
    
    def __str__(self):
        return f"Fachname: {self.name}, Note des Schülers: {self.note}"

class Schueler:
    MAX_FAECHER = 10
    
    def __init__(self, name, klasse):
        self.name = name
        self.klasse = klasse
        self.faecher = []

    def fach_hinzufuegen(self, fach):
        if len(self.faecher) < self.MAX_FAECHER:
            self.faecher.append(fach)
    
    @property
    def durchschnittsnote(self):
        durchschnittsnote = sum(fach.note for fach in self.faecher) / len(self.faecher)
        return durchschnittsnote
    
    def __eq__(self, other):
        return (
            self.name == other.name and
            self.klasse == other.klasse
        )
    
    def __str__(self):
        header = f"Schüler: {self.name} | Klasse: {self.klasse}\n"
        header += "-" * 30 + "\n"
        header += f"{'Fach':<20} | {'Note':<5}\n"
        header += "-" * 30 + "\n"
        faecher_liste = "\n".join(f"{fach.name:<20} | {fach.note:<5}" for fach in self.faecher)
        footer = f"{'Durchschnittsnote':<20} | {self.durchschnittsnote}"
        return header + faecher_liste + "\n" + footer

mathe = Fach("Mathe", 6)
deutsch = Fach("Deutsch", 4)

schueler = Schueler("Benedikt Brenk", "8b")
schueler.fach_hinzufuegen(mathe)
schueler.fach_hinzufuegen(deutsch)

schueler2 = Schueler("Benedikt Bohne", "9b")
schueler2.fach_hinzufuegen(mathe)

print(schueler)
print(schueler2)
 


# ### **6. Optional: Erweitern Sie das System um eine Verwaltungsklasse `Schule`:**  
# - Die Klasse `Schule` soll eine Liste aller Schüler enthalten.  
# - Sie soll Methoden haben, um Schüler hinzuzufügen und zu entfernen.  
# - Implementieren Sie eine Methode `bester_schüler()`, die den Schüler mit der besten Durchschnittsnote zurückgibt.  
# - Überschreiben Sie die Methode `__str__()`, um eine übersichtliche Darstellung aller Schüler und ihrer Noten auszugeben.  
# - Ergänzen Sie zuletzt das Klassendiagramm.  