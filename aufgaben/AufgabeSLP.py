from abc import ABC, abstractmethod

class Geraet(ABC):
    def __init__(self, hersteller: str, modell: str, einsatzjahr: int):
        self._hersteller = hersteller
        self._modell = modell
        self._einsatzjahr = einsatzjahr
        self._status = "ausgeschaltet"

    #@abstractmethod
    def zeige_status(self):
        '''zeige_status() – soll Gerätedaten und aktuellen Status anzeigen'''
        pass

    #@abstractmethod
    def geraete_typ(self):
        '''geraetetyp() – soll "Server", "Switch" oder "Storage" zurückgeben'''
        pass 
    
    def starten(self):
        '''starten() – setzt _status auf "aktiv"'''
        self._status = "aktiv"
    
    def ausschalten(self):
        '''ausschalten() – setzt _status auf "ausgeschaltet"'''
        self._status = "ausgeschaltet"

    def wartung_starten(self):
        '''wartung_starten() – setzt _status auf "in Wartung"'''
        self._status = "in Wartung"
    
    def ist_aktiv(self):
        return self._status == "aktiv"


class Server(Geraet):
    def __init__(self, hersteller: str, modell: str, einsatzjahr: int, anzahl_kerne: int):
        super().__init__(hersteller, modell, einsatzjahr)
        self.anzahl_kerne = anzahl_kerne
    
    def zeige_status(self):
        print(f"Gerät: {self._modell} | Status: {self._status}")
    
    def geraetetyp(self) -> str:
        print(f"Aufgabe doof, Kein Gerätetyp festgelegt. Deswegen printe ich einfach 'Server'.")
        print("Gerätetyp: Server")              
    

class Storage(Geraet):
    def __init__(self, hersteller: str, modell: str, einsatzjahr: int, kapazitaet_tb: float):
        super().__init__(hersteller, modell, einsatzjahr)
        self.kapazitaet_tb = kapazitaet_tb

    def zeige_status(self):
        print(f"Gerät: {self._modell} | Status: {self._status}")

    def geraetetyp(self) -> str:
        print(f"Aufgabe doof, Kein Gerätetyp festgelegt. Deswegen printe ich einfach 'Server'.")
        print("Gerätetyp: Server")

class Rechenzentrum:
    def __init__(self):
        self.__geraete = []

    def geraet_hinzufuegen(self, geraet: Geraet):
        self.__geraete.append(geraet)

    def alle_geraete_anzeigen(self):
        for geraet in self.__geraete:
            geraet.zeige_status()

    def aktive_geraete_anzeigen(self):
        for geraete in self.__geraete:
            if geraete.ist_aktiv():
                geraete.zeige_status()

    def geraete_nach_typ(self, typ: str):
        for geraete in self.__geraete:
            if geraete.geraetetyp().lower() == typ.lower():
                geraete.zeige_status()

    def suche_geraet_nach_modell(self, modellname: str):
        for geraete in self.__geraete:
            if modellname.lower() in geraete._modell.lower():
                geraete.zeige_status()



# fritzbox = Geraet("Fritzbox", "7730", 2010, "deaktiviert")

# fritzbox.starten()

# print(fritzbox.zeige_status())