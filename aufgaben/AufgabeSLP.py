from abc import ABC, abstractmethod

class Geraet:

    def __init__(self, hersteller, modell, einsatzjahr, status):
        #super().__init__(self, _hersteller, _modell, _einsatzjahr, _status)
        self._hersteller: str = hersteller
        self._modell:str = modell
        self._einsatzjahr:int = einsatzjahr
        self._status:str = status

    #@abstractmethod
    def zeige_status(self):
        '''zeige_status() – soll Gerätedaten und aktuellen Status anzeigen'''
        return f"Hersteller:{self._hersteller}\nModell:{self._modell}\nEinsatzjahr:{self._einsatzjahr}\nStatus:{self._status}" # Hier muss ich noch den Status anpassen

    #@abstractmethod
    def geraete_typ(self):
        '''geraetetyp() – soll "Server", "Switch" oder "Storage" zurückgeben'''
        return 
    
    def starten(self):
        '''starten() – setzt _status auf "aktiv"'''
        self._status = "aktiv"
        return self._status
    
    def ausschalten(self):
        '''ausschalten() – setzt _status auf "ausgeschaltet"'''
        self._status = "ausgeschaltet"
        return self._status

    def wartung_starten(self):
        '''wartung_starten() – setzt _status auf "in Wartung"'''
        self._status = "in Wartung"
        return self._status
    
    def ist_aktiv(self):
        '''ist_aktiv() – gibt zurück, ob das Gerät "aktiv" ist'''
        if self._status == "aktiv":
            return f"Gerät ist aktiv."
        else:
            return f"Gerät ist nicht aktiv"


# 2. Abgeleitete Klasse Server
# Zusätzliches Attribut:

# anzahl_kerne (int)

# Implementierung von:

# zeige_status() – z. B. "Server Dell R740 (2019) – 16 Kerne – Status: aktiv"

# geraetetyp() – "Server"

# class Server(Geraet):

#     def __init__(self, anzahl_kerne):
#         super().__init__()


fritzbox = Geraet("Fritzbox", "7730", 2010, "deaktiviert")

fritzbox.starten()

print(fritzbox.zeige_status())