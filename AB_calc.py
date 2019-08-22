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

def school_year(start,end):
    start = string_to_date(start)
    end = string_to_date(end)
    cal = c.Calendar(firstweekday=6)
    days = []
    return days

def main():
    #reader = file_maker.load()
    print(school_year(start,end))
