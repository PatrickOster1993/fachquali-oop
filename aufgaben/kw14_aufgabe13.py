class Song:

    def __init__(self, titel, kuenstler, genre, dauer, id):
        self.__titel = titel
        self.kuenstler = kuenstler
        self.__genre = genre
        self.dauer = dauer
        self.id = id

    def __str__(self):
        return f"Song-ID: {self.id} | Titel: {self.__titel} | Künstler: {self.kuenstler} | Genre: {self.__genre} | Dauer (s): {self.dauer}"

class Playlist:
    
    def __init__(self, name, id):
        self.name = name
        self.__id = id
        self.__dauer = 0
        self.__songs = []
    
    def __str__(self):
        infos = "Playlist: " + self.name + " | Dauer: " + str(self.__dauer) + "\n"
        for song in self.__songs:
            infos += (str(song) + "\n")
        return infos

    def __add__(self, song):
        self.__songs.append(song)
        self.__berechneAbspieldauer()
        return self

    def __berechneAbspieldauer(self):
        abspieldauer = 0
        for song in self.__songs:
            abspieldauer += song.dauer
        self.__dauer = abspieldauer

    def getAnzahlTitel(self):
        return len(self.__songs)

    def getHaufigsterKuenstler(self):
        kuenstler_liste = []
        kuenstler_count = []
        for song in self.__songs:
            kuenstler = song.kuenstler
            kuenstler_liste.append(kuenstler)
        for i in range(len(kuenstler_liste)):
            kuenstler = kuenstler_liste[i]
            kuenstler_count.append(kuenstler_liste.count(kuenstler))
        kuenstler_index = kuenstler_count.index(max(kuenstler_count))
        return kuenstler_liste[kuenstler_index]

    def sucheSong(self, songID):
        for song in self.__songs:
            if song.id == songID:
                return song
        return None

############ sd my_playlist #############
song1 = Song("Yellow Submarine", "The Beatles", "Pop/Rock", 200, "P-B-01")
print(song1)

song2 = Song("Paint it black", "The Rolling Stones", "Rock", 220, "R-R-01")
song3 = Song("Satisfaction", "The Rolling Stones", "Rock", 180, "R-R-02")

playlist = Playlist("Lieblingssongs", "PL-01")
playlist += song1
playlist += song2
playlist += song3
print(playlist)

print(playlist.getHaufigsterKuenstler())
print(playlist.sucheSong("P-B-01"))
############ sd my_playlist #############
