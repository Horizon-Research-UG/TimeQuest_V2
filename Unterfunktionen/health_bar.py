# Funktion zur Anzeige eines Gesundheitsbalkens
# Start Kapazität: 100%
# geht jede Minute um 1% runter

import time

def health_bar():
    health = 100
    while health >= 0:
        bar = "|" * (health // 2)  # 50 Zeichen bei 100%
        print(f"Health: [{bar:<50}] {health}%")
        time.sleep(0.01)  # 1 Sekunde warten
        health -= 1

if __name__ == "__main__":
    health_bar()