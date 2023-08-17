import tkinter as tk
import mysql.connector
from tkinter import *
import time
import pyglet
import random

#main screen window
mainsc=tk.Tk()
mainsc.title('ARPANET')
mainsc.configure(bg='#FFFFFF')
mainsc.geometry('1204x612')

#background
img = PhotoImage(file="/Users/apple/Desktop/Other/Class 12/Computer Science/ARPANET.png")
label = Label(mainsc,image=img)
label.place(x=0, y=0)

#equation
equ=''

def calculator():
    global equ
    def equation(n):
        global equ
        equ+=n
        info_lo=tk.Label(mainsc,text=equ,font=("Courier",19),bg='#E7D0E0',fg='#244781')
        info_lo.place(x=70,y=60)
        
    def problem(x):
        global equ
        lst,num=[],''
        for i in range(len(x)):
            if i==(len(x)-1):
                num+=x[i]
                lst.append(num)
            elif x[i].isdecimal() or x[i]=='.':
                num+=x[i]
            elif x[i]=='+':
                lst.append(num)
                lst.append('+')
                num=''
            elif x[i]=='-':
                lst.append(num)
                lst.append('-')
                num=''
            elif x[i]=='x':
                lst.append(num)
                lst.append('x')
                num=''
            elif x[i]=='/':
                lst.append(num)
                lst.append('/')
                num=''
        
        for j in range(len(lst)):
            partition = lst[j].partition('.')
            if lst[j].isdecimal():
                lst[j]=int(lst[j])
            if (partition[0].isdigit() and partition[1] == '.' and partition[2].isdigit()) or (partition[0] == '' and partition[1] == '.' and partition[2].isdigit()) or (partition[0].isdigit() and partition[1] == '.' and partition[2] == ''):
                lst[j]=float(lst[j])
        
        ans=0
        for k in range(1,len(lst),2):
            if lst[k]=='+':
                ans=lst[k-1]+lst[k+1]
                lst[k+1]=ans
            elif lst[k]=='-':
                ans=lst[k-1]-lst[k+1]
                lst[k+1]=ans
            elif lst[k]=='x':
                ans=lst[k-1]*lst[k+1]
                lst[k+1]=ans
            elif lst[k]=='/':
                ans=lst[k-1]/lst[k+1]
                lst[k+1]=ans
        
        tk.messagebox.showinfo("Your Answer!!", x+'='+str(round(ans,3)))
        info_lo=tk.Label(mainsc,text=' '*30,font=("Courier",19),bg='#E7D0E0',fg='#244781')
        info_lo.place(x=70,y=60)
        
        equ=''

    
    mainsc=tk.Tk()
    mainsc.title('CALCULATOR')
    mainsc.configure(bg='#E7D0E0')
    mainsc.geometry('350x350')
    
    info_lo=tk.Label(mainsc,text='Enter Your Equation',font=("Courier",19),bg='#E7D0E0')
    info_lo.place(x=60,y=20)
    
    info_lo=tk.Label(mainsc,text='1',font=("Courier",26),bg='#E7D0E0')
    info_lo.place(x=50,y=100)
    info_lo.bind('<Button-1>',lambda e:equation('1'))
    
    info_ln=tk.Label(mainsc,text='2',font=("Courier",26),bg='#E7D0E0')
    info_ln.place(x=120,y=100)
    info_ln.bind('<Button-1>',lambda e:equation('2'))
    
    info_lm=tk.Label(mainsc,text='3',font=("Courier",26),bg='#E7D0E0')
    info_lm.place(x=190,y=100)
    info_lm.bind('<Button-1>',lambda e:equation('3'))
    
    info_lk=tk.Label(mainsc,text='4',font=("Courier",26),bg='#E7D0E0')
    info_lk.place(x=50,y=160)
    info_lk.bind('<Button-1>',lambda e:equation('4'))
    
    info_lj=tk.Label(mainsc,text='5',font=("Courier",26),bg='#E7D0E0')
    info_lj.place(x=120,y=160)
    info_lj.bind('<Button-1>',lambda e:equation('5'))
    
    info_li=tk.Label(mainsc,text='6',font=("Courier",26),bg='#E7D0E0')
    info_li.place(x=190,y=160)
    info_li.bind('<Button-1>',lambda e:equation('6'))
    
    info_lh=tk.Label(mainsc,text='7',font=("Courier",26),bg='#E7D0E0')
    info_lh.place(x=50,y=220)
    info_lh.bind('<Button-1>',lambda e:equation('7'))
    
    info_lg=tk.Label(mainsc,text='8',font=("Courier",26),bg='#E7D0E0')
    info_lg.place(x=120,y=220)
    info_lg.bind('<Button-1>',lambda e:equation('8'))
    
    info_lf=tk.Label(mainsc,text='9',font=("Courier",26),bg='#E7D0E0')
    info_lf.place(x=190,y=220)
    info_lf.bind('<Button-1>',lambda e:equation('9'))
    
    info_le=tk.Label(mainsc,text='0',font=("Courier",26),bg='#E7D0E0')
    info_le.place(x=120,y=280)
    info_le.bind('<Button-1>',lambda e:equation('0'))
    
    info_ld=tk.Label(mainsc,text='+',font=("Courier",26),bg='#E7D0E0')
    info_ld.place(x=260,y=100)
    info_ld.bind('<Button-1>',lambda e:equation('+'))
    
    info_lc=tk.Label(mainsc,text='-',font=("Courier",26),bg='#E7D0E0')
    info_lc.place(x=260,y=160)
    info_lc.bind('<Button-1>',lambda e:equation('-'))
    
    info_lb=tk.Label(mainsc,text='x',font=("Courier",26),bg='#E7D0E0')
    info_lb.place(x=260,y=210)
    info_lb.bind('<Button-1>',lambda e:equation('x'))
    
    info_la=tk.Label(mainsc,text='/',font=("Courier",26),bg='#E7D0E0')
    info_la.place(x=190,y=280)
    info_la.bind('<Button-1>',lambda e:equation('/'))
    
    info_la=tk.Label(mainsc,text='.',font=("Courier",26),bg='#E7D0E0')
    info_la.place(x=50,y=280)
    info_la.bind('<Button-1>',lambda e:equation('.'))
    
    info_ll=tk.Label(mainsc,text='=',font=("Courier",26),bg='#E7D0E0')
    info_ll.place(x=260,y=280)
    info_ll.bind('<Button-1>',lambda e:problem(equ))
    
    mainsc.mainloop()

#modify
def modification():
    def check_password():
        password=pas.get()
        if password=='group9':
            display_code()
        else:
            tk.messagebox.showerror("Incorrect!!", "Wrong Password Entered")
    
    mainscq=tk.Tk()
    mainscq.title('PASSWORD')
    mainscq.configure(bg='#FDFDD3')
    mainscq.geometry('650x350')
    
    info_lq=tk.Label(mainscq,text='Enter Password To Check Authority',font=("Courier",17),bg="#FDFDD3")
    info_lq.place(x=150,y=80)
    
    pas=tk.Entry(mainscq,width=40)
    pas.place(x=140,y=150)

    sbutq=tk.Button(mainscq,text='CHECK PASSWORD',font=('courier',17),bg='#FDFDD3',command=check_password)
    sbutq.place(x=250,y=230)
    
    def display_code():
        mainsc=tk.Tk()
        mainsc.title('CODE NUMBERS')
        mainsc.configure(bg='#98c9e1')
        mainsc.geometry('1050x700')
        
        sc=mysql.connector.connect(host="localhost",user="root",passwd="zeel2004",database="Project")
        csr=sc.cursor()
        csr.execute("select code, link_heading from extra order by code asc")
        infot=csr.fetchall()
        infot.insert(0,('CODE','LINK HEADING'))
        infot.insert(21,('CODE','LINK HEADING'))
        z1,z2,count=0,0,0
        for i in infot:
            if count==0 or count==21:
                if count==0:
                    first=tk.Label(mainsc,text=i[0],font=('courier',12),bg='#98c9e1')
                    first.place(x=20,y=25+z1)
                    firsts=tk.Label(mainsc,text=i[1],font=('courier',12),bg='#98c9e1')
                    firsts.place(x=75,y=25+z1)
                    z1+=40
                else:
                    first=tk.Label(mainsc,text=i[0],font=('courier',12),bg='#98c9e1')
                    first.place(x=575,y=25+z2)
                    firsts=tk.Label(mainsc,text=i[1],font=('courier',12),bg='#98c9e1')
                    firsts.place(x=645,y=25+z2)
                    z2+=40
                count+=1
            elif count>20:
                first=tk.Label(mainsc,text=i[0],font=('courier',10),bg='#98c9e1')
                first.place(x=575,y=25+z2)
                firsts=tk.Label(mainsc,text=i[1],font=('courier',10),bg='#98c9e1')
                firsts.place(x=645,y=25+z2)
                z2+=30
            else:
                first=tk.Label(mainsc,text=i[0],font=('courier',10),bg='#98c9e1')
                first.place(x=20,y=25+z1)
                firsts=tk.Label(mainsc,text=i[1],font=('courier',10),bg='#98c9e1')
                firsts.place(x=75,y=25+z1)
                z1+=30
                count+=1
        
        sbut=tk.Button(mainsc,text='NEXT',font=('courier',15),bg='#E7D0E0',command=full_info)
        sbut.place(x=960,y=650)
        
        mainsc.mainloop()
    
    def full_info():
        mainsc=tk.Tk()
        mainsc.title('MODIFY')
        mainsc.configure(bg='#E7D0E0')
        mainsc.geometry('650x350')

        def display():
            
            def update():
                desc=desc_name.get()
                head=head_name.get()
                info=info_name.get()
                
                fcata=mysql.connector.connect(host="localhost",user="root",passwd="zeel2004",database="Project")
                cursora=fcata.cursor()
                x='update extra set link=\''+desc+'\' where code='+sh
                cursora.execute(x)
                fcata.commit()
                
                fcata=mysql.connector.connect(host="localhost",user="root",passwd="zeel2004",database="Project")
                cursora=fcata.cursor()
                x='update extra set link_heading=\''+head+'\' where code='+sh
                cursora.execute(x)
                fcata.commit()
                
                fcata=mysql.connector.connect(host="localhost",user="root",passwd="zeel2004",database="Project")
                cursora=fcata.cursor()
                x='update extra set info=\''+info+'\' where code='+sh
                cursora.execute(x)
                fcata.commit()
                
                tk.messagebox.showinfo("Your Info!!", "Your Information has been updated in the base.")
                
            
            disp=tk.Tk()
            disp.title('Modify')
            disp.configure(bg='#F6E9C6')
            disp.geometry('1305x1000')
            shx=sch.get()
            sh=shx.lower()
            
            first=tk.Label(disp,text='PREVIOUS INFORMATION',font=('courier',19),bg='#F6E9C6')
            first.place(x=560,y=20)
            
            
            sc=mysql.connector.connect(host="localhost",user="root",passwd="zeel2004",database="Project")
            csr=sc.cursor()
            csr.execute("select link_heading, info from extra where code="+sh)
            infot=csr.fetchall()
            
            first=tk.Label(disp,text=infot[0][0],font=('courier',19),bg='#F6E9C6')
            first.place(x=45,y=55)
            
            y=infot[0][1]
            h,x,string=0,1,''
            for i in range(len(y)):
                if i>2050 and y[i]==' ':
                    sec_x=tk.Label(disp,text=string+'....',font=('courier',12),bg='#F6E9C6')
                    sec_x.place(x=40,y=80+h)
                    break
                elif y[i]=='\n':
                    sec_x=tk.Label(disp,text=string,font=('courier',12),bg='#F6E9C6')
                    sec_x.place(x=40,y=80+h)
                    h+=20
                    string,x='',1
                elif x%160==0:
                    sec_x=tk.Label(disp,text=string,font=('courier',12),bg='#F6E9C6')
                    sec_x.place(x=40,y=80+h)
                    h+=20
                    string,x=y[i],1
                else:
                    string+=y[i]
                    x+=1
            sec_x=tk.Label(disp,text=string,font=('courier',12),bg='#F6E9C6')
            sec_x.place(x=40,y=80+h)
            
            
            first=tk.Label(disp,text='UPDATED INFORMATION',font=('courier',19),bg='#F6E9C6')
            first.place(x=560,y=500)
            
            desc_l=tk.Label(disp,text='Enter Updated description :',font=("Courier",12),bg="#F6E9C6")
            desc_l.place(x=485,y=560)
            desc_name=tk.Entry(disp)
            desc_name.place(x=700,y=560)

            head_l=tk.Label(disp,text='Enter Updated heading :',font=("Courier",12),bg="#F6E9C6")
            head_l.place(x=515,y=620)
            head_name=tk.Entry(disp,width=35)
            head_name.place(x=700,y=620)
            
            info_l=tk.Label(disp,text='Enter Updated information (Enter "\ n" for new line) :',font=("Courier",12),bg="#F6E9C6")
            info_l.place(x=300,y=680)
            info_name=tk.Entry(disp,width=45)
            info_name.place(x=700,y=680)
            
            sbut=tk.Button(disp,text='UPDATE',font=('courier',17),bg='#F6E9C6',command=update)
            sbut.place(x=650,y=730)
            
            disp.mainloop()


        info_l=tk.Label(mainsc,text='Enter Code Of Your Record To Be Modified',font=("Courier",17),bg="#E7D0E0")
        info_l.place(x=100,y=80)
        
        sch=tk.Entry(mainsc,width=20)
        sch.place(x=220,y=150)

        sbut=tk.Button(mainsc,text='CHECK',font=('courier',17),bg='#E7D0E0',command=display)
        sbut.place(x=290,y=210)

        mainsc.mainloop()
        
    mainscq.mainloop()


#addition
def add():
    def check_password():
        password=pas.get()
        if password=='group9':
            full_info()
        else:
            tk.messagebox.showerror("Incorrect!!", "Wrong Password Entered")
    
    mainscq=tk.Tk()
    mainscq.title('PASSWORD')
    mainscq.configure(bg='#FFD4B1')
    mainscq.geometry('650x350')
    
    info_lq=tk.Label(mainscq,text='Enter Password To Check Authority',font=("Courier",17),bg="#FFD4B1")
    info_lq.place(x=150,y=80)
    
    pas=tk.Entry(mainscq,width=40)
    pas.place(x=140,y=150)

    sbutq=tk.Button(mainscq,text='CHECK PASSWORD',font=('courier',17),bg='#FFD4B1',command=check_password)
    sbutq.place(x=250,y=230)
    
    def full_info():
        add=tk.Tk()
        add.title("ADD RECORDS")
        add.configure(bg="#fae7eb")
        add.geometry("830x350")

        category_l=tk.Label(add,text='Enter category of your topic :',font=("Courier",12),bg="#fae7eb")
        category_l.place(x=40,y=30)
        cat_name=tk.Entry(add,width=40)
        cat_name.place(x=400,y=30)

        refword_l=tk.Label(add,text='Enter reference words related to the topic :',font=("Courier",12),bg="#fae7eb")
        refword_l.place(x=40,y=70)
        refword_name=tk.Entry(add,width=40)
        refword_name.place(x=400,y=70)

        desc_l=tk.Label(add,text='Enter description :',font=("Courier",12),bg="#fae7eb")
        desc_l.place(x=40,y=110)
        desc_name=tk.Entry(add,width=40)
        desc_name.place(x=400,y=110)

        head_l=tk.Label(add,text='Enter heading :',font=("Courier",12),bg="#fae7eb")
        head_l.place(x=40,y=150)
        head_name=tk.Entry(add,width=40)
        head_name.place(x=400,y=150)

        fn_l=tk.Label(add,text='Enter unique name for the information :',font=("Courier",12),bg="#fae7eb")
        fn_l.place(x=40,y=190)
        fn_name=tk.Entry(add,width=40)
        fn_name.place(x=400,y=190)

        info_l=tk.Label(add,text='Enter information (Enter "\ n" for new line) :',font=("Courier",12),bg="#fae7eb")
        info_l.place(x=40,y=230)
        info_name=tk.Entry(add,width=40)
        info_name.place(x=400,y=230)


        def addition():
            cat=cat_name.get()
            refword=refword_name.get()
            desc=desc_name.get()
            head=head_name.get()
            fn=fn_name.get()
            info=info_name.get()


            fcats=mysql.connector.connect(host="localhost",user="root",passwd="zeel2004",database="Project")
            cursors=fcats.cursor()
            cursors.execute("select code from extra")
            categoriess=cursors.fetchall()
            code=1
            for i in categoriess:
                for x in i:
                    code=x+1
            
            fcata=mysql.connector.connect(host="localhost",user="root",passwd="zeel2004",database="Project")
            cursora=fcata.cursor()
            cursora.execute('insert into extra values ("' + refword + '" , "' + head + '" , "' + desc + '" , "' + cat + '" , "' + fn + '()" , "' + info + '" , ' + str(code) + ' )')
            fcata.commit()
            tk.messagebox.showinfo("Your Info!!", "Your Information has been added to the base.")

        addbut = tk.Button(add, text="ADD THE INFORMATION", font=("Courier",15), bg="#FFFFFF",command=addition)
        addbut.place(x=330, y=290)

        add.mainloop()
    mainscq.mainloop()


#extra displays
def show1(x,y):
        xtr=tk.Tk()
        xtr.title(x)
        xtr.configure(bg='#a0c9a9')
        xtr.geometry('1200x600')
        first_x=tk.Label(xtr,text=x,font=('courier',17),bg='#a0c9a9')
        first_x.place(x=40,y=40)
        h,x,string=0,1,''
        for i in range(len(y)):
            if y[i]=='\n':
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#a0c9a9')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x='',1
            elif x%160==0:
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#a0c9a9')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x=y[i],1
            else:
                string+=y[i]
                x+=1
        sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#a0c9a9')
        sec_x.place(x=40,y=80+h)
        sbuta=tk.Button(xtr,text='GO BACK',font=('courier',15),bg='#a0c9a9',command=xtr.destroy)
        sbuta.place(x=1120,y=560)
        xtr.mainloop()

def show2(x,y):
        xtr=tk.Tk()
        xtr.title(x)
        xtr.configure(bg='#fcece4')
        xtr.geometry('1200x600')
        first_x=tk.Label(xtr,text=x,font=('courier',17),bg='#fcece4')
        first_x.place(x=40,y=40)
        h,x,string=0,1,''
        for i in range(len(y)):
            if y[i]=='\n':
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#fcece4')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x='',1
            elif x%160==0:
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#fcece4')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x=y[i],1
            else:
                string+=y[i]
                x+=1
        sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#fcece4')
        sec_x.place(x=40,y=80+h)
        sbuta=tk.Button(xtr,text='GO BACK',font=('courier',15),bg='#a0c9a9',command=xtr.destroy)
        sbuta.place(x=1120,y=560)
        xtr.mainloop()

def show3(x,y):
        xtr=tk.Tk()
        xtr.title(x)
        xtr.configure(bg='#8493ca')
        xtr.geometry('1200x600')
        first_x=tk.Label(xtr,text=x,font=('courier',17),bg='#8493ca')
        first_x.place(x=40,y=40)
        h,x,string=0,1,''
        for i in range(len(y)):
            if y[i]=='\n':
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#8493ca')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x='',1
            elif x%160==0:
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#8493ca')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x=y[i],1
            else:
                string+=y[i]
                x+=1
        sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#8493ca')
        sec_x.place(x=40,y=80+h)
        sbuta=tk.Button(xtr,text='GO BACK',font=('courier',15),bg='#a0c9a9',command=xtr.destroy)
        sbuta.place(x=1120,y=560)
        xtr.mainloop()


def show4(x,y):
        xtr=tk.Tk()
        xtr.title(x)
        xtr.configure(bg='#98c9e1')
        xtr.geometry('1200x600')
        first_x=tk.Label(xtr,text=x,font=('courier',17),bg='#98c9e1')
        first_x.place(x=40,y=40)
        h,x,string=0,1,''
        for i in range(len(y)):
            if y[i]=='\n':
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#98c9e1')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x='',1
            elif x%160==0:
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#98c9e1')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x=y[i],1
            else:
                string+=y[i]
                x+=1
        sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#98c9e1')
        sec_x.place(x=40,y=80+h)
        sbuta=tk.Button(xtr,text='GO BACK',font=('courier',15),bg='#a0c9a9',command=xtr.destroy)
        sbuta.place(x=1120,y=560)
        xtr.mainloop()


def show5(x,y):
        xtr=tk.Tk()
        xtr.title(x)
        xtr.configure(bg='#bfbfbf')
        xtr.geometry('1200x600')
        first_x=tk.Label(xtr,text=x,font=('courier',17),bg='#bfbfbf')
        first_x.place(x=40,y=40)
        h,x,string=0,1,''
        for i in range(len(y)):
            if y[i]=='\n':
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#bfbfbf')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x='',1
            elif x%160==0:
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#bfbfbf')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x=y[i],1
            else:
                string+=y[i]
                x+=1
        sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#bfbfbf')
        sec_x.place(x=40,y=80+h)
        sbuta=tk.Button(xtr,text='GO BACK',font=('courier',15),bg='#a0c9a9',command=xtr.destroy)
        sbuta.place(x=1120,y=560)
        xtr.mainloop()

def show6(x,y):
        xtr=tk.Tk()
        xtr.title(x)
        xtr.configure(bg='#fbfbc7')
        xtr.geometry('1200x600')
        first_x=tk.Label(xtr,text=x,font=('courier',17),bg='#fbfbc7')
        first_x.place(x=40,y=40)
        h,x,string=0,1,''
        for i in range(len(y)):
            if y[i]=='\n':
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#fbfbc7')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x='',1
            elif x%160==0:
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#fbfbc7')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x=y[i],1
            else:
                string+=y[i]
                x+=1
        sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#fbfbc7')
        sec_x.place(x=40,y=80+h)
        sbuta=tk.Button(xtr,text='GO BACK',font=('courier',15),bg='#a0c9a9',command=xtr.destroy)
        sbuta.place(x=1120,y=560)
        xtr.mainloop()

def show7(x,y):
        xtr=tk.Tk()
        xtr.title(x)
        xtr.configure(bg='#fce4ec')
        xtr.geometry('1200x600')
        first_x=tk.Label(xtr,text=x,font=('courier',17),bg='#fce4ec')
        first_x.place(x=40,y=40)
        h,x,string=0,1,''
        for i in range(len(y)):
            if y[i]=='\n':
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#fce4ec')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x='',1
            elif x%160==0:
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#fce4ec')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x=y[i],1
            else:
                string+=y[i]
                x+=1
        sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#fce4ec')
        sec_x.place(x=40,y=80+h)
        sbuta=tk.Button(xtr,text='GO BACK',font=('courier',15),bg='#a0c9a9',command=xtr.destroy)
        sbuta.place(x=1120,y=560)
        xtr.mainloop()

def show10(x,y):
        xtr=tk.Tk()
        xtr.title(x)
        xtr.configure(bg='#e2f4e9')
        xtr.geometry('1200x600')
        first_x=tk.Label(xtr,text=x,font=('courier',17),bg='#e2f4e9')
        first_x.place(x=40,y=40)
        h,x,string=0,1,''
        for i in range(len(y)):
            if y[i]=='\n':
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#e2f4e9')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x='',1
            elif x%160==0:
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#e2f4e9')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x=y[i],1
            else:
                string+=y[i]
                x+=1
        sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#e2f4e9')
        sec_x.place(x=40,y=80+h)
        sbuta=tk.Button(xtr,text='GO BACK',font=('courier',15),bg='#a0c9a9',command=xtr.destroy)
        sbuta.place(x=1120,y=560)
        xtr.mainloop()

def show12(x,y):
        xtr=tk.Tk()
        xtr.title(x)
        xtr.configure(bg='#eee3dd')
        xtr.geometry('1200x600')
        first_x=tk.Label(xtr,text=x,font=('courier',17),bg='#eee3dd')
        first_x.place(x=40,y=40)
        h,x,string=0,1,''
        for i in range(len(y)):
            if y[i]=='\n':
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#eee3dd')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x='',1
            elif x%160==0:
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#eee3dd')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x=y[i],1
            else:
                string+=y[i]
                x+=1
        sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#eee3dd')
        sec_x.place(x=40,y=80+h)
        sbuta=tk.Button(xtr,text='GO BACK',font=('courier',15),bg='#a0c9a9',command=xtr.destroy)
        sbuta.place(x=1120,y=560)
        xtr.mainloop()
        
def show11(x,y):
        xtr=tk.Tk()
        xtr.title(x)
        xtr.configure(bg='#d89279')
        xtr.geometry('1200x600')
        first_x=tk.Label(xtr,text=x,font=('courier',17),bg='#d89279')
        first_x.place(x=40,y=40)
        h,x,string=0,1,''
        for i in range(len(y)):
            if y[i]=='\n':
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#d89279')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x='',1
            elif x%160==0:
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#d89279')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x=y[i],1
            else:
                string+=y[i]
                x+=1
        sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#d89279')
        sec_x.place(x=40,y=80+h)
        sbuta=tk.Button(xtr,text='GO BACK',font=('courier',15),bg='#a0c9a9',command=xtr.destroy)
        sbuta.place(x=1120,y=560)
        xtr.mainloop()

def show13(x,y):
        xtr=tk.Tk()
        xtr.title(x)
        xtr.configure(bg='#CCDDFF')
        xtr.geometry('1200x600')
        first_x=tk.Label(xtr,text=x,font=('courier',17),bg='#CCDDFF')
        first_x.place(x=40,y=40)
        h,x,string=0,1,''
        for i in range(len(y)):
            if y[i]=='\n':
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#CCDDFF')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x='',1
            elif x%160==0:
                sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#CCDDFF')
                sec_x.place(x=40,y=80+h)
                h+=20
                string,x=y[i],1
            else:
                string+=y[i]
                x+=1
        sec_x=tk.Label(xtr,text=string,font=('courier',12),bg='#CCDDFF')
        sec_x.place(x=40,y=80+h)
        sbuta=tk.Button(xtr,text='GO BACK',font=('courier',15),bg='#a0c9a9',command=xtr.destroy)
        sbuta.place(x=1120,y=560)
        xtr.mainloop()


#displays
def display():
    def page2(infont):
        
        #window for page 2
        disp=tk.Toplevel()
        disp.title('Search - Page 2')
        disp.configure(bg='#F4DCD6')
        disp.geometry('1300x650')
        sh=sch.get()
        
        #text for page 2
        tim=tk.Label(disp,text='PAGE 2',font=('courier',19),bg='#F4DCD6')
        tim.place(x=55,y=30)
        time1=round(time.time() * 1000)
        
        h=65
        first=tk.Label(disp,text=infont[6][0],font=('courier',17),bg='#F4DCD6',fg='#40916c')
        first.place(x=55,y=h)
        first.bind('<Button-1>',lambda e:show2(infont[6][0],infont[6][2]))
        z,sen,lst=0,'',[]
        for j in range(len(infont[6][1])):
            if j%170==0:
                lst.append(sen)
                sen=infont[6][1][j]
            else:
                sen+=infont[6][1][j]
        lst.append(sen)
        for k in lst:
            sec=tk.Label(disp,text=k,font=('courier',12),bg='#F4DCD6',fg='#40916c')
            sec.place(x=50,y=h+z)
            z+=20
        h=h+z+30
        
        #3
        first=tk.Label(disp,text=infont[7][0],font=('courier',17),bg='#F4DCD6',fg='#40916c')
        first.place(x=55,y=h)
        first.bind('<Button-1>',lambda e:show3(infont[7][0],infont[7][2]))
        z,sen,lst=0,'',[]
        for j in range(len(infont[7][1])):
            if j%170==0:
                lst.append(sen)
                sen=infont[7][1][j]
            else:
                sen+=infont[7][1][j]
        lst.append(sen)
        for k in lst:
            sec=tk.Label(disp,text=k,font=('courier',12),bg='#F4DCD6',fg='#40916c')
            sec.place(x=50,y=h+z)
            z+=20
        h=h+z+30
        
        
        #4
        first=tk.Label(disp,text=infont[8][0],font=('courier',17),bg='#F4DCD6',fg='#40916c')
        first.place(x=55,y=h)
        first.bind('<Button-1>',lambda e:show4(infont[8][0],infont[8][2]))
        z,sen,lst=0,'',[]
        for j in range(len(infont[8][1])):
            if j%170==0:
                lst.append(sen)
                sen=infont[8][1][j]
            else:
                sen+=infont[8][1][j]
        lst.append(sen)
        for k in lst:
            sec=tk.Label(disp,text=k,font=('courier',12),bg='#F4DCD6',fg='#40916c')
            sec.place(x=50,y=h+z)
            z+=20
        h=h+z+30
        
        
        #5
        first=tk.Label(disp,text=infont[9][0],font=('courier',17),bg='#F4DCD6',fg='#40916c')
        first.place(x=55,y=h)
        first.bind('<Button-1>',lambda e:show5(infont[9][0],infont[9][2]))
        z,sen,lst=0,'',[]
        for j in range(len(infont[9][1])):
            if j%170==0:
                lst.append(sen)
                sen=infont[9][1][j]
            else:
                sen+=infont[9][1][j]
        lst.append(sen)
        for k in lst:
            sec=tk.Label(disp,text=k,font=('courier',12),bg='#F4DCD6',fg='#40916c')
            sec.place(x=50,y=h+z)
            z+=20
        h=h+z+30
        
        
        #6
        first=tk.Label(disp,text=infont[10][0],font=('courier',17),bg='#F4DCD6',fg='#40916c')
        first.place(x=55,y=h)
        first.bind('<Button-1>',lambda e:show6(infont[10][0],infont[10][2]))
        z,sen,lst=0,'',[]
        for j in range(len(infont[10][1])):
            if j%170==0:
                lst.append(sen)
                sen=infont[10][1][j]
            else:
                sen+=infont[10][1][j]
        lst.append(sen)
        for k in lst:
            sec=tk.Label(disp,text=k,font=('courier',12),bg='#F4DCD6',fg='#40916c')
            sec.place(x=50,y=h+z)
            z+=20
        h=h+z+30
        
        #6
        first=tk.Label(disp,text=infont[11][0],font=('courier',17),bg='#F4DCD6',fg='#40916c')
        first.place(x=55,y=h)
        first.bind('<Button-1>',lambda e:show7(infont[11][0],infont[11][2]))
        z,sen,lst=0,'',[]
        for j in range(len(infont[11][1])):
            if j%170==0:
                lst.append(sen)
                sen=infont[11][1][j]
            else:
                sen+=infont[11][1][j]
        lst.append(sen)
        for k in lst:
            sec=tk.Label(disp,text=k,font=('courier',12),bg='#F4DCD6',fg='#40916c')
            sec.place(x=50,y=h+z)
            z+=20
        
        #time second
        time2=round(time.time() * 1000)
        
        diff_time=time2-time1
        tim=tk.Label(disp,text='Records displayed in :'+str(diff_time/1000)+' seconds',font=('courier',12),bg='#F4DCD6')
        tim.place(x=1000,y=20)
        
        calc=tk.Label(disp,text='GO BACK',font=('courier',15),bg='#F4DCD6')
        calc.place(x=1220,y=620)
        calc.bind('<Button-1>',lambda e:disp.destroy())
        
        disp.mainloop()

    
    #time first
    time1=round(time.time() * 1000)
    
    #window
    disp=tk.Toplevel()
    disp.title('Search')
    disp.configure(bg='#e1ccec')
    disp.geometry('1300x650')
    sh=sch.get()
    
    #text
    tim=tk.Label(disp,text='RELATED SEARCHES',font=('courier',19),bg='#e1ccec')
    tim.place(x=55,y=30)
    
    #connector 1
    sc=mysql.connector.connect(host="localhost",user="root",passwd="zeel2004",database="Project")
    csr=sc.cursor()
    csr.execute("select link_heading, link, info from extra where reference_words like \'%"+sh+"%\'")
    infot=csr.fetchall()
    
    #1
    if len(infot)==1 :
        first=tk.Label(disp,text=infot[0][0],font=('courier',17),bg='#e1ccec',fg='#d00000')
        first.place(x=55,y=80)
        first.bind('<Button-1>',lambda e:show1(infot[0][0],infot[0][2]))
        z,sen,lst=0,'',[]
        for j in range(len(infot[0][1])):
            if j%170==0:
                lst.append(sen)
                sen=infot[0][1][j]
            else:
                sen+=infot[0][1][j]
        lst.append(sen)
        for k in lst:
            sec=tk.Label(disp,text=k,font=('courier',12),bg='#e1ccec',fg='#d00000')
            sec.place(x=50,y=80+z)
            z+=20
        h=z+100
    
    #check more related
    elif len(infot)>1 :
        
        first=tk.Label(disp,text=infot[0][0],font=('courier',17),bg='#e1ccec',fg='#d00000')
        first.place(x=55,y=80)
        first.bind('<Button-1>',lambda e:show1(infot[0][0],infot[0][2]))
        z,sen,lst=0,'',[]
        for j in range(len(infot[0][1])):
            if j%170==0:
                lst.append(sen)
                sen=infot[0][1][j]
            else:
                sen+=infot[0][1][j]
        lst.append(sen)
        for k in lst:
            sec=tk.Label(disp,text=k,font=('courier',12),bg='#e1ccec',fg='#d00000')
            sec.place(x=50,y=80+z)
            z+=20
        h=z+100
        
        
        first=tk.Label(disp,text=infot[1][0],font=('courier',17),bg='#e1ccec',fg='#d00000')
        first.place(x=55,y=h)
        first.bind('<Button-1>',lambda e:show10(infot[1][0],infot[1][2]))
        z,sen,lst=0,'',[]
        for j in range(len(infot[1][1])):
            if j%170==0:
                lst.append(sen)
                sen=infot[1][1][j]
            else:
                sen+=infot[1][1][j]
        lst.append(sen)
        for k in lst:
            sec=tk.Label(disp,text=k,font=('courier',12),bg='#e1ccec',fg='#d00000')
            sec.place(x=50,y=h+z)
            z+=20
        h=h+z+30
        
        if len(infot)>2:
            first=tk.Label(disp,text=infot[2][0],font=('courier',17),bg='#e1ccec',fg='#d00000')
            first.place(x=55,y=h)
            first.bind('<Button-1>',lambda e:show11(infot[2][0],infot[2][2]))
            z,sen,lst=0,'',[]
            for j in range(len(infot[2][1])):
                if j%170==0:
                    lst.append(sen)
                    sen=infot[2][1][j]
                else:
                    sen+=infot[2][1][j]
            lst.append(sen)
            for k in lst:
                sec=tk.Label(disp,text=k,font=('courier',12),bg='#e1ccec',fg='#d00000')
                sec.place(x=50,y=h+z)
                z+=20
            h=h+z+30
            
            if len(infot)>3:
                first=tk.Label(disp,text=infot[3][0],font=('courier',17),bg='#e1ccec',fg='#d00000')
                first.place(x=55,y=h)
                first.bind('<Button-1>',lambda e:show12(infot[3][0],infot[3][2]))
                z,sen,lst=0,'',[]
                for j in range(len(infot[3][1])):
                    if j%170==0:
                        lst.append(sen)
                        sen=infot[3][1][j]
                    else:
                        sen+=infot[3][1][j]
                lst.append(sen)
                for k in lst:
                    sec=tk.Label(disp,text=k,font=('courier',12),bg='#e1ccec',fg='#d00000')
                    sec.place(x=50,y=h+z)
                    z+=20
                h=h+z+30
                
                if len(infot)>4:
                    first=tk.Label(disp,text=infot[4][0],font=('courier',17),bg='#e1ccec',fg='#d00000')
                    first.place(x=55,y=h)
                    first.bind('<Button-1>',lambda e:show13(infot[4][0],infot[4][2]))
                    z,sen,lst=0,'',[]
                    for j in range(len(infot[4][1])):
                        if j%170==0:
                            lst.append(sen)
                            sen=infot[4][1][j]
                        else:
                            sen+=infot[4][1][j]
                    lst.append(sen)
                    for k in lst:
                        sec=tk.Label(disp,text=k,font=('courier',12),bg='#e1ccec',fg='#d00000')
                        sec.place(x=50,y=h+z)
                        z+=20
                    h=h+z+30
    
    else:
        h,z=80,50
    
    
    #connector not same
    scr=mysql.connector.connect(host="localhost",user="root",passwd="zeel2004",database="Project")
    cusr=scr.cursor()
    cusr.execute("select link_heading, link, info from extra where reference_words not like \'%"+sh+"%\'")
    infont=cusr.fetchall()
    random.shuffle(infont)
    
    #2
    first=tk.Label(disp,text=infont[0][0],font=('courier',17),bg='#e1ccec',fg='#40916c')
    first.place(x=55,y=h)
    first.bind('<Button-1>',lambda e:show2(infont[0][0],infont[0][2]))
    z,sen,lst=0,'',[]
    for j in range(len(infont[0][1])):
        if j%170==0:
            lst.append(sen)
            sen=infont[0][1][j]
        else:
            sen+=infont[0][1][j]
    lst.append(sen)
    for k in lst:
        sec=tk.Label(disp,text=k,font=('courier',12),bg='#e1ccec',fg='#40916c')
        sec.place(x=50,y=h+z)
        z+=20
    h=h+z+30
    
    #3
    first=tk.Label(disp,text=infont[1][0],font=('courier',17),bg='#e1ccec',fg='#40916c')
    first.place(x=55,y=h)
    first.bind('<Button-1>',lambda e:show3(infont[1][0],infont[1][2]))
    z,sen,lst=0,'',[]
    for j in range(len(infont[1][1])):
        if j%170==0:
            lst.append(sen)
            sen=infont[1][1][j]
        else:
            sen+=infont[1][1][j]
    lst.append(sen)
    for k in lst:
        sec=tk.Label(disp,text=k,font=('courier',12),bg='#e1ccec',fg='#40916c')
        sec.place(x=50,y=h+z)
        z+=20
    h=h+z+30
    
    
    #4
    first=tk.Label(disp,text=infont[2][0],font=('courier',17),bg='#e1ccec',fg='#40916c')
    first.place(x=55,y=h)
    first.bind('<Button-1>',lambda e:show4(infont[2][0],infont[2][2]))
    z,sen,lst=0,'',[]
    for j in range(len(infont[2][1])):
        if j%170==0:
            lst.append(sen)
            sen=infont[2][1][j]
        else:
            sen+=infont[2][1][j]
    lst.append(sen)
    for k in lst:
        sec=tk.Label(disp,text=k,font=('courier',12),bg='#e1ccec',fg='#40916c')
        sec.place(x=50,y=h+z)
        z+=20
    h=h+z+30
    
    
    #5
    first=tk.Label(disp,text=infont[3][0],font=('courier',17),bg='#e1ccec',fg='#40916c')
    first.place(x=55,y=h)
    first.bind('<Button-1>',lambda e:show5(infont[3][0],infont[3][2]))
    z,sen,lst=0,'',[]
    for j in range(len(infont[3][1])):
        if j%170==0:
            lst.append(sen)
            sen=infont[3][1][j]
        else:
            sen+=infont[3][1][j]
    lst.append(sen)
    for k in lst:
        sec=tk.Label(disp,text=k,font=('courier',12),bg='#e1ccec',fg='#40916c')
        sec.place(x=50,y=h+z)
        z+=20
    h=h+z+30
    
    
    #6
    first=tk.Label(disp,text=infont[4][0],font=('courier',17),bg='#e1ccec',fg='#40916c')
    first.place(x=55,y=h)
    first.bind('<Button-1>',lambda e:show6(infont[4][0],infont[4][2]))
    z,sen,lst=0,'',[]
    for j in range(len(infont[4][1])):
        if j%170==0:
            lst.append(sen)
            sen=infont[4][1][j]
        else:
            sen+=infont[4][1][j]
    lst.append(sen)
    for k in lst:
        sec=tk.Label(disp,text=k,font=('courier',12),bg='#e1ccec',fg='#40916c')
        sec.place(x=50,y=h+z)
        z+=20
    h=h+z+30
    
    #6
    first=tk.Label(disp,text=infont[5][0],font=('courier',17),bg='#e1ccec',fg='#40916c')
    first.place(x=55,y=h)
    first.bind('<Button-1>',lambda e:show7(infont[5][0],infont[5][2]))
    z,sen,lst=0,'',[]
    for j in range(len(infont[5][1])):
        if j%170==0:
            lst.append(sen)
            sen=infont[5][1][j]
        else:
            sen+=infont[5][1][j]
    lst.append(sen)
    for k in lst:
        sec=tk.Label(disp,text=k,font=('courier',12),bg='#e1ccec',fg='#40916c')
        sec.place(x=50,y=h+z)
        z+=20
    
    #time second
    time2=round(time.time() * 1000)
    
    diff_time=time2-time1
    tim=tk.Label(disp,text='Records displayed in :'+str(diff_time/1000)+' seconds',font=('courier',12),bg='#e1ccec')
    tim.place(x=1000,y=20)
    
    calc=tk.Label(disp,text='GO BACK',font=('courier',15),bg='#e1ccec')
    calc.place(x=1180,y=50)
    calc.bind('<Button-1>',lambda e:disp.destroy())
    
    pg2=tk.Label(disp,text='Pg 2',font=('courier',19),bg='#e1ccec')
    pg2.place(x=1220,y=610)
    pg2.bind('<Button-1>',lambda e:page2(infont))

    disp.mainloop()

#menu
def menu():
    menu=tk.Tk()
    menu.title('MENU')
    menu.configure(bg='#bfede1')
    menu.geometry('300x350')
    
    add_con=tk.Label(menu,text='ADMIN FEATURES',font=('courier',19),bg='#bfede1')
    add_con.place(x=62,y=20)
    
    add_con=tk.Label(menu,text='ADD CONTENT',font=('courier',20))
    add_con.place(x=70,y=70)
    add_con.bind('<Button-1>',lambda e:add())

    mod_con=tk.Label(menu,text='MODIFY CONTENT',font=('courier',20))
    mod_con.place(x=50,y=140)
    mod_con.bind('<Button-1>',lambda e:modification())
    
    add_con=tk.Label(menu,text='EXTRA FEATURES',font=('courier',19),bg='#bfede1')
    add_con.place(x=62,y=210)
    
    calc=tk.Label(menu,text='CALCULATOR',font=('courier',20))
    calc.place(x=80,y=280)
    calc.bind('<Button-1>',lambda e:calculator())
    
    menu.mainloop()

#main screen buttons
    
'''filepath='Music.mp4'
window=pyglet.window.Window()
source=pyglet.media.StreamingSource
player=pyglet.media.Player()
MediaLoad=pyglet.media.load(filepath)
player.queue(MediaLoad)
player.play()
@window.event
def on_draw():
    if player.source and player.source.video_format:
        player.get_texture().blit(10,10)
pyglet.app.run()'''

sch=tk.Entry(mainsc,width=50)
sch.place(x=325,y=335)

sbuta=tk.Button(mainsc,text='SEARCH',font=('courier',19),command=display)
sbuta.place(x=820,y=337)

imag = PhotoImage(file='/Users/apple/Desktop/Other/Class 12/Computer Science/menu.png')
sbut=tk.Button(mainsc,text=' ',image=imag,font=('courier',3),command=menu)
sbut.place(x=10,y=10)

calc=tk.Label(mainsc,text='MENU',font=('courier',22),bg='#b5e8e0',fg='#FFFFFF')
calc.place(x=5,y=50)

mainsc.mainloop()