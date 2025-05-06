# Rollenspiel-System

Du sollst ein einfaches Rollenspiel-System erstellen. Dabei werden die Prinzipien der OOP (Vererbung, Kapselung, Polymorphismus, Komposition/Aggregation und Operatorüberladung) angewendet. Gehe die folgenden Schritte nacheinander durch.

## Teil 1: Neue Klassen hinzufügen (Vererbung und Abstraktion)
- **Erstelle eine abstrakte Basisklasse `Charakter`:**
  - Diese Klasse enthält die grundlegenden Attribute (z. B. `name`, `lebenspunkte`, `angriffskraft`, `ruestung`).
  - Definiere die Methode `angreifen`, aber lasse sie abstrakt (`@abstractmethod`).
  - Implementiere eine Methode `checkStatus`, die den Status eines Charakters ausgibt.

- **Erstelle abgeleitete Klassen `Magier` und `Schurke`:**
  - **Magier:**
    - Hat zusätzlich das Attribut `mana`.
    - Überschreibt die Methode `angreifen`, um mit Magie anzugreifen (Mana wird verbraucht).
    - Hat eine Methode `zaubern`, die mehr Schaden verursacht, aber mehr Mana kostet.
  - **Schurke:**
    - Hat zusätzlich das Attribut `geschicklichkeit`.
    - Überschreibt die Methode `angreifen`, um eine Chance auf einen kritischen Treffer zu haben (doppelter Schaden bei Glück).
    - Hat eine Methode `verstecken`, die die Wahrscheinlichkeit erhöht, Angriffen auszuweichen.

## Teil 2: Kapselung anwenden
- Überlege, welche Attribute und Methoden der Klassen nur intern verwendet werden sollen.
- Mache die Attribute `lebenspunkte`, `angriffskraft`, `ruestung`, `mana` und `geschicklichkeit` privat oder geschützt.
- Erstelle für diese Attribute **Getter** und **Setter**, die sicherstellen, dass die Werte nur sinnvoll verändert werden können (z. B. keine negativen Lebenspunkte). Überlege dir dabei, welche Attribute einer gewisse Logik beinhalten (=Props). Andere können gerne als einfache Attribute implementiert werden.

## Teil 3: Polymorphismus und Method Override
- Implementiere eine Funktion `kampf_szenario(charakter_1, charakter_2)`, die zwei Charaktere als Argumente akzeptiert - Funktion soll sich außerhalb der Klasse befinden.
- Die Funktion lässt die beiden Charaktere abwechselnd angreifen, bis einer besiegt ist (`Lebenspunkte <= 0`).
- Nutze dabei **Method Override**, um sicherzustellen, dass die Methode `angreifen` korrekt für jeden Charaktertyp aufgerufen wird. Dabei wird die Methode `angreifen` in den abgeleiteten Klassen (z. B. `Magier` und `Schurke`) überschrieben, sodass die Implementierung des jeweiligen Charakters verwendet wird, ohne den genauen Typ des Charakters prüfen zu müssen.

## Teil 4: Komposition und Aggregation
- **Erstelle eine Klasse `Gilde`:**
  - Eine Gilde kann mehrere Charaktere (z. B. Krieger, Magier, Schurken) enthalten.
  - Die Klasse soll Methoden enthalten wie:
    - `hinzufuegen(charakter)`: Fügt einen Charakter zur Gilde hinzu.
    - `anzeigen()`: Zeigt die Namen aller Charaktere in der Gilde an.
    - `anfuehrerBestimmen(charakter)`: Wählt einen Charakter als Anführer der Gilde aus.
- **Erstelle eine Klasse `Waffe`:**
  - Eine Waffe hat Attribute wie `name`, `schaden`, und `haltbarkeit`.
  - Charaktere sollen eine Waffe besitzen und diese im Kampf nutzen können.
  - Wenn die Haltbarkeit der Waffe aufgebraucht ist, kann sie nicht mehr verwendet werden.

## Teil 5: Überladung von Operatoren
- Implementiere die Überladung des `+`-Operators für die Klasse `Waffe`:
  - Der `+`-Operator soll es ermöglichen, zwei Waffen zu kombinieren (z. B. ihre Haltbarkeit und Schaden zu addieren, um eine stärkere Waffe zu erzeugen).
- Implementiere die Überladung des `==`-Operators für die Klasse `Charakter`:
  - Zwei Charaktere gelten als gleich, wenn ihre Attribute (`name`, `angriffskraft`, `ruestung`) identisch sind.

## Bonus:
Erweitere die Anwendung ganz nach deinem Belieben. Du kannst gerne weitere Klassen erstellen (z. B. `Priester`). Hier bist du in der Implementierung völlig frei - deiner Kreativität sind dabei keinerlei Grenzen gesetzt!