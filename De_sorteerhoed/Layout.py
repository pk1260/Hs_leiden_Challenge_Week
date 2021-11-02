# Importing Tkinter module
from tkinter import *
from tkinter.ttk import *
import openpyxl
  path = "Vragen.xlsx"
# Creating master Tkinter window
master = Tk()
master.geometry('175x175')



# Tkinter string variable
# able to store any string value
v = StringVar(master, "1")
 
# Style class to add style to Radiobutton
# it can be used to style any ttk widget
style = Style(master)
style.configure("TRadiobutton", background = "green",
                foreground = "red", font = ("arial", 10, "bold"))
 
# Dictionary to create multiple buttons

 wb_obj = openpyxl.load_workbook(path)
sheet_obj = wb_obj.active


cell_obj = sheet_obj.cell(row = 2, column = 2)
values = {cell_obj  : "1",
          "RadioButton 2" : "2",
          "RadioButton 3" : "3",
          "RadioButton 4" : "4",
          "RadioButton 5" : "5"}
 
# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(master, text = text, variable = v,
                value = value).pack(side = TOP, ipady = 5)
 
# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
mainloop()
