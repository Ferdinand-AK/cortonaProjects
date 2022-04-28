# Bezeichnung           Abkürzung                      Bedeutung                                                               Beispiel
# integer                 int                          ganze Zahl                                                              3
# float                   ?float?                      Fließkommazahl                                                          3.1
# string                  str                          Zeichenkette                                                            "Äpfel, Birnen" 
# boolean                 bool                         boolesche Werte (Wahrheitswerte)                                        True oder False
# list                    list                         Liste                                                                   ["Äpfel","Birnen"]
# tuple                   tuple                        Tupel (Elemente nicht veränderbar)                                      ('Äpfel','Birnen')

import sys


def istFloatZahl(textNummer):
    countComma = 0
    for c in textNummer:
        if not c.isdigit():
            if c == "." or c == ",":
                countComma += 1
            else:
                return False
            
    if countComma == 1:
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



Text = input()

if istNatuerlicheZahl(Text):
    print("ich bin eine natürliche Zahl")
elif istFloatZahl(Text):
    print("ich bin eine float Zahl")
elif istTuple(Text):
    print("ich bin ein tuple")
elif istListe(Text):
    print("ich bin eine liste")
elif istBoolean(Text):
    print("ich bin ein boolean")
else:
    print("ich bin ein text")

    # if Text[0] == "[": #list
    #     print("list") #list
    # elif Text[0] == "'": #tuple
    #     print("tuple") #tuple
    # elif str(Text):
    #     it_is = True
    #     print("string")
