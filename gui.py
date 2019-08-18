#https://tkdocs.com/tutorial/
from  tkinter import *
from tkinter import ttk

class Application (Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.alld = ''
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.all_day = Checkbutton(self)
        self.all_day['text']='All day event'
        self.all_day['variable']=self.alld
        self.all_day['onvalue']='True'
        self.all_day['offvalue']='False'
        self.all_day['command']=self.test(self.alld)
        self.all_day.pack(side='top')

    def test(self,name):
        print(f'{name} clicked')



root = Tk()
root.title("AB Day Calendar Creator")
app = Application(master=root)
app.mainloop()
