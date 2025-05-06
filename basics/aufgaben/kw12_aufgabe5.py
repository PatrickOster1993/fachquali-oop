#Schreiben Sie ein Python-Programm, das eine Zahl vom Benutzer einliest und folgende Prüfungen durchführt:
#1. Falls die Zahl negativ ist → "Die Zahl ist negativ.“
#2. Falls die Zahl 0 ist → "Die Zahl ist null.“
#3. Falls die Zahl positiv und gerade ist → "Die Zahl ist positiv und gerade.“
#4. Falls die Zahl positiv und ungerade ist, dann:
    #(1) Falls die Zahl größer als 100 ist → "Die Zahl ist positiv, ungerade und größer als 100.“
    #(2) Ansonsten → "Die Zahl ist positiv und ungerade.“
#5. Bonus: Prüfen Sie, ob die Zahl eine Primzahl ist (s. https://de.wikipedia.org/wiki/
#Primzahl)! Falls ja, ergänzen Sie die Ausgabe um: "Zusätzlich ist die Zahl eine Primzahl!“

# Benutzereingabe:
#zahl1 = 5
#zahl2 = "5"
#print(type(zahl1), type(int(zahl2)))

zahl = int(input("Bitte geben Sie eine Zahl ein: "))
print("Typ der Zahl:", type(zahl))

# Variable zur Überprüfung, damit wir uns nicht wiederholen (Stichwort "DRY")
ist_gerade = zahl % 2 == 0
text_opener = "Die Zahl ist "

# Überprüfung (= Aufgabenstellung)
if zahl < 0:
    print(text_opener + "negativ.")
elif zahl == 0:
    print(text_opener + "null.")
else:
    if ist_gerade:
        print(text_opener + "positiv und gerade.")
    else:
        if zahl > 100:
            print(text_opener + "positiv, ungerade und größer als 100.")
        else:
            print(text_opener + "positiv und ungerade.")

# Bonus (Primzahlen):
def is_prime(zahl):
  for i in range(2, zahl):
    check = zahl%i
    print("Index:", i, "//", "Rest:", check)
    if (check) == 0:
      return False
  return True

if is_prime(zahl):
   print("Zusätzlich ist die Zahl eine Primzahl!")
