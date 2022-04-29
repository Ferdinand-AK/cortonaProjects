# Bezeichnung           Abkürzung                      Bedeutung                                                               Beispiel
# integer                 int                          ganze Zahl                                                              3
# float                   ?float?                      Fließkommazahl                                                          3.1
# string                  str                          Zeichenkette                                                            "Äpfel, Birnen" 
# boolean                 bool                         boolesche Werte (Wahrheitswerte)                                        True oder False
# list                    list                         Liste                                                                   ["Äpfel","Birnen"]
# tuple                   tuple                        Tupel (Elemente nicht veränderbar)                                      ('Äpfel','Birnen')

import sys

Text = input()

def istFloatZahl(textNummer):
    countComma = 0
    for c in textNummer:
        if not c.isdigit():
            if c == "." or c == ",":
                countComma += 1
            else:
                return False

    if countComma > 0:
        return True
    else:
        return False

def istNatuerlicheZahl(textNummer):
    for z in textNummer:
        if not z.isdigit():
            return False
    return True

def istListe(text):
    if text[0] == "[" and text[-1] == "]":
        return True
    return False

def istTuple(text):
    if text[0] == "(" and text[-1] == ")":
        return True
    return False
    
def istBoolean(text):
    if text in ["true", "True", "Wahr", "wahr", "False", "false", "Falsch", "falsch"]:
        return True
    return False


if istNatuerlicheZahl(Text):
    print("Ich bin eine natürliche Zahl")
elif istFloatZahl(Text):
    print("Ich bin eine float Zahl")
elif istTuple(Text):
    print("Ich bin ein tuple")
elif istListe(Text):
    print("Ich bin eine liste")
elif istBoolean(Text):
    print("Ich bin ein boolean")
else:
    print("Ich bin ein text")
