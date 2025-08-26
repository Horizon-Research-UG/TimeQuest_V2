import msvcrt
import time

def loading_animation():
    print("Ladeanimation läuft... (Drücke 'x' zum Überspringen)")
    while True:
        # Animation anzeigen (z.B. Punkt)
        print(".", end="", flush=True)
        time.sleep(0.5)
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == b'x':
                print("\nLadeanimation übersprungen!")
                break

# Beispiel-Aufruf
loading_animation()