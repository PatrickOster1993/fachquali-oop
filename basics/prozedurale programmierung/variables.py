# Numerisch
x = 1_000_000
y = 1
z = x + y

print("Ergebnis z =", z)

hex_zahl = 0x1
print("Hexadezimal:", hex(hex_zahl))

oct_zahl = 0o1
print("Oktalzahl:", oct(oct_zahl))

bin_zahl = 0b1011
print("Binärzahl:", bin(bin_zahl))

dez_zahl = 11
print("Binärzahl aus Dezimalzahl:", bin(dez_zahl))

print("#################")
# String
name = "Patrick"
print(len(str(3)))

# Typen-Check
x = None
print("Typ:", type(None))
手动阀 = 3

print(手动阀)

# ID checken
i = 3
n = 5
print(id(i), id(n))

# Logische Operatoren (binär)
# &   |   ^

# 1110 1001
# &
# 1101 1011
# ---------
# 1100 1001

binary_one = 0b101
binary_two = 0b111

x = 4
y = 3
z = x & y


# 0b101
# &
# 0b111
# -----
# 0b101

print("Dez. Lösung:", z)

binary_result = binary_one & binary_two

print("Lösung:", binary_result)

# == != < > <= >=

# Bedingungen

a = True
b = False
c = 3
d = 5
e = 3

if a:
    print("1. If-Statement wahr!")
elif a:
    print("elif wahr!")
else:
    print("1. If-Statement falsch!")

if c != 3:
    print("2. if-Statement wahr!")
    
else:
    print("2. If-Statement falsch!")


# Shift-Operator

zahl1 = 0b1001

zahl2 = zahl1 << 1

# 0000 0111
# 0000 0100
# &
# 0000 0100 >> 1

print("Zahl 1:", bin(zahl1))
print("Zahl 2:", bin(zahl2))

# Python-Konvention / -Spezifisches:

## Variablenbezeichnungen (prozedural)
test = 3
my_variable = 5

## Konstanten (gibt es nicht wirklich, aber Konvention!)
PI = 3.14
SSH_KEY = "SLDFJSLKFJKLSDFJL"

## mehrere Variablen in einer Zeile deklarieren

x, y = 3, 5
print("Mehrere Variablen in 1 Zeile deklariert:", x, y)

## Simple Verwendung für dieses sog. "Ideom"

x, y = y, x
print("Zahlen vertauscht:", x, y)







