
  
# Prinzipien der Objektorientierten Programmierung (OOP)

## 1. Vererbung (Inheritance)

Vererbung ermöglicht einer Unterklasse, Eigenschaften und Methoden der Oberklasse zu erben und anzupassen.

**Beispiel:**
```plain
+-----------------------+
|         Tier          |
+-----------------------+
| + bewegen(): void     |
+-----------------------+
          ▲
          |
  +-------+-------+
  |               |
+-----------+   +------------+
|   Hund    |   |   Katze    |
+-----------+   +------------+
| + bellen():   | + miauen():|
|   void        |   void     |
+-----------+   +------------+
```
```python
class Tier:
	def bewegen(self):
		print("Das Tier bewegt sich.")

class Hund(Tier):
	def bellen(self):
		print("Der Hund bellt.")

class Katze(Tier):
	def miauen(self):
		print("Die Katze miaut.")
```

## 2. Abstraktion (Abstraktion)

**Definition:**

Abstraktion bedeutet, nur die wesentlichen Merkmale eines Objekts oder Prozesses offenzulegen und unwichtige Details zu verbergen. Sie konzentriert sich darauf, was ein Objekt macht, und nicht, wie es das macht.

Dies wird oft als "Information Hiding" bezeichnet, da die Implementierungsdetails versteckt werden.
  
**Ziel:**

Die Komplexität von Systemen reduzieren und eine klare Schnittstelle (Interface) bereitstellen, um Objekte oder Prozesse zu nutzen.

### Beispiel
```plain
+---------------------------+
|          Tier             |
+---------------------------+
| + essen(): void           |
| # bewegen(): abstract     |
+---------------------------+
          ▲
          |
  +-------+--------+
  |                |
+------------+   +-------------+
|   Hund     |   |   Vogel     |
+------------+   +-------------+
| + bewegen():   | + bewegen():|
|   void     |   |   void      |
+------------+   +-------------+
```
```python
from abc import ABC, abstractmethod

class Tier(ABC):
	@abstractmethod
	def bewegen(self):
		pass

	def essen(self):
		print("Das Tier isst.")  # Funktionalität für alle Tiere

class Hund(Tier):
	def bewegen(self):
		print("Der Hund läuft.")

class Vogel(Tier):
	def bewegen(self):
		print("Der Vogel fliegt.")
```

## 3. Kapselung (Encapsulation)

**Definition:**

Kapselung bedeutet, dass Daten (Attribute) und die darauf zugreifende Logik (Methoden) in einer Klasse zusammengefasst werden. Der Zugriff auf diese Daten wird kontrolliert, um sicherzustellen, dass nur erlaubte Änderungen vorgenommen werden.

**Ziel:**

Schutz der Daten und Erhöhung der Wartbarkeit.

**Umsetzung in Python:**

-  **Ohne Unterstrich:** Öffentliche Attribute und Methoden, die direkt zugänglich sind.

Beispiel: `self.name`

-  **Ein Unterstrich (`_`)**: Geschützte Attribute und Methoden, die als privat angesehen werden sollten, aber technisch nicht strikt geschützt sind. Sie signalisieren, dass diese Attribute oder Methoden nur innerhalb der Klasse oder ihrer Unterklassen verwendet werden sollten.

Beispiel: `self._geheimnis`

-  **Doppelunterstrich (`__`):** Namens-Mangling zur Vermeidung von Namenskonflikten in Unterklassen. Python modifiziert den Namen intern, um ihn einzigartig zu machen. Dies bietet einen höheren Schutz vor versehentlichem Zugriff.

Beispiel: `self.__streng_geheim`

### Beispiel:
```plain
+---------------------------+
|        BankKonto          |
+---------------------------+
| + blz: str                |
| # bankCode: str           |
| _ pin: str                |
+---------------------------+
| + __init__(blz, pin):     |
|   void                    |
| + checkPin(eingabe):      |
|   bool                    |
| + zeigeBankcode():        |
|   str                     |
+---------------------------+
```
```python
class BankKonto:
	def __init__(self, blz, pin):
		self.blz = blz # Öffentlich
		self._bankCode =  "XYZ123"  # Geschützt
		self.__pin = pin # Privat (Namens-Mangling)

	def checkPin(self, eingabe):
	"""Prüft, ob der eingegebene PIN korrekt ist."""
		return eingabe ==  self.__pin

	def zeigeBankcode(self):
	"""Gibt den Bankcode zurück (als Beispiel für geschützte Attribute)."""
		return self._bankCode

# Nutzung:
konto = BankKonto("MEINE_BANKLEITZAHL", "1234")
print(konto.blz)  				# Öffentlich: MEINE_BANKLEITZAHL
print(konto.zeigeBankcode())  	# Geschützt, kontrollierter Zugriff:XYZ123
print(konto.checkPin("1234"))  	# True (korrekter PIN)
print(konto.checkPin("0000"))  	# False (falscher PIN)

# Direkter Zugriff:
# print(konto.__pin) 			# Fehler: Zugriff nicht erlaubt
```

## 4. Polymorphismus

**Definition:**

Polymorphismus bedeutet, dass Objekte unterschiedlichster Klassen über die gleiche Schnittstelle angesprochen werden können.

**Ziel:**

Flexibilität erhöhen und allgemeine Algorithmen für verschiedene Typen nutzbar machen.

**Arten von Polymorphismus:**

-  **Methodenüberschreibung (Override):** Eine Unterklasse kann eine Methode der Oberklasse überschreiben.

-  **Methodenüberladung (Overload):** Mehrere Methoden mit demselben Namen, aber unterschiedlichen Parametern (in Python nur durch `*args` / `**kwargs` simulierbar).

### Beispiel:

#### a) Methodenüberschreibung mit Override
```plain
+-----------------------+
|         Tier          |
+-----------------------+
| + bewegen(): void     |
+-----------------------+
          ▲
          |
+-----------------------+
|        Katze          |
+-----------------------+
| + bewegen(): void     |
+-----------------------+
```
```python
class Tier:
	def bewegen(self):
		print("Das Tier bewegt sich.")
		
class Katze(Tier):
	def bewegen(self):
		print("Die Katze schleicht.")
```

#### b) Methodenüberladung (Overload in Python)

```python
class Rechner:
	def addiere(self, *args):
		return sum(args)

rechner = Rechner()
print(rechner.addiere(1, 2))  # 3
print(rechner.addiere(1, 2, 3, 4))  # 10
```

## Weitere namhafte Prinzipien (=SOLID)

### 1. Single Responsibility Principle (SRP)

Eine Klasse sollte nur eine Aufgabe haben. Das bedeutet, dass eine Klasse nur für eine einzige Funktionalität verantwortlich sein sollte. Änderungen an einer Klasse sollten nur durch Änderungen der Aufgabe oder Funktionalität der Klasse notwendig werden.

### 2. Open/Closed Principle (OCP)

Klassen sollen offen für Erweiterung, aber geschlossen für Änderungen sein. Das bedeutet, dass das Verhalten einer Klasse durch Erweiterungen (z.B. Vererbung) angepasst werden kann, ohne dass der bestehende Code der Klasse geändert werden muss.

### 3. Liskov Substitution Principle (LSP)

Objekte einer Basisklasse sollten durch Objekte ihrer abgeleiteten Klassen ersetzt werden können, ohne dass sich das Verhalten des Programms ändert. Das bedeutet, dass eine Unterklasse die Erwartungen erfüllen muss, die an die Basisklasse gestellt werden, und keine zusätzlichen Anforderungen hinzufügen darf.

### 4. Interface Segregation Principle (ISP)

Es ist besser, viele kleine, spezifische Schnittstellen zu haben, die genau die Anforderungen einzelner Module erfüllen, als eine große, allgemeine Schnittstelle, die für alle Module genutzt wird. Klassen sollten keine Methoden implementieren müssen, die sie nicht benötigen.

### 5. Dependency Inversion Principle (DIP)

Höherwertige Module sollten nicht von niederen Modulen abhängen, sondern beide von Abstraktionen. Dies fördert die Entkopplung von Modulen und sorgt dafür, dass Änderungen an niedrigerwertigen Modulen die höherwertigen Module nicht beeinträchtigen.

## Komposition vs. Aggregation

### 1. Komposition

**Definition:**

Eine starke Beziehung, bei der das enthaltene Objekt vom übergeordneten Objekt vollständig kontrolliert wird. Wenn das übergeordnete Objekt zerstört wird, werden auch die enthaltenen Objekte zerstört.

**Beispiel:**
```plain
+---------------------------+
|          Motor            |
+---------------------------+
| + starten(): void         |
+---------------------------+
          ▲
          |
    «uses»
          |
+---------------------------+
|          Auto             |
+---------------------------+
| # motor: Motor            |
+---------------------------+
| + __init__(): void        |
| + fahren(): void          |
+---------------------------+
```
```python
class Motor:
	def starten(self):
		print("Motor gestartet.")
		
class Auto:
	def __init__(self):
		self._motor = Motor()  # Motor wird vollständig kontrolliert
	
	def fahren(self):
		self._motor.starten()
		print("Auto fährt.")
```
  
### 2. Aggregation

**Definition:**

Eine schwächere Beziehung, bei der das enthaltene Objekt unabhängig existieren kann. Das übergeordnete Objekt referenziert die enthaltenen Objekte, kontrolliert sie aber nicht vollständig.

### Beispiel:
```plain
+---------------------------+
|         Student           |
+---------------------------+
| + name: str               |
+---------------------------+
| + __init__(name): void    |
+---------------------------+

              0..*
          «contains»
              ▲
              |
+---------------------------+
|      Klassenzimmer        |
+---------------------------+
| + schueler: list[Student] |
+---------------------------+
| + __init__(): void        |
| + hinzufuegen(student):   |
|   void                    |
+---------------------------+
```
```python
class Student:
    def __init__(self, name):
		self.name = name

class Klassenzimmer:
	def __init__(self):
		self.schueler = [] # Sammlung unabhängiger Schüler

	def hinzufuegen(self, student):
		self.schueler.append(student)
```

## Bonus: Überladung von Operatoren

Die Überladung von Operatoren in Python ermöglicht es, die Funktionalität von Standardoperatoren wie `+`, `-` oder `*` für benutzerdefinierte Klassen anzupassen. Dies geschieht durch spezielle Methoden wie `__add__`, `__sub__` oder `__mul__`. Ein einfaches Beispiel ist die Addition zweier Strings (`"Hallo" + " Welt"`), die intern die Methode `__add__` verwendet, um die Zeichenketten zu verketten. Auf ähnliche Weise kann man eigene Klassen definieren, bei denen der `+`-Operator eine spezifische Bedeutung erhält, etwa das Addieren von Bruchzahlen oder Punkten im Raum. Diese Flexibilität macht Python besonders leistungsstark und anpassungsfähig.

### Beispiel:

```python
class Vector:
	coordinates = (None, None)

	def __init__(self, x, y):
		self.coordinates[0] = x
		self.coordinates[1] = y

	def __add__(self, other):
		"""Überladen des + Operators."""
		if isinstance(other, Vector):
			x1 = self.coordinates[0]
			y2 = self.coordinates[1]
			x2 = other.coordinates[0]
			y2 = other.coordinates[1]
			return Vector(x1 + x2, y1 + y2)
		return  NotImplemented

# Nutzung:
v1 = Vector(1, 2)
v2 = Vector(3, 4)

v3 = v1 + v2 			# Dies ruft die __add__ Methode auf
print(v3)  				# (4, 6)
```
> **Tipp**: [Hier](https://refactoring.guru/design-patterns/catalog) finden Sie wertvolle, von echt smarten Dudes aus der Vergangenheit erstellte, für eine Vielzahl von bekannten Use-Cases anwendbare, Design-Pattern für Ihre SW-Architektur!