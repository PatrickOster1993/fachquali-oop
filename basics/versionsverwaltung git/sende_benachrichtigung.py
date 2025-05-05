from versionsverwaltung.XY import prüfe_antragsvoraussetzungen

def sende_benachrichtigung(wartezeit):
    antragsvoraussetzung_erfüllt = prüfe_antragsvoraussetzungen()
    email_text = f"Guten Tag, Ihr Personalausweis ist beantragt. Die derzeitige Wartezeit beträgt: {wartezeit}."

