#Υπολογισμός τηας καθαρής παρούσας αξίας μιας σειράς ταμειακών ροών.

from tkinter import *

def disappear(a):
    a.place(x=0,y=0,width=0,height=0)

def OK():
    t=float(entry1.get())
    cf=float(entry2.get())
    n=int(entry3.get())
    global npv
    npv+=cf/((1+t)**n)
    entry1.delete(0,END)
    entry2.delete(0, END)
    entry3.delete(0, END)

def DONE():
    disappear(label1)
    disappear(entry1)
    disappear(label2)
    disappear(entry2)
    disappear(label3)
    disappear(entry3)
    disappear(submit_button)
    disappear(done_button)
    label1.config(text='Η καθαρή παρούσα αξία των ταμειακών ροών ισούται με: '+str(round(npv,2)))
    label1.place(x=80,y=80,width=440,height=20)


window= Tk()
window.title('Καθαρή παρούσα αξία')

window.geometry('600x600')

label1=Label(text='προεξοφλητικό επιτόκιο')
label2=Label(text='ταμειακή ροή')
label3=Label(text='η ταμειακή ροή λαμβάνει χώρα σε πόσα χρόνια: ')

entry1=Entry(window,font=('Arial',10))
entry2=Entry(window,font=('Arial',10))
entry3=Entry(window,font=('Arial',10))

submit_button=Button(window,text="OK",command=OK)
done_button=Button(window,text="ΤΕΛΟΣ",command=DONE)

entry1.place(x=290, y=80,width=150,height=20)
label1.place(x=80, y=80,width=200,height=20)
entry2.place(x=290, y=110,width=150,height=20)
label2.place(x=80, y=110,width=200,height=20)
entry3.place(x=290, y=140,width=150,height=20)
label3.place(x=10, y=140,width=270,height=20)
submit_button.place(x=400, y=170,width=50,height=20)
done_button.place(x=400,y=200,width=50,height=20)

global npv
npv=0

window.mainloop()