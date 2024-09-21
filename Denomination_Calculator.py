from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
root = Tk()
root.title("Denomination Calculator")
root.geometry("650x400")
upload = Image.open("D:\ACER\Desktop\PYTHON PROGRAMS\denominastion_img.jpeg")
upload = upload.resize((300,300))
image=ImageTk.PhotoImage(upload)
label=Label(root,image=image)
label.place(x=180,y=20)
label1 = Label(root,text="Hey User! Welcome to denomination calculator app.")
label1.place(relx=0.5,y=340,anchor=CENTER)
def msg():
    msgdox=messagebox.showinfo('Alert','Do you want to calculate the denomination count')
    if msgdox=='ok':
        topwin()
button1=Button(root,text="Lets Get started",command=msg)
button1.place(x=260,y=360)
def topwin():
    top=Toplevel()
    top.geometry("600x350+50+50")
    label=Label(top,text="Enter total amount")
    entry=Entry(top)
    lbl=Label(top,text="Here are the number of notes in your denomination!")
    l1=Label(top,text="2000")
    l2=Label(top,text="500")
    l3=Label(top,text="200")
    t1=Entry(top)
    t2=Entry(top)
    t3=Entry(top)
    def calculator():
        try:
            global amount
            amount=int(entry.get())
            note2000=amount//2000
            amount%=2000
            note500=amount//500
            amount%=500
            note200=amount//200
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)
            t1.insert(END,str(note2000))
            t2.insert(END,str(note500))
            t3.insert(END,str(note200))
        except ValueError():
            messagebox.showerror('ERROR!',"Please enter a valid amount")
    btn=Button(top,text="calculate",command=calculator)
    label.place(x=230,y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    lbl.place(x=140,y=170)
    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)
    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)
    top.mainloop()
root.mainloop()