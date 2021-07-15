from tkinter import *
import datetime
import time
import winsound

def alarm(postavi_alarm):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%Y")
        print("Postavljeni datum je:",date)
        print(now)
        if now == postavi_alarm:
            print("Vrijeme je za budjenje")
        winsound.PlaySound("sound.wav",winsound.SND_ASYNC)
        break

def actual_time():
    postavi_alarm = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(postavi_alarm)

clock = Tk()

clock.title("Alarm / Sat ")
clock.geometry("400x200")
time_format=Label(clock, text= "Unesite 24-satni format", fg="yellow",bg="black",font="Arial").place(x=60,y=120)
addTime = Label(clock,text = "Sat  Min   Sek",font=60).place(x = 110)
setYourAlarm = Label(clock,text = "Kada ce zazvoniti alarm",fg="blue",relief = "solid",font=("Helvetica",7,"bold")).place(x=0, y=29)

#inicijalizija varijabli za postavljanje sata

hour = StringVar()
min = StringVar()
sec = StringVar()

#vrijeme koje zelimo namjestiti na satu

hourTime= Entry(clock,textvariable = hour,bg = "yellow",width = 15).place(x=110,y=30)
minTime= Entry(clock,textvariable = min,bg = "yellow",width = 15).place(x=150,y=30)
secTime = Entry(clock,textvariable = sec,bg = "yellow",width = 15).place(x=200,y=30)

#preuzeti input korisnika

submit = Button(clock,text = "Postavi alarm",fg="red",width = 10,command = actual_time).place(x =110,y=70)

clock.mainloop()
#slijedi prikaz prozora za realiziranje koda