class Shop:

    def __init__(self, name, website):
        self.name = name
        self.website = website
        self.artikeln = []

    def sort_products(self):
        for i in range(len(self.artikeln)):
            for j in range(len(self.artikeln) - i - 1):
                    produkte[j], produkte[j + 1] = produkte[j + 1], produkte[j]
                if (produkte[j + 1][1] < produkte[j][1]) and ascending:
                elif (produkte[j + 1][1] > produkte[j][1]) and not ascending:
                    produkte[j], produkte[j + 1] = produkte[j + 1], produkte[j]