#https://docs.python.org/3/library/calendar.html
import calendar as c
import datetime as d
import file_maker

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

def make_A(date):
    date = date_to_string(date)
    file_maker.new_entry("A Day",date)
def make_B(date):
    date = date_to_string(date)
    file_maker.new_entry("B Day",date)

def format(gen, start, end,m):
    month = []
    for day in gen:
        if day < start or day > end:
            pass#it's not part of the school year
        elif day.month != m:
            pass#it's not in the current month
        elif day.weekday() in (5,6):
            pass#it's a weekend
        else:
            month.append(day)
    return month

def school_year(start,end):
    start = string_to_date(start)
    end = string_to_date(end)
    cal = c.Calendar(firstweekday=6)
    school_days = []
    date = start
    m = date.month
    y = date.year
    while date < end:
        gen = cal.itermonthdates(date.year, date.month)
        month = format(gen,start,end,m)
        school_days.append(month)
        m = date.month + 1
        if m == 13:
            m = 1
            y = date.year+1
        date = d.date(y,m,1)
    return school_days

def main(start,end):
    dates = file_maker.load_dates()
    final = []
    for i in dates:
        final.append(string_to_date(i['Start Date']))
    year = school_year(start,end)
    Aday = True
    for month in year:
        for day in month:
            if day in final:
                pass
            elif Aday:
                make_A(day)
                Aday = False
            else:
                make_B(day)
                Aday = True
