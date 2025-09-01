#lade bibliotheken
import werkzeug.abstand as abstand
#für abstand
import werkzeug.loading as loading 
#für ladeanimation
import time 
#für Zeitverzögerung & visuell vereinfachte informationsaufnahme
import werkzeug.health_bar as health_bar 
#für health bar

##########################################
print("--->   Hauptnemü   <---")
a1()
while True:
    try:
        print("1 (Ladesequenz)")
        print("2 (Fortschritt anzeigen)")
        abstand.abstand1()
        if input("Eingabe = ") == "1":
            print("Erfolg")
        else:
            print("Erfolg 2")
    except Error:
        pass
##########################################