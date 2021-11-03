from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
root = Tk()
root.geometry('400x300')
root.resizable(True, True)
root.title('Iemand van de belasting komt aan de deur want je hebt geen belasting betaald Wat zou jij doen ?')

def download_clicked():
    showinfo(
        title='Information',
        message='Download button clicked!'
    )



#FOTO GEDEELTE SUCCES
img= (Image.open("tiemo.png"))
#RESIZE FOTO
resized_image= img.resize((300,205), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)
#Creëer Foto
download_button = ttk.Button(
    root,
    image=new_image,
    compound=tk.LEFT,
    command=download_clicked
)
#geen idee
download_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

#einde
root.mainloop()
