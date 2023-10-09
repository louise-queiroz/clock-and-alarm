from tkinter import *
from tkinter import messagebox
import time
import datetime
import threading
from pygame import mixer

root= Tk()
root.title("Alarme")
root.geometry("750x550")
root.configure(bg='#A6BCDE')



mixer.init()

def th():
	t1 = threading.Thread(target=a, args=())
	t1.start()


def a():

	a = hr.get()
	if a == "":
		msg = messagebox.showerror('Dados inválidos!','Por favor, reentre com dados válidos.')
	else:
		Alarmtime= a
		CurrentTime = time.strftime("%H:%M")

		while Alarmtime != CurrentTime:
			CurrentTime = time.strftime("%H:%M")
			
		if Alarmtime == CurrentTime:
			mixer.music.load('tone.mp3')
			mixer.music.play()
			msg = messagebox.showinfo('Está na hora!',f'{amsg.get()}')
			if msg:
				mixer.music.stop()


def update():
	time_string = time.strftime("%H:%M:%S")
	time_label.config(text=time_string)
	day_string = time.strftime("%A")
	day_label.config(text=day_string)
	date_string = time.strftime("%d %B, %Y")
	date_label.config(text=date_string)
	
	root.after(1000,update)

header =Frame(root)
header.place(x=5,y=5)

head =Label(root,text="ALARME",font=('cantarell',20), bg='#A6BCDE')
head.pack(fill=X)

panel = Frame(root, bg='#A6BCDE')
panel.place(x=5,y=70)

alpp = PhotoImage(file='clock.png')
alpp = alpp.subsample(2, 2)
alp = Label(panel,image=alpp, bg='#A6BCDE')
alp.grid(rowspan=4,column=0)


atime = Label(panel,text="Hora do alarme \n(Hr:Min)",font=('cantarell',18), bg='#A6BCDE')
atime.grid(row=0,column=1,padx=10,pady=5)

hr = Entry(panel,font=('cantarell',20),width=5)
hr.grid(row=0,column=2,padx=10,pady=5)

amessage = Label(panel,text="Mensagem",font=('cantarell',20),bg='#A6BCDE')
amessage.grid(row=1,column=1,columnspan=2,padx=10,pady=5)

amsg = Entry(panel,font=('cantarell',15),width=25)
amsg.grid(row=2,column=1,columnspan=2,padx=10,pady=5)


start = Button(panel,text="Iniciar alarme",font=('cantarell',20),command=th, bg='#8999b3')
start.grid(row=3,column=1,columnspan=2,padx=10,pady=5)

time_label = Label(panel, font=('cantarell',20), bg='#A6BCDE')
time_label.grid(row=4, column=1, columnspan=2, padx=10, pady=5)

day_label = Label(panel, font=('cantarell',20), bg='#A6BCDE')
day_label.grid(row=5, column=1, columnspan=2, padx=10, pady=5)

date_label = Label(panel, font=('cantarell',20), bg='#A6BCDE')
date_label.grid(row=6, column=1, columnspan=2, padx=10, pady=5)


update()




root.mainloop()