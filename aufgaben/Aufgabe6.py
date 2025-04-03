class OnlineShop:

    def __init__(self, produkte):
        self.produkte = produkte

    def check_product(self, name):
        for zeile in self.produkte:
            for spalte in self.produkte:
                if spalte[0] == name:
                    return True
        return False        
        
    


        


    def add_product(self, name, preis):
        if self.check_product(name):
            print(f"{name} ist bereits vorhanden!")
        else:
            self.produkte.append([name, preis])

    def __str__(self):
        return f"{self.produkte}"


    # def produkte_unsortiert(ascending):
    #     # gibt True zurück, wenn produkte sortiert, und False, falls nicht!
    #     counter = 0

    #     for i in range(len(produkte) - 1):
    #         aktueller_preis = produkte[i][1]
    #         naechster_preis = produkte[i + 1][1]
    #         diff = naechster_preis - aktueller_preis
    #         if ascending and diff > 0:
    #             counter += 1
    #         elif not ascending and diff < 0:
    #             counter
        
    #     if counter == 4:
    #         if ascending:
    #             print("Produkte bereits aufsteigend sortiert!")
    #         elif not ascending:
    #             print("Produkte bereits absteigend sortiert!")
    #         return False
    #     return True

    # ## Bubblesort mit Auswahl, ob auf- u. absteigend:
    # def sort_products(ascending = True):
    #     if produkte_unsortiert(ascending):
    #         for i in range(len(produkte)):
    #             for j in range(len(produkte) - i - 1):
    #                 if (produkte[j + 1][1] < produkte[j][1]) and ascending:
    #                     produkte[j], produkte[j + 1] = produkte[j + 1], produkte[j]
    #                 elif (produkte[j + 1][1] > produkte[j][1]) and not ascending:
    #                     produkte[j], produkte[j + 1] = produkte[j + 1], produkte[j]

    # # 2. Überprüfen, ob Produkt in Liste
    # def produkt_in_liste(produktname):
    #     produkt_nicht_enthalten = True
    #     for produkt in produkte:
    #         bezeichnung = produkt[0]
    #         if bezeichnung == produktname:
    #             produkt_nicht_enthalten = False
    #             preis = produkt[1]
    #             print(f"Produkt {produktname} kostet {preis} €!")
    #     if produkt_nicht_enthalten:
    #         print(produktname + " nicht in Liste enthalten!")





onlineshop = OnlineShop(produkte=[])

onlineshop.add_product("PC", 700)
onlineshop.add_product("Handy", 700)

onlineshop.add_product("Laptop", 700)
print(onlineshop)

onlineshop.add_product("Handy", 700)
