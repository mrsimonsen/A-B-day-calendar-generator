#https://docs.python.org/3/library/csv.html?highlight=csv
import csv

FN = ['Subject','Start Date','Start Time','End Date','End Time','All Day Event']

def default():
    #https://support.google.com/calendar/answer/37118?hl=en
    with open("AB_days.csv", "w", newline='') as csvfile:
        w = csv.DictWriter(csvfile, fieldnames=FN)
        w.writeheader()

#date format is MM/DD/YYYY

def new_entry(sub, sd, st="", ed="", et="", alld=True):
    with open("AB_days.csv", "a", newline='') as f:
        w = csv.DictWriter(f, fieldnames=FN)
        w.writerow({'Subject':sub,'Start Date':sd,'Start Time':st,'End Date':ed,'End Time':et,'All Day Event':alld})

def load_dates():
    with open("AB_days.csv",'r',newline="") as f:
        r = csv.DictReader(f)
        dates = []
        for entry in r:
            dates.append(entry)
    return dates
