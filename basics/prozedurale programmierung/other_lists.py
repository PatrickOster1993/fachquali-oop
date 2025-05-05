# Tupel:
meine_liste = [5, 2, 1]
mein_tupel = (5, 2, 1) # = unveränderliche Liste / Array

print(type(mein_tupel))
print(mein_tupel)

mein_neuer_tupel = tuple(meine_liste)
print(mein_neuer_tupel)
# mein_tupel[0] = 10 # nicht erlaubt!!!

# Set:
mein_set = {5, 2, 1}
print(type(mein_set))
print(mein_set)

mein_neues_set = set(meine_liste)
print(mein_neues_set)

mein_set.add(10)
mein_set.add(10)
mein_set.add(5)
print(mein_set)

# Dictionary:

person = {
    "name": {
        "vorname": "Patrick",
        "nachname": "Oster"
    },
    "bundesland": "Bayern",
    "alter": 18,
    "hobby": ["programmieren", "sk8en", "..."]
}

# meine_personen = [person] * 5
print(type(person))
print(person)

lieblingshobby = person["hobby"][1]
print(lieblingshobby)

# print(meine_personen)