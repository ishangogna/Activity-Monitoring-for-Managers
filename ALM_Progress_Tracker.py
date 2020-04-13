import time
from tkinter import *
import pandas
import filename
    
    
master = Tk()
master.title("Progress Tracker - v1.0 Developed by Ishan Gogna")
master.geometry("1200x500")
df = pandas.read_csv(filename)
pandas.set_option('display.max_rows', 500)
pandas.set_option('display.max_columns', 500)
pandas.set_option('display.width', 1000)
def populate():
    T1.insert(0.0,df)
def findDone():
    T2.insert(0.0,"{} days".format(df["TAT"].mean()))
    
    
T1 = Text(master, height=20, width=40)
B1 = Button(master, text='View All Tasks (Live Data)', width=25, command = populate)
B2 = Button(master, text='Generate Average TAT for Completed Tasks', width=25, command = findDone)
T2 = Text(master, height=5, width=5)
B1.pack(fill= X)
T1.pack(fill = X)
B2.pack(fill = X)
T2.pack(fill = X)
mainloop() 
