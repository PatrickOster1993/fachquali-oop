from magier import Magier
from schurke import Schurke
from waffe import Waffe
from gilde import Gilde
from kampfSzenario import kampf_szenario

# Anwendung
magier1 = Magier("Kyle", 125, 20, 10, 50, Waffe("Kleiner Zauberstab", 15, 100))
magier2 = Magier("Stan", 100, 10, 20, 75, Waffe("Großer Zauberstab", 20, 150))
magier3 = Magier("Kenny", 25, 25, 5, 50) # Kenny hat keine Waffe!
schurke1 = Schurke("Cartman", 150, 30, 15, 15, Waffe("Großer Dolch", 25, 75))
schurke2 = Schurke("Butters", 75, 20, 10, 5, Waffe("Kleiner Dolch", 15, 50))
print("###########################################")
magier1.checkStatus()
schurke1.checkStatus()
print("###########################################")
gilde1 = Gilde("Coon & Friends")
gilde1.hinzufuegen(magier1)
gilde1.hinzufuegen(magier2)
gilde1.hinzufuegen(magier3)
gilde1.hinzufuegen(schurke1)
gilde1.hinzufuegen(schurke2)
gilde1.anfuehrerBestimmen(schurke1)
print("###########################################")
gilde1.anzeigen()
print("###########################################")
kampf_szenario(magier1, schurke1) # Weil Kyle nicht mit Cartman als Anführer zufrieden ist :(
print("###########################################")
magier1.checkStatus()
schurke1.checkStatus()
print("###########################################")
print("Gleiche Charaktere? ", magier1 == schurke1)
print("###########################################")
klauen_des_Coons = Waffe("Blitzschnelle Klinge", 50, 200) + Waffe("Unsichtbare Klinge", 30, 100)
klauen_des_Coons.name = "Klauen des Coons"
schurke1.waffe = klauen_des_Coons
schurke1.checkStatus()
print("###########################################")
