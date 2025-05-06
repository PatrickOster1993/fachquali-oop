try:
    print("Bitte geben Sie Ihren Text ein.")
    
    # Mehrzeilige Eingabe
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    original_text = ""
    for line in lines:
        original_text += line + "\n" # Zeilenumbruch für jede Zeile!
    
    modified_text = original_text.replace(".", "SNAKE_WAS_HERE")
    
    with open("snake.txt", "w", encoding="utf-8") as file:
        file.write(modified_text)
    
    print("Ihr Text wurde in 'snake.txt' gespeichert...")

except Exception as e:
    print(f"Ein Fehler ist aufgetreten: {e}")