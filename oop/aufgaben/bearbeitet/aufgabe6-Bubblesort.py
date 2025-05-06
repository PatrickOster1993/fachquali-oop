# IT-Handbuch Seite 581-582

def bubblesort(list):
# Endlosschleife bis auf Weiteres:
    while True:
        is_sorted = True # Annahme: bereits sortiert
        for i in range(0, len(list) - 1):
            # Element i größer als Element i + 1?
            if list[i] > list[i + 1]:
                # Die beiden Elemente vertauschen:
                list[i], list[i + 1] = list[i + 1], list[i]
                # Aha, also noch nicht sortiert:
                is_sorted = False
        # Bereits sortiert?
        if is_sorted:
            # Endlosschleife verlassen:
            break

if __name__ == '__main__':
    l = [9, 1, 8, 2, 7, 3, 6, 4, 5]
    bubblesort(l)
    print(l)
    l = ["Zebra", "Affe", "Marabu", "Elefant"] # ascii zeichen oder auch Unicode (148 ersten zeichen sind ASCII)
    bubblesort(l)
    print(l)

