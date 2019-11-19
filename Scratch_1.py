import os
import pandas as pd
import tkinter as tk
import xlwt 
import PySimpleGUI27 as sg

#___________________________
# Retrieve current working directory (`cwd`)
#cwd = os.getcwd()

# Change directory 
#os.chdir("/Users/riccardosaglio/Desktop/Py_")

# List all files and directories in current directory
#os.listdir('.')
#_________________________________

#master=tk.Tk()
#tk.Label(master, text=" finestra 1").grid(row=0)
#tk.Label(master, text=" finestra 2").grid(row=1)

#e1=tk.Entry(master)
#e2=tk.Entry(master)

#e1.grid(row=0, column=1)
#e2.grid(row=1, column=1)

#master.mainloop()
# continue from https://www.python-course.eu/tkinter_entry_widgets.php
#_______________________________________
# GUI 
layout = [      
          [sg.Text('Insert Company Name, name of the job, link')],      
          [sg.Text('Company Name', size=(15, 1)), sg.InputText('name')],      
          [sg.Text('Name of the job', size=(15, 1)), sg.InputText('address')],      
          [sg.Text('link', size=(15, 1)), sg.InputText('phone')],      
          [sg.Submit(), sg.Cancel()]      
         ]

window = sg.Window('Job Apllications').Layout(layout)         
button, values = window.Read()

print(button, values[0], values[1], values[2])

#__________________________
#workbook = xlwt.Workbook()
#sheet = workbook.add_sheet("Sheet Name")
