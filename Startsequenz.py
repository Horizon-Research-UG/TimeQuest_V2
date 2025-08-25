import Unterfunktionen.abstand as abstand
import Unterfunktionen.loading as loading
import time
import Unterfunktionen.health_bar

abstand.abstand()
print("--- >  Herzlich Willkommen zu TimeQuest!  <---")
abstand.abstand()
time.sleep(1)
loading.loading()

Unterfunktionen.health_bar.health_bar()