import json
import random


def last_sekk():
    try:
        with open("sekken.json", "r") as fil:
            return json.load(fil)
    except FileNotFoundError:
        return []

# Skriver tilbake til JSON-filen
def lagre_sekk(sekken):
    with open("sekken.json", "w") as fil:
        json.dump(sekken, fil)
# Hovedprogram
sekken = last_sekk()



print("Hei på deg, hvordan har du det")
print()
print("din nåvarende sekk har:")
for ting in sekken:
    print(ting)


print()
inter = input("trykk på intter")
print()
print()

while True:
    print("\nSekken din inneholder nå:")
    if sekken:
        for ting in sekken:
            print(f"- {sekken}")
    else:
        print("Sekken er tom ")

    print("\nHva vil du gjøre?")
    print("1: Legge til noe i sekken")
    print("2: Fjerne noe fra sekken")
    print("3: Avslutt")

    valg = input("Skriv inn valget ditt (1/2/3): ")

    if valg == "1":
        ny_ting = input("Hva vil du legge til? ")
        sekken.append(ny_ting)
        lagre_sekk(sekken)
        print(f"La til '{ny_ting}' i sekken.")

    elif valg == "2":
        fjern_ting = input("Hva vil du fjerne? ")
        if fjern_ting in sekken:
            sekken.remove(fjern_ting)
            lagre_sekk(sekken)
            print(f"🗑 Fjernet '{fjern_ting}' fra sekken.")
        else:
            print(f" '{fjern_ting}' finnes ikke i sekken.")

    elif valg == "3":
        print("Avslutter... Ha en velsignet dag!")
        break

    else:
        print("Ugyldig valg. Prøv igjen.")




