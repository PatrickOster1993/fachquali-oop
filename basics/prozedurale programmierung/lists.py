# Komplexere / Zusammengesetzte Datentypen: Schwerpunkt Listen (="Arrays")

# Einfache Liste:
a = [3, 7, 1, 2]
b = ["a", "b", "c"]
print(a)
# print(b)

# Ein Element der Liste hinzufügen:
a.append(6)
print(a)

# Auf Element innerhalb der Liste über Index zugreifen:
print(a[0]) # 1. Element = Index 0 (ganz ganz wichtig!!!)

# Verhalten des Speichers:

x = 1
y = 2

## zunächst bei einfachen Variablen:
print("Speicheradresse von x:", id(x), "Speicheradresse von y:", id(y))

## jetzt bei Listen:
print("Liste a:", a, "Adresse a:", id(a))
a.append(0)
print("Liste a:", a, "Adresse a:", id(a))
print("Liste b:", b, "Adresse b:", id(b))
print(id(a) - id(b))

## Referenzieren / Identitätsoperator
c = ['d', 'e', 'f']
print("Liste b:", b)
print("Liste c:", c)

c = b
# c = b.copy()
print("Liste b:", b)
print("Liste c:", c)

print("#################")
c.append('g')

print("Liste b:", b)
print("Liste c:", c)

d = ['a', 'b', 'c', 'g']

print("Wert von c:", c, "Adress von c:", id(c))
print(c == d)
print("Wert von d:", d, "Adress von d:", id(d))
print(c is d)

d = c

print("Wert von c:", c, "Adress von c:", id(c))
print(c == d)
print("Wert von d:", d, "Adress von d:", id(d))
print(c is d)

# in-Operator
print('####################')
print('a' in d)
print('z' in d)

if 'a' in d:
    print("a befindet sich in d-Liste!")
else:
    print("Kein a in d-Liste vorhanden!")

# Listenelemente in einer Schleife durchlaufen:
print("######### Schleifen ###########")

i = 0

# Kopfgesteuerte while-Schleife
while i < 10:
    print(i)
    i += 1

i = 0

print("################")

# Fußgesteuerte while-Schleife
while True:
    print(i)
    i += 1
    if i > 0:
        break

## jetzt auf Listen / Arrays angewandt:
meine_liste = ["Hallo", "ich", "heiße", "Patrick"]
i = 0

while i < len(meine_liste):
    print(meine_liste[i])
    i += 1

# Reverse-Ansatz
i = len(meine_liste) - 1
while i >= 0:
    print(meine_liste[i])
    i -= 1

# Exkurs: Flexible Verwendung von Listen (nicht so wichtig für Prüfung --> Python-natives Wissen)
# hey = [3, "hallo", True]
# print(hey)

# for-Schleife mit vielen Ausprägungen

print("######## for-Schleifen #########")
for i in range(0, len(meine_liste)):
    print(meine_liste[i])

# oder viel kompakter...
print("######## Kompakte for-Schleifen #########")

for inhalt in meine_liste:
    print("Inhalt:", inhalt)

# Weitere wichtige Grundlagen bzgl. Arrays / Listen:

print("#################")



neue_liste = [1, 2, 3, 4]

print("######## Comprehension #########")
print(neue_liste)
doppelt = [elem * 2 for elem in neue_liste]
print(doppelt)
print("################################")

## Letztes Element der Liste entfernen:
neue_liste.pop()
print(neue_liste)

## Beliebiges Element entfernen:
print("####### Element entfernen #########")
neue_liste.append(2)
print(neue_liste)
first_index_of_2 = neue_liste.index(2)
print(first_index_of_2)
neue_liste.remove(2)
print(neue_liste)
print("###################################")

## Elemente an beliebiger Stelle hinzufügen
neue_liste.insert(1, 10)
print(neue_liste)

## Listenelemente umdrehen!!!
neue_liste.reverse(); print(neue_liste) # geht auch in 1 Zeile (aber: bad-practice-Ansatz!!!)

print('###################')
print(neue_liste)
## Auf das erste und letzte Element explizit zugreifen:
print(neue_liste[0]) # auf 1. Element in der Liste zugreifen (= Index 0 --> ganz wichtig!)
print(neue_liste[-1]) # auf letzte Element in der Liste zugreifen

## zur Ergänzung: von Vorne oder Hinten zugreifen auf beliebigen Wert in Liste:
print(neue_liste[1]) # hier auf 2. Element zugreifen
print(neue_liste[-2]) # hier auf vorletztes Element zugreifen

## Neue Liste als "Teil-Liste" einer vorhandenen Liste erstellen:
teil_liste = neue_liste[1:3]
print(teil_liste)
print(id(neue_liste), id(teil_liste))

## Experiment mit "del":
# print("++++++++++++++++++++++++++++")
# print(neue_liste)
# del neue_liste
# print(neue_liste)
# print("++++++++++++++++++++++++++++")



# reverse_liste = neue_liste.copy()
# reverse_liste.reverse()

# print(neue_liste)
# print(reverse_liste)












