personen_daten = {
    "Name": "",
    "Alter": "",
    "Lieblingsessen": ""
}

personen_daten["Name"] = input("Wie heißt du? ")
personen_daten["Alter"] = input("Wie alt bist du? ")
personen_daten["Lieblingsessen"] = input("Was ist dein Lieblingsessen? ")

print(f"Hallo {personen_daten['Name']}, du bist {personen_daten['Alter']} Jahre alt und dein Lieblingsessen ist {personen_daten['Lieblingsessen']}.")