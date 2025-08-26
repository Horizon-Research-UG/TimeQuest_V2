import time
try:
    import werkzeug.abstand as abstand
except ModuleNotFoundError:
    import abstand
import msvcrt

def loading():
    abstand.abstand()
    print("(Drücke eine Taste zum Überspringen)")
    abstand.abstand()
    time.sleep(1.6)
    while True:

        s = "loading............"
        for _ in range(12):
            s = s[:-1]  # entfernt das letzte Zeichen
            print(s) 
            time.sleep(0.05)  # wartet 0.05 Sekunden
        s2 = "loading"
        for _ in range(12):
            print(s2)
            s2 = s2 + "."
            time.sleep(0.05)  # wartet 0.05 Sekunden
        #abstand.abstand()
        #print("loading complete")
        #abstand.abstand()
        if msvcrt.kbhit():
            msvcrt.getch()
            print("\nLadeanimation übersprungen!")
            abstand.abstand()
            break


if __name__ == "__main__":
    loading()
