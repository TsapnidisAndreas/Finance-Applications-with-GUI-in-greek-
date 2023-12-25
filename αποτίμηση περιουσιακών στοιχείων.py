#Αποτίμηση διαφορετικών τύπων ομολόγων και μετοχών με βάση τις ταμειακές ροές που θα αποδώσουν και του προεξοφλητικού
#επιτοκίου

from tkinter import *

def μηδενικό_τοκομερίδιο():
    disappear_all()
    entry1.place(x=270, y=80,width=150,height=20)
    label1.place(x=110, y=80,width=150,height=20)
    entry2.place(x=270, y=110,width=150,height=20)
    label2.place(x=110, y=110,width=150,height=20)
    entry3.place(x=270, y=140,width=150,height=20)
    label3.place(x=110, y=140,width=150,height=20)
    submit_button.place(x=400, y=170,width=50,height=20)
    global k
    k=0

def διηνεκές():
    disappear_all()
    entry1.place(x=270, y=80,width=150,height=20)
    label1.place(x=110, y=80,width=150,height=20)
    entry4.place(x=270, y=110,width=150,height=20)
    label4.place(x=110, y=110,width=150,height=20)
    submit_button.place(x=400, y=170,width=50,height=20)
    global k
    k=1


def σύνηθες():
    disappear_all()
    entry1.place(x=270, y=80,width=150,height=20)
    label1.place(x=110, y=80,width=150,height=20)
    entry2.place(x=270, y=110,width=150,height=20)
    label2.place(x=110, y=110,width=150,height=20)
    entry3.place(x=270, y=140,width=150,height=20)
    label3.place(x=110, y=140,width=150,height=20)
    entry4.place(x=270, y=170,width=150,height=20)
    label4.place(x=110, y=170,width=150,height=20)
    submit_button.place(x=400, y=170,width=50,height=20)
    global k
    k=2

def σταθερά_μερίσματα():
    disappear_all()
    entry1.place(x=270, y=80,width=150,height=20)
    label1.place(x=110, y=80,width=150,height=20)
    entry5.place(x=270, y=110,width=150,height=20)
    label5.place(x=110, y=110,width=150,height=20)
    submit_button2.place(x=400, y=170,width=50,height=20)
    global k
    k=0

def μερίσματα_αυξανόμενα_με_σταθερό_ρυθμό():
    disappear_all()
    entry1.place(x=300, y=80,width=150,height=20)
    label1.place(x=110, y=80,width=150,height=20)
    entry5.place(x=300, y=110,width=150,height=20)
    label5.place(x=110, y=110,width=150,height=20)
    entry6.place(x=300, y=140,width=150,height=20)
    label6.place(x=110, y=140,width=190,height=20)
    submit_button2.place(x=450, y=170,width=50,height=20)
    global k
    k=1

def submit(k):
    disappear_all()
    t=(entry1.get())
    F=(entry2.get())
    n=(entry3.get())
    P=(entry4.get())
    t=float(t)
    calculation(k, t, F, n, P)

def submit2(k):
    disappear_all()
    t=(entry1.get())
    P=(entry5.get())
    g=(entry6.get())
    t=float(t)
    calculation2(k, t, P, g)

def OK():
    disappear_all()
    label.config(text='Από το μενού επιλέξτε το είδος του περιουσιακού στοιχείου')
    label.place(x=90,y=80,width=400,height=20)

def disappear(a):
    a.place(x=0, y=0, width=0, height=0)

def disappear_all():
    disappear(label)
    disappear(label1)
    disappear(entry1)
    disappear(label2)
    disappear(entry2)
    disappear(label3)
    disappear(entry3)
    disappear(label4)
    disappear(entry4)
    disappear(label5)
    disappear(entry5)
    disappear(label6)
    disappear(entry6)
    disappear(submit_button)
    disappear(submit_button2)
    disappear(OK_button)



def calculation(k,t,F,n,P):
    if k==0:
        F=int(F)
        n=int(n)
        ans=F/(1+t)**n
    elif k==1:
        P=int(P)
        ans=P/t
    elif k==2:
        F=int(F)
        n=int(n)
        P=int(P)
        ans=0
        for i in range (1,n+1):
            ans+=P/(1+t)**n
        ans+=F/(1+t)**n
    ans = round(ans, 2)
    answer = "Η αξία του ομολόγου ειναι: " + str(ans)
    print(round(ans,2))
    label.config(text=answer)
    label.place(x=130, y=80,width=200,height=20)
    OK_button.place(x=450, y=170, width=50, height=20)

def calculation2(k,t,P,g):
    if k==1:
        P=int(P)
        g=float(g)
        ans=P/(t-g)
    elif k==0:
        P=int(P)
        ans=P/t
    ans=round(ans,2)
    answer = "Η αξία της μετοχής ειναι: " + str(ans)
    print(round(ans,2))
    label.config(text=answer)
    label.place(x=150, y=80,width=200,height=20)
    OK_button.place(x=450, y=170, width=50, height=20)


window = Tk()
window.geometry('500x500')
window.title('Αποτίμηση Περιουσιακών Στχοιχείων')

label=Label(window, text='Από το μενού επιλέξτε το είδος του περιουσιακού στοιχείου')
label.place(x=90,y=80)

menubar=Menu(window)
window.config(menu=menubar)

ομόλογο=Menu(menubar,tearoff=0)
menubar.add_cascade(label='ομόλογο',menu=ομόλογο)
ομόλογο.add_command(label='μηδενικό_τοκομερίδιο',command=μηδενικό_τοκομερίδιο)
ομόλογο.add_command(label='διηνεκές',command=διηνεκές)
ομόλογο.add_command(label='σύνηθες',command=σύνηθες)

μετοχή=Menu(menubar,tearoff=0)
menubar.add_cascade(label='μετοχή',menu=μετοχή)
μετοχή.add_command(label='σταθερά μερίσματα',command=σταθερά_μερίσματα)
μετοχή.add_command(label='μερίσματα αυξανόμενα με σταθερό ρυθμό',command=μερίσματα_αυξανόμενα_με_σταθερό_ρυθμό)

entry1=Entry(window, font=('Arial',10))
label1=Label(window,text="Προεξοφλητικό Επιτόκιο")

entry2=Entry(window, font=('Arial',10))
label2=Label(window,text="Ονομαστική Αξία")

entry3=Entry(window, font=('Arial',10))
label3=Label(window,text="Έτη")

entry4=Entry(window, font=('Arial',10))
label4=Label(window,text="Πληρωμή ανά έτος")

entry5=Entry(window, font=('Arial',10))
label5=Label(window,text="Μέρισμα")

entry6=Entry(window, font=('Arial',10))
label6=Label(window,text="Ρυθμός Αύξησης Μερισμάτων")

submit_button=Button(window,text="OK", command=lambda: submit(k))
submit_button2 = Button(window, text="OK", command=lambda: submit2(k))
OK_button=Button(window,text='OK',command=OK)

window.mainloop()