# Importing the libraries

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score

# Importing the dataset

df = pd.read_csv('cancer.csv')
df.replace('?', -99999, inplace=True)
df.drop(['id'], 1, inplace=True)

X = np.array(df.drop(['classes'], 1))
y = np.array(df['classes'])

# Splitting the dataset into the Training set and Test set

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

# Feature Scaling

from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting KNN to the Training set

from sklearn.neighbors import KNeighborsClassifier


classifier = KNeighborsClassifier(n_neighbors=3)
trained_model = classifier.fit(X_train, y_train)
trained_model.fit(X_train, y_train)

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
arr = [[]]
print(entry1.get())
def Append():
    arr[0].append(int(float(entry1.get())))
    arr[0].append(int(float(entry2.get())))
    arr[0].append(int(float(entry3.get())))
    arr[0].append(int(float(entry4.get())))
    arr[0].append(int(float(entry5.get())))
    arr[0].append(int(float(entry6.get())))
    arr[0].append(int(float(entry7.get())))
    arr[0].append(int(float(entry8.get())))
    arr[0].append(int(float(entry9.get())))
    gui.destroy()
Button = tk.Button(gui,text = "Submit", height=2, width=15,command=Append, relief=tk.RAISED, bd=4, bg="skyblue")
Button.place(x=450,y=650)

gui.mainloop()

# Predicting the Test set results

arr = sc.transform(arr)
#print(arr)
y_pred = classifier.predict(arr)

if y_pred[0] == 0:
    gui1 = tk.Tk()
    gui1.title("Cancer Message")
    gui1.geometry("600x300")
    label = tk.Label(gui1,width=300,height=200)
    label.place(x=0,y=0)
    message10 = tk.Message(gui1,text = "HURRAY!! YOU ARE SAFE",fg="green",bg="black",width=400,padx=20,pady=20)
    message10.place(x=200,y=90)
    gui1.mainloop()
else:
    gui1 = tk.Tk()
    gui1.title("Cancer Message")
    gui1.geometry("600x300")
    label = tk.Label(gui1, width=300, height=200)
    label.place(x=0, y=0)
    message10 = tk.Message(gui1, text="SORRY!!! YOU GOT IT",fg="red",bg="black", width=400, padx=20, pady=20)
    message10.place(x=200, y=90)
    gui1.mainloop()

