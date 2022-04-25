from datetime import datetime

now = datetime.now()

endOfWorkDay = now.replace(hour=17, minute=0, second=0, microsecond=0)
endOfPraktikum = datetime(2022,4,29,17,0)

todayWoringkHours = endOfWorkDay.hour - now.hour -1
todayWoringkMinutes = 60 - now.minute

diffDays = endOfPraktikum.day - now.day 
restDaysWorkingHours = diffDays * 8

totalworkingHours = todayWoringkHours + restDaysWorkingHours
strTotalworkingHours = str(totalworkingHours)

print("Willkommen zum Praktikum Philipp.")
print("Du hast noch " + strTotalworkingHours + " Stunden und " + str(todayWoringkMinutes) + " Minuten zu arbeiten.")
