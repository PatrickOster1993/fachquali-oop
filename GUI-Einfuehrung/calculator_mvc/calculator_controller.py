class CalculatorController:
    def __init__(self, model):
        """
        Initialisiert den Controller mit einem Model.
        """
        self.model = model
        self.view = None  # Wird später gesetzt
    
    def set_view(self, view):
        """
        Setzt die View-Komponente.
        """
        self.view = view
    
    def handle_button_click(self, button_text):
        """
        Verarbeitet Tastendrücke und aktualisiert Model und View.
        """
        if button_text == 'C':
            # Löscht die aktuelle Eingabe
            result = self.model.clear_input()
        elif button_text == '=':
            # Berechnet das Ergebnis
            result = self.model.calculate_result()
        else:
            # Fügt die Tasteneingabe zur aktuellen Eingabe hinzu
            result = self.model.append_input(button_text)
        
        # Aktualisiert die Anzeige in der View
        if self.view:
            self.view.update_display(result)