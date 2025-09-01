#lade bibliotheken
import werkzeug.abstand as abstand
#für abstand
import werkzeug.loading as loading 
#für ladeanimation
import time 
#für Zeitverzögerung & visuell vereinfachte informationsaufnahme
import werkzeug.health_bar as health_bar 
#für health bar


###############################################
#Ticket 4 : Hauptmenü bauen
#Ticket 4a: welche Reiter sollen ins Hauptmenü
# 1 -> Ladesequenz starten
# 2 -> Fortschritt anzeigen
# 3 -> etwas anderes
###############################################





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
time.sleep(1)
#Ladeanimation



abstand.abstand()
print("Deine Reise beginnt jetzt...")
abstand.abstand()
time.sleep(1.6)


health_bar.health_bar() 
#health bar
#siehe werkzeug.health_bar


abstand.abstand()
print("Satz mit x")
abstand.abstand()




###########################
# Ticket 1: X in einer Liste speichern

import csv

def save_value(x, filename="dokumente/werte.csv"):
    with open(filename, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([x])

# Beispiel: Wert speichern
x = input("How to be alive and play the game? :  )  --->  : ")
save_value(x)
abstand.abstand()
print(f"Wert '{x}' wurde gespeichert.")
abstand.abstand()

###############################



######################################################
# Ticket 2: Ladeanimation skippen, wenn man x drückt
######################################################



#############################################################
#Ticket 3: Fortschrittsanzeige für 10 000 Stunden TimeQuest
#############################################################
