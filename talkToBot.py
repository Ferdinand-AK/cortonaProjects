#!/usr/bin/python

# TODO:
# 1. bot antwortet auf verschiedene vorgegeben Fragen => erledigt
# 2. Bot antwortet auf komplexere Fragen: wie spät ist es? zum Beispiel ... => erledigt
# 3. rescherchiere wie und ob man auch Fragen über google gelöst werden können => noch zu bearbeiten


#answers = {
 # "Hallo": "Guten Tag",
 # "Wie heißen sie": "Das geht sie nichts an",
 # "Hmm schade. Können sie mir helfen?": "Nagut",
 # "Danke für ihre Hilfe": "Bitteschön",
 # "Auf Wiedersehen": "Tschüss"
#}


#print(answers["Hallo"])
#print(answers["Wie heißen sie"])
#print(answers["Hmm schade. Können sie mir helfen?"])
#print(answers["Danke für ihre Hilfe"])
#print(answers["Auf Wiedersehen"])

from datetime import datetime
from datetime import timedelta

now = datetime.now()
tomorrow = datetime.now() + timedelta(days=1)
yesterday = datetime.now() - timedelta(days=1)

answers = {
  "Wie viel Uhr ist es?": now.strftime("%H:%M:%S"),
  "Und welches Datum ist heute?": now.strftime("%d.%m.%Y"),
  "Und welches Datum ist morgen?": tomorrow.strftime("%d.%m.%Y"),
  "und welches Datum war gestern?": yesterday.strftime("%d.%m.%Y"),
  "Danke dir": "Kein Problem",
}

# print(answers["Wie viel Uhr ist es?"])
# print(answers["Und welches Datum ist heute?"])
# print(answers["Und welches Datum ist morgen?"])
# print(answers["und welches Datum war gestern?"])
# print(answers["Danke dir"])

# Google hat ein Synonymsystem das ein Wort, auch wenn es mehrere Bedeutungen hat, fast immer das findet, was du suchst, da er mehrere Wörten zusammen setzten und verbinden kann. 


# Etwas erweitert:
print("#####################################################")
print("#                   Talk to me                      #")
print("#####################################################")
print("Bot: Hallo ich bin Bot'ty und ich kann auf deine Fragen oder anmerkungen reagieren. Schreibe etwas in das Terminal und drücke auf Enter.")
print("Bot: Wenn du nicht mit mir sprechen willst, dann schreibe einfach 'tschüß'.")
while True:
    say = input("You: ").strip()

    if say in answers:
      answer = answers[say]
      print("Bot: " + answer)

    elif say in ["q", "", "quit", "exit", "end", "tschüß"]:
        print("Tschüß")
        break
    else:
      found = False

      # Versuche alternative Fragen zu finden.
      for q in answers:
        splitQuestion = say.replace(',', ' ').replace('.', ' ').replace('?', ' ').split(" ")
        if any(word in q for word in splitQuestion) and input("Bot: Meinst du: '" + q + "' ? (y/n) ") == "y":
          print("Bot: " + answers[q])
          found = True
          break

      if not found:
        print("Bot: Ich habe deine Aussage nicht verstanden, kannst du es anders fomulieren?")

print("Bot: Schade dass du schon los musst.")
