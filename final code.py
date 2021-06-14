from Tkinter import*
import random
import time
import datetime
manohar=Tk()
manohar.geometry("850x700")
manohar.title("Restaurant Bill")

Tops=Frame(manohar, width=800)
Tops.pack(side=TOP)
f1=Frame(manohar,width=600,height=400)
f1.pack(side=LEFT)




Fries=StringVar()
Noodles=StringVar()
SubTotal=StringVar()
Soup=StringVar()
Total=StringVar()
Service_Charge=StringVar()
Drinks=StringVar()
Tax=StringVar()
Cost=StringVar()
Burger=StringVar()
Sandwich=StringVar()
CostFries=StringVar()
CostNoodles=StringVar()
CostSoup=StringVar()
CostBurger=StringVar()
CostSandwich=StringVar()
CostDrink=StringVar()

def Ref():
       if (Fries.get()==""):
           CostFries=0
       else:
           CostFries=float(Fries.get())
    
       if (Noodles.get()==""):
           CostNoodles=0
       else:
           CostNoodles=float(Noodles.get())
       if (Soup.get()==""):
           CostSoup=0
       else:
           CostSoup=float(Soup.get())
           
       if (Burger.get()==""): 
           CostBurger=0
       else:
           CostBurger=float(Burger.get())
 
       if (Sandwich.get()==""):
           CostSandwich=0
       else:
           CostSandwich=float(Sandwich.get())

       if (Drinks.get()==""):
           CostDrinks=0
       else:
           CostDrinks=float(Drinks.get())

       CostofFries =(CostFries * 30)
       CostofNoodles = (CostNoodles* 30)
       CostofSoup= (CostSoup*10)
       CostofBurger = (CostBurger* 25)
       CostofDrinks=(CostDrinks * 35)
       CostofSandwich=(CostSandwich * 15)

       CostofMeal= str('%.2f' % ((CostofFries)+(CostofDrinks)+(CostofNoodles)+(CostofSoup)+ (CostofBurger)+(CostofSandwich)))
       SaleTax=((CostofFries+CostofDrinks+CostofSoup+CostofNoodles+CostofBurger+CostofSandwich) * 0.05)
       Subtotal=((CostofFries)+(CostofDrinks)+(CostofSoup)+(CostofNoodles)+(CostofBurger)+(CostofSandwich))
       Ser_Charge= (((CostofFries)+(CostofDrinks)+(CostofSoup)+(CostofNoodles)+(CostofBurger)+(CostofSandwich))*0.15)
       Service = "Rs", str ('%.2f' % Ser_Charge)
       OverAllCost ="Rs", str ('%.2f' % (SaleTax+Subtotal+Ser_Charge))
       SalesTax= "Rs", str ('%.2f' % SaleTax)
       Service_Charge.set(Service)
       Cost.set(CostofMeal)
       Tax.set(SaleTax)
       SubTotal.set(CostofMeal)
       Total.set(OverAllCost)
    
def qExit():
    root.destroy()
def Reset(): 
    Fries.set("")
    Noodles.set("")
    Soup.set("")
    SubTotal.set("")
    Total.set("")
    Service_Charge.set("")
    Drinks.set("")
    Tax.set("")
    Cost.set("")
    Burger.set("")
    Sandwich.set("")




labelFries= Label(f1, font=('arial', 16, 'bold'),text="Fries",bd=6,anchor="w")
labelFries.grid(row=1, column=0)
textFries=Entry(f1, font=('arial',16,'bold'),textvariable=Fries,bd=10,insertwidth=4,bg="skyblue",justify='right')
textFries.grid(row=1,column=1)


labelNoodles= Label(f1, font=('arial', 16, 'bold'),text="Noodles",bd=16,anchor="w")
labelNoodles.grid(row=2, column=0)
textNoodles=Entry(f1, font=('arial',16,'bold'),textvariable=Noodles,bd=10,insertwidth=4,bg="skyblue",justify='right')
textNoodles.grid(row=2,column=1)

labelBurger= Label(f1, font=('arial',16, 'bold'),text="Burger",bd=16,anchor="w")
labelBurger.grid(row=3, column=0)
textBurger=Entry(f1, font=('arial',16,'bold'),textvariable=Burger,bd=10,insertwidth=4,bg="skyblue",justify='right')
textBurger.grid(row=3,column=1)

labelSoup= Label(f1, font=('arial',16, 'bold'),text="Soup",bd=16,anchor="w")
labelSoup.grid(row=4, column=0)
textSoup=Entry(f1, font=('arial',16,'bold'),textvariable=Soup,bd=10,insertwidth=4,bg="skyblue",justify='right')
textSoup.grid(row=4,column=1)



labelSandwich= Label(f1, font=('arial',16, 'bold'),text="Sandwich",bd=16,anchor="w")
labelSandwich.grid(row=5, column=0)
textSandwich=Entry(f1, font=('arial',16,'bold'),textvariable=Sandwich,bd=10,insertwidth=4,bg="skyblue",justify='right')
textSandwich.grid(row=5,column=1)

labelDrinks= Label(f1, font=('arial', 16, 'bold'),text="Drinks",bd=16,anchor="w")
labelDrinks.grid(row=6, column=0)
textDrinks=Entry(f1, font=('arial',16,'bold'),textvariable=Drinks,bd=10,insertwidth=4,bg="skyblue",justify='right')
textDrinks.grid(row=6,column=1)

labelCost= Label(f1, font=('arial', 16, 'bold'),text="Cost of Meal",bd=16,anchor="w")
labelCost.grid(row=1, column=4)
textCost=Entry(f1, font=('arial',16,'bold'),textvariable=Cost,bd=10,insertwidth=4,bg="skyblue",justify='right')
textCost.grid(row=1,column=5)


labelService= Label(f1, font=('arial', 16, 'bold'),text="Service Charge",bd=16,anchor="w")
labelService.grid(row=2, column=4)
textService=Entry(f1, font=('arial',16,'bold'),textvariable=Service_Charge,bd=10,insertwidth=4,bg="skyblue",justify='right')
textService.grid(row=2,column=5)


labelStateTax= Label(f1, font=('arial', 16, 'bold'),text="State Tax",bd=16,anchor="w")
labelStateTax.grid(row=3, column=4)
textStateTax=Entry(f1, font=('arial',16,'bold'),textvariable=Tax,bd=10,insertwidth=4,bg="skyblue",justify='right')
textStateTax.grid(row=3,column=5)

labelSubTotal= Label(f1, font=('arial', 16, 'bold'),text="Sub Total",bd=16,anchor="w")
labelSubTotal.grid(row=4, column=4)
textSubTotal=Entry(f1, font=('arial',16,'bold'),textvariable=SubTotal,bd=10,insertwidth=4,bg="skyblue",justify='right')
textSubTotal.grid(row=4,column=5)

labelTotalCost= Label(f1, font=('arial', 16, 'bold'),text="Total Cost",bd=16,anchor="w")
labelTotalCost.grid(row=5, column=4)
textTotalCost=Entry(f1, font=('arial',16,'bold'),textvariable=Total,bd=10,insertwidth=4,bg="skyblue",justify='right')
textTotalCost.grid(row=5,column=5)

buttonTotal=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Total",bg="skyblue",command=Ref).grid(row=7,column=1)
buttonReset=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Reset",bg="skyblue",command=Reset).grid(row=7,column=3)
buttonExit=Button(f1,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),width=10,text="Exit",bg="skyblue",command=qExit).grid(row=7,column=5)


manohar.mainloop()
