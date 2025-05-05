# Teil 4: Komposition und Aggregation
class Gilde:
    def __init__(self, name):
        self.name = name
        self.mitglieder = []
        self.anfuehrer = None

    def hinzufuegen(self, charakter):
        self.mitglieder.append(charakter)
        print(f"{charakter.name} wurde der Gilde {self.name} hinzugefügt.")

    def anzeigen(self):
        print(f"Mitglieder der Gilde {self.name}:")
        for mitglied in self.mitglieder:
            print(f"- {mitglied.name}")

    def anfuehrerBestimmen(self, charakter):
        if charakter in self.mitglieder:
            self.anfuehrer = charakter
            print(f"{charakter.name} wurde zum Anführer der Gilde {self.name} ernannt.")