from datetime import datetime


def getDaysOfYear(year):
    startOfYear = datetime(year,1,1,0,0)
    endOfYear= datetime(year+1,1,1,0,0)
    return (endOfYear - startOfYear).days

count = 0
while True:
    if count == 0:
        print("Ich kann die Tage in einem beliebigen Jahr ausrechnen. Frage mich eine Zahl ab!")
    elif count == 5:
        print("Du bist ja immernoch dabei. Toll, mach weiter")
    elif count == 10:
        print("Nur noch 5 bis zur Belohnung. Mach weiter, nur ein wenig weiter.")
    elif count == 15:
        print("Herzlichen Glückwunsch, du hast absolut nichts gewonnen =).")
        break
    else:
        print("Nenne mir ein neues Jahr.")
    count += 1

    searchYear = input().strip()
    searchYearNum = int(searchYear)

    print("Du hast mich das Jahr " + (searchYear) + " abgefragt. Hier ist deine Antwort.")
    tage = getDaysOfYear(searchYearNum)
    print(tage)
    print("Ich habs dir doch gesagt, dass ich die Tage in einem beliebigen Jahr ausrechnen kann. Willst du nochmal die Tage eines beliebigen Jahr ausrechnen?")

    x = input().strip()
    if x in ["nein", "", "n", "no", "ne", "nee"]:
        print("Ok schade, bis zum nächsten mal.")
        break
    print("Ok, dann nochmal.")
