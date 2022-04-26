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
"Und welches Datum ist heute?": now.strftime("%Y.%m.%d"),
"Und welches Datum ist morgen?": tomorrow.strftime("%Y.%m.%d"),
"und welches Datum war gestern?": yesterday.strftime("%Y.%m.%d"),
"Danke dir": "kein Probelm",
}

print(answers["Wie viel Uhr ist es?"])
print(answers["Und welches Datum ist heute?"])
print(answers["Und welches Datum ist morgen?"])
print(answers["und welches Datum war gestern?"])
print(answers["Danke dir"])

# Google hat ein Synonymsystem das ein Wort, auch wenn es mehrere Bedeutungen hat, fast immer das findet, was du suchst, da er mehrere Wörten zusammen setzten und verbinden kann. 
