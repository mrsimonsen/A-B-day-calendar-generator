#https://docs.python.org/3/library/calendar.html
import calendar as c
import datetime as d

def string_to_date(user):
    out = user.split('/')
    for i in range(len(out)):
        out[i] = int(out[i])
    out = d.date(out[2],out[0],out[1])
    return out

def date_to_string(user):
    day = str(user.day)
    month = str(user.month)
    year = str(user.year)
    if len(day)==1:
        day = '0'+day
    if len(month)==1:
        month = '0'+month
    out = month+'/'+day+'/'+year
    return out

def int_to_day(num):
    days = ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday')
    return days[num]
