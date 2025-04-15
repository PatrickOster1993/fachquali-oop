from abc import ABC, abstractmethod

# Aufgabe: Gerätemanagement in einem Rechenzentrum
# Szenario:
# Du entwickelst ein System zur Verwaltung von Geräten (z. B. Servern, Switches, Speichereinheiten) in einem Rechenzentrum. 
# Jedes Gerät hat spezifische Eigenschaften und kann gewartet, heruntergefahren oder gestartet werden. 
# Es gibt gemeinsame Eigenschaften und Methoden, aber auch gerätespezifische Unterschiede.

# Anforderungen
# 1. Abstrakte Klasse Geraet
# Erstelle eine abstrakte Klasse Geraet mit folgenden Elementen:

# Geschützte Attribute
# _hersteller (str)

# _modell (str)

# _einsatzjahr (int)

# _status (str) – mögliche Werte: "aktiv", "in Wartung", "ausgeschaltet"

# Abstrakte Methoden
# zeige_status() – soll Gerätedaten und aktuellen Status anzeigen

# geraetetyp() – soll "Server", "Switch" oder "Storage" zurückgeben

# Konkrete Methoden
# starten() – setzt _status auf "aktiv"

# ausschalten() – setzt _status auf "ausgeschaltet"

# wartung_starten() – setzt _status auf "in Wartung"

# ist_aktiv() – gibt zurück, ob das Gerät "aktiv" ist

# Verwende dafür das Modul abc:

# python
# Kopieren
# Bearbeiten

class Geraet(ABC):

    def __init__(self, _hersteller:str, _modell:str, _einsatzjahr:int, _status:str, _geraetetyp:str):
        self._hersteller = _hersteller
        self._modell = _modell
        self._einsatzjahr = _einsatzjahr
        self._status = "aktiv" or "in Wartung" or "ausgeschaltet"
        self._geraetetyp = _geraetetyp


    
    @abstractmethod
    def zeige_status(self):
        pass

    
    @abstractmethod
    def geraetetyp(self):
        pass

    @abstractmethod
    def starten(self):
        pass

    @abstractmethod
    def starten(self):
        pass

    @abstractmethod
    def wartung_starten(self):
        pass

    @abstractmethod
    def ist_aktiv(self):
        pass

    

# 2. Abgeleitete Klasse Server
# Zusätzliches Attribut:

# anzahl_kerne (int)

# Implementierung von:

# zeige_status() – z. B. "Server Dell R740 (2019) – 16 Kerne – Status: aktiv"

# geraetetyp() – "Server"

class Server(Geraet):

    def __init__(self, _hersteller: str, _modell: str, _einsatzjahr: int, _status: str, _geraetetyp:str, _anzahl_kerne:int):
        super().__init__(_hersteller, _modell, _einsatzjahr, _status, _geraetetyp)
        self._anzahlkerne = _anzahl_kerne
        



    def zeige_status(self):
        print (f" Hersteller: {self._hersteller} \n Modell: {self._modell} \n Einsatzjahr: {self._einsatzjahr} \n Status: {self._status} \n Anzahlkerne: {self._anzahlkerne} \n Gerätetyp: {self._geraetetyp}") 
        

    def starten(self):
        self._status = "aktiv"
        print ("System aktiviert")

    def starten(self):
        self._status = "ausgeschaltet"
        print ("System ausgeschaltet")

    def wartung_starten(self):
        self._status = "in Wartung"
        print ("Wartung gestartet")

    def ist_aktiv(self):
        if self._status == "aktiv":
            print("Ist Aktiv")
            return
        else:
            print("Ist nicht Aktiv")
            return


server1 = Server("Dell", "M12", 1990, "aktiv", 12, "Server")

print (server1.wartung_starten())
print (server1.ist_aktiv())
print (server1.geraetetyp())
print (server1.zeige_status())





# 3. Abgeleitete Klasse Switch
# Zusätzliches Attribut:

# ports (int)

# Implementierung von:

# zeige_status() – z. B. "Switch Cisco C2960 (2020) – 48 Ports – Status: ausgeschaltet"

# geraetetyp() – "Switch"







# 4. Abgeleitete Klasse Storage
# Zusätzliches Attribut:

# kapazitaet_tb (float)

# Implementierung von:

# zeige_status() – z. B. "Storage NetApp FAS (2021) – 24.0 TB – Status: in Wartung"

# geraetetyp() – "Storage"

# 5. Klasse Rechenzentrum
# Diese Klasse verwaltet eine Liste von Geräten:

# Privates Attribut
# __geraete – Liste von Geraet-Objekten

# Methoden
# geraet_hinzufuegen(geraet: Geraet)

# alle_geraete_anzeigen() – ruft zeige_status() für alle Geräte auf

# aktive_geraete_anzeigen()

# geraete_nach_typ(typ: str) – z. B. "Server" → gibt nur diese zurück

# suche_geraet_nach_modell(modellname: str) – filtert anhand des Modellnamens

# Zusatzaufgaben (optional)
# Füge eine Methode hinzu, um alle Geräte nach Einsatzjahr zu sortieren.

# Implementiere einen Wartungsbericht als Textdatei, in dem alle Geräte mit Status "in Wartung" gelistet sind.

# Baue ein einfaches Benutzerinterface in der Konsole zur Verwaltung (Menü mit Eingaben).