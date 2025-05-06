#Aufgabe 17 Bubblesort & Lineare Suche
#Sie arbeiten als Entwickler für einen Online-Shop, der Elektronikartikel verkauft. Kunden können sich Produkte in einer Liste anzeigen lassen, entweder aufsteigend oder absteigend nach Preis. Außerdem möchten sie ein bestimmtes Produkt schnell finden. Zusätzlich sollen sie die Möglichkeit haben, neue Produkte zur Liste hinzuzufügen. Die Anwendung startet mit folgenden Produkten:
#[ [‚Laptop‘, 1200], [‚Smartphone’, 800], [‚Tablet’, 500], [‚Monitor‘, 300], [‚Maus‘, 50]]
#Ihre Aufgabe ist es, eine Python-Anwendung zu schreiben, die folgende Funktionen bietet:

#Sortierung der Produktpreise mit Bubblesort:
#• Implementieren Sie den Bubblesort-Algorithmus zur Sortierung der Produktliste.
#• Der Benutzer kann wählen, ob die Liste aufsteigend (günstigstes Produkt zuerst) oder
#absteigend (teuerstes Produkt zuerst) sortiert werden soll.
#• Der Algorithmus soll optimiert werden, sodass er abbricht, wenn die Liste bereits sortiert
#ist.
#Lineare Suche nach einem Produkt:
#• Implementieren Sie eine Funktion, die mithilfe der linearen Suche nach einem Produktnamen sucht.
#
# • Falls das Produkt existiert, soll der Preis ausgegeben werden, ansonsten eine entsprechende Meldung erscheinen.
#Hinzufügen neuer Produkte:
#• Der Benutzer soll ein neues Produkt mit Namen und Preis zur Liste hinzufügen können.
#• Die Liste soll danach automatisch sortiert werden (nach der zuletzt gewählten
#Sortiermethode).

produkte = [['Laptop', 1200], ['Smartphone', 800], ['Tablet', 500], ['Monitor', 300], ['Maus', 50]]
zuletzt_aufsteigend = True

# 1. Sortierung & Überprüfung:

## Überprüfung, ob bereits sortiert:
def produkte_unsortiert(ascending):
    # gibt True zurück, wenn produkte sortiert, und False, falls nicht!
    counter = 0

    for i in range(len(produkte) - 1):
        aktueller_preis = produkte[i][1]
        naechster_preis = produkte[i + 1][1]
        diff = naechster_preis - aktueller_preis
        if ascending and diff > 0:
            counter += 1
        elif not ascending and diff < 0:
            counter
    
    if counter == 4:
        if ascending:
            print("Produkte bereits aufsteigend sortiert!")
        elif not ascending:
            print("Produkte bereits absteigend sortiert!")
        return False
    return True

## Bubblesort mit Auswahl, ob auf- u. absteigend:
def sort_products(ascending = True):
    if produkte_unsortiert(ascending):
        for i in range(len(produkte)):
            for j in range(len(produkte) - i - 1):
                if (produkte[j + 1][1] < produkte[j][1]) and ascending:
                    produkte[j], produkte[j + 1] = produkte[j + 1], produkte[j]
                elif (produkte[j + 1][1] > produkte[j][1]) and not ascending:
                    produkte[j], produkte[j + 1] = produkte[j + 1], produkte[j]

# 2. Überprüfen, ob Produkt in Liste
def produkt_in_liste(produktname):
    produkt_nicht_enthalten = True
    for produkt in produkte:
        bezeichnung = produkt[0]
        if bezeichnung == produktname:
            produkt_nicht_enthalten = False
            preis = produkt[1]
            print(f"Produkt {produktname} kostet {preis} €!")
    if produkt_nicht_enthalten:
        print(produktname + " nicht in Liste enthalten!")

# 3. Neues Produkt der Liste hinzufügen:
def add_product(name, preis):
    produkte.append([name, preis])
    sort_products(zuletzt_aufsteigend)

print("####### Unsortiere Liste #######")
print(produkte)

print("####### Aufsteigend sortierte Liste #######")
sort_products(ascending=True)
zuletzt_aufsteigend = True
print(produkte)
print("#######################")
sort_products(ascending=True)
zuletzt_aufsteigend = True
print(produkte)

print("####### Absteigend sortierte Liste #######")
sort_products(ascending=False)
zuletzt_aufsteigend = False
print(produkte)

print("####### Überprüfen, ob Produkt in Liste #######")
produkt_in_liste('Smartphone')
produkt_in_liste('iPhone')

print("####### Produkt hinzufügen #######")
add_product('iPhone', 700)
produkt_in_liste('iPhone')
print(produkte)

# Bugfix: Variable "zuletzt_aufsteigend" lässt sich nicht in innerem Scope ansprechen (Bsp.: "sort_products()")