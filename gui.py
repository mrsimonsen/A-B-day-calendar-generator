#https://tkdocs.com/tutorial/
from  tkinter import *
from tkinter import ttk
from tkinter import messagebox
import file_maker
import AB_calc

file_maker.default()

def add(*args):
    if sub.get() == '' or sd.get() == '':
        messagebox.showinfo(message='Subject and Start Date are required!', title="Error!")
    elif '/' not in sd.get() or len(sd.get())!=10:
        messagebox.showinfo(message='Date Format must be MM/DD/YYYY', title="Error!")
    elif ('/' not in ed.get() or len(ed.get())!=10) and ed.get() != '':
        messagebox.showinfo(message='Date Format must be MM/DD/YYYY', title="Error!")
    elif (':' not in st.get() or len(st.get())!=5) and st.get() != '':
        messagebox.showinfo(message='Time Format must be HH:MM', title="Error!")
    elif (':' not in et.get() or len(et.get())!=5) and et.get() != '':
        messagebox.showinfo(message='Time Format must be HH:MM', title="Error!")
    else:
        file_maker.new_entry(sub.get(),sd.get(),st.get(),ed.get(),et.get(),alld.get())

def start_end(*args):
    if start.get() == '' or end.get() == '':
        messagebox.showinfo(message='Start Date and End Date are required!', title="Error!")
    elif '/' not in start.get() or len(start.get())!=10:
        messagebox.showinfo(message='Start Date Format must be MM/DD/YYYY', title="Error!")
    elif '/' not in end.get() or len(end.get())!=10:
        messagebox.showinfo(message='End Date Format must be MM/DD/YYYY', title="Error!")
    else:
        AB_calc.main(start.get(),end.get())
        messagebox.showinfo(message='AB_days.csv created!',title="Complete")
        root.destroy()


def AB(*args):
    user = messagebox.askyesno(message="Have you entered in all Holidays and Special Schedule days?", title="Are you sure?", icon='question')
    if user:
        t = Toplevel(mainframe)
        t.title('Start and End Dates')

        ttk.Label(t,text="Please set the First and Last days of School using the MM/DD/YYYY format").grid(column=1, row=1,columnspan = 2)

        ttk.Label(t, text="First Day of School:").grid(column=1,row=2,sticky=W)
        ttk.Entry(t, width = 10, textvariable=start).grid(column=2, row=2, sticky =(W,E))

        ttk.Label(t, text="Last Day of School:").grid(column=1,row=3,sticky=W)
        ttk.Entry(t,width=10,textvariable=end).grid(column=2,row=3,sticky= (W,E))

        ttk.Button(t,text="Calculate",command=start_end).grid(column=1,row=4,columnspan=2)

root = Tk()
root.title("NUAMES Calendar Creator")
mainframe = ttk.Frame(root,padding="3 3 12 12")
mainframe.grid(column=0,row=0,sticky=(N,W,E,S))
root.columnconfigure(0,weight=1)
root.rowconfigure(0,weight=1)

sub = StringVar()#subject
sd = StringVar()#start date
st = StringVar()#start time, optional
st_ampm = StringVar()#am/pm start time
ed = StringVar()#end date, optional
et = StringVar()#end time, optional
et_ampm = StringVar()#am/pm end time
alld = StringVar()#all day event?
start = StringVar()#first day of school
end = StringVar()#last day of school

ttk.Label(mainframe, text="Event Subject:").grid(column=1,row=1,sticky=W)
ttk.Entry(mainframe, width = 25, textvariable=sub).grid(column=2, row=1, columnspan=4,sticky =(W,E))

ttk.Label(mainframe, text="Start Date:\nMM/DD/YYYY").grid(column=1,row=2,sticky=W)
ttk.Entry(mainframe, width = 10, textvariable=sd).grid(column=2, row=2, sticky =(W,E))

ttk.Label(mainframe, text="Start Time:\nHH:MM\n(Optional)").grid(column=3,row=2, sticky=W)
ttk.Entry(mainframe, width = 5, textvariable=st).grid(column=4, row=2, sticky =(W,E))
x = ttk.Radiobutton(mainframe, text='AM', variable=st_ampm, value='AM')
x.invoke()
x.grid(column=5,row=2,sticky=(S,W))
ttk.Radiobutton(mainframe, text='PM', variable=st_ampm, value='PM').grid(column=5,row=3,sticky=(N,W))

ttk.Label(mainframe, text="End Date:\nMM/DD/YYYY\n(Optional)").grid(column=1,row=4, sticky=W)
ttk.Entry(mainframe, width = 10, textvariable=ed).grid(column=2, row=4, sticky =(W,E))

ttk.Label(mainframe, text="End Time:\nHH:MM\n(Optional)").grid(column=3,row=4, sticky=W)
ttk.Entry(mainframe, width = 5, textvariable=et).grid(column=4, row=4, sticky =(W,E))
x = ttk.Radiobutton(mainframe, text='AM', variable=et_ampm, value='AM')
x.invoke()
x.grid(column=5,row=4,sticky=(W,S))
del x
ttk.Radiobutton(mainframe, text='PM', variable=et_ampm, value='PM').grid(column=5,row=5,sticky=(N,W))

alld_yes = ttk.Radiobutton(mainframe, text='All Day Event', variable=alld, value='True')
alld_yes.grid(column=1,row=7,sticky=(W,S))
alld_yes.invoke()
alld_no = ttk.Radiobutton(mainframe, text='Not All Day Event', variable=alld, value='False')
alld_no.grid(column=1,row=8,sticky=(N,W))

ttk.Button(mainframe,text="Add Event", command=add).grid(column=2, row=7, rowspan=2, sticky=W)

ttk.Button(mainframe, text="Generate A/B days", command=AB).grid(column=3, row=7, rowspan=2, sticky=W)

root.bind('<Return>',add)

root.mainloop()
