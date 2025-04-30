# Klasse = "Blueprint"
class Book:
    # Konstruktor
    def __init__(self, author, title, year, price):
        self.author = author
        self.title = title
        self.year = year
        self.price = price
        self.zustand = "neu"

    def __str__(self):
        return f"Author: {self.author}, Title: {self.title}, Year: {self.year}, Price: {self.price}, Zustand: {self.zustand}"
    
    def changeZustand(self, zustand):
        if self.zustand != zustand:
            self.zustand = zustand
            self.changePrice()
    
    def changePrice(self):
        if self.zustand != "neu":
            self.price *= 0.7

# Instanzen / Objekte der Klasse "Book" erstellen
mein_buch = Book("Patrick Oster", "Mein Titel", 2025, 19.99)
dein_buch = Book("Max Mustermann", "Sein Titel", 2024, 9.99)

anderes_buch = Book(
    author="Patrick Oster", 
    title="Anderer Titel", 
    year=2023,
    price = 14.99
)

print(mein_buch)

mein_buch.changeZustand("leichte Dellen")
print(mein_buch)

mein_buch.changeZustand("leichte Dellen")
print(mein_buch)

# meine_buecher_liste = [mein_buch, dein_buch, anderes_buch]

# mein_author = mein_buch.author
# print(mein_author)

# mein_title = mein_buch.title
# print(mein_title)