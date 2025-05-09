import sys
import os

# Stelle sicher, dass das Hauptverzeichnis im Python-Pfad ist
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.append(project_root)

from PyQt5.QtWidgets import QApplication
from controller.main_controller import MainController
from model.logger_service import LoggerService

def main():
    # Konfiguriere Logging
    log_dir = os.path.join(project_root, "logs")
    os.makedirs(log_dir, exist_ok=True)
    log_file = os.path.join(log_dir, "wawi.log")
    
    LoggerService.configure(log_file=log_file)
    logger = LoggerService.get_logger('Main')
    
    try:
        logger.info("Starting application...")
        
        # Erstelle Qt-Anwendung
        app = QApplication(sys.argv)
        
        # Erstelle Hauptcontroller
        controller = MainController()
        
        # Starte Anwendung
        controller.start()
        
        # Ausführen der Ereignisschleife
        return_code = app.exec_()
        
        logger.info(f"Application exited with code {return_code}")
        return return_code
        
    except Exception as e:
        logger.error(f"Unhandled exception: {e}", exc_info=True)
        return 1

if __name__ == "__main__":
    sys.exit(main())