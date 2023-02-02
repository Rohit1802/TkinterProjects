from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text="type" ,src="English", dest="Hindi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text=text1, src=src1, dest=dest1)
    return trans1

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    masg = Sor_txt.get(1.0, END)
    textget = change(text = masg, src=s, dest=d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END, textget)


root = Tk()
root.title("Translator")
root.geometry("500x750")
root.config(bg='skyBlue')

#Label is starting
lab_txt = Label(root, text="Translator", font=("Poppins", 24, "bold"), bg="skyBlue")
lab_txt.place(x=100, y=40, height=50, width=250)


frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="Source Text", font=("Poppins", 16, "bold") ,fg="black")
lab_txt.place(x=100, y=100, height=30, width=250)

Sor_txt = Text(frame, font=("Poppins", 16, "bold"), wrap = WORD)
Sor_txt.place(x=10, y=140, height=200, width=480)


list_text = list(LANGUAGES.values())
comb_sor = ttk.Combobox(frame, value=list_text)
comb_sor.place(x=10, y=350, height=40, width=150)
comb_sor.set("english")

button_change = Button(frame, text="Translate", relief=RAISED , command=data)
button_change.place(x=180, y=350, height=40, width=100)

comb_dest = ttk.Combobox(frame, value=list_text)
comb_dest.place(x=300, y=350, height=40, width=150)
comb_dest.set("english")

lab_txt = Label(root, text="Destination Text", font=("Poppins", 16, "bold") ,fg="black")
lab_txt.place(x=100, y=400, height=30, width=250)

dest_txt = Text(frame, font=("Poppins", 16, "bold"), wrap = WORD)
dest_txt.place(x=10, y=440, height=200, width=480)
root.mainloop()
