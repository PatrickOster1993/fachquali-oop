get_fahrenheit_by_celsius = lambda celsius: 1.8 * celsius + 32

# Alternative:
# def get_fahrenheit_by_celsius(celsius):
    # return (1.8 * celsius + 32)

try:
    celsius = float(input("Bitte geben Sie die Temperatur in Celsius ein: "))
    fahrenheit = get_fahrenheit_by_celsius(celsius)

    print(f"Die Temperatur von {celsius}°C entspricht {fahrenheit:.2f}°F.")

except ValueError:
    print("Fehler: Bitte geben Sie eine gültige Zahl ein.")
    
except Exception as e:
    print(f"Ein unerwarteter Fehler ist aufgetreten: {e}")