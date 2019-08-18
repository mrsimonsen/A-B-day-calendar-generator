#https://docs.python.org/3/library/csv.html?highlight=csv
import csv

def default():
    #https://support.google.com/calendar/answer/37118?hl=en
    with open("AB_days.csv", "w", newline='') as csvfile:
        w = csv.writer(csvfile, delimiter= ",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
        w.writerow(['Subject','Start Date','Start Time','End Date','End Time','All Day Event'])

def new_entry(sub, sd, st, ed, et, alld=True):
    with open ("AB_days.csv", "a", newline='') as f:
        w = csv.writer(f, delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
        w.writerow([sub,sd,st,ed,et,alld])
