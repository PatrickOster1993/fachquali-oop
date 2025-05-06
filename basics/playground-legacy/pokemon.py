import requests

RAW_URL = "https://pokeapi.co/api/v2/pokemon/"

pokemon = input("Pokemon eingeben: ")
response = requests.get(RAW_URL + pokemon.lower())

code = response.status_code

if code == 200:
    print(response.json())
    # Tipp: Struktur über https://jsonbeautifier.org ansehen
    # (alle Unterobjekte zuklappen für Überblick)
else:
    print("Fehler:", code)