class CalculatorModel:
    def __init__(self):
        """
        Initialisiert das Model mit Standardwerten.
        """
        self.current_input = ""  # Aktuelle Eingabe als Zeichenkette
        self.last_result = 0     # Letztes berechnetes Ergebnis
    
    def append_input(self, value):
        """
        Fügt einen Wert zur aktuellen Eingabe hinzu.
        """
        self.current_input += value
        return self.current_input
    
    def clear_input(self):
        """
        Löscht die aktuelle Eingabe.
        """
        self.current_input = ""
        return self.current_input
    
    def calculate_result(self):
        """
        Berechnet das Ergebnis des aktuellen Ausdrucks.
        """
        try:
            # Hinweis: In professionellen Anwendungen würde man
            # einen sicheren Parser statt eval() verwenden!
            self.last_result = eval(self.current_input)
            self.current_input = str(self.last_result)
            return self.current_input
        except Exception as e:
            # Bei Fehlern geben wir eine Fehlermeldung zurück
            return "Error"
    
    def get_current_input(self):
        """
        Gibt die aktuelle Eingabe zurück.
        """
        return self.current_input