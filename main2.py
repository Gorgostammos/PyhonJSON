import json
import random

def last_sekk():
    try:
        with open("bibel.json", "r") as fil:
            return json.load(fil)
    except FileNotFoundError:
        return []

# Skriver tilbake til JSON-filen
def lagre_sekk(bible_vers):
    with open("bibel.json", "w") as fil:
        json.dump(bible_vers, fil)
# Hovedprogram
bible_vers = last_sekk()


print()
tilfeldig_ting = random.choice(bible_vers)
print(f"{tilfeldig_ting}")
