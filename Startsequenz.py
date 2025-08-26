#lade bibliotheken
import werkzeug.abstand as abstand 
#für abstand
import werkzeug.loading as loading 
#für ladeanimation
import time 
#für Zeitverzögerung & visuell vereinfachte informationsaufnahme
import werkzeug.health_bar as health_bar 
#für health bar


#################
#einstiegssequenz
#################

abstand.abstand() 
#abstand
print("--- >  Herzlich Willkommen zu TimeQuest!  <---")
#drucken
abstand.abstand() 
#abstand
time.sleep(1) 
#warte 1 sekunde
loading.loading() 
#Ladeanimation

health_bar.health_bar() 
#health bar
#siehe werkzeug.health_bar


###########################
x = input("Wie kann ich wieder leben? ")
###########################
# Ticket 1: X in einer Liste speichern

import csv

def save_value(x, filename="dokumente/werte.csv"):
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([x])

# Beispiel: Wert speichern
x = input("Gib einen Wert ein: ")
save_value(x)

#append