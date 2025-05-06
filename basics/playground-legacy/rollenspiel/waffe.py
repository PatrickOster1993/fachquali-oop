# Teil 4: Komposition und Aggregation
class Waffe:
    def __init__(self, name, schaden, haltbarkeit):
        self.name = name
        self.schaden = schaden
        self.haltbarkeit = haltbarkeit

    def __add__(self, andereWaffe):
        neuerSchaden = self.schaden + andereWaffe.schaden
        neueHaltbarkeit = self.haltbarkeit + andereWaffe.haltbarkeit
        return Waffe(None, neuerSchaden, neueHaltbarkeit)