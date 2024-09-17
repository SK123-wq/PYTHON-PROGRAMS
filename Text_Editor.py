from tkinter import *
from tkinter.filedialog import askopenfilename,asksaveasfilename
window=Tk()
window.title("Codingal's Text Editor")
window.geometry('600x500')
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)
def openfile():
    filepath=askopenfilename(filetypes=[('Text Files','*.txt'),('All Files','*.*')])
    if not filepath:
        return
    text_edit.delete(1.0,END)
    with open(filepath,'r') as input_file:
        text=input_file.read()
        text_edit.insert(END,text)
    window.title(f"Codingal's text editor-{filepath}")
def savefile():
    filepath=asksaveasfilename(defaultextension="txt",filetypes=[('Text Files','*.txt'),('All Files','*.*')])
    if not filepath:
        return
    with open(filepath,'w') as output_file:
        text=text_edit.get(1.0,END)
        output_file.write(text)
    window.title(f"Codingal's text editor-{filepath}")
text_edit=Text(window)
frame=Frame(window,relief=RAISED,bd=2)
btn_open=Button(frame,text="Open",command=openfile)
btn_save=Button(frame,text="Save as",command=savefile)
btn_open.grid(row=0, column=0, sticky="ew", padx=5,pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
frame.grid(row=0,column=0,sticky='ns')
text_edit.grid(row=0,column=1,sticky='nsew')
window.mainloop()