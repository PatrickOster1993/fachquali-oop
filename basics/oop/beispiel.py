# Klasse = "Blueprint"
class Book:
    # Konstruktor
    def __init__(self, author, title, year):
        self.author = author
        self.title = title
        self.year = year

    def __str__(self):
        return f"Author: {self.author}, Title: {self.title}, Year: {self.year}"

# Instanzen / Objekte der Klasse "Book" erstellen
mein_buch = Book("Patrick Oster", "Mein Titel", 2025)
dein_buch = Book("Max Mustermann", "Sein Titel", 2024)

anderes_buch = Book(
    author="Patrick Oster", 
    title="Anderer Titel", 
    year=2023
)

print(mein_buch)
print(dein_buch)
print(anderes_buch)

meine_buecher_liste = [mein_buch, dein_buch, anderes_buch]

# mein_author = mein_buch.author
# print(mein_author)

# mein_title = mein_buch.title
# print(mein_title)
