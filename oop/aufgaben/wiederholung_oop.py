from abc import ABC, abstractmethod

class Content(ABC):
    
    def __init__(self, id, titel, genre, altersfreigabe, dauer):
        self._id = id
        self._titel = titel
        self._genre = genre
        self._altersfreigabe = altersfreigabe
        self._dauer = dauer
    
    def getID(self):
        return self._id
    
    def getDauer(self):
        return self._dauer
    
    @abstractmethod
    def overview(self):
        pass
        
class Film(Content):
    
    def __init__(self, id, titel, genre, altersfreigabe, dauer):
        super().__init__(id, titel, genre, altersfreigabe, dauer)
    
    def overview(self):
        return f"ID: {self._id} | Titel: {self._titel} | Genre: {self._genre} | FSK: {self._altersfreigabe} | Dauer (min): {self._dauer}"

class Serie(Content):

    def __init__(self, id, titel, genre, altersfreigabe, dauer, anzEpisoden):
        super().__init__(id, titel, genre, altersfreigabe, dauer)
        self.__anzEpisoden = anzEpisoden

    def overview(self):
        return f"ID: {self._id} | Titel: {self._titel} | Genre: {self._genre} | FSK: {self._altersfreigabe} | Dauer (min): {self._dauer} | Episoden: {self.__anzEpisoden}"

class Watchlist:

    def __init__(self, name, id):
        self.__inhalte = []
        self.__dauer = 0.0
        self.__id = id
        self.name = name

    def __add__(self, contentToAdd):
        content_to_add_id = contentToAdd.getID()
        if self.__inhalte == []:
            self.__inhalte.append(contentToAdd)
        else:
            if contentToAdd in self.__inhalte:
                print(f"Film mit ID {content_to_add_id} bereits in der Watchlist!")
            else:
                self.__inhalte.append(contentToAdd)
        self.__berechneGesamtdauer()
        return self
  
    def __str__(self):
        watchlist_overview = f"Meine Watchlist: {self.name} | Gesamtdauer: {self.__dauer}\n-----------------------------------------------------\n"
        for inhalt in self.__inhalte:
            watchlist_overview += inhalt.overview()
            watchlist_overview += "\n"
        return watchlist_overview

    def __berechneGesamtdauer(self):
        gesamtdauer = 0.0
        for inhalt in self.__inhalte:
            inhalt_dauer = inhalt.getDauer()
            gesamtdauer += inhalt_dauer
        self.__dauer = gesamtdauer

##### Sequenz für Sequenzdiagramm (Beginn) #####
my_watchlist = Watchlist("Meisterwerke", "WL-001")

my_film = Film("CF-001", "Stereotypischer Actionfilm", "Action", 6, 120.75)
print(my_film.overview())
my_serie = Serie("CS-001", "Das große Python-Drama", "Drama", 16, 600.0, 20)

my_watchlist += my_film
my_watchlist += my_serie
my_watchlist += my_serie

print(my_watchlist)
##### Sequenz für Sequenzdiagramm (Ende) #####