from tkinter import *
from tkinter import messagebox,ttk,font
from PIL import ImageTk,ImageFilter,Image,ImageDraw
# import  sqlite3
import smtplib as s
import matplotlib.pyplot
import mysql.connector

# import matplotlib.

class Login:
    def __init__(self,root):
        self.root = root
        self.root.title('Entry Page')
        self.root.geometry("%dx%d"%(self.root.winfo_screenwidth(),self.root.winfo_screenheight()))
        self.im = ImageTk.PhotoImage(file='pqr.png')
        p = Label(self.root,image = self.im)
        p.place(anchor='c',relx =.5,rely=0.5)
        details='''
            Rights of a tenant under the Indian law!

Tenancy refers to the possession or occupancy of lands, buildings or other property by 
title through a lease or on payment of rent. 
The two types of tenancy agreements in India are:

Lease Agreements which are covered by rent control laws and;
Lease and License Agreement which are not covered by rent control laws

A Lease (or Rental) Agreement is covered by restrictive rent control laws. 
The amount of rent that can be charged is determined by a formula devised by the local executive, 
legislative or judicial government, as the case maybe. For Delhi, the maximum annual rent is 10% of the cost
of construction and the market price of the land, but the cost of construction 
and the price of land are both based on historical values and not the current market valuation...
  '''
      

        bac = Label(self.root,text = details,compound = CENTER,font=('times new roman',25,'bold'),image=self.im)
        bac.pack()
        
        
        back = Label(self.root,text = 'Rental Property',font =('times new roman',30,'bold'),bg ='black',fg ='red',bd=10,relief=GROOVE)
        back.place(x= 0,y = 0,relwidth = 1)

        btn = Button(self.root,text='Enter',width = 13,font=('times new roman',20,'bold'),bg='black',fg='red',command=self.enr)
        btn.place(anchor = 'c',relx=.9,rely=.9)
        self.root.mainloop()

#=================================================================================================================================
       
    def enr(self):
        self.tp= Toplevel()
        self.tp.title('Log In')
        self.tp.geometry("%dx%d"%(self.root.winfo_screenwidth(),self.root.winfo_screenheight()))
        self.im = ImageTk.PhotoImage(file='rpk.png')
        self.bg = Label(self.tp,image=self.im)
        self.bg.pack()

        # variables for enter data

        self.firstname=StringVar()
        self.lastname=StringVar()
        self.email = StringVar()
        self.Password = StringVar()

        login_frame = Frame(self.tp,bg = 'black')
        login_frame.place(anchor="c", relx=.5, rely=.5)

        self.logo_pic = ImageTk.PhotoImage(file= 'sdl_p5.png')
        logo_lable= Label(login_frame,image = self.logo_pic,bd =2)
        logo_lable.grid(row = 0 ,columnspan =2,pady = 20)


        label_first = Label(login_frame,text= 'First Name :',compound = LEFT,font =('times new roman',20,'bold'),bg = 'black',fg='white')
        label_first.grid(row = 1,column = 0,padx= 20,pady =10)
        self.textfirst= Entry(login_frame,bd = 5,textvariable=self.firstname,relief = GROOVE,font=('',15))
        self.textfirst.grid(row = 1,column=1,padx =20)

        label_last = Label(login_frame,text= 'Last Name :',compound = LEFT,font =('times new roman',20,'bold'),bg = 'black',fg='white')
        label_last.grid(row = 2,column = 0,padx= 20,pady =10)
        self.textlast= Entry(login_frame,bd = 5,textvariable=self.lastname,relief = GROOVE,font=('',15))
        self.textlast.grid(row = 2,column=1,padx =20)

        label_email = Label(login_frame,text= 'Email :',compound = CENTER,font =('times new roman',20,'bold'),bg = 'black',fg='white')
        label_email.grid(row = 3,column = 0,padx= 20,pady =10)
        self.textemail= Entry(login_frame,bd = 5,textvariable=self.email,relief = GROOVE,font=('',15))
        self.textemail.grid(row = 3,column=1,padx =20)

        label_pass = Label(login_frame,text= 'Password :',compound = CENTER,font =('times new roman',20,'bold'),bg = 'black',fg='white')
        label_pass.grid(row = 4,column = 0,padx= 20,pady =10)
        self.textpassword = Entry(login_frame,bd = 5,show='*',textvariable=self.Password,relief = GROOVE,font=('',15))
        self.textpassword.grid(row = 4,column=1,padx =20)

        login_button_owner = Button(login_frame,text = 'Looking for property ',width = 30,font=('times new roman',14,'bold'),bg = 'yellow',fg= 'red',command=self.login)
        login_button_owner.grid(row=6,column=1,pady =10)

        login_button_owner = Button(login_frame,text = 'Login As Owner ',width = 25,font=('times new roman',14,'bold'),bg = 'yellow',fg= 'red',command =self.login_owner)
        login_button_owner.grid(row=5,column=1,pady =10)
        self.tp.mainloop()
    
#======================================================================================================================================================================    
    def login(self):
        if self.firstname.get()=='' or self.lastname.get()=='' or self.email.get()=='' or self.Password.get()=='':
            messagebox.showerror('Error','all fields are required!')

        
        else:
            if len(self.Password.get()) <6:
                messagebox.showwarning('warning','Passworn atleast 6 character!')

            else:
                mydb = mysql.connector.connect(host='localhost',user='root',password='environment@12#',database = 'library')
                cr = mydb.cursor()
                cr.execute('use library;')
                cr.execute('''create  table IF NOT EXISTS  login  (
                        f_name text,
                        l_name text,
                        email_add text,
                        password text)
                    ''')
                cr.execute("insert into login values (%s,%s,%s,%s);",(self.firstname.get(),self.lastname.get(),self.email.get(), self.Password.get()))

                mydb.commit()
                mydb.close()
                self.login_page = Toplevel()
                x=self.root.winfo_screenwidth()
                y =self.root.winfo_screenheight()
                x1= (x//2)-(950//2)
                y1=(y//2)-(650//2)
                self.login_page.geometry(f'950x660+{x1}+{y1}')
                self.login_page.title('enter the data ')
                self.login_page.config(bg='black')


                title_login_page = Label(self.login_page,text = f'welcome {self.textfirst.get()}',font =('times new roman',30,'bold'),bg ='red',fg ='black',bd=10,relief=GROOVE)
                title_login_page.place(x= 0,y = 0,relwidth = 1)


#===========    =====Variables===================================
                self.fn = StringVar()
                self.ph = StringVar()

                full_name=Label(self.login_page,text= 'Full name :',font =('times new roman',20,'bold'),fg='white',bg='black')
                full_name.place(x=80,y=100)
                self.fullname= Entry(self.login_page,textvariable=self.fn,bd = 5,width=42,relief = GROOVE,font=('',15))
                self.fullname.place(x=240,y=100)

                prorerty_type = Label(self.login_page,text= 'property type : ',font =('times new roman',20,'bold'),fg='white',bg='black')
                prorerty_type.place(x=80,y=200)
                self.p_t = StringVar()
                self.p_t.set('flat')
                self.propertytype=OptionMenu(self.login_page,self.p_t,'flat','shop','home')
                self.propertytype.config(width=12)
                self.propertytype.place(x=290,y=200)

                city = Label(self.login_page,text= 'city name: ',font =('times new roman',20,'bold'),fg='white',bg='black')
                city.place(x=485,y=200)
                self.ct = StringVar()
                self.ct.set('pune')
                self.city_name=OptionMenu(self.login_page,self.ct,'pune','mumbai','ahmedabad','chainni','delhi','bangalore','surat','patna','ujjain')
                self.city_name.config(width=12)
                self.city_name.place(x=650,y=200)


                rent = Label(self.login_page,text= 'rent :',font =('times new roman',20,'bold'), fg='white',bg='black')
                rent.place(x=90,y=300)
                self.r_price=StringVar()
                self.r_price.set('5000')
                self.rp=OptionMenu(self.login_page,self.r_price,'1000','2500','5000','7500','10000','above 10000')
                self.rp.config(width=14)
                self.rp.place(x=260,y=300)


                time = Label(self.login_page,text= 'time : ',font =('times new roman',20,'bold'),fg='white',bg='black')
                time.place(x=510,y=300)
                self.tm = StringVar()
                self.tm.set('1 month')
                self.t_p=OptionMenu(self.login_page,self.tm,'1 month','3 months','6 months','8 months','12 months','above 1 year')
                self.t_p.config(width=14)
                self.t_p.place(x=650,y=300)


                ph = Label(self.login_page,text= 'phone number :',font =('times new roman',20,'bold'),fg='white',bg='black')
                ph.place(x=80,y=400)
                self.ph_no= Entry(self.login_page,bd = 5,width=11,textvariable=self.ph,relief = GROOVE,font=('',15))
                self.ph_no.place(x=290,y=400)


                search = Button(self.login_page,text = 'search property ',width = 15,font=('times new roman',14,'bold'),bg = 'yellow',fg= 'red',command=self.get_data)
                search.place(anchor='s',relx=.5,rely=.9,relwidth=1)




                self.login_page.mainloop()

#======================================================================================================================================================================

    def get_data(self):
        if self.fn.get()=='' or self.ph.get()=='' :
            messagebox.showerror('error','All Fields Are Required!')

        else:

            self.data = Toplevel()
            x = self.root.winfo_screenwidth()
            y= self.root.winfo_screenheight()
            self.data.title('Fatched Data!')
            self.data.geometry("%dx%d"%(x,y))
            self.bg =ImageTk.PhotoImage(file = 'ss.png')
    
            b = Label(self.data,text = f'Sorry {self.fn.get()}, record not found !',compound = CENTER,font=('times new roman',40,'bold'),image = self.bg)
            b.pack()
            mydb = mysql.connector.connect(host='localhost',user='root',password='environment@12#',database = 'library')

            cr = mydb.cursor()

            cr.execute('''create table  IF NOT EXISTS  tenant_data(
                        full_name varchar(20),
                        property_type varchar(20),
                        city_name varchar(20),
                        rent varchar(20),
                        time varchar(20),
                        phone_number int
                    )

                    ''')
            cr.execute('insert into tenant_data values (%s,%s,%s,%s,%s,%s);',(self.fn.get(),self.p_t.get(), self.ct.get(),self.r_price.get(),self.tm.get(),self.ph.get()))
            

            records = cr.execute("select * from owner_list where property = %s and city = %s and rent =%s and time = %s;",(self.p_t.get(),self.ct.get(),self.r_price.get(),self.tm.get()))
            records = cr.fetchall()
            print(records)

            if  not records:
                # s_label = Label(self.data,text = f'Sorry {self.fn.get()}, record not found !',compound = CENTER,font=('times new roman',40,'bold'),image= )
                # s_label.place(anchor = 'c',relx=.5,rely=.5)
                btn = Button(self.data,text='Log Out!!!',width=20,font=('times new roman',20,'bold'),bg='white',fg='black',command=self.quit)
                btn.place(anchor = 'c',relx=.9,rely=.9)
                b = Button(self.data,text='Back',width=20,font=('times new roman',20,'bold'),bg='black',fg='red',command=self.login)
                b.place(anchor = 'c',relx=.1,rely=.9)
            yr=1
            self.lst = []

            if records:
                back = Label(self.data,text = 'Property',font =('times new roman',30,'bold'),bg ='yellow',fg ='red',bd=10,relief=GROOVE)
                back.place(x= 0,y = 0,relwidth = 1)
                f = Frame(self.data,bg ='black',relief="groove",width = self.data.winfo_screenwidth(),height=15)
                # f.place(anchor='c',relx=.25,rely=.25)
                f.place(y=75)
                s_b = Scrollbar(f)
                s_b.pack(side = RIGHT,fill = Y)
                # p =self.data.winfo_screenmmwidth()-100
                # c = self.data.winfo_screenheight()
                ls = Listbox(f,width = 95,height=17,yscrollcommand = s_b.set,font= ('times new roman',30),bg='white',fg='black')
                
                for i in range(len(records)):
                    for j,k in zip(records[i],range(7)):

                        if k ==0 :
                            ls.insert(END,f'Owner Name       :{j}')
                        if k ==1 :
                            ls.insert(END,f'Property Type      :{j}')
                        if k ==2:
                            ls.insert(END,f'City                     :{j}')
                        if k ==3:
                            ls.insert(END,f'Rant                    :{j}')
                        if k ==4:
                            ls.insert(END,f'Time Duratin       :{j}')
                        if k ==5:
                            ls.insert(END,f'Phone number     :{j}')
                        if k ==6:
                            ls.insert(END,f'Mail Id                :{j}')
                            ls.insert(END," ")
                            ls.insert(END," ")



                            self.lst.append(j)

                        yr = yr+ 1
                        ls.pack(side=LEFT,fill=BOTH,padx=1,pady=1,expand=True)
                        s_b.config(command = ls.yview)
                    btn = Button(self.data,text='Log Out!!!',width=20,font=('times new roman',20,'bold'),bg='black',fg='red',command=self.quit)
                    btn.place(anchor = 'c',relx=.9,rely=.95)
                    bt = Button(self.data,text = 'Connect',width= 20,font = ('times new roman',20,'bold'),bg='black',fg='red',command=self.send_mail)
                    bt.place(anchor='c',relx=0.5,rely=0.95)
                    b = Button(self.data,text='Back',width=20,font=('times new roman',20,'bold'),bg='black',fg='red',command=self.login)
                    b.place(anchor = 'c',relx=.1,rely=.95)

            mydb.commit()
            mydb.close()

            
            self.data.mainloop()

    def send_mail(self):
        self.mail =Toplevel()
        self.mail.title('sending mail to owners')
        self.mail.geometry('%dx%d'%(self.root.winfo_screenwidth(),self.root.winfo_screenheight()))
        self.mail.config(bg='black')
        self.im = ImageTk.PhotoImage(file='pk.png')
        self.bc = Label(self.mail,text = 'Thank You!!!',compound = CENTER,font=('times new roman',90,'bold'),fg='white',image=self.im)
        self.bc.pack()
    
        btn = Button(self.mail,text='Log Out!!!',width=20,font=('times new roman',20,'bold'),bg='white',fg='black',command=self.quit)
        btn.place(anchor = 'c',relx=.9,rely=.9)

        self.mail.mainloop()

        ob = s.SMTP('smtp.gmail.com',587)
        ob.starttls()
        ob.login('tenantproperty2000@gmail.com','Tanant@12#')
        self.subject = 'Tenant Propery'
        self.body = f'{self.fn.get()} looking for property to contact that person  phone no is : {self.ph.get()}'

        self.msss = f'Subject:{self.subject} \n\n\n {self.body}'

        self.lst_add= self.lst
        ob.sendmail('tenantproperty2000@gmail.com',self.lst_add,self.msss)
        ob.quit()

    

    def quit(self):
       
        self.textlast.delete(0,END)
        self.textemail.delete(0,END)
        self.textpassword.delete(0,END)
        self.textfirst.delete(0,END)
        self.root.destroy()
    def login_owner(self):
        if self.firstname.get()=='' or self.lastname.get()=='' or self.email.get()=='' or self.Password.get()=='':
            messagebox.showerror('Error','all fields are required!')

        
        else:
            if len(self.Password.get()) <6:
                messagebox.showwarning('warning','Passworn atleast 6 character!')
            else:
                mydb = mysql.connector.connect(host='localhost',user='root',password='environment@12#',database = 'library')
                cr = mydb.cursor()
            
                cr.execute('use library;')
            
                cr.execute('''create  table IF NOT EXISTS  login  (
                        f_name text,
                        l_name text,
                        email_add text,
                        password text)
                    ''')
                cr.execute("insert into login values (%s,%s,%s,%s);",(self.firstname.get(),self.lastname.get(),self.email.get(), self.Password.get()))
            
                mydb.commit()
                mydb.close()
                self.login_page = Toplevel()
                x=self.root.winfo_screenwidth()
                y =self.root.winfo_screenheight()
                x1= (x//2)-(950//2)
                y1=(y//2)-(650//2)
                self.login_page.geometry(f'950x660+{x1}+{y1}')
                self.login_page.title('enter the data ')
                self.login_page.config(bg='black')
        
    
                title_login_page = Label(self.login_page,text = f'welcome {self.textfirst.get()}',font =('times new roman',30,'bold'),bg ='red',fg ='black',bd=10,relief=GROOVE)
                title_login_page.place(x= 0,y = 0,relwidth = 1)
    
    
#===========    ======================================================================================================================================================
                self.fn = StringVar()
                self.ph = StringVar()
                self.eml = StringVar()
    
                full_name=Label(self.login_page,text= 'Full name :',font =('times new roman',20,'bold'),fg='white',bg='black')
                full_name.place(x=80,y=100)
                self.fullname= Entry(self.login_page,textvariable=self.fn,bd = 5,width=42,relief = GROOVE,font=('',15))
                self.fullname.place(x=240,y=100)
    
                prorerty_type = Label(self.login_page,text= 'property type : ',font =('times new roman',20,'bold'),fg='white',bg='black')
                prorerty_type.place(x=80,y=200)
                self.p_t = StringVar()
                self.p_t.set('flat')
                self.propertytype=OptionMenu(self.login_page,self.p_t,'flat','shop','home')
                self.propertytype.config(width=12)
                self.propertytype.place(x=290,y=200)
    
                city = Label(self.login_page,text= 'city name: ',font =('times new roman',20,'bold'),fg='white',bg='black')
                city.place(x=485,y=200)
                self.ct = StringVar()
                self.ct.set('pune')
                self.city_name=OptionMenu(self.login_page,self.ct,'pune','mumbai','ahmedabad','chainni','delhi','bangalore','surat','patna','ujjain')
                self.city_name.config(width=12)
                self.city_name.place(x=650,y=200)
    
    
                rent = Label(self.login_page,text= 'rent :',font =('times new roman',20,'bold'), fg='white',bg='black')
                rent.place(x=90,y=300)
                self.r_price=StringVar()
                self.r_price.set('5000')
                self.rp=OptionMenu(self.login_page,self.r_price,'1000','2500','5000','7500','10000','above 10000')
                self.rp.config(width=14)
                self.rp.place(x=260,y=300)
                
    
                time = Label(self.login_page,text= 'time : ',font =('times new roman',20,'bold'),fg='white',bg='black')
                time.place(x=510,y=300)
                self.tm = StringVar()
                self.tm.set('1 month')
                self.t_p=OptionMenu(self.login_page,self.tm,'1 month','3 months','6 months','8 months','12 months','above 1 year')
                self.t_p.config(width=14)
                self.t_p.place(x=650,y=300)
    
    
                ph = Label(self.login_page,text= 'phone number :',font =('times new roman',20,'bold'),fg='white',bg='black')
                ph.place(x=80,y=400)
                self.ph_no= Entry(self.login_page,bd = 5,width=11,textvariable=self.ph,relief = GROOVE,font=('',15))
                self.ph_no.place(x=290,y=400)
    
                email = Label(self.login_page,text= 'email :',font =('times new roman',20,'bold'),fg='white',bg='black')
                email.place(x=80,y=500)
                self.em= Entry(self.login_page,bd = 5,width=35,textvariable=self.eml,relief = GROOVE,font=('',15))
                self.em.place(x=200,y=500)
    
    
                search = Button(self.login_page,text = 'Conform ',width = 15,font=('times new roman',14,'bold'),bg = 'yellow',fg= 'red',command=self.conform_owner)
                search.place(anchor='s',relx=.5,rely=.95,relwidth=1)
                
                
                self.login_page.mainloop()

    def conform_owner(self):
        if self.firstname.get()=='' or self.ph_no.get()=='' or self.em.get()=='' :
            messagebox.showerror('Error','all fields are required!')
        else:
            messagebox.showinfo('done','you succesfully created account.')

            mydb = mysql.connector.connect(host='localhost',user='root',password='environment@12#',database = 'library')
            cr = mydb.cursor()
            cr.execute("insert into owner_list values(%s,%s,%s,%s,%s,%s,%s);",(self.fn.get(), self.p_t.get(),self.ct.get(),self.r_price.get(),self.tm.get(),self.ph.get(),self.eml.get()))

            mydb.commit()
            mydb.close()

            self.mail_o =Toplevel()
            self.mail_o.title('sending mail to owners')
            self.mail_o.geometry('%dx%d'%(self.root.winfo_screenwidth(),self.root.winfo_screenheight()))
            # self.mail_o.config(bg='black')
            self.im = ImageTk.PhotoImage(file='pk.png')
            self.bc = Label(self.mail_o,text = 'Thank You!!!',compound = CENTER,font=('times new roman',90,'bold'),fg='white',image=self.im)
            self.bc.pack()

            btn = Button(self.mail_o,text='Log Out!!!',width=20,font=('times new roman',20,'bold'),bg='white',fg='black',command=self.quit)
            btn.place(anchor = 'c',relx=.9,rely=.9)


            self.mail_o.mainloop()

            ob = s.SMTP('smtp.gmail.com',587)
            ob.starttls()
            ob.login('tenantproperty2000@gmail.com','Tanant@12#')
            self.subject = 'Tenant Propery'
            self.body = f'Thank you {self.fn.get()} to suppoert us!'    
            self.msss = f'Subject:{self.subject} \n\n\n {self.body}'
          
            ob.sendmail('tenantproperty2000@gmail.com',self.eml.get(),self.msss)
            ob.quit()
          
#===============================================================================================================================================================

root = Tk()
ob = Login(root)


