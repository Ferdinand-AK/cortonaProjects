from datetime import datetime
print("Ich kann die Tage in einem beliebigen Jahr ausrechnen. Frage mich eine Zahl ab!")

def getDaysOfYear(year):
    startOfYear = datetime(year,1,1,0,0)
    endOfYear= datetime(year+1,1,1,0,0)
    return (endOfYear - startOfYear).days

searchYear = input()
searchYearNum = int(searchYear)

print("Du hast mich das Jahr " + (searchYear) + " abgefragt. Hier ist deine Antwort.")
tage = getDaysOfYear(searchYearNum)
print(tage)
print("Ich habs dir doch gesagt, dass ich die Tage in einem beliebigen Jahr ausrechnen kann.")
