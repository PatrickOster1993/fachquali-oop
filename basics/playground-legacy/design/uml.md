
# UML (Unified Modeling Language)

Die Unified Modeling Language (UML) ist eine standardisierte Modellierungssprache, die verwendet wird, um die Struktur und das Verhalten von Softwaresystemen zu beschreiben, zu visualisieren, zu konzipieren und zu dokumentieren. UML bietet eine grafische Notation, die es Entwicklern und Architekten ermöglicht, komplexe Softwarestrukturen klar und verständlich darzustellen.

## Grundprinzipien der UML

- **Abstraktion**: UML hilft dabei, die wesentlichen Aspekte eines Systems herauszuarbeiten, indem es Details abstrahiert.
- **Visualisierung**: Die Sprache unterstützt die Erstellung von Diagrammen, die eine visuelle Darstellung der Systemstruktur und -prozesse bieten.
- **Standardisierung**: UML folgt einem standardisierten Ansatz, der es verschiedenen Entwicklern und Teams ermöglicht, effektiv zusammenzuarbeiten.
- **Vielseitigkeit**: UML kann für verschiedene Arten von Systemen verwendet werden, von der Softwareentwicklung über Datenbankdesign bis hin zur Geschäftsprozessmodellierung.

---

## Arten von UML-Diagrammen

UML-Diagramme lassen sich grob in zwei Kategorien einteilen:

1. **Strukturelle Diagramme**: Diese Diagramme beschreiben die statische Struktur des Systems.
   - **Klassendiagramm (wichtig für uns)**
   - Objektdiagramm
   - Komponentendiagramm
   - Verteilungsdiagramm
   
2. **Verhaltensdiagramme**: Diese Diagramme modellieren das dynamische Verhalten eines Systems.
   - Use-Case-Diagramm
   - **Sequenzdiagramm (wichtig für uns)**
   - Aktivitätsdiagramm
   - Zustandsdiagramm

---

## Klassendiagramm

Das **Klassendiagramm** ist eines der wichtigsten UML-Diagramme, das die statische Struktur eines Systems beschreibt. Es zeigt die Klassen eines Systems und die Beziehungen zwischen ihnen. Ein Klassendiagramm besteht aus folgenden Elementen:

- **Klassen**: Repräsentieren Entitäten im System, z. B. Personen oder Fahrzeuge.
  - Eine Klasse wird durch ein Rechteck dargestellt, das in drei Teile unterteilt ist:
    1. **Name der Klasse**
    2. **Attribute** (Eigenschaften der Klasse)
    3. **Methoden** (Operationen der Klasse)
  
- **Beziehungen**:
  - **Assoziation**: Zeigt die Verbindung zwischen zwei Klassen.
  - **Vererbung**: Eine Klasse kann von einer anderen Klasse erben.
  - **Realisierung**: Eine Klasse kann eine abstrakte Klasse / Interface realisieren.
  - **Aggregation**: Eine "Teil-von"-Beziehung, bei der das existierende Objekt auch ohne das andere existieren kann.
  - **Komposition**: Eine stärkere Form der Aggregation, bei der das Teil-Objekt nicht ohne das Container-Objekt existieren kann.

- **Kapselung**:
	- **private** (-)
	- **protected** (#)
	- **public** (+)

### Beispiel: Bibliotheksverwaltung

```mermaid
classDiagram
    %% Basisklasse Buch
    class Buch {
        + titel: string
        + autor: string
        + isbn: string
        + details(): string
        + lesen(): void
    }

    %% Unterklasse Sachbuch
    class Sachbuch {
        - thema: string
        + wissenVermitteln(): void
        + lesen(): void
    }

    %% Unterklasse Roman
    class Roman {
        + genre: string
        + fsk: int
        + lesen(): void
    }

    %% Aggregation: Bibliothek
    class Bibliothek {
        - buecher: List<Buch>
        + buchHinzufuegen(buch: Buch): void
        + buchEntfernen(buch: Buch): void
    }

    %% Kundenklasse
    class Kunde {
        + name: string
        - buecher: List<Buch>
        + ausleihen(buch: Buch): void
        + zurueckgeben(buch: Buch): void
    }

    %% Beziehungen
    Buch <|-- Sachbuch: erbt
    Buch <|.. Roman: implementiert lesen() (besser, da abstrakt)
    Bibliothek o-- "1..*" Buch: enthält (Aggr.)
    Bibliothek *-- "1..*" Kunde: registriert (Komp.)
    Kunde "1" --> "*" Buch: leiht aus (Assoziation)
   ```

### Aufgabe:
Zeichnen Sie ein Klassendiagramm für unsere frühere Übungsaufgabe **rollenspiel** *(20 min.)*

## Sequenzdiagramm

Das **Sequenzdiagramm** ist ein weiteres wichtiges UML-Diagramm, das den Ablauf von Interaktionen zwischen Objekten / Instanzen im System über die Zeit hinweg darstellt. Es wird hauptsächlich verwendet, um den zeitlichen Ablauf von Nachrichten zwischen den Objekten und deren Interaktionen zu visualisieren.

### Wichtige Elemente des Sequenzdiagramms:
- **Objekte**: Repräsentieren Instanzen von Klassen und werden horizontal in der oberen Zeile des Diagramms dargestellt.
- **Lebenslinie**: Eine senkrechte gestrichelte Linie, die den Lebenszyklus eines Objekts darstellt. Sie wird unter jedem Objekt angezeigt.
- **Nachrichten**: Zeigen Interaktionen zwischen Objekten und werden als Pfeile von einem Objekt zu einem anderen gezeichnet. Die Richtung des Pfeils zeigt, welches Objekt die Nachricht sendet und welches sie empfängt.
- **Aktivierungsbalken**: Ein schmaler rechteckiger Balken, der den Zeitraum darstellt, in dem ein Objekt eine Aktion ausführt.
- **Rückgabewerte**: Nachrichten, die das Ergebnis einer Funktion oder einer Methode darstellen, werden durch gestrichelte Pfeile angezeigt.

### Beispiel: Bibliotheksverwaltung (vereinfacht)

```mermaid
sequenceDiagram
    participant K as Kunde
    participant B as Bibliothek
    participant S as Sachbuch
    participant R as Roman
    participant BK as Buch

    %% Instanzen erstellen
    K->>K: Kunde erstellen (Patrick)
    S->>BK: Sachbuch erstellen ("Physik ist toll", "Albert Zweistein", "123456789", "Physik")
    R->>BK: Roman erstellen ("Der große Gatsby", "F. Scott Fitzgerald", "123456789", "erotik")
    
    %% Buch-Details anzeigen
    S->>BK: details() - zeigt Buchdetails (Titel, Autor, ISBN)
    R->>BK: details() - zeigt Buchdetails (Titel, Autor, ISBN)
    S->>S: wissenVermitteln() - Ausgabe: "Das Buch Physik ist toll vermittelt Wissen zum Thema Physik."
    S->>S: lesen() - Ausgabe: "Ich lese, um zu lernen!"
    R->>R: lesen() - Ausgabe: "Ich lese, um in eine fesselnde Welt einzutauchen."

    %% Bücher zur Bibliothek hinzufügen
    B->>S: buchHinzufuegen(S) - Hinzufügen von Sachbuch
    B->>R: buchHinzufuegen(R) - Hinzufügen von Roman
    
    %% Buch entfernen
    B->>R: buchEntfernen(R) - Entfernen von Roman

    %% Buch erneut zur Bibliothek hinzufügen
    B->>R: buchHinzufuegen(R) - Hinzufügen von Roman erneut
    
    %% Kunde zur Bibliothek hinzufügen
    B->>B: kundeHinzufuegen(K) - Hinzufügen von Kunde Patrick
    
    %% Bücher an Kunden verleihen
    B->>K: buchVerleihen(S, K) - Sachbuch an Kunde verleihen
    B->>K: buchVerleihen(R, K) - Roman an Kunde verleihen

    %% Buch zurücknehmen
    B->>K: buchZuruecknehmen(R, K) - Roman zurücknehmen
    
    %% Bücher erneut zur Bibliothek hinzufügen
    B->>S: buchHinzufuegen(S) - Sachbuch erneut hinzufügen
    
    %% Buchbestand anzeigen
    B->>B: zeigeBuchbestand() - Zeigt gesamten Buchbestand
   ```
    
## Cheatsheet

> siehe: [Link](https://www.oose.de/wp-content/uploads/2012/05/UML-Notations%C3%BCbersicht-2.5.pdf)