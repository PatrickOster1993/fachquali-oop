from abc import ABC, abstractmethod

class Geraet(ABC):
    def __init__(self, hersteller: str, modell: str, einsatzjahr: int):
        self._hersteller = hersteller
        self._modell = modell
        self._einsatzjahr = einsatzjahr
        self._status = "ausgeschaltet"

    @abstractmethod
    def zeige_status(self):
        '''zeige_status() – soll Gerätedaten und aktuellen Status anzeigen'''
        pass

    @abstractmethod
    def geraetetyp(self):
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

class Switch(Geraet):
    def __init__(self, hersteller: str, modell: str, einsatzjahr: int, ports: int):
        super().__init__(hersteller, modell, einsatzjahr)
        self.ports = ports

    def zeige_status(self):
        print(f"Gerät: {self._modell}| Ports: {self.ports} | Status: {self._status}")

    def geraetetyp(self) -> str:
        return "Switch"

class Server(Geraet):
    def __init__(self, hersteller: str, modell: str, einsatzjahr: int, anzahl_kerne: int):
        super().__init__(hersteller, modell, einsatzjahr)
        self.anzahl_kerne = anzahl_kerne
    
    def zeige_status(self):
        print(f"Gerät: {self._modell} | Anzahl Kerne: {self.anzahl_kerne} | Status: {self._status}")
    
    def geraetetyp(self) -> str:
        return "Server"     
    

class Storage(Geraet):
    def __init__(self, hersteller: str, modell: str, einsatzjahr: int, kapazitaet_tb: float):
        super().__init__(hersteller, modell, einsatzjahr)
        self.kapazitaet_tb = kapazitaet_tb

    def zeige_status(self):
        print(f"Gerät: {self._modell}| Speicherkapazität: {self.kapazitaet_tb} | Status: {self._status}")

    def geraetetyp(self) -> str:
        return "Storage"

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
            if geraete.geraetetyp() == typ: # laut gpt ist das unsauber, weil Falscheingaben (Groß und Kleinschreibung) zu Fehlerhaften ausgabe führen können (.lower() benutzen. 
                # Außerdem greifen wir auf eine protected Variable zu.. das sollten wir eigentlich nicht tun. 
                # Demnach sollte man eine Getter methode einbauen in der Klasse, auf die dann hier zugegriffen werden soll.
                geraete.zeige_status()

    def suche_geraet_nach_modell(self, modellname: str):
        for geraete in self.__geraete:
            if modellname == geraete._modell:# laut gpt ist das unsauber, weil Falscheingaben (Groß und Kleinschreibung) zu Fehlerhaften ausgabe führen können (.lower() benutzen. 
                # Außerdem greifen wir auf eine protected Variable zu.. das sollten wir eigentlich nicht tun. 
                # Demnach sollte man eine Getter methode einbauen in der Klasse, auf die dann hier zugegriffen werden soll.
                geraete.zeige_status()


if __name__ == "__main__":
    server1 = Server("HP", "2210", 2025, 12)
    switch1 = Switch("TP-Link", "840", 2021, 8)
    storage1 = Storage("Samsung", "980", 2021, 4)

    rechenzentrum1 = Rechenzentrum()

    rechenzentrum1.geraet_hinzufuegen(server1)
    rechenzentrum1.geraet_hinzufuegen(switch1)
    rechenzentrum1.geraet_hinzufuegen(storage1)

    server1.starten()

    storage1.wartung_starten()

    rechenzentrum1.alle_geraete_anzeigen()
    print("###############################################################")
    rechenzentrum1.aktive_geraete_anzeigen()
    print("###############################################################")
    rechenzentrum1.suche_geraet_nach_modell("840")
    print("###############################################################")
    rechenzentrum1.geraete_nach_typ("Storage")
