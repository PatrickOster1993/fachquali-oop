
# Einführung in die Objektorientierte Programmierung (OOP) – Tag 1

## Was ist Objektorientierte Programmierung? (Wozu OOP?)

Objektorientierte Programmierung (OOP) ist ein Paradigma der Softwareentwicklung, bei dem das Programm in "Objekte" unterteilt wird. Diese Objekte können Daten (Attribute) und Funktionen (Methoden) enthalten. Der große Vorteil von OOP ist, dass es hilft, Code zu organisieren, wiederzuverwenden und leichter zu warten. Mit OOP können wir Modelle aus der realen Welt nachbilden und komplexe Programme effizienter strukturieren.

### Vorteile der OOP:
- **Modularität**: Der Code wird in kleinere, unabhängige Teile (Objekte) aufgeteilt, die einzeln entwickelt, getestet und gewartet werden können.
- **Wiederverwendbarkeit**: Einmal erstellte Objekte können in verschiedenen Programmen oder Teilen des Programms wiederverwendet werden.
- **Erweiterbarkeit**: Wenn wir neue Funktionen hinzufügen möchten, können wir Objekte leicht erweitern, ohne den gesamten Code umzuschreiben.
- **Verständlichkeit**: OOP ermöglicht es, komplexe Programme auf eine natürliche Weise zu strukturieren, was die Lesbarkeit und Wartung des Codes erleichtert.

## Die Grundlagen der OOP

Die zentralen Konzepte der OOP sind:
- **Objekte**: Instanzen von Klassen, die sowohl Daten als auch Methoden enthalten.
- **Klassen**: Baupläne oder Vorlagen für Objekte, die die Attribute (Daten) und Methoden (Funktionen) definieren.
- **Attribute**: Variablen innerhalb einer Klasse, die die Eigenschaften eines Objekts beschreiben.
- **Methoden**: Funktionen innerhalb einer Klasse, die das Verhalten der Objekte definieren.
- **Konstruktor**: Eine spezielle Methode (meist `__init__` in Python), die beim Erstellen eines Objekts aufgerufen wird und die Attribute initialisiert.

### Beispiel: Krieger-Klasse in einem Spiel

Stellen wir uns vor, wir bauen ein Spiel, in dem Krieger gegeneinander kämpfen. Ein Krieger hat Attribute wie „Lebenspunkte“, „Angriffskraft“ und „Rüstung“ sowie Methoden wie „angreifen()“ und „verteidigen()“. Die Klasse „Krieger“ ist die Vorlage für jeden Krieger im Spiel.

### Einfache Struktur einer Klasse

```plaintext
+--------------------------+
|        Krieger            |
+--------------------------+
| - name: String            |
| - lebenspunkte: int       |
| - angriffskraft: int      |
| - ruestung: int           |
+--------------------------+
| + __init__(...): void     |
| + angreifen(): void       |
| + verteidigen(): void     |
+--------------------------+