import random
zufallszahl = random.randint(1,100)
ratezahl = 0
counter = 0
while ratezahl != zufallszahl:
    ratezahl = int(input("Rate die Zahl:"))
    counter += 1
    if ratezahl > zufallszahl:
        print(ratezahl,"ist zu groß.")
    elif ratezahl < zufallszahl:
        print(ratezahl,"ist zu klein.")
print("Glückwunsch,",zufallszahl,"ist die richtige Zahl! Zähler:", counter)
