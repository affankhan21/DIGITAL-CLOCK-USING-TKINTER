from tkinter import *
#creating object i.e clock1 of class Tk()
from datetime import datetime

def date1():
    time= datetime.now()
    hr=time.strftime("%I")
    minu=time.strftime("%M")
    sec=time.strftime("%S")
    am=time.strftime("%p")
    date11=time.strftime("%d")
    month1=time.strftime("%m")
    year1=time.strftime("%y")
    day1=time.strftime("%a")

    lab_hr.config(text=hr)
    lab_min.config(text=minu)
    lab_sec.config(text=sec)
    lab_am.config(text=am)
    lab_date.config(text=date11)
    lab_month.config(text=month1)
    lab_year.config(text=year1)
    lab_day.config(text=day1)

    lab_hr.after(1000,date1)












clock1=Tk()
clock1.title("  ****Digital Clock****                ")
clock1.geometry('1000x500')
var = StringVar()
label = Label( clock1,textvariable=var,font=("Times New Roman",25,"bold"),bg="#FFEFD5",fg="#FF8000",width="100",pady="4",anchor="center",
relief=RAISED)
var.set("DIGITAL CLOCK")
label.pack()


clock1.config(bg="#FFD39B")

##TIME########
lab_hr=Label(clock1,text="00",font=("Times New Roman",60,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_hr.place(x=120,y=50,height=110,width=100)
lab_hr_text=Label(clock1,text="HOUR",font=("Times New Roman",20,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_hr_text.place(x=120,y=190,height=40,width=100)

lab_min=Label(clock1,text="00",font=("Times New Roman",60,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_min.place(x=340,y=50,height=110,width=100)
lab_min_text=Label(clock1,text="MIN",font=("Times New Roman",20,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_min_text.place(x=340,y=190,height=40,width=100)




lab_sec=Label(clock1,text="00",font=("Times New Roman",60,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_sec.place(x=560,y=50,height=110,width=100)
lab_sec_text=Label(clock1,text="SEC",font=("Times New Roman",20,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_sec_text.place(x=560,y=190,height=40,width=100)





lab_am=Label(clock1,text="00",font=("Times New Roman",50,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_am.place(x=780,y=50,height=110,width=100)
lab_am_text=Label(clock1,text="AM/PM",font=("Times New Roman",20,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_am_text.place(x=780,y=190,height=40,width=100)
#mainloop function is used for graphics.

############# date start ############

lab_date=Label(clock1,text="00",font=("Times New Roman",60,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_date.place(x=120,y=270,height=110,width=100)
lab_date._text=Label(clock1,text="DATE",font=("Times New Roman",20,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_date._text.place(x=120,y=410,height=40,width=100)


lab_month=Label(clock1,text="00",font=("Times New Roman",60,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_month.place(x=340,y=270,height=110,width=100)
lab_month_text=Label(clock1,text="MONTH",font=("Times New Roman",20,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_month_text.place(x=340,y=410,height=40,width=100)

lab_year=Label(clock1,text="00",font=("Times New Roman",60,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_year.place(x=560,y=270,height=110,width=100)
lab_year_text=Label(clock1,text="YEAR",font=("Times New Roman",20,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_year_text.place(x=560,y=410,height=40,width=100)



lab_day=Label(clock1,text="00",font=("Times New Roman",40,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_day.place(x=780,y=270,height=110,width=100)
lab_day_text=Label(clock1,text="DAY",font=("Times New Roman",20,"bold"),bg="#FF8000",fg="#F8F8FF")
lab_day_text.place(x=780,y=410,height=40,width=100)



















date1()
clock1.mainloop()