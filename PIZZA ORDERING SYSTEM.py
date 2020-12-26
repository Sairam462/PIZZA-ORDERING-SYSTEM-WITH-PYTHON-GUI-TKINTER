from tkinter import*
import random
import time
import sqlite3
from tkinter import messagebox
#--------------- Order sequence >> OrdeerId>>Name>>Mobile>>Total ------------
Order = []
operator = ""
roo = Tk()
rand1 = StringVar()
rand2 = StringVar()
name1 = StringVar()
mobile = StringVar()
roo.title("Admin Login")
roo.geometry("1600x800+0+0")
lblinfo1 = Label(roo, font=( 'arial', 30, 'bold' ),text="Pizza Ordering System",fg="steel blue",bd=10,bg="bisque",anchor='w',relief=RAISED)
lblinfo1.pack()


username_lable = Label(roo, font=('Times New Roman',16,'bold'), text="Username * ")
username_lable.pack()
username_entry = Entry(roo, textvariable=rand1 , bd=8 ,insertwidth=5 ,bg="white")
username_entry.pack()
password_lable = Label(roo, font=('Times New Roman',16,'bold'), text="Password * ")
password_lable.pack()
password_entry = Entry(roo, textvariable=rand2 , bd=8 ,insertwidth=5 ,bg="white", show='*')
password_entry.pack()
Name1 = Label(roo,font=('Times New Roman',16,'bold'), text="Name Of the Admin")
Name1.pack()
Name1 = Entry(roo, textvariable=name1 , bd=8 ,insertwidth=5,bg="white")
Name1.pack()
Mobile = Label(roo, font=('Times New Roman',16,'bold'),text="Mobile")
Mobile.pack()
Mobile = Entry(roo, textvariable=mobile , bd=8 ,insertwidth=5 ,bg="white")
Mobile.pack()
#######################################################################################
                                # function for sqlite3 database

def get_all_from_database():
    conn = sqlite3.connect('pizzaOrder.db')
    c = conn.cursor()
    c.execute("SELECT * FROM Orders")
    data=''
    for i in c.fetchall():
        data+=f"Order Id : {i[0]}, Name : {i[1]}, Mobile : {i[2]}, Total Bill : {i[3]} [{i[4]}] \n\n"
    return data


def delete_from_ord():
    c.execute('DELETE FROM Orders')


def send_to_database(ord_detile):
    conn = sqlite3.connect('pizzaOrder.db')
    c = conn.cursor()

    def get_time():
        return time.asctime(time.localtime(time.time()))

    def insert_ord(OrderId, name, mobile, tbill):
        with conn:
            c.execute("INSERT INTO Orders VALUES (:OrderId, :name, :mobile, :total_bill, :date_time )",
                {'OrderId': OrderId,
                 'name': name,
                 'mobile':mobile, 
                 'total_bill': tbill,
                 'date_time':get_time()
                 }
                 )


    def get_order_by_orderid(OrderId):
        c.execute("SELECT * FROM Orders WHERE OrderId=:Id", {'Id': OrderId})
        return c.fetchone()

    try:
        c.execute("""CREATE TABLE Orders(
                    OrderId integer,
                    name text,
                    mobile integer,
                    total_bill real,
                    date_time text
                    )""")
        conn.commit()
    except sqlite3.OperationalError:
        pass
    finally:
        insert_ord(*tuple(ord_detile))
        conn.commit()
        print(get_order_by_orderid(ord_detile[0]))
        conn.close()


#######################################################################################

def admin():
    r2=Tk()
    r2.geometry("600x220+0+0")
    r2.title("Admin List")
    lblinfo = Label(r2, font=('aria', 15, 'bold'), text="Sai Ram", fg="black", bd=5)
    lblinfo.pack()
    

def name():
    Order.clear()
    name_1 = name1.get()
    mobile_1 = mobile.get()
    Order.append(name_1)
    Order.append(mobile_1)

    if rand1.get() == 'sai' and rand2.get()=='123':
        messagebox.showinfo("Admin","Welcome Back to Pizza Ordering System")
        roo.destroy()
        root = Tk()
        root.geometry("1600x800+0+0")
        root.title("Pizza Ordering System")


        Tops = Frame(root,bg="navajo white",width = 1600,height=50,relief=SUNKEN)
        Tops.pack(side=TOP)

        f1 = Frame(root,width = 800,height=700,relief=SUNKEN,bg="grey94")
        f1.pack(side=LEFT)

        f2 = Frame(root ,width = 250,height=700,relief=SUNKEN,bg="aquamarine")
        f2.pack(side=RIGHT)


        #------------------TIME--------------
        localtime=time.asctime(time.localtime(time.time()))

        #-----------------INFO TOP------------
        lblinfo = Label(Tops, font=( 'arial' ,30, 'bold' ),text="Pizza Ordering System",fg="steel blue",bd=10,anchor='w',relief=SUNKEN)
        lblinfo.grid(row=0,column=0)
        lblinfo = Label(Tops, font=( 'arial' ,20,'bold' ),text=localtime,fg="black",anchor=W)
        lblinfo.grid(row=1,column=0)

        lblinfo = Label(Tops, font=( 'Times New Roman' ,20, 'bold' ),text="Billing Person ::   " + name1.get() + "\t" + "Mobile :    "  + mobile.get(),fg="tomato4",bd=10,anchor='w')
        lblinfo.grid(row=2,column=0)


    

        #---------------Calculator------------------
        text_Input=StringVar()
        operator =""

        txtdisplay = Entry(f2,font=('arial' ,20,'bold'), textvariable=text_Input , bd=30 ,insertwidth=7 ,bg="white",justify='right')
        txtdisplay.grid(columnspan=4)

        def Take_Input():
            rand=rand.get()
            Fries=Fries.get()
            Largefries=Largefries.get
            Burger=Burger.get()
            Filet=Filet.get()
            Subtotal=Subtotal.get()
            Total=Total.get()
            Service_Charge=Service_Charge.get()
            Drinks=Drinks.get()
            Tax=Tax.get()
            cost=cost.get()
            Cheese_burger=Cheese_burger.get()

        def  btnclick(numbers):
            global operator
            operator=operator + str(numbers)
            text_Input.set(operator)

        def clrdisplay():
            global operator
            operator=""
            text_Input.set("")

        def eqals():
            global operator
            sumup=str(eval(operator))

            text_Input.set(sumup)
            operator = ""

        def Ref():
            x=random.randint(12980, 50876)
            randomRef = str(x)
            OrderId = randomRef
            Order.insert(0, OrderId)
            rand.set(randomRef)

            cof =float(Fries.get())
            colfries= float(Largefries.get())
            cob= float(Burger.get())
            cofi= float(Filet.get())
            cochee= float(Cheese_burger.get())
            codr= float(Drinks.get())

            costoffries = cof*150
            costoflargefries = colfries*200
            costofburger = cob*150
            costoffilet = cofi*250
            costofcheeseburger = cochee*150
            costofdrinks = codr*25

            costofmeal = "Rs.",('%.2f'% (costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks))
            PayTax=((costoffries +  costoflargefries + costofburger + costoffilet +  costofcheeseburger + costofdrinks)*0.02)
            Totalcost=(costoffries +  costoflargefries + costofburger + costoffilet  + costofcheeseburger + costofdrinks)
            Ser_Charge=((costoffries +  costoflargefries + costofburger + costoffilet + costofcheeseburger + costofdrinks)/99)
            Service="Rs.",('%.2f'% Ser_Charge)
            total=PayTax + Totalcost + Ser_Charge
            OverAllCost="Rs.",str(total)
            PaidTax="Rs.",('%.2f'% PayTax)

            Service_Charge.set(Service)
            cost.set(costofmeal)
            Tax.set(PaidTax)
            Subtotal.set(costofmeal)
            Total.set(OverAllCost)
            Order.append(total)

            send_to_database(Order)


        def qexit():
            root.destroy()

        def reset():
            rand.set("0")
            Fries.set("0")
            Largefries.set("0")
            Burger.set("0")
            Filet.set("0")
            Subtotal.set("0")
            Total.set("")
            Service_Charge.set("0")
            Drinks.set("0")
            Tax.set("0")
            cost.set("0")
            Cheese_burger.set("0")


        btn7=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20 ,'bold'),text="7",bg="powder blue", command=lambda: btnclick(7) )
        btn7.grid(row=2,column=0)

        btn8=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20 ,'bold'),text="8",bg="powder blue", command=lambda: btnclick(8) )
        btn8.grid(row=2,column=1)

        btn9=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20 ,'bold'),text="9",bg="powder blue", command=lambda: btnclick(9) )
        btn9.grid(row=2,column=2)

        Addition=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20 ,'bold'),text="+",bg="powder blue", command=lambda: btnclick("+") )
        Addition.grid(row=2,column=3)
        #---------------------------------------------------------------------------------------------
        btn4=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20 ,'bold'),text="4",bg="powder blue", command=lambda: btnclick(4) )
        btn4.grid(row=3,column=0)

        btn5=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20 ,'bold'),text="5",bg="powder blue", command=lambda: btnclick(5) )
        btn5.grid(row=3,column=1)

        btn6=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20 ,'bold'),text="6",bg="powder blue", command=lambda: btnclick(6) )
        btn6.grid(row=3,column=2)

        Substraction=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20 ,'bold'),text="-",bg="powder blue", command=lambda: btnclick("-") )
        Substraction.grid(row=3,column=3)
        #-----------------------------------------------------------------------------------------------
        btn1=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('ariel', 20 ,'bold'),text="1",bg="powder blue", command=lambda: btnclick(1) )
        btn1.grid(row=4,column=0)

        btn2=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('ariel', 20 ,'bold'),text="2",bg="powder blue", command=lambda: btnclick(2) )
        btn2.grid(row=4,column=1)

        btn3=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('ariel', 20 ,'bold'),text="3",bg="powder blue", command=lambda: btnclick(3) )
        btn3.grid(row=4,column=2)

        multiply=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('ariel', 20 ,'bold'),text="*",bg="powder blue", command=lambda: btnclick("*") )
        multiply.grid(row=4,column=3)
        #------------------------------------------------------------------------------------------------
        btn0=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20 ,'bold'),text="0",bg="powder blue", command=lambda: btnclick(0) )
        btn0.grid(row=5,column=0)

        btnc=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20 ,'bold'),text="c",bg="powder blue", command=clrdisplay)
        btnc.grid(row=5,column=1)

        btnequal=Button(f2,padx=16,pady=16,bd=8,width = 20, fg="black", font=('arial', 20 ,'bold'),text="=",bg="peach puff",command=eqals)
        btnequal.grid(columnspan=4)

        Decimal=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20 ,'bold'),text=".",bg="powder blue", command=lambda: btnclick(".") )
        Decimal.grid(row=5,column=2)

        Division=Button(f2,padx=16,pady=16,bd=8, fg="black", font=('arial', 20 ,'bold'),text="/",bg="powder blue", command=lambda: btnclick("/") )
        Division.grid(row=5,column=3)
        #---------------------------------------------------------------------------------------
        rand = IntVar()
        Fries = IntVar()
        Largefries =IntVar()
        Burger = IntVar()
        Filet = IntVar()
        Subtotal = IntVar()
        Total =IntVar()
        Service_Charge = IntVar()
        Drinks = IntVar()
        Tax = IntVar()
        cost = IntVar()
        Cheese_burger = IntVar()


        lblreference = Label(f1, font=( 'arial' ,16, 'bold' ),text="Order ID.",fg="steel blue",bd=10,anchor='w')
        lblreference.grid(row=0,column=0)
        txtreference = Entry(f1,font=('arial' ,16,'bold'), textvariable=rand , bd=25,insertwidth=4,bg="powder blue" ,justify='right')
        txtreference.grid(row=0,column=1)

        lblfries = Label(f1, font=( 'arial' ,16, 'bold' ),text="Chicken Pizza",fg="steel blue",bd=10,anchor='w')
        lblfries.grid(row=1,column=0)
        txtfries = Entry(f1,font=('arial' ,16,'bold'), textvariable=Fries , bd=25,insertwidth=4,bg="powder blue" ,justify='right')
        txtfries.grid(row=1,column=1)

        lblLargefries = Label(f1, font=( 'arial' ,16, 'bold' ),text="Veg Pizza",fg="steel blue",bd=10,anchor='w')
        lblLargefries.grid(row=2,column=0)
        txtLargefries = Entry(f1,font=('arial' ,16,'bold'), textvariable=Largefries , bd=25,insertwidth=4,bg="powder blue" ,justify='right')
        txtLargefries.grid(row=2,column=1)


        lblburger = Label(f1, font=( 'arial' ,16, 'bold' ),text="Capsicum Pizza",fg="steel blue",bd=10,anchor='w')
        lblburger.grid(row=3,column=0)
        txtburger = Entry(f1,font=('arial' ,16,'bold'), textvariable=Burger , bd=25,insertwidth=4,bg="powder blue" ,justify='right')
        txtburger.grid(row=3,column=1)

        lblFilet = Label(f1, font=( 'arial' ,16, 'bold' ),text=" Greek Pizza",fg="steel blue",bd=10,anchor='w')
        lblFilet.grid(row=4,column=0)
        txtFilet = Entry(f1,font=('arial' ,16,'bold'), textvariable=Filet , bd=25,insertwidth=4,bg="powder blue" ,justify='right')
        txtFilet.grid(row=4,column=1)

        lblCheese_burger = Label(f1, font=( 'arial' ,16, 'bold' ),text="Cheese burger",fg="steel blue",bd=10,anchor='w')
        lblCheese_burger.grid(row=5,column=0)
        txtCheese_burger = Entry(f1,font=('arial' ,16,'bold'), textvariable=Cheese_burger , bd=25,insertwidth=4,bg="powder blue" ,justify='right')
        txtCheese_burger.grid(row=5,column=1)

        #--------------------------------------------------------------------------------------
        lblDrinks = Label(f1, font=( 'arial' ,16, 'bold' ),text="Drinks",fg="steel blue",bd=10,anchor='w')
        lblDrinks.grid(row=0,column=2)
        txtDrinks = Entry(f1,font=('arial' ,16,'bold'), textvariable=Drinks , bd=25,insertwidth=4,bg="powder blue" ,justify='right')
        txtDrinks.grid(row=0,column=3)

        lblcost = Label(f1, font=( 'arial' ,16, 'bold' ),text="Cost",fg="steel blue",bd=10,anchor='w')
        lblcost.grid(row=1,column=2)
        txtcost = Entry(f1,font=('arial' ,16,'bold'), textvariable=cost , bd=25,insertwidth=25,bg="powder blue" ,justify='right')
        txtcost.grid(row=1,column=3)

        lblService_Charge = Label(f1, font=( 'arial' ,16, 'bold' ),text="Service Charge",fg="steel blue",bd=10,anchor='w')
        lblService_Charge.grid(row=2,column=2)
        txtService_Charge = Entry(f1,font=('arial' ,16,'bold'), textvariable=Service_Charge , bd=25,insertwidth=4,bg="powder blue" ,justify='right')
        txtService_Charge.grid(row=2,column=3)

        lblTax = Label(f1, font=( 'arial' ,16, 'bold' ),text="Tax",fg="steel blue",bd=10,anchor='w')
        lblTax.grid(row=3, column=2)
        txtTax = Entry(f1, font=('arial' ,16,'bold'), textvariable=Tax , bd=25,insertwidth=4,bg="powder blue" ,justify='right')
        txtTax.grid(row=3, column=3)

        lblSubtotal = Label(f1, font=( 'arial' ,16, 'bold' ),text="Subtotal",fg="steel blue",bd=10,anchor='w')
        lblSubtotal.grid(row=4,column=2)
        txtSubtotal = Entry(f1,font=('arial' ,16,'bold'), textvariable=Subtotal , bd=25,insertwidth=4,bg="powder blue" ,justify='right')
        txtSubtotal.grid(row=4,column=3)

        lblTotal = Label(f1, font=( 'arial' ,16, 'bold' ),text="Total",fg="steel blue",bd=10,anchor='w')
        lblTotal.grid(row=5,column=2)
        txtTotal = Entry(f1,font=('arial' ,16,'bold'), textvariable=Total , bd=25,insertwidth=4,bg="powder blue" ,justify='right')
        txtTotal.grid(row=5,column=3)

        #-----------------------------------------buttons------------------------------------------
        lblTotal = Label(f1,text="---------------------",fg="white")
        lblTotal.grid(row=6,columnspan=3)

        btnTotal=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="TOTAL", bg="powder blue",command=Ref)
        btnTotal.grid(row=7, column=1)

        btnreset=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="RESET", bg="powder blue",command=reset)
        btnreset.grid(row=7, column=2)

        btnexit=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="QUIT", bg="red",command=qexit)
        btnexit.grid(row=7, column=3)

        def price():
            roo = Tk()
            roo.geometry("600x220+0+0")
            roo.title("Price List")
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="ITEM", fg="black", bd=5)
            lblinfo.grid(row=0, column=0)
            lblinfo = Label(roo, font=('aria', 15,'bold'), text="_____________", fg="white", anchor=W)
            lblinfo.grid(row=0, column=2)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="PRICE", fg="orange", anchor=W)
            lblinfo.grid(row=0, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Chicken Pizza", fg="steel blue", anchor=W)
            lblinfo.grid(row=1, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="250", fg="steel blue", anchor=W)
            lblinfo.grid(row=1, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="GREEK PIZZA", fg="steel blue", anchor=W)
            lblinfo.grid(row=2, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="200", fg="steel blue", anchor=W)
            lblinfo.grid(row=2, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="CAPSICUM PIZZA", fg="steel blue", anchor=W)
            lblinfo.grid(row=3, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="350", fg="steel blue", anchor=W)
            lblinfo.grid(row=3, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="DRINKS", fg="steel blue", anchor=W)
            lblinfo.grid(row=4, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="25", fg="steel blue", anchor=W)
            lblinfo.grid(row=4, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="Cheese Burger", fg="steel blue", anchor=W)
            lblinfo.grid(row=5, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="300", fg="steel blue", anchor=W)
            lblinfo.grid(row=5, column=3)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="CRISPY PIZZA", fg="steel blue", anchor=W)
            lblinfo.grid(row=6, column=0)
            lblinfo = Label(roo, font=('aria', 15, 'bold'), text="200", fg="steel blue", anchor=W)
            lblinfo.grid(row=6, column=3)

            roo.mainloop()

        btnprice=Button(f1,padx=16,pady=8, bd=10 ,fg="black",font=('ariel' ,16,'bold'),width=10, text="PRICE", bg="powder blue",command=price)
        btnprice.grid(row=7, column=0)

        root.mainloop()
    else:
        messagebox.showerror("Error","You are Not Allowed")
        roo.destroy()

btn1 = Button(fg="black",font=('ariel' ,10,'bold'),width=8, text="SUBMIT", bg="khaki1",relief=RAISED,command=name)
btn1.pack()

roo.mainloop()

