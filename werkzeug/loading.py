import time
import werkzeug.abstand as abstand

def loading():
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
    abstand.abstand()
    print("loading complete")
    abstand.abstand()


if __name__ == "__main__":
    loading()
