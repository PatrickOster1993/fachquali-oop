from klasse import Krieger

# Beispiel: Erstellen von zwei Kriegern und ein Kampf
krieger1 = Krieger(name="Herbert", lebenspunkte=100, angriffskraft=20, ruestung=10)
krieger2 = Krieger(name="Maximilian", lebenspunkte=80, angriffskraft=25, ruestung=15)
krieger3 = Krieger(name="Patrick", lebenspunkte=50, angriffskraft=50, ruestung=5)

# Krieger 1 greift Krieger 2 an
krieger1.angreifen(gegner=krieger2)

# Krieger 2 verteidigt sich
krieger2.verteidigen()

krieger1.angreifen(gegner=krieger2)

# Status von Krieger 2 checken
krieger2.checkStatus()

# Beispiel für Setter-Methoden
krieger2.lebenspunkte = 90  # Lebenspunkte ändern
krieger2.angriffskraft = 30  # Angriffskraft ändern
krieger2.ruestung = 20      # Rüstung ändern