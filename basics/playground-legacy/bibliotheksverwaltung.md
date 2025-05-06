### **Aufgabe: Bibliotheksverwaltung**

Du sollst ein kleines Programm zur Verwaltung einer Bibliothek erstellen. Die Bibliothek enthält eine Sammlung von **Büchern**. Es gibt verschiedene Arten von Büchern, z. B. **Sachbücher** und **Romane**. Jedes Buch hat bestimmte Eigenschaften, aber es gibt auch Unterschiede zwischen den Bucharten.

#### **1. Erstellung einer Basisklasse:**

Erstelle eine Basisklasse `Buch`, die die gemeinsamen Attribute und Methoden für alle Bücher enthält.

**Gemeinsame Attribute:**
- `titel`: Der Titel des Buches.
- `autor`: Der Autor des Buches.
- `isbn`: Die ISBN des Buches.

**Gemeinsame Methoden:**
- `details`: Gibt eine kurze Beschreibung des Buches aus (Titel, Autor, ISBN).

#### **2. Vererbung:**

Erstelle zwei Unterklassen `Sachbuch` und `Roman`, die von der Klasse `Buch` erben.

- **Sachbuch**:
  - Zusätzlich zu den Attributen aus der Basisklasse soll es ein weiteres Attribut `thema` haben, das das Thema des Sachbuches angibt.
  - Eine Methode `wissenVermitteln`, die in der Konsole ausgibt, zu welchem Thema das Buch Wissen vermittelt (als Satz).

- **Roman**:
  - Zusätzlich zu den Attributen aus der Basisklasse soll es ein weiteres Attribut `genre` haben, das das Genre des Romans angibt (z. B. "Thriller", "Drama", ...).
  - Auch soll die Klasse eine Property `fsk` beinhalten,  welche sich (abhängig vom jeweiligen Genre auf 0, 6, 12 oder 18 setzt.

#### **3. Abstraktion:**

Erstelle eine abstrakte Methode in der Klasse `Buch`, die in den Unterklassen implementiert werden muss. Die Methode `lesen()` soll in jeder Unterklasse unterschiedlich implementiert werden:
- **Sachbuch**: Gibt "Ich lese, um zu lernen!" aus.
- **Roman**: Gibt "Ich lese, um in eine fesselnde Welt einzutauchen." aus.

#### **4. Kapselung:**

Entscheiden Sie selbst, welche Attribute, Properties und Methoden für Sie als `privat (__)`, `protected (_)` oder `public` gelten. 

#### **5. Aggregation:**

Erstelle eine Klasse `Bibliothek`, die mehrere Bücher speichern kann. Die `Bibliothek` enthält eine Liste von `Buch`-Objekten. Sie soll Methoden zum Hinzufügen und Entfernen von Büchern haben.

#### **6. Klassendiagramm:**

Erstellen Sie ein `Klassendiagramm`, welches die Klassen, ihre Beziehung zueinander sowie etwaige Attribute, Properties und Methoden enthält.
> Hinweis: Auch die Aspekte der Kapselung sollen daraus hervorgehen (+, #, -)!

#### **7. Bonus:**

Erstelle eine Klasse `Kunde`, die mehrere Bücher ausleihen kann. Die Klasse `Bibliothek`soll eine Liste aus Objekten der Klasse `Kunde`halten (= registrierte Kunden). Die Kunden selbst verfügen ebenso über ein Attribut `buecher`, welches die aktuell geliehenen Bücher enthält. Erstelle zuletzt noch eine Logik für den Verleih der Bücher.
>Bedenke: Eine Bibliothek sollte über eine begrenzte Anzahl einzelner Exemplare verfügen. Sollte ein Kunde sich ein Buch leihen wollen, dieses aber aktuell nicht verfügbar ist, soll eine entsprechende Meldung in der Konsole erscheinen.

#### **8. Bonus:**

Erweitere die Bibliotheksverwaltung ganz nach deiner eigenen Vorstellung - der Kreativität sind wie immer keinerlei Grenzen gesetzt!