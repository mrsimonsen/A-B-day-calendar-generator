from tkinter import *
from tkinter import ttk
from datetime import date

def calculate(*args):
    try:
        days.set(count(month.get(),day.get()))
    except ValueError:
        pass

def count(month, day):
    today = date.today()
    bday = date(today.year,int(month),int(day))
    if bday < today:
        bday = bday.replace(year = today.year + 1)
    time = abs(bday - today)
    return time.days

root = Tk()
root.title("Days to Birthday")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

month = StringVar()
day = StringVar()
days = StringVar()

month_entry = ttk.Entry(mainframe, width=4, textvariable=month)
month_entry.grid(column=1, row=1, sticky=(W,E))
day_entry = ttk.Entry(mainframe, width=4, textvariable=day)
day_entry.grid(column=3, row=1, sticky=(W,E))

ttk.Label(mainframe, textvariable=days).grid(column=1,row=2,stick=(W,E))
ttk.Button(mainframe,text='Calculate',command='calculate').grid(column=4,row=2,sticky=W)

ttk.Label(mainframe,text='Month').grid(column=2,  row=1, sticky=W)
ttk.Label(mainframe,text='Day').grid(column=4,row=1,sticky=W)
ttk.Label(mainframe,text="days till Birthday").grid(column=2,row=2,sticky=E)


for child in mainframe.winfo_children(): child.grid_configure(padx=5,pady=5)

month_entry.focus()
root.bind('<Return>',calculate)

root.mainloop()
