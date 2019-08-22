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

def format(month):
    for i in month:
        #remove weekends, return back
        #remove days that are not within the start and end dates
        pass
    return month

def school_year(start,end):
    start = string_to_date(start)
    end = string_to_date(end)
    c.setfirstweeday(6)
    school_days = []
    date = start
    while date < end:
        month = calendar.monthdatescalendar(date.year, date.year)
        month = format(month)
        school_days.append(month)
        date.month += 1
        if date.month == 13:
            date.month = 1
            date.year +=1

    return school_days

def main(start,end):
    #reader = file_maker.load()
    print(school_year(start,end))
