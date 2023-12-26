#Πρόγραμμα παρακολούθησης αποθεμάτων. Ο χρήσης επιλέγει την μέθοδο που προτιμά(LIFO, FIFO ή ΜΣΤΚ) και τον φάκελο
#που θα χρησιμοποιηθεί ως βάση δεδομένων.  Κατόπιν εισάγει κάθε πώληση η αγορά εμπορευμάτων. Στο μενού μπορεί να επιλέξει
#την επιλογή Άποθέματα' για να δει τα εμπορεύματα που υπάρχουν στην αποθήκη, καθώς και την επιλογή 'Αποτελέσματα' που
#εμφανίζει τις συνολικές αγορές, πωλήσεις και κόστος πωλήσεων. Ταυτόχρονα η βάση δεδομένων ενημερώνεται αυτόματα με την χρήση
#ενός αρχείου txt που εμφανίζει τις πωλήσεις ανά μήνα, ενώ περιλαμβάνει και το αντίστοιχο διάγραμμα.



from tkinter import *
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from datetime import date

class Agora:
    def __init__(self,q,p):
        self.q=q
        self.p=p

    def update(self,a):
        self.q=self.q-a




def disappear(a):
    a.place(x=0,y=0,width=0,height=0)

def disappear_all():
    global labelsapo
    for i in labels:
        disappear(i)
    for i in entries:
        disappear(i)
        i.delete(0,END)
    for i in buttons:
        disappear(i)
    for i in range(0,len(labelsapo)):
        disappear(labelsapo[i])
    disappear(submit_button)
def clear_all():
    for i in entries:
        i.delete(0,END)

def appear():
    label1.place(x=50,y=80,width=150,height=20)
    label2.place(x=50, y=110, width=150, height=20)
    entry1.place(x=200,y=80,width=150,height=20)
    entry2.place(x=200, y=110, width=150, height=20)

def agora():
    disappear_all()
    appear()
    submit_button.place(x=350,y=140,width=50,height=20)
    global litourgia
    litourgia=1

def polisi():
    disappear_all()
    appear()
    submit_button.place(x=350,y=140,width=50,height=20)
    global litourgia
    litourgia=2

def apo():
    disappear_all()
    global labelsapo
    global apothemata
    global k
    global MSTK
    global MSTKq
    j2=80
    if k==3:
        Label_=Label(window)
        labels.append(Label_)
        Label_.config(text = 'Ποσότητα: ' + str(MSTKq) + '  Τιμή: ' + str(MSTK))
        Label_.place(x=200,y=80,width=150,height=20)
    else:
        for j in range(0, len(apothemata)):
            labelsapo.append(Label(window,text=''))
            labelsapo[j].config(text = 'Ποσότητα: ' + str(apothemata[j].q) + '  Τιμή: ' + str(apothemata[j].p))
            labelsapo[j].place(x=200, y=j2, width=150, height=20)
            j2 += 30

def apot():
    disappear_all()
    label3.config(text='Αγορές: ' +str(agores) +"     Πωλήσεις: "+str(poliseis)+'     Κόστος Πωλήσεων: '+str(kostos_poliseon))
    label3.place(x=100,y=80,width=400,height=20)
def FIFO():
    global k
    k=1
    disappear_all()

def LIFO():
    global k
    k=2
    disappear_all()

def MSTKf():
    global k
    k=3
    disappear_all()

def delete_zeros():
    global apothemata
    while apothemata[0].q==0:
        for i in range (0,len(apothemata)-1):
            apothemata[i]=apothemata[i+1]
    del apothemata[len(apothemata)-1]

def submit():
    q=int(entry1.get())
    p=float(entry2.get())
    clear_all()
    if litourgia==1:
        litourgia1(q,p)
    elif litourgia==2:
        litourgia2(q,p)

def litourgia1(q,p):
    global apothemata
    apothemata.append(Agora(q,p))
    global agores
    agores+=q*p
    if k==3:
        global MSTK
        global MSTKq
        global MSTKv
        MSTKv+=p*q
        MSTKq+=q
        MSTK=(MSTKv/MSTKq)
        MSTK=round(MSTK,2)
def litourgia2(q,p):
    global k
    global apothemata
    global poliseis
    poliseis+=q*p
    polisi=p*q
    update(polisi)
    global kostos_poliseon
    if k==1:
        i=0
        sum=0
        while q>sum:
            sum+=apothemata[i].q
            i+=1
        for j in range (0,i-1):
            kostos_poliseon+=apothemata[j].p*apothemata[j].q
            q-=apothemata[j].q
            apothemata[j].update(apothemata[j].q)
        kostos_poliseon+=q*apothemata[i-1].p
        apothemata[i - 1].update(q)
        delete_zeros()
    if k==2:
        sum = 0
        i = len(apothemata) - 1
        while q > sum:
            sum += apothemata[i].q
            i -= 1
        i += 1
        for j in range(len(apothemata) - 1, i, -1):
            kostos_poliseon += apothemata[j].p * apothemata[j].q
            q -= apothemata[j].q
            apothemata[j].update(apothemata[j].q)
        kostos_poliseon += q * apothemata[i].p
        apothemata[i].update(q)
        for i in range(0, len(apothemata)):
            if apothemata[i].q == 0:
                del apothemata[i]
    if k==3:
            global MSTKq
            kostos_poliseon+=MSTK*q
            MSTKq -= q

def path_take():
    disappear(label4)
    disappear(entry3)
    disappear(path_button)
    global path
    path=entry3.get()
    global df
    df=pd.read_csv(path+'data.txt',header=None,skiprows=[0],usecols=[1],sep=' ').astype('float')
    global months
    df.index = months
    df.columns = columns = ['Πωλήσεις']

def update(polisi):
    month = date.today().month

    if month == 1:
        month = 'Ιανο.'
    elif month == 2:
        month = 'Φεβρ.'
    elif month == 3:
        month = 'Μαρτ.'
    elif month == 4:
        month = 'Απρι.'
    elif month == 5:
        month = 'Μαιο.'
    elif month == 6:
        month = 'Ιουν.'
    elif month == 7:
        month = 'Ιουλ.'
    elif month == 8:
        month = 'Αυγο.'
    elif month == 9:
        month = 'Σεπτ.'
    elif month == 10:
        month = 'Οκτο.'
    elif month == 11:
        month = 'Νοεμ.'
    elif month == 12:
        month = 'Δεκε.'
    global df
    df.loc[month]['Πωλήσεις'] += polisi
    plott(df)
    save(df)

def plott(df):
    plt.plot(df['Πωλήσεις'], c='r')
    global months
    plt.xlabel(months)
    plt.axis('off')
    global path
    plt.savefig(path+'διάγραμμα.png')


def save(df):
    global path
    df.to_csv(path+'data.txt',sep=' ')


window=Tk()
window.title('Αποθέματα')
window.geometry('600x600')

menubar=Menu(window)
window.config(menu=menubar)
menubar.add_command(label='Αγορά',command=agora)
menubar.add_command(label='Πώληση',command=polisi)
menubar.add_command(label='Απόθεμα',command=apo)
menubar.add_command(label='Αποτελέσματα',command=apot)

labels=[]
entries=[]
buttons=[]

label=Label(window,text='Επιλέξτε μέθοδο')
label1=Label(window,text='Ποσότητα')
label2=Label(window,text='Τιμή ανά μονάδα')
label3=Label(window,text=' ')
label4=Label(window,text='Φάκελος Αποθήκευσης')

labels.append(label)
labels.append(label1)
labels.append(label2)
labels.append(label3)

entry1=Entry(window,font=('Arial',10))
entry2=Entry(window,font=('Arial',10))
entry3=Entry(window,font=('Arial',10))

entries.append(entry1)
entries.append(entry2)

button1=Button(text='FIFO',command=FIFO)
button2=Button(text='LIFO',command=LIFO)
button3=Button(text='ΜΣΤΚ',command=MSTKf)
submit_button=Button(text='OK',command=submit)
path_button=Button(text='OK',command=path_take)

buttons.append(button1)
buttons.append(button2)
buttons.append(button3)

label.place(x=250,y=80,width=100,height=20)
button1.place(x=150,y=110,width=100,height=20)
button2.place(x=250,y=110,width=100,height=20)
button3.place(x=350,y=110,width=100,height=20)
label4.place(x=150,y=140,width=200,height=20)
entry3.place(x=360,y=140,width=200,height=20)
path_button.place(x=360,y=170)

global apothemata
apothemata=[]
global agores
agores=0
global poliseis
poliseis=0
global kostos_poliseon
kostos_poliseon=0
global labelsapo
labelsapo=[]
global MSTKq
MSTKq = 0
global MSTK
MSTK=0
global MSTKv
MSTKv=0

global path

global months
months=['Ιανο.','Φεβρ.','Μαρτ.','Απρι.','Μαιο.','Ιουν.','Ιουλ.','Αυγο.','Σεπτ.','Οκτο.','Νοεμ.','Δεκε.']


window.mainloop()