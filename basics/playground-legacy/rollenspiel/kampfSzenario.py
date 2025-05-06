# Teil 2: Polymorphismus und Method Override
def kampf_szenario(charakter1, charakter2):
    while charakter1.lebenspunkte > 0 and charakter2.lebenspunkte > 0:
        charakter1.angreifen(charakter2)
        if charakter2.lebenspunkte <= 0:
            print(f"{charakter2.name} wurde besiegt!")
            break
        charakter2.angreifen(charakter1)
        if charakter1.lebenspunkte <= 0:
            print(f"{charakter1.name} wurde besiegt!")