import datetime as d

today = d.date.today()
bday = d.date(today.year,3,1)
if bday < today:
    bday = bday.replace(year = today.year + 1)
time_to = abs(bday - today)
print(time_to.days)
