import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
class reastaurantordermanagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Restaurant Management App")
        self.menuitems={
            "Burger":10,
            "pizza":5,
            "icecream":6.5
        }
        self.exchangerate=132
        self.setupbackground(root)
        frame=ttk.Frame(root)
        frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
        ttk.Label(frame,text="Restaurant Order Management",font=("Arial",20,"bold")).grid(row=0,columnspan=3,padx=10,pady=10)
        self.menulabel={}
        self.menuquantities={}
        for i,(item,price) in enumerate(self.menuitems.items(),start=1):
            label=ttk.Label(frame,text=f"{item} (${price}):")
            label.grid(row=i,column=0,padx=10,pady=5)
            self.menulabel[item]=label
            quantityentry=ttk.Entry(frame,width=5)
            quantityentry.grid(row=i,column=1,padx=10,pady=5)
            self.menuquantities[item]=quantityentry
        self.currencyvar=tk.StringVar()
        ttk.Label(frame,text="Currency:").grid(row=len(self.menuitems)+1,column=0,padx=10,pady=5)
        currencydropdown=ttk.Combobox(frame,textvariable=self.currencyvar,state="readonly",width=18,values=('USD','NEPALI RS'))
        currencydropdown.grid(row=len(self.menuitems)+1,column=1,padx=10,pady=5)
        currencydropdown.current(1)
        self.currencyvar.trace("w",self.updatemenuprices)
        orderbutton=ttk.Button(frame,text="place order",command=self.placeorder)
        orderbutton.grid(row=len(self.menuitems)+2,columnspan=3,padx=10,pady=10)
    def setupbackground(self,root):
        bgwidht,bgheight=800,600
        canvas=tk.Canvas(root,width=bgwidht,height=bgheight)
        canvas.pack()
        img=Image.open("D:/ACER/Desktop/PYTHON PROGRAMS/images.jpeg")
        img=img.resize((bgwidht,bgheight))
        originalimage=ImageTk.PhotoImage(img)
        canvas.create_image(40,30,anchor=tk.NW,image=originalimage)
        canvas.image=originalimage
    def updatemenuprices(self,*args):
        currency=self.currencyvar.get()
        symbol="₹" if currency=="NEPALI RS" else "$"
        rate = self.exchangerate if currency=="NEPALI RS" else 1
        for item,label in self.manulabels.items():
            price=self.menuitems[item]*rate    
            label.config(text=F"{item} ({symbol} {price})")
    def placeorder(self):
        totalcost=0
        ordersummary="order summary:\n"
        currency=self.currencyvar.get()
        symbol="₹" if currency=="NEPALI RS" else "$"
        rate = self.exchangerate if currency=="NEPALI RS" else 1
        for item,entry in self.menuquantities.items():
            quantity=entry.get()
            if quantity.isdigit():
                quantity=int(quantity)
                price=self.menuitems[item]*rate
                cost=quantity*price
                totalcost+=cost
                if quantity>0:
                    ordersummary+=f"\n total cost: {item}: {quantity} x {symbol} {price}={symbol}{cost}\n"
        if totalcost>0:
            ordersummary+=f"\n total cost:{symbol}{totalcost}"
            messagebox.showinfo("Order Placed",ordersummary)
        else:
            messagebox.showerror("Error","Please order atleast one item")
if __name__=="__main__":
    root=tk.Tk()
    app=reastaurantordermanagement(root)
    root.geometry("800x600")
    root.mainloop()