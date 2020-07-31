from venv import code_ML
import tkinter as tk
from PIL import Image,ImageTk


gui = tk.Tk()

img = Image.open("E:\\BIG DATA PROJECT\Breast/venv/3.jpg")
img = img.resize((1080, 720), Image.ANTIALIAS)

background = ImageTk.PhotoImage(img)

gui.title("Breast cancer detection")
gui.geometry("1080x720")

label = tk.Label(gui, height=720, width=1080, image=background)
label.place(x=0, y=0)

message = tk.Message(label, text="CANCER DETECTION APPLICATION", fg="green", width=700, padx=200, pady=20)
message.place(x=200, y=20)

entry1 = tk.Entry(gui)
entry1.place(x = 500,y = 200)
message1 = tk.Message(label, text="Clump Thickness", fg="green", width=100, padx=1, pady=1)
message1.place(x=390, y=200)

entry2 = tk.Entry(gui)
entry2.place(x = 500,y = 250)
message2 = tk.Message(label, text="Unit Cell Size", fg="green", width=100, padx=1, pady=1)
message2.place(x=390, y=250)

entry3 = tk.Entry(gui)
entry3.place(x = 500,y = 300)
message3 = tk.Message(label, text="Unit Cell Shape", fg="green", width=100, padx=1, pady=1)
message3.place(x=390, y=300)

entry4 = tk.Entry(gui)
entry4.place(x = 500,y = 350)
message4 = tk.Message(label, text="Marg Adhesion", fg="green", width=100, padx=1, pady=1)
message4.place(x=390, y=350)

entry5 = tk.Entry(gui)
entry5.place(x = 500,y = 400)
message5 = tk.Message(label, text="Single epith Cell Size", fg="green", width=100, padx=1, pady=1)
message5.place(x=390, y=400)

entry6 = tk.Entry(gui)
entry6.place(x = 500,y = 450)
message6 = tk.Message(label, text="Bare Nuclei", fg="green", width=100, padx=1, pady=1)
message6.place(x=390, y=450)

entry7 = tk.Entry(gui)
entry7.place(x = 500,y = 500)
message7 = tk.Message(label, text="Bland Chrom", fg="green", width=100, padx=1, pady=1)
message7.place(x=390, y=500)

entry8 = tk.Entry(gui)
entry8.place(x = 500,y =550)
message8 = tk.Message(label, text="Norm Nucleoli", fg="green", width=100, padx=1, pady=1)
message8.place(x=390, y=550)

entry9 = tk.Entry(gui)
entry9.place(x = 500,y = 600)
message9 = tk.Message(label, text="Mitoses", fg="green", width=100, padx=1, pady=1)
message9.place(x=390, y=600)

Button = tk.Button(gui,text = "Submit", height=2, width=15,command=Append(), relief=tk.RAISED, bd=4, bg="skyblue")
Button.place(x=450,y=650)

def Append():
    arr.append(entry1.get())
    arr.append(entry2.get())
    arr.append(entry3.get())
    arr.append(entry4.get())
    arr.append(entry5.get())
    arr.append(entry6.get())
    arr.append(entry7.get())
    arr.append(entry8.get())
    arr.append(entry9.get())


gui.mainloop()