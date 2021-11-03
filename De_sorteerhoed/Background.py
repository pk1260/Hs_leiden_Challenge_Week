
from tkinter import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
# Create object
root = Tk()
root.geometry('500x600')
root.resizable(True, True)
root.title('Iemand van de belasting komt aan de deur want je hebt geen belasting betaald Wat zou jij doen ?')
# Adjust size
root.geometry("400x400")


img= (Image.open("image/Hogwarts.jpg"))
resized_image= img.resize((450,505), Image.ANTIALIAS)
Background= ImageTk.PhotoImage(resized_image)
# Add image file

Button_background= (Image.open("tiemo.png"))
#RESIZE FOTO
resized_image= Button_background.resize((200,105), Image.ANTIALIAS)
Foto= ImageTk.PhotoImage(resized_image)
# Show image using label
label1 = Label(root, image=Background)
label1.place(x=0, y=0)

label2 = Label(root, text="Welcome")
label2.pack(pady=10)

# Create Frame
frame1 = Frame(root)
frame1.pack(pady=10)



# Add buttons
button1 = Button(frame1, text="Exit", foreground = "red" , font = ("arial", 20, "bold"))
button1.pack(pady=0)

button2 = Button(frame1, text="Start",image=Foto )
button2.pack(pady=0)


button3 = Button(frame1, text="Reset")
button3.pack(pady=0)

# Execute tkinter
root.mainloop()