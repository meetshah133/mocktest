import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import sqlite3
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import  random
import  numpy as np


class Welcome:
    def __init__(self, root):
        self.root = root

        welcomeimage = PhotoImage(file="welcomePage.png")
        self.frame1 = Frame(root)
        welcomelabel = Label(self.frame1, image=welcomeimage, height=1000, width=720)
        welcomelabel.grid(row=0, column=0)
        nextbutton = PhotoImage(file="nextButtonIcon.png")
        self.nextbutton = Button(self.frame1, image=nextbutton, command=lambda: Frontpage(root),relief="flat",width=118,height=40)
        self.nextbutton.grid(row=0, column=0, sticky='s', pady=80)

        self.frame1.grid(row=0, column=0, sticky='nsew')
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.columnconfigure(0, weight=1)

        root.mainloop()


class Frontpage:

    def clickedStudent(self):
        self.backframe.destroy()
        a = StudentLogin(root)

    def clickedFaculty(self):
        self.backframe.destroy()
        b=TeacherLogin(root)

    def __init__(self, root):
        self.root = root
        background = PhotoImage(file="background.png")
        self.backframe = Frame(self.root)
        backround = Label(self.backframe, image=background)
        backround.grid(row=0, sticky='nsew')
        backholdframe = Frame(self.backframe)
        self.frontframe = Frame(backholdframe, bg='white', relief='raised', bd=2)
        facultyicon = PhotoImage(file="facultyIcon.png")
        self.facultyButton = Button(self.frontframe, image=facultyicon, bg="white", relief="flat",
                                    command=self.clickedFaculty)
        self.facultyButton.grid(row=0, column=0, pady=50, padx=50, sticky='nsew')
        studenticon = PhotoImage(file="studentIcon1.png")
        self.studentButton = Button(self.frontframe, image=studenticon, bg="white", relief='flat',
                                    command=self.clickedStudent)
        self.studentButton.grid(row=0, column=1, sticky='nsew', padx=50, pady=50, ipadx=20, ipady=10)


        self.frontframe.grid(row=1, column=1, sticky='news')
        self.frontframe.rowconfigure(0, weight=1)
        self.frontframe.rowconfigure(1, weight=1)
        self.frontframe.rowconfigure(2, weight=1)
        self.frontframe.rowconfigure(3, weight=1)
        self.frontframe.rowconfigure(4, weight=1)
        self.frontframe.rowconfigure(5, weight=1)

        self.frontframe.columnconfigure(0, weight=1)
        self.frontframe.columnconfigure(1, weight=1)

        backholdframe.grid(row=0, column=0)
        backholdframe.rowconfigure(0, weight=1)
        backholdframe.rowconfigure(1, weight=5)
        backholdframe.rowconfigure(2, weight=1)
        backholdframe.columnconfigure(0, weight=1)
        backholdframe.columnconfigure(1, weight=5)
        backholdframe.columnconfigure(2, weight=1)
        self.backframe.grid(row=0, sticky='nsew')
        self.backframe.rowconfigure(0, weight=1)
        self.backframe.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        root.mainloop()


class Student:
    conn = sqlite3.connect("mockTest.db")
    cur = conn.cursor()

    def __init__(self, root):

        self.root = root
        backgroundimage = PhotoImage(file="background.png")
        self.signupBackFrame = Frame(root)
        backlabel = Label(self.signupBackFrame,image=backgroundimage).grid(row=0,column=0,sticky='nsew')
        self.signupBackFrame2 = Frame(self.signupBackFrame)
        signupBackFrame1 = Frame(self.signupBackFrame2)


        self.signupform = Frame(signupBackFrame1, bg='white', bd=2, relief='raised')
        singupicon = PhotoImage(file="studentIcon.png")
        icon = Label(self.signupform, image=singupicon, bg='white').grid(row=0,column=0, sticky='ne', pady=10)
        namel = Label(self.signupform, text="Enter your name :", font=("Times", "15"), bg='white', padx=10).grid(row=1,
                                                                                                                 column=0,
                                                                                                                 sticky='nw',padx=25,pady=15)
        self.name = Entry(self.signupform, font=("Times", "15"), bg='#E5EFE7')
        self.name.grid(row=1, column=1, sticky='new',padx=25,pady=15)

        pidl = Label(self.signupform, text="Enter your pid no. :", font=("Times", "15"), bg='white', padx=10).grid(
            row=2, column=0, sticky='nw',padx=25,pady=15)
        self.pid = Entry(self.signupform, font=("Times", "15"), bg='#E5EFE7')
        self.pid.grid(row=2, column=1, sticky='new',padx=25,pady=15)

        passl = Label(self.signupform, text="Create a new password : \n (minimum 8 characters)", font=("Times", "15"),
                      bg='white', padx=10).grid(row=3, column=0, sticky='nw',padx=25,pady=15)
        self.passw = Entry(self.signupform, font=("Times", "15"), bg='#E5EFE7', show='*')
        self.passw.grid(row=3, column=1, sticky='new',padx=25,pady=15)

        cpassl = Label(self.signupform, text="Confirm your password :", font=("Times", "15"), bg='white', padx=10).grid(
            row=4, column=0, sticky='nw',padx=25,pady=15)
        self.cpassw = Entry(self.signupform, font=("Times", "15"), bg='#E5EFE7', show='*')
        self.cpassw.grid(row=4, column=1, sticky='new',padx=25,pady=15)
        securityl = Label(self.signupform, text="What is your pet name :\n (security question) ", font=("Times", "15"),
                          bg='white', padx=10).grid(row=5, column=0, sticky='nw',padx=25,pady=15)
        self.securitya = Entry(self.signupform, font=("Times", "15"), bg='#E5EFE7')
        self.securitya.grid(row=5, column=1, sticky='new',padx=25,pady=15)
        submitIcon = PhotoImage(file="submitButtonIcon.png")
        submit = Button(self.signupform, image=submitIcon, font=("Times", "15"), bg='white', fg='white',
                        activebackground='#069778', command=self.createuser,relief='flat')
        submit.grid(row=6, columnspan=2, sticky='s',pady=15)
        backIcon = PhotoImage(file="backButtonIcon.png")
        goback = Button(self.signupform, image=backIcon, bg="white", command=lambda: StudentLogin(root),
                        relief="flat").grid(
            row=7 , columnspan=2, padx=20,pady=10)
        self.signupform.rowconfigure(0, weight=1)
        self.signupform.rowconfigure(1, weight=1)
        self.signupform.rowconfigure(2, weight=1)
        self.signupform.rowconfigure(3, weight=1)
        self.signupform.rowconfigure(4, weight=1)
        self.signupform.rowconfigure(5, weight=1)
        self.signupform.rowconfigure(6, weight=1)
        self.signupform.rowconfigure(7, weight=1)

        self.signupform.columnconfigure(0, weight=1)
        self.signupform.columnconfigure(1, weight=1)
        self.signupform.columnconfigure(2, weight=1)
        self.signupform.grid(row=1, column=1, sticky='nsew')

        self.signupBackFrame.rowconfigure(0,weight=1)
        self.signupBackFrame.columnconfigure(0, weight=1)


        self.signupBackFrame2.rowconfigure(0,weight=1)
        self.signupBackFrame2.rowconfigure(1, weight=7)
        self.signupBackFrame2.rowconfigure(2, weight=1)
        self.signupBackFrame2.columnconfigure(0, weight=1)
        self.signupBackFrame2.columnconfigure(1, weight=7)
        self.signupBackFrame2.columnconfigure(2, weight=1)
        self.signupBackFrame2.grid(row=0,column=0)
        signupBackFrame1.rowconfigure(0, weight=1)
        signupBackFrame1.rowconfigure(1, weight=5)
        signupBackFrame1.rowconfigure(2, weight=1)
        signupBackFrame1.columnconfigure(0, weight=1)
        signupBackFrame1.columnconfigure(1, weight=4)
        signupBackFrame1.columnconfigure(2, weight=1)
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0,weight=1)

        self.signupBackFrame.grid(row=0,column=0,sticky='nsew')
        signupBackFrame1.grid(row=1,column=1,sticky='nsew')

        root.mainloop()

    def createuser(self):
        sname = self.name.get()
        pid = self.pid.get()
        spass = str(self.passw.get())
        cpassd = str(self.cpassw.get())
        security = self.securitya.get().lower()
        if (len(sname) != 0 and len(pid) != 0 and len(spass) != 0 and len(cpassd) != 0 and len(security) != 0):
            if(sname.isdigit()):
                nameerror = messagebox.showerror("Name Error", "Name should only contain characters")

            else:
                if (len(spass) > 7):
                    if (spass == cpassd):
                        self.cur.execute(
                        '''Create Table if not exists Studentdetails(sname varchar(50),pid varchar(50) UNIQUE ,spass varchar(50),security char)''')
                        try:
                            self.cur.execute("Insert into Studentdetails(sname,pid,spass,security) values(?,?,?,?)",
                                             (sname, pid, spass, security))
                        except:
                            userexist = messagebox.showerror("Error", "User already exist !!")
                            return
                        successful = messagebox.showinfo("Registration", "Registration Successfull !")
                        self.conn.commit()
                        self.conn.close()
                        self.signupBackFrame.destroy()
                        a=StudentLogin(root)






                    else:
                        passwerror = messagebox.showerror("Password Error",
                                                          "Password and confirmed password didnot matched !!")
                else:
                    paswdlerror = messagebox.showerror("Error", "Password should be atleast 8 characters long!!")

        else:
            emptyerror = messagebox.showerror("Error", "All fields are required")

    def viewtable(self):
        self.cur.execute("Select * from Studentdetails")
        for row in self.cur:
            print(row)


class StudentLogin:

    #uerpass = StringVar()
    con = sqlite3.connect("mockTest.db")
    cur = con.cursor()
    def loginStudent(self):


        self.spid = self.pid.get()
        self.spass = self.userpass.get()
        if(len(self.spid) >= 0 and len(self.spass) > 0):
          if(len(self.spass)>7):
              try:
                  self.cur.execute('''SELECT pid,spass from Studentdetails where pid=? and spass =?''',(self.spid,self.spass))
                  l=[]
                  for r in self.cur:
                      l.append((r))
                      print(l)
                  if(l[0]==(str(self.spid),str(self.spass))):
                      success = messagebox.showinfo("Login","Login Successfull")
                      b=StudentHome(root,self.spid)


              except:
                  error = messagebox.showerror("User Error", "User does not exist")

            #else:
             #   error = messagebox.showerror("User Error","User does not exist")
          else:
            paswdlerror = messagebox.showerror("Error", "Password should be atleast 8 characters long!!")
          #try:
           #   self.cur.execute('''SELECT pid,spass from Studentdetails where pid=? and spass = ?''', (str(spid),str(spass)))
            #  success = messagebox.showinfo("Login", "Login Successfull")


        else:
            error1 = messagebox.showerror("Error", "All fields are required !!!")


    def __init__(self, root):
        userp = StringVar()

        self.root = root
        background = PhotoImage(file="background.png")
        self.Loginframe =  Frame(self.root)
        loginbackround = Label(self.Loginframe,image=background)
        loginbackround.grid(row=0, sticky='nsew')
        Loginframe2 = Frame(self.Loginframe)
        Loginframe3 = Frame(Loginframe2,bg='white',relief='raised')

        loginicon = PhotoImage(file="loginIcon.png")
        iconlabel = Label(Loginframe3,image=loginicon,bg="white").grid(row=0,columnspan=2,pady=20)

        pidl = Label(Loginframe3, text="Enter your pid no. :", font=("Times", "15"), bg='white', padx=10).grid(
            row=1, column=0, sticky='nw',pady=20,padx=10)
        self.pid = Entry(Loginframe3, font=("Times", "15"), bg='#E5EFE7')
        self.pid.grid(row=1, column=1, sticky='new',pady=20,padx=10)

        passl = Label(Loginframe3, text="Enter your password :", font=("Times", "15"), bg='white').grid(
            row=2, column=0, sticky='nw',pady=20,padx=20)
        self.userpass = Entry(Loginframe3, font=("Times", "15"), show="*", bg='#E5EFE7')
        self.userpass.grid(row=2, column=1, sticky='new', pady=20, padx=10)

        forget = PhotoImage(file="forgetpassword.png")
        signup = Button(Loginframe3, image=forget, bg="white", command=lambda: Reset(root), relief="flat").grid(
            row=4, pady=10, column=0, padx=20)

        signupIcon = PhotoImage(file="newusers.png")
        signup = Button(Loginframe3, image=signupIcon, bg="white", command=lambda: Student(root), relief="flat").grid(
            row=4, pady=30, column=1, padx=20)

        backIcon = PhotoImage(file="backButton.png")
        signup = Button(Loginframe3, image=backIcon, bg="white", command=lambda: Frontpage(root), relief="flat").grid(
            row=5, pady=30, column=0,sticky=W,padx=20)

        submiticon = PhotoImage(file="loginnow.png")
        submit = Button(Loginframe3, image=submiticon, bg="white", command=self.loginStudent, relief="flat").grid(row=5,
                                                                                                                  pady=5,
                                                                                                                  column=0,
                                                                                                                  columnspan=2,
                                                                                                                  padx=20)


        Loginframe3.grid(row=1,column=1,sticky='news')
        Loginframe3.rowconfigure(0,weight=1)
        Loginframe3.rowconfigure(1, weight=1)
        Loginframe3.rowconfigure(2, weight=1)
        Loginframe3.rowconfigure(3, weight=1)
        Loginframe3.rowconfigure(4, weight=1)
        Loginframe3.rowconfigure(5, weight=1)
        Loginframe3.columnconfigure(0, weight=1)
        Loginframe3.columnconfigure(1, weight=2)
        Loginframe3.columnconfigure(2, weight=1)
        Loginframe2.grid(row=0,column=0)
        Loginframe2.rowconfigure(0,weight=1)
        Loginframe2.rowconfigure(1,weight=3)
        Loginframe2.rowconfigure(2,weight=1)
        Loginframe2.columnconfigure(0,weight=1)
        Loginframe2.columnconfigure(1,weight=2)
        Loginframe2.columnconfigure(2,weight=1)
        self.Loginframe.grid(row=0,sticky='nsew')
        self.Loginframe.rowconfigure(0,weight=1)
        self.Loginframe.columnconfigure(0,weight=1)
        root.mainloop()


class Reset:
    con = sqlite3.connect("mockTest.db")
    cur = con.cursor()
    def checkSecurity(self):


        self.spid = self.pid.get()
        self.securityvalue = self.secuityans.get().lower()
        if(len(self.spid)!=0 and len(self.securityvalue)!=0):

            self.cur.execute("Select pid,security from Studentdetails WHERE pid = ? and security = ?", (str(self.spid),str(self.securityvalue)))
            securityResult=[]
            for r in self.cur:
                securityResult.append(r)
            if(len(securityResult)!=0):
                print(securityResult)
                if(securityResult[0][0] == str(self.spid) and securityResult[0][1] == str(self.securityvalue)):
                    print(securityResult)
                    a=self.resetPassword()
            else:
                incorrectAns = messagebox.showerror("Incorrect Security Answer","You are not allowed to change the password")


        else:
            error1 = messagebox.showerror("Error", "All fields are required !!!")


    def __init__(self, root):
        userp = StringVar()

        self.root = root
        background = PhotoImage(file="background.png")
        self.Resetframe =  Frame(self.root)
        loginbackround = Label(self.Resetframe, image=background)
        loginbackround.grid(row=0, sticky='nsew')
        Resetframe2 = Frame(self.Resetframe)
        self.Resetframeframe3 = Frame(Resetframe2,bg='white',relief='raised')
        forgeticon = PhotoImage(file="forgetIcon.png")
        iconlabel = Label(self.Resetframeframe3,image=forgeticon,bg="white").grid(row=0,columnspan=2,pady=20)
        pidl = Label(self.Resetframeframe3, text="Enter your pid no. :", font=("Times", "15"), bg='white', padx=10).grid(
            row=1, column=0, sticky='nw',pady=20,padx=10)

        self.pid = Entry(self.Resetframeframe3, font=("Times", "15"), bg='#E5EFE7')
        self.pid.grid(row=1, column=1, sticky='new',pady=20,padx=10)
        securityl = Label(self.Resetframeframe3, text="Whats is your pet name :", font=("Times", "15"), bg='white').grid(
            row=2, column=0, sticky='nw',pady=20,padx=20)
        self.secuityans = Entry(self.Resetframeframe3, font=("Times", "15"), bg='#E5EFE7')
        self.secuityans.grid(row=2, column=1, sticky='new', pady=20, padx=10)

        self.submiticon = PhotoImage(file="submitButton.png")
        self.submit = Button(self.Resetframeframe3, image=self.submiticon,bg="white",command=self.checkSecurity,relief="flat")
        self.submit.grid(row=3,pady=30,columnspan=2,padx=20)
        backIcon = PhotoImage(file="backButtonIcon.png")
        goback = Button(self.Resetframeframe3, image=backIcon, bg="white", command=lambda: StudentLogin(root),
                        relief="flat").grid(
            row=4, columnspan=2, padx=20,pady=10)



        self.Resetframeframe3.grid(row=1,column=1,sticky='news')
        self.Resetframeframe3.rowconfigure(0,weight=1)
        self.Resetframeframe3.rowconfigure(1, weight=1)
        self.Resetframeframe3.rowconfigure(2, weight=1)
        self.Resetframeframe3.rowconfigure(3, weight=1)
        self.Resetframeframe3.rowconfigure(4, weight=1)
        self.Resetframeframe3.rowconfigure(5, weight=1)
        self.Resetframeframe3.columnconfigure(0, weight=1)
        self.Resetframeframe3.columnconfigure(1, weight=2)
        self.Resetframeframe3.columnconfigure(2, weight=1)
        Resetframe2.grid(row=0,column=0)
        Resetframe2.rowconfigure(0,weight=1)
        Resetframe2.rowconfigure(1,weight=3)
        Resetframe2.rowconfigure(2,weight=1)
        Resetframe2.columnconfigure(0,weight=1)
        Resetframe2.columnconfigure(1,weight=2)
        Resetframe2.columnconfigure(2,weight=1)
        self.Resetframe.grid(row=0, sticky='nsew')
        self.Resetframe.rowconfigure(0, weight=1)
        self.Resetframe.columnconfigure(0, weight=1)
        root.mainloop()
    def resetPassword(self):
        self.submit.destroy()
        newpassl = Label(self.Resetframeframe3, text="Enter your new password : ", font=("Times", "15"), bg='white').grid(
            row=3, column=0, sticky='nw',pady=20,padx=20)
        self.newpasse = Entry(self.Resetframeframe3, font=("Times", "15"), bg='#E5EFE7',show='*')
        self.newpasse.grid(row=3, column=1, sticky='new', pady=20, padx=10)
        confirmpassl = Label(self.Resetframeframe3, text="Confirm your new password : ", font=("Times", "15"),
                         bg='white').grid(row=4, column=0, sticky='nw', pady=20, padx=20)
        self.confirmpasse = Entry(self.Resetframeframe3, font=("Times", "15"), bg='#E5EFE7', show='*')
        self.confirmpasse.grid(row=4, column=1, sticky='new', pady=20, padx=10)
        self.submit2 = Button(self.Resetframeframe3, image=self.submiticon,bg="white",command=self.chnagePassword,relief="flat")
        self.submit2.grid(row=5,pady=30,columnspan=2,padx=20)


    def chnagePassword(self):
        self.newpass = self.newpasse.get()
        self.confirmpass = self.confirmpasse.get()
        if(len(self.newpass)>7 and len(self.confirmpass)>7):

            if (self.newpass == self.confirmpass):
                self.cur.execute("Update Studentdetails Set spass = ?", [str(self.newpass)])
                con.commit()
                success = messagebox.showinfo("Password Update ", "Password Changed Successfully")
            else:
                passerror = messagebox.showerror("Password Error", "Entered Password and Confirmed Password didnot match")
        else:
            leneror = messagebox.showerror("Password Length Error","Password Should be minimum 8 characters longs")


class Teacher:
    conn = sqlite3.connect("mockTest.db")
    cur = conn.cursor()

    def __init__(self, root):
        #self.viewtable()
        self.root = root
        backgroundimage = PhotoImage(file="background.png")
        self.signupBackFrame = Frame(root)
        backlabel = Label(self.signupBackFrame,image=backgroundimage).grid(row=0,column=0,sticky='nsew')
        self.signupBackFrame2 = Frame(self.signupBackFrame)
        signupBackFrame1 = Frame(self.signupBackFrame2)


        self.signupform = Frame(signupBackFrame1, bg='white', bd=2, relief='raised')
        singupicon = PhotoImage(file="loginIcon.png")
        icon = Label(self.signupform, image=singupicon, bg='white').grid(row=0,column=0, sticky='ne', pady=10)
        namel = Label(self.signupform, text="Enter your name :", font=("Times", "15"), bg='white', padx=10).grid(row=1,
                                                                                                                 column=0,
                                                                                                                 sticky='nw',padx=25,pady=15)
        self.name = Entry(self.signupform, font=("Times", "15"), bg='#E5EFE7')
        self.name.grid(row=1, column=1, sticky='new',padx=25,pady=15)

        pidl = Label(self.signupform, text="Enter your pid no. :", font=("Times", "15"), bg='white', padx=10).grid(
            row=2, column=0, sticky='nw',padx=25,pady=15)
        self.pid = Entry(self.signupform, font=("Times", "15"), bg='#E5EFE7')
        self.pid.grid(row=2, column=1, sticky='new',padx=25,pady=15)

        passl = Label(self.signupform, text="Create a new password : \n (minimum 8 characters)", font=("Times", "15"),
                      bg='white', padx=10).grid(row=3, column=0, sticky='nw',padx=25,pady=15)
        self.passw = Entry(self.signupform, font=("Times", "15"), bg='#E5EFE7', show='*')
        self.passw.grid(row=3, column=1, sticky='new',padx=25,pady=15)

        cpassl = Label(self.signupform, text="Confirm your password :", font=("Times", "15"), bg='white', padx=10).grid(
            row=4, column=0, sticky='nw',padx=25,pady=15)
        self.cpassw = Entry(self.signupform, font=("Times", "15"), bg='#E5EFE7', show='*')
        self.cpassw.grid(row=4, column=1, sticky='new',padx=25,pady=15)
        securityl = Label(self.signupform, text="What is your pet name :\n (security question) ", font=("Times", "15"),
                          bg='white', padx=10).grid(row=5, column=0, sticky='nw',padx=25,pady=15)
        self.securitya = Entry(self.signupform, font=("Times", "15"), bg='#E5EFE7')
        self.securitya.grid(row=5, column=1, sticky='new',padx=25,pady=15)
        submitIcon = PhotoImage(file="submitButtonIcon.png")
        submit = Button(self.signupform, image=submitIcon, font=("Times", "15"), bg='white', fg='white',
                        activebackground='#069778', command=self.createuser,relief='flat')
        submit.grid(row=6, columnspan=2, sticky='s',pady=15)
        backIcon = PhotoImage(file="backButtonIcon.png")
        goback = Button(self.signupform, image=backIcon, bg="white", command=lambda: TeacherLogin(root),
                        relief="flat").grid(
            row=7 , columnspan=2, padx=20,pady=10)
        self.signupform.rowconfigure(0, weight=1)
        self.signupform.rowconfigure(1, weight=1)
        self.signupform.rowconfigure(2, weight=1)
        self.signupform.rowconfigure(3, weight=1)
        self.signupform.rowconfigure(4, weight=1)
        self.signupform.rowconfigure(5, weight=1)
        self.signupform.rowconfigure(6, weight=1)
        self.signupform.rowconfigure(7, weight=1)

        self.signupform.columnconfigure(0, weight=1)
        self.signupform.columnconfigure(1, weight=1)
        self.signupform.columnconfigure(2, weight=1)
        self.signupform.grid(row=1, column=1, sticky='nsew')

        self.signupBackFrame.rowconfigure(0,weight=1)
        self.signupBackFrame.columnconfigure(0, weight=1)


        self.signupBackFrame2.rowconfigure(0,weight=1)
        self.signupBackFrame2.rowconfigure(1, weight=7)
        self.signupBackFrame2.rowconfigure(2, weight=1)
        self.signupBackFrame2.columnconfigure(0, weight=1)
        self.signupBackFrame2.columnconfigure(1, weight=7)
        self.signupBackFrame2.columnconfigure(2, weight=1)
        self.signupBackFrame2.grid(row=0,column=0)
        signupBackFrame1.rowconfigure(0, weight=1)
        signupBackFrame1.rowconfigure(1, weight=5)
        signupBackFrame1.rowconfigure(2, weight=1)
        signupBackFrame1.columnconfigure(0, weight=1)
        signupBackFrame1.columnconfigure(1, weight=4)
        signupBackFrame1.columnconfigure(2, weight=1)
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0,weight=1)

        self.signupBackFrame.grid(row=0,column=0,sticky='nsew')
        signupBackFrame1.grid(row=1,column=1,sticky='nsew')

        root.mainloop()

    def createuser(self):
        sname = self.name.get()
        pid = self.pid.get()
        spass = str(self.passw.get())
        cpassd = str(self.cpassw.get())
        security = self.securitya.get().lower()
        if (len(sname) != 0 and len(pid) != 0 and len(spass) != 0 and len(cpassd) != 0 and len(security) != 0):
            if(sname.isdigit()):
                nameerror = messagebox.showerror("Name Error", "Name should only contain characters")
            else:


                if (len(spass) > 7):
                    if (spass == cpassd):
                        self.cur.execute(
                        '''Create Table if not exists Teacherdetails(sname varchar(50),pid varchar(50) UNIQUE ,spass varchar(50),security char)''')
                        try:
                            self.cur.execute("Insert into Teacherdetails(sname,pid,spass,security) values(?,?,?,?)",
                                             (sname, pid, spass, security))
                        except:
                            userexist = messagebox.showerror("Error", "User already exist !!")
                            return
                        successful = messagebox.showinfo("Registration", "Registration Successfull !")
                        self.conn.commit()
                        self.conn.close()
                        self.signupBackFrame.destroy()
                        a=TeacherLogin(root)






                    else:
                        passwerror = messagebox.showerror("Password Error",
                                                          "Password and confirmed password didnot matched !!")
                else:
                    paswdlerror = messagebox.showerror("Error", "Password should be atleast 8 characters long!!")

        else:
            emptyerror = messagebox.showerror("Error", "All fields are required")

    def viewtable(self):
        self.cur.execute("Select * from Teacherdetails")
        for row in self.cur:
            print(row)


class TeacherLogin:
    #uerpass = StringVar()
    con = sqlite3.connect("mockTest.db")
    cur = con.cursor()
    def loginStudent(self):


        self.spid = self.pid.get()
        self.spass = self.userpass.get()
        if(len(self.spid) >= 0 and len(self.spass) > 0):
          if(len(self.spass)>7):
              try:
                  self.cur.execute('''SELECT pid,spass from Teacherdetails where pid=? and spass =?''',(self.spid,self.spass))
                  l=[]
                  for r in self.cur:
                      l.append((r))
                      print(l)
                  if(l[0]==(str(self.spid),str(self.spass))):
                      success = messagebox.showinfo("Login","Login Successfull")
                      a=TeachersHome(root,self.spid,0)


              except:
                  error = messagebox.showerror("User Error", "User does not exist")

            #else:
             #   error = messagebox.showerror("User Error","User does not exist")
          else:
            paswdlerror = messagebox.showerror("Error", "Password should be atleast 8 characters long!!")
          #try:
           #   self.cur.execute('''SELECT pid,spass from Studentdetails where pid=? and spass = ?''', (str(spid),str(spass)))
            #  success = messagebox.showinfo("Login", "Login Successfull")


        else:
            error1 = messagebox.showerror("Error", "All fields are required !!!")


    def __init__(self, root):
        userp = StringVar()

        self.root = root
        background = PhotoImage(file="background.png")
        self.Loginframe =  Frame(self.root)
        loginbackround = Label(self.Loginframe,image=background)
        loginbackround.grid(row=0, sticky='nsew')
        Loginframe2 = Frame(self.Loginframe)
        Loginframe3 = Frame(Loginframe2,bg='white',relief='raised')

        loginicon = PhotoImage(file="loginIcon.png")
        iconlabel = Label(Loginframe3,image=loginicon,bg="white").grid(row=0,columnspan=2,pady=20)

        pidl = Label(Loginframe3, text="Enter your pid no. :", font=("Times", "15"), bg='white', padx=10).grid(
            row=1, column=0, sticky='nw',pady=20,padx=10)
        self.pid = Entry(Loginframe3, font=("Times", "15"), bg='#E5EFE7')
        self.pid.grid(row=1, column=1, sticky='new',pady=20,padx=10)

        passl = Label(Loginframe3, text="Enter your password :", font=("Times", "15"), bg='white').grid(
            row=2, column=0, sticky='nw',pady=20,padx=20)
        self.userpass = Entry(Loginframe3, font=("Times", "15"), show="*", bg='#E5EFE7')
        self.userpass.grid(row=2, column=1, sticky='new', pady=20, padx=10)

        forget = PhotoImage(file="forgetpassword.png")
        signup = Button(Loginframe3, image=forget, bg="white", command=lambda: ResetTeacher(root), relief="flat").grid(
            row=4, pady=10, column=0, padx=20)

        signupIcon = PhotoImage(file="newusers.png")
        signup = Button(Loginframe3, image=signupIcon, bg="white", command=lambda :Teacher(root), relief="flat").grid(row=4, pady=30, column=1, padx=20)

        backIcon = PhotoImage(file="backButton.png")
        signup = Button(Loginframe3, image=backIcon, bg="white", command=lambda: Frontpage(root), relief="flat").grid(
            row=5, pady=30, column=0, padx=20,sticky=W)

        submiticon = PhotoImage(file="loginnow.png")
        submit = Button(Loginframe3, image=submiticon, bg="white", command=self.loginStudent, relief="flat").grid(row=5,
                                                                                                                  pady=5,
                                                                                                                  column=0,
                                                                                                                  columnspan=2,
                                                                                                                  padx=20)

        Loginframe3.grid(row=1,column=1,sticky='news')
        Loginframe3.rowconfigure(0,weight=1)
        Loginframe3.rowconfigure(1, weight=1)
        Loginframe3.rowconfigure(2, weight=1)
        Loginframe3.rowconfigure(3, weight=1)
        Loginframe3.rowconfigure(4, weight=1)
        Loginframe3.rowconfigure(5, weight=1)
        Loginframe3.columnconfigure(0, weight=1)
        Loginframe3.columnconfigure(1, weight=2)
        Loginframe3.columnconfigure(2, weight=1)
        Loginframe2.grid(row=0,column=0)
        Loginframe2.rowconfigure(0,weight=1)
        Loginframe2.rowconfigure(1,weight=3)
        Loginframe2.rowconfigure(2,weight=1)
        Loginframe2.columnconfigure(0,weight=1)
        Loginframe2.columnconfigure(1,weight=2)
        Loginframe2.columnconfigure(2,weight=1)
        self.Loginframe.grid(row=0,sticky='nsew')
        self.Loginframe.rowconfigure(0,weight=1)
        self.Loginframe.columnconfigure(0,weight=1)
        root.mainloop()


class TeachersHome:
    n=0
    p=0
    con=sqlite3.connect("mockTest.db")
    cur = con.cursor()

    def createquestion(self):
        try :
            self.prompt.destroy()
            self.createquestionContent()
        except :
            self.createquestionContent()

    def createquestionContent(self):
        try:
            self.createpaper.destroy()
            self.checanalysis.destroy()
            self.selectsubject.config(state='disable')
            self.selectsubjected.destroy()
        except:
            pass


        if(self.n!=1):
            self.n+=1

        self.fileicon = PhotoImage(file="chooseFileIcon.png")
        self.chosefile = Button(self.frontframe, image=self.fileicon, bg='white', relief='flat',command=self.chooseFilePrompt)
        self.chosefile.grid(row=2, column=0, pady=10,padx=20)

        self.paper = PhotoImage(file="CreateSetIcon.png")
        self.makepaper = Button(self.frontframe, image=self.paper, bg='white', relief='flat',command=self.createManualQues)
        self.makepaper.grid(row=2, column=1, pady=10)

        self.backicon = PhotoImage(file="backButtonIcon.png")
        self.back = Button(self.frontframe, image=self.backicon, bg='white', relief='flat',command=self.clicksubmit)
        self.back.grid(row=3, columnspan=2, pady=10)

    def logout(self):
        self.p+=1

        if(self.p%2==1):
            self.logoutbutton = Button(self.frontframe,text="Logout",command = lambda:Frontpage(root),bg="white",relief='flat',fg="#4a90e2",font="Helvetica 15")
            self.logoutbutton.grid(row=0,column=2,padx=10)

        else:
            self.logoutbutton.destroy()


    def clicksubmit(self):
        self.n+=1

        if(self.n%2==1):
            self.selectsubject.config(state='disable')

        else:
            self.selectsubject.config(state='normal')

        self.selectsubjected.destroy()



        self.setpaper = PhotoImage(file="setPaperIcon.png")
        self.createpaper = Button(self.frontframe, image=self.setpaper,bg='white', relief='flat',command=self.createquestion)
        self.createpaper.grid(row=2, columnspan=2, pady=10)

        self.analysis = PhotoImage(file="analysisIcon.png")
        self.checanalysis = Button(self.frontframe, image=self.analysis, bg='white', relief='flat',command=self.checkAnalysis)
        self.checanalysis.grid(row=3, columnspan=2, pady=10)

        try:
         self.makepaper.destroy()
         self.chosefile.destroy()
         self.prompt.destroy()

        except:
            pass

    def checkAnalysis(self):
        self.subjectchosen = self.selectsubject.get()
        self.selectsubject.config(state="normal")
        a=Performance(self.subjectchosen)
        self.n+=1

    def chooseFilePrompt(self):
        self.prompt = Label(self.frontframe,fg='white',relief=RAISED)
        self.prompt.grid(row=1,columnspan=2)

        self.goImg = PhotoImage(file='goButton.png')
        self.go = Button(self.prompt, image=self.goImg, command=self.loadfile)
        self.go.grid(row=0, column=0,sticky=NS)

        self.sampleImg = PhotoImage(file='sampleButton.png')
        self.sample = Button(self.prompt, image=self.sampleImg, command=lambda:Sample(root,self.pid))
        self.sample.grid(row=0,column=1,sticky=NS)

        Label(self.prompt,text='(Max 10 Questions can be added at time)',font='Helvetica',fg='#4A90E2').grid(row=1,columnspan=2)
        Button(self.prompt,image=self.backicon,command=self.createquestion).grid(row=2,columnspan=2)

    def loadfile(self):
        self.prompt.destroy()
        # file = askopenfilenames(filetypes=(("All files","*.*")))
        fname='sample.txt'
        #fname = askopenfilename(filetypes=(("All files", "txt {*.txt}")))

        callToChoosenFile=QuesFromChoosenFile(root,fname,self.pid)


    def createManualQues(self):

        callToQues=Question(root,self.pid)


    def __init__(self,root,pid,a):
        self.pid = pid
        self.root = root



        background = PhotoImage(file="background.png")
        self.backframe =  Frame(self.root)
        backround = Label(self.backframe, image=background)
        backround.grid(row=0, sticky='nsew')
        backholdframe = Frame(self.backframe)
        self.frontframe = Frame(backholdframe,bg='white',relief='raised',bd=2)


        loginicon = PhotoImage(file="teacherIcon.png")
        iconlabel = Label(self.frontframe,image=loginicon,bg="white").grid(row=0,column=0,pady=20,padx=10)

        self.cur.execute('''Select sname from Teacherdetails where pid = {}'''.format(self.pid))
        l=[]
        for r in self.cur:
            l.append(r)
            print(l)
        name = "Hello " + l[0][0]
       # var = StringVar()
      #  var.set("Welcome " + " ".join(l))

        self.welcomemsg = Button(self.frontframe, text=name, font="Helvetica 16 ", bg="white", fg="#4a90e2",
                                 command=self.logout, relief="flat")
        self.welcomemsg.grid(row=0, column=1, padx=5, pady=10)

        var = StringVar()
        var.set("Please select a subject")
        # selectsubject = OptionMenu(self.frontframe,var,"Python","Computer Networks","COA",command=self.selectedsubject)

        self.selectsubject = Spinbox(self.frontframe, values=('Python', 'CN', 'COA', 'AT', 'OS'), bg='white')
        self.selectsubject.grid(row=1, columnspan=2, pady=10, sticky='ns')

        if (a == 1):

            self.createquestionContent()

        else:

            submit = PhotoImage(file="submitButtonIcon.png")
            self.selectsubjected = Button(self.frontframe, image=submit, bg='white', relief='flat',
                                          command=self.clicksubmit)
            self.selectsubjected.grid(row=2, columnspan=2, pady=10)

       # submit = PhotoImage(file="submitButton.png")
      #  selectbutton = Label(self.frontframe,image=submit)
       # selectsubject.grid(row=2,sticky='s')

        self.frontframe.grid(row=1,column=1,sticky='news')
        self.frontframe.rowconfigure(0,weight=1)
        self.frontframe.rowconfigure(1, weight=1)
        self.frontframe.rowconfigure(2, weight=1)
        self.frontframe.rowconfigure(3, weight=1)
        self.frontframe.rowconfigure(4, weight=1)
        self.frontframe.rowconfigure(5, weight=1)

        self.frontframe.columnconfigure(0, weight=1)
        self.frontframe.columnconfigure(1, weight=1)
        self.frontframe.columnconfigure(2, weight=1)

        backholdframe.grid(row=0,column=0)
        backholdframe.rowconfigure(0,weight=1)
        backholdframe.rowconfigure(1,weight=5)
        backholdframe.rowconfigure(2,weight=1)
        backholdframe.columnconfigure(0,weight=1)
        backholdframe.columnconfigure(1,weight=5)
        backholdframe.columnconfigure(2,weight=1)

        self.backframe.grid(row=0, sticky='nsew')
        self.backframe.rowconfigure(0, weight=1)
        self.backframe.columnconfigure(0, weight=1)
        root.mainloop()

    def selectedsubject(self, value):
        self.value = value


class Sample:

    def __init__(self,root,usrId):
        self.root = root
        background = PhotoImage(file="background.png")
        self.backframe = Frame(self.root)
        backround = Label(self.backframe, image=background)
        backround.grid(row=0, sticky='nsew')
        backholdframe = Frame(self.backframe)
        self.frontframe = Frame(backholdframe, bg='white', relief='raised', bd=2)
        self.usrId=usrId

        sampleBckgrd = PhotoImage(file='sampleImage.png')
        sampleScreen = Label(self.frontframe, image=sampleBckgrd)
        sampleScreen.grid(row=0)

        doneImg = PhotoImage(file='doneButton1.png')
        done = Button(self.frontframe, image=doneImg,command=self.donecommand)
        done.grid(row=6)

        self.frontframe.grid(row=1,column=1,sticky='news')
        self.frontframe.rowconfigure(0,weight=1)
        self.frontframe.rowconfigure(1, weight=1)
        self.frontframe.rowconfigure(2, weight=1)
        self.frontframe.rowconfigure(3, weight=1)
        self.frontframe.rowconfigure(4, weight=1)
        self.frontframe.rowconfigure(5, weight=1)

        self.frontframe.columnconfigure(0, weight=1)
        self.frontframe.columnconfigure(1, weight=1)
        self.frontframe.columnconfigure(2, weight=1)

        backholdframe.grid(row=0,column=0)
        backholdframe.rowconfigure(0,weight=1)
        backholdframe.rowconfigure(1,weight=5)
        backholdframe.rowconfigure(2,weight=1)
        backholdframe.columnconfigure(0,weight=1)
        backholdframe.columnconfigure(1,weight=5)
        backholdframe.columnconfigure(2,weight=1)

        self.backframe.grid(row=0, sticky='nsew')
        self.backframe.rowconfigure(0, weight=1)
        self.backframe.columnconfigure(0, weight=1)
        root.mainloop()


    def donecommand(self):
        TeachersHome(root,self.usrId,1)


class ResetTeacher:
    con = sqlite3.connect("mockTest.db")
    cur = con.cursor()
    def checkSecurity(self):


        self.spid = self.pid.get()
        self.securityvalue = self.secuityans.get().lower()
        if(len(self.spid)!=0 and len(self.securityvalue)!=0):

            self.cur.execute("Select pid,security from Teacherdetails WHERE pid = ? and security = ?", (str(self.spid),str(self.securityvalue)))
            securityResult=[]
            for r in self.cur:
                securityResult.append(r)
            if(len(securityResult)!=0):
                print(securityResult)
                if(securityResult[0][0] == str(self.spid) and securityResult[0][1] == str(self.securityvalue)):
                    print(securityResult)
                    a=self.resetPassword()
            else:
                incorrectAns = messagebox.showerror("Incorrect Security Answer","You are not allowed to change the password")


        else:
            error1 = messagebox.showerror("Error", "All fields are required !!!")


    def __init__(self, root):
        userp = StringVar()

        self.root = root
        background = PhotoImage(file="background.png")
        self.Resetframe =  Frame(self.root)
        loginbackround = Label(self.Resetframe, image=background)
        loginbackround.grid(row=0, sticky='nsew')
        Resetframe2 = Frame(self.Resetframe)
        self.Resetframeframe3 = Frame(Resetframe2,bg='white',relief='raised')
        forgeticon = PhotoImage(file="forgetIcon.png")
        iconlabel = Label(self.Resetframeframe3,image=forgeticon,bg="white").grid(row=0,columnspan=2,pady=20)
        pidl = Label(self.Resetframeframe3, text="Enter your pid no. :", font=("Times", "15"), bg='white', padx=10).grid(
            row=1, column=0, sticky='nw',pady=20,padx=10)

        self.pid = Entry(self.Resetframeframe3, font=("Times", "15"), bg='#E5EFE7')
        self.pid.grid(row=1, column=1, sticky='new',pady=20,padx=10)
        securityl = Label(self.Resetframeframe3, text="Whats is your pet name :", font=("Times", "15"), bg='white').grid(
            row=2, column=0, sticky='nw',pady=20,padx=20)
        self.secuityans = Entry(self.Resetframeframe3, font=("Times", "15"), bg='#E5EFE7')
        self.secuityans.grid(row=2, column=1, sticky='new', pady=20, padx=10)

        self.submiticon = PhotoImage(file="submitButton.png")
        self.submit = Button(self.Resetframeframe3, image=self.submiticon,bg="white",command=self.checkSecurity,relief="flat")
        self.submit.grid(row=3,pady=30,columnspan=2,padx=20)
        backIcon = PhotoImage(file="backButtonIcon.png")
        goback = Button(self.Resetframeframe3, image=backIcon, bg="white", command=lambda: TeacherLogin(root),
                        relief="flat").grid(
            row=4, columnspan=2, padx=20,pady=10)



        self.Resetframeframe3.grid(row=1,column=1,sticky='news')
        self.Resetframeframe3.rowconfigure(0,weight=1)
        self.Resetframeframe3.rowconfigure(1, weight=1)
        self.Resetframeframe3.rowconfigure(2, weight=1)
        self.Resetframeframe3.rowconfigure(3, weight=1)
        self.Resetframeframe3.rowconfigure(4, weight=1)
        self.Resetframeframe3.rowconfigure(5, weight=1)
        self.Resetframeframe3.columnconfigure(0, weight=1)
        self.Resetframeframe3.columnconfigure(1, weight=2)
        self.Resetframeframe3.columnconfigure(2, weight=1)
        Resetframe2.grid(row=0,column=0)
        Resetframe2.rowconfigure(0,weight=1)
        Resetframe2.rowconfigure(1,weight=3)
        Resetframe2.rowconfigure(2,weight=1)
        Resetframe2.columnconfigure(0,weight=1)
        Resetframe2.columnconfigure(1,weight=2)
        Resetframe2.columnconfigure(2,weight=1)
        self.Resetframe.grid(row=0, sticky='nsew')
        self.Resetframe.rowconfigure(0, weight=1)
        self.Resetframe.columnconfigure(0, weight=1)
        root.mainloop()
    def resetPassword(self):
        self.submit.destroy()
        newpassl = Label(self.Resetframeframe3, text="Enter your new password : ", font=("Times", "15"), bg='white').grid(
            row=3, column=0, sticky='nw',pady=20,padx=20)
        self.newpasse = Entry(self.Resetframeframe3, font=("Times", "15"), bg='#E5EFE7',show='*')
        self.newpasse.grid(row=3, column=1, sticky='new', pady=20, padx=10)
        confirmpassl = Label(self.Resetframeframe3, text="Confirm your new password : ", font=("Times", "15"),
                         bg='white').grid(row=4, column=0, sticky='nw', pady=20, padx=20)
        self.confirmpasse = Entry(self.Resetframeframe3, font=("Times", "15"), bg='#E5EFE7', show='*')
        self.confirmpasse.grid(row=4, column=1, sticky='new', pady=20, padx=10)
        self.submit2 = Button(self.Resetframeframe3, image=self.submiticon,bg="white",command=self.chnagePassword,relief="flat")
        self.submit2.grid(row=5,pady=30,columnspan=2,padx=20)


    def chnagePassword(self):
        self.newpass = self.newpasse.get()
        self.confirmpass = self.confirmpasse.get()
        if(len(self.newpass)>7 and len(self.confirmpass)>7):

            if (self.newpass == self.confirmpass):
                self.cur.execute("Update Studentdetails Set spass = ?", [str(self.newpass)])
                con.commit()
                success = messagebox.showinfo("Password Update ", "Password Changed Successfully")
            else:
                passerror = messagebox.showerror("Password Error", "Entered Password and Confirmed Password didnot match")
        else:
            leneror = messagebox.showerror("Password Length Error","Password Should be minimum 8 characters longs")


class QuesFromChoosenFile:

    def __init__(self,screen,fname,pid):

        self.root = root
        self.fname=fname
        self.pid=pid

        background = PhotoImage(file="background.png")
        self.backframe = Frame(self.root)

        backround = Label(self.backframe, image=background)
        backround.grid(row=0, sticky='nsew')

        backholdframe = Frame(self.backframe)
        self.frontframe = Frame(backholdframe, bg='white', relief='raised', bd=2)

        self.f = Label(self.frontframe)
        self.f.grid(row=0, rowspan=10, column=0, columnspan=5, sticky=W)

        self.tempQues = []
        self.quesList=[]

        self.callOfOneQues = 0
        self.callOfTwoQues = 0
        self.callOfThreeQues = 0
        self.callOfPreview = 0

        self.saveImg = PhotoImage(file='saveButton.png')
        self.yesImg = PhotoImage(file='yesButton.png')
        self.noImg = PhotoImage(file='noButton.png')

        self.r=open(self.fname,'r+')
        self.w=open('python.txt','a+')

        self.counter = self.r.readlines()
        print(len(self.counter)/6)
        self.r.seek(0)

        self.frontframe.grid(row=1, column=1, sticky='news')
        self.frontframe.rowconfigure(0, weight=1)
        self.frontframe.rowconfigure(1, weight=1)
        self.frontframe.rowconfigure(2, weight=1)
        self.frontframe.rowconfigure(3, weight=1)
        self.frontframe.rowconfigure(4, weight=1)
        self.frontframe.rowconfigure(5, weight=1)

        self.frontframe.columnconfigure(0, weight=1)
        self.frontframe.columnconfigure(1, weight=1)
        self.frontframe.columnconfigure(2, weight=1)

        backholdframe.grid(row=0, column=0)
        backholdframe.rowconfigure(0, weight=1)
        backholdframe.rowconfigure(1, weight=5)
        backholdframe.rowconfigure(2, weight=1)
        backholdframe.columnconfigure(0, weight=1)
        backholdframe.columnconfigure(1, weight=5)
        backholdframe.columnconfigure(2, weight=1)

        self.backframe.grid(row=0, sticky='nsew')
        self.backframe.rowconfigure(0, weight=1)
        self.backframe.columnconfigure(0, weight=1)

        self.appendToMainList()

        root.mainloop()

    def appendToList(self):
        self.nxt = 0
        while True:
            if self.r.read(1) == '\n':
                break
            self.nxt += 1
        self.r.seek(self.prv)
        self.l.append(self.r.read(self.nxt))
        self.prv = self.prv + self.nxt + 1
        self.r.seek(self.prv)

    def callForAppend(self):
        self.l = []
        for x in range(6):
            self.appendToList()

    def appendToMainList(self):
        self.prv = 0
        self.quesList = []
        for i in range(int(len(self.counter)/6)):
            self.callForAppend()
            self.quesList.append(self.l)

        self.previewStartPage()

    def previewStartPage(self):

        self.callOfPreview += 1

        try:
            self.noQues.destroy()
            self.home.destroy()
            self.prvwImg=PhotoImage(file='previewButton.png')
            self.preview=Button(self.f, image=self.prvwImg, command=self.previewMainPage)
            self.preview.grid(row=0,column=0,columnspan=2)

        except:
            self.prvwImg = PhotoImage(file='previewButton.png')
            self.preview = Button(self.f, image=self.prvwImg, command=self.previewMainPage)
            self.preview.grid(row=0, column=0, columnspan=2)

    def previewMainPage(self):

            if self.callOfPreview > 0 and self.callOfOneQues == 0 and self.callOfTwoQues == 0 and self.callOfThreeQues == 0:

                self.preview.destroy()
                self.mainPageContent()

            elif self.callOfOneQues > 0:

                self.quesOneOfOne.config(state=NORMAL)
                self.quesOneOfOne.destroy()

                self.next.destroy()
                self.mainPageContent()

            elif self.callOfTwoQues > 0 :

                self.quesTwoOfOne.config(state=NORMAL)
                self.quesTwoOfTwo.config(state=NORMAL)

                self.quesTwoOfOne.destroy()
                self.quesTwoOfTwo.destroy()

                self.next.destroy()
                self.mainPageContent()

            elif self.callOfThreeQues > 0:

                self.quesThreeOfOne.config(state=NORMAL)
                self.quesThreeOfTwo.config(state=NORMAL)
                self.quesThreeOfThree.config(state=NORMAL)

                self.quesThreeOfOne.destroy()
                self.quesThreeOfTwo.destroy()
                self.quesThreeOfThree.destroy()

                self.next.destroy()
                self.mainPageContent()


    def mainPageContent(self):

        if int(len(self.quesList)) == 0:
            self.noQues = Label(self.f, text='No Question is entered by You..!!', font='Helvetica 18 bold',
                                fg='#4A90E2')
            self.noQues.grid(row=1,columnspan=3)
            self.displayHomeButton()
            self.home.grid(row=2, columnspan=3)

        elif int(len(self.quesList)) == 1 :

            if self.callOfOneQues == 0 :
                self.oneQuesDisplay(self.quesList[0])
            else :
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=2,columnspan=3)

        elif int(len(self.quesList)) == 2:

            if self.callOfTwoQues ==0:
                self.twoQuesDisplay(self.quesList[:2])
            else:
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=3,columnspan=3)

        elif int(len(self.quesList)) == 3:

            if self.callOfThreeQues==0:
                self.threeQuesDisplay(self.quesList[:3])
            else:
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=4,columnspan=3)

        elif int(len(self.quesList)) == 4:

            if self.callOfThreeQues == 0 and self.callOfOneQues == 0:
                self.threeQuesDisplay(self.quesList[0:3])

            elif self.callOfThreeQues > 0 and self.callOfOneQues == 0 :
                self.oneQuesDisplay(self.quesList[3:])

            elif self.callOfThreeQues > 0 and self.callOfOneQues > 0 :
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=2,columnspan=3)

        elif int(len(self.quesList)) == 5:

            if self.callOfThreeQues==0 :
                self.threeQuesDisplay(self.quesList[0:3])

            elif self.callOfThreeQues != 0 and self.callOfTwoQues == 0:
                self.oneQuesDisplay(self.quesList[3:])

            elif self.callOfThreeQues != 0 and self.callOfTwoQues != 0:
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=3,columnspan=3)

        elif int(len(self.quesList)) == 6:

            if self.callOfThreeQues==0 :
                self.threeQuesDisplay(self.quesList[0:3])

            elif self.callOfThreeQues ==1 :
                self.threeQuesDisplay(self.quesList[3:])

            elif self.callOfThreeQues > 1:
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=4,columnspan=3)


        elif int(len(self.quesList)) == 7:

            if self.callOfThreeQues == 0:
                self.threeQuesDisplay(self.quesList[0:3])

            elif self.callOfThreeQues == 1:
                self.threeQuesDisplay(self.quesList[3:6])

            elif self.callOfThreeQues > 1 and self.callOfOneQues == 0 :
                self.oneQuesDisplay(self.quesList[6:])

            elif self.callOfThreeQues > 1 and self.callOfOneQues > 0 :
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=2,columnspan=3)

        elif int(len(self.quesList)) == 8 :

            if self.callOfThreeQues == 0:
                self.threeQuesDisplay(self.quesList[0:3])

            elif self.callOfThreeQues == 1:
                self.threeQuesDisplay(self.quesList[3:6])

            elif self.callOfThreeQues > 1 and self.callOfTwoQues == 0:
                self.twoQuesDisplay(self.quesList[6:])

            elif self.callOfThreeQues > 1 and self.callOfTwoQues > 0:
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=3,columspan=3)

        elif int(len(self.quesList)) == 9:

            if self.callOfThreeQues == 0:
                self.threeQuesDisplay(self.quesList[0:3])

            elif self.callOfThreeQues == 1:
                self.threeQuesDisplay(self.quesList[3:6])

            elif self.callOfThreeQues == 2:
                self.threeQuesDisplay(self.quesList[6:])

            elif self.callOfThreeQues > 2 :
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=4,columnspan=3)

        elif int(len(self.quesList)) == 10:

            if self.callOfThreeQues == 0:
                self.threeQuesDisplay(self.quesList[0:3])

            elif self.callOfThreeQues == 1:
                self.threeQuesDisplay(self.quesList[3:6])

            elif self.callOfThreeQues == 2:
                self.threeQuesDisplay(self.quesList[6:9])

            elif self.callOfThreeQues > 2 and self.callOfOneQues == 0:
                self.oneQuesDisplay(self.quesList[9:])

            elif self.callOfThreeQues > 2 and self.callOfOneQues > 0:
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=2,columnspan=3)

    def title(self):
        self.pythonDisplay=Label(self.f,text='Python',font='Helvetica 18 bold',fg='#4A90E2')
        self.pythonDisplay.grid(row=0,columnspan=3,padx=5,pady=5)

    def oneQuesDisplay(self,localList):

        self.callOfOneQues+=1
        self.localList=localList
        print(self.localList)
        self.varOneOfOne=IntVar()
        self.title()

        self.quesOneOfOne=Checkbutton(self.f, text=str(self.localList[0][0]) + '\n' + str(self.localList[0][1]) + '\n' + str(self.localList[0][2]) + '\n' +
                                                   str(self.localList[0][3]) + '\n' + str(self.localList[0][4]) + '\n' +str(self.localList[0][5]) + '\n',
                                      font='helvetica 15',fg='#4A90E2',justify=LEFT,variable=self.varOneOfOne,
                                      offvalue=0,onvalue=1)
        self.quesOneOfOne.grid(row=1,columnspan=3,sticky=W,padx=5,pady=5)

        self.saveOfOne = Button(self.f, image=self.saveImg, command=self.saveAlertOfOne)
        self.saveOfOne.grid(row=2,columnspan=3,pady=5)

    def twoQuesDisplay(self, localList):

        self.callOfTwoQues += 1
        self.localList = localList
        self.varTwoOfOne = IntVar()
        self.varTwoOfTwo = IntVar()

        self.title()

        self.quesTwoOfOne = Checkbutton(self.f, text=str(self.localList[0][0]) + '\n' + str(self.localList[0][1]) + '\n' + str(self.localList[0][2]) + '\n' +
                                                     str(self.localList[0][3]) + '\n' + str(self.localList[0][4]) + '\n' + str(self.localList[0][5]),
                                        font='helvetica 15', fg='#4A90E2', justify=LEFT, variable=self.varTwoOfOne,
                                        offvalue=0, onvalue=1)
        self.quesTwoOfOne.grid(row=1, columnspan=3, sticky=W, padx=5, pady=5)

        self.quesTwoOfTwo = Checkbutton(self.f, text=str(self.localList[1][0]) + '\n' + str(self.localList[1][1]) + '\n' +
                                                     str(self.localList[1][2]) + '\n' +
                                                     str(self.localList[1][3]) + '\n' + str(self.localList[1][4]) + '\n' +
                                                     str(self.localList[1][5]),
                                        font='helvetica 15', fg='#4A90E2', justify=LEFT, variable=self.varTwoOfTwo,
                                        offvalue=0, onvalue=1)
        self.quesTwoOfTwo.grid(row=2, columnspan=3, sticky=W, padx=5, pady=5)

        self.saveOfTwo = Button(self.f, image=self.saveImg, command=self.saveAlertOfTwo)
        self.saveOfTwo.grid(row=3, columnnspan=3, pady=5)

    def threeQuesDisplay(self, localList):

        self.callOfThreeQues += 1

        self.localList = localList
        self.varThreeOfOne = IntVar()
        self.varThreeOfTwo = IntVar()
        self.varThreeOfThree = IntVar()

        self.title()

        self.quesThreeOfOne = Checkbutton(self.f, text=str(self.localList[0][0]) + '\n' + str(self.localList[0][1]) + '\n' +
                                                     str(self.localList[0][2]) + '\n' +
                                                     str(self.localList[0][3]) + '\n' + str(self.localList[0][4]) + '\n' +
                                                     str(self.localList[0][5]),
                                        font='helvetica 15', fg='#4A90E2', justify=LEFT, variable=self.varThreeOfOne,
                                        offvalue=0, onvalue=1)
        self.quesThreeOfOne.grid(row=1, columnspan=3, sticky=W, padx=5, pady=5)

        self.quesThreeOfTwo = Checkbutton(self.f, text=str(self.localList[1][0]) + '\n' + str(self.localList[1][1]) + '\n' +
                                                     str(self.localList[1][2]) + '\n' +
                                                     str(self.localList[1][3]) + '\n' + str(self.localList[1][4]) + '\n' +
                                                     str(self.localList[1][5]),
                                        font='helvetica 15', fg='#4A90E2', justify=LEFT, variable=self.varThreeOfTwo,
                                        offvalue=0, onvalue=1)
        self.quesThreeOfTwo.grid(row=2, columnspan=3, sticky=W, padx=5, pady=5)

        self.quesThreeOfThree = Checkbutton(self.f, text=str(self.localList[2][0]) + '\n' + str(self.localList[2][1]) + '\n' +
                                                     str(self.localList[2][2]) + '\n' +
                                                     str(self.localList[2][3]) + '\n' + str(self.localList[2][4]) + '\n' +
                                                     str(self.localList[2][5]),
                                        font='helvetica 15', fg='#4A90E2', justify=LEFT, variable=self.varThreeOfThree,
                                        offvalue=0, onvalue=1)
        self.quesThreeOfThree.grid(row=3, columnspan=3, sticky=W, padx=5, pady=5)

        self.saveOfThree = Button(self.f, image=self.saveImg, command=self.saveAlertOfThree)
        self.saveOfThree.grid(row=4, columnspan=3, pady=5)


    def noOfAll(self):
        self.no=Button(self.f1,image=self.noImg,command=self.noFuncOfAll)

    def noFuncOfAll(self):
        self.f1.destroy()

    def saveAlertOfOne(self):
        self.f1=Label(self.f,relief=RAISED)
        self.f1.grid(row=1,columnspan=3)
        self.saveLabelOfOne=Label(self.f1, text='Do you really want to save?', font='Helvetica 17 bold', fg='#4A90E2')
        self.saveLabelOfOne.grid(row=0, columnspan=3)
        self.yesOfOne = Button(self.f1, image=self.yesImg, command=self.yesFuncOfOne)
        self.yesOfOne.grid(row=1,columnspan=3,sticky=W,padx=10)
        self.noOfAll()
        self.no.grid(row=1,columnspan=3,sticky=E,padx=10)

    def saveAlertOfTwo(self):
        self.f1=Label(self.f,relief=RAISED)
        self.f1.grid(row=1,columnspan=3)
        self.saveLabelOfTwo=Label(self.f1,text='Do you really want to save?',font='Helvetica 17 bold',fg='#4A90E2')
        self.saveLabelOfTwo.grid(row=0,columnspan=3)
        self.yesOfOne = Button(self.f1, image=self.yesImg, command=self.yesFuncOfTwo)
        self.yesOfOne.grid(row=1,columnspan=3,sticky=W,padx=10)
        self.noOfAll()
        self.no.grid(row=1,columnspan=3,sticky=E,padx=10)

    def saveAlertOfThree(self):
        self.f1=Label(self.f,relief=RAISED)
        self.f1.grid(row=2,columnspan=3)
        self.saveLabelOfThree=Label(self.f1,text='Do you really want to save?',font='Helvetica 17 bold',fg='#4A90E2')
        self.saveLabelOfThree.grid(row=0,columnspan=3)
        self.yesOfOne = Button(self.f1, image=self.yesImg, command=self.yesFuncOfThree)
        self.yesOfOne.grid(row=1,columnspan=3,sticky=W,padx=10)
        self.noOfAll()
        self.no.grid(row=1,columnspan=3,sticky=E,padx=10)

    def yesFuncOfOne(self):

        self.quesOneOfOne.config(state=DISABLED)

        if self.varOneOfOne.get() > 0 :
            for i in range(6):
                self.w.write(''+str(self.localList[0][i])+'\n')

        self.f1.destroy()
        self.saveOfOne.destroy()
        self.displayNextButton()
        self.next.grid(row=2,columnspan=3,sticky=E)
        self.localList=[]

    def yesFuncOfTwo(self):

        self.quesTwoOfOne.config(state=DISABLED)
        self.quesTwoOfTwo.config(state=DISABLED)

        if self.varTwoOfOne.get() > 0 and self.varTwoOfTwo.get() > 0:
            for i in range(2):
                for j in range(6):
                    self.w.write(''+str(self.localList[i][j])+'\n')

        elif self.varTwoOfOne.get() > 0:
            for i in [0]:
                for j in range(6):
                    self.w.write(''+str(self.localList[i][j])+'\n')

        elif self.varTwoOfTwo.get() > 0:
            for i in [1]:
                for j in range(6):
                    self.w.write(''+str(self.localList[i][j])+'\n')

        self.f1.destroy()
        self.saveOfTwo.destroy()
        self.displayNextButton()
        self.next.grid(row=3, columnspan=3, sticky=E)
        self.localList = []

    def yesFuncOfThree(self):

        self.quesThreeOfOne.config(state=DISABLED)
        self.quesThreeOfTwo.config(state=DISABLED)
        self.quesThreeOfThree.config(state=DISABLED)

        print(self.varThreeOfThree.get())

        if self.varThreeOfOne.get() > 0 and self.varThreeOfTwo.get() > 0 and self.varThreeOfThree.get() > 0 :
            for i in range(3):
                for j in range(6):
                    self.w.write(''+str(self.localList[i][j]) + '\n')

        elif self.varThreeOfOne.get() > 0 and self.varThreeOfTwo.get() > 0:
            for i in [0,1]:
                for j in range(6):
                    self.w.write(''+str(self.localList[i][j])+'\n')

        elif self.varThreeOfTwo.get() > 0 and self.varThreeOfThree.get() > 0:
            for i in [1,2]:
                for j in range(6):
                    self.w.write(''+str(self.localList[i][j]) +'\n')

        elif self.varThreeOfOne.get() > 0 and self.varThreeOfThree.get() > 0:
            for i in [0,2]:
                for j in range(6):
                    self.w.write(''+str(self.localList[i][j]) +'\n')

        elif self.varThreeOfOne.get() > 0 :
            for i in [0]:
                for j in range(6):
                    self.w.write(''+str(self.localList[i][j]) +'\n')

        elif self.varThreeOfTwo.get() > 0 :
            for i in [1]:
                for j in range(6):
                    self.w.write(''+str(self.localList[i][j]) +'\n')

        elif self.varThreeOfThree.get() > 0:
            for i in [2]:
                for j in range(6):
                    self.w.write(''+str(self.localList[i][j]) +'\n')

        self.f1.destroy()
        self.saveOfThree.destroy()
        self.displayNextButton()
        self.next.grid(row=4, columnspan=3, sticky=E)
        self.localList = []

    def displayNextButton(self):
        self.nextImg=PhotoImage(file='nxtButton.png')
        self.next=Button(self.f,image=self.nextImg, command=self.previewMainPage)

    def displayHomeButton(self):
        self.homeImg=PhotoImage(file='homeButton.png')
        self.home=Button(self.f, image=self.homeImg,command=self.homeFunc)

    def homeFunc(self):
        backToTeacherHome=TeachersHome(root,self.pid,0)


class Question():
    def __init__(self,root,pid):

        self.root = root
        self.pid=pid

        background = PhotoImage(file="background.png")
        self.backframe = Frame(self.root)

        backround = Label(self.backframe, image=background)
        backround.grid(row=0, sticky='nsew')

        backholdframe = Frame(self.backframe)
        self.frontframe = Frame(backholdframe, bg='white', relief='raised', bd=2)

        self.tempQues = []

        self.quesContent = []
        self.allStartHere()


        self.frontframe.grid(row=1, column=1, sticky='news')
        self.frontframe.rowconfigure(0, weight=1)
        self.frontframe.rowconfigure(1, weight=1)
        self.frontframe.rowconfigure(2, weight=1)
        self.frontframe.rowconfigure(3, weight=1)
        self.frontframe.rowconfigure(4, weight=1)
        self.frontframe.rowconfigure(5, weight=1)

        self.frontframe.columnconfigure(0, weight=1)
        self.frontframe.columnconfigure(1, weight=1)
        self.frontframe.columnconfigure(2, weight=1)

        backholdframe.grid(row=0, column=0)
        backholdframe.rowconfigure(0, weight=1)
        backholdframe.rowconfigure(1, weight=5)
        backholdframe.rowconfigure(2, weight=1)
        backholdframe.columnconfigure(0, weight=1)
        backholdframe.columnconfigure(1, weight=5)
        backholdframe.columnconfigure(2, weight=1)

        self.backframe.grid(row=0, sticky='nsew')
        self.backframe.rowconfigure(0, weight=1)
        self.backframe.columnconfigure(0, weight=1)

        root.mainloop()



    def allStartHere(self):
        self.call = 0
        try:
            self.f.destroy()
            self.startToSet()

        except:
            self.startToSet()

    def startToSet(self):

        self.f = Label(self.frontframe)
        self.f.grid(row=0, rowspan=15, column=0, columnspan=5, sticky=W)

        self.headLine = Label(self.f, text='Questions', font='Helvetica 20 bold', fg='#4A90E2')
        self.headLine.grid(row=0, column=0, columnspan=3, padx=5, pady=10)

        self.noOfQuesLabel = Label(self.f, text='No. of Questions', font='Helvetica 14', fg='#4A90E2')
        self.noOfQuesLabel.grid(row=1, column=0, padx=5, pady=10, sticky=W)

        self.quesSpinBox = Spinbox(self.f, from_=1, to=10, fg='#4A90E2')
        self.quesSpinBox.grid(row=1, column=1,columnspan=2, padx=5, pady=10, sticky=W)

        self.noOfQues = int(self.quesSpinBox.get())

        self.backImg = PhotoImage(file='backButton.png')
        self.bacKToTeacher=Button(self.f,image=self.backImg,command=self.funcToTeacherHome)
        self.bacKToTeacher.grid(row=2,sticky=W)

        self.nxtImg = PhotoImage(file='nxtButton1.png')
        self.nxt = Button(self.f, image=self.nxtImg, command=self.enterQues)
        self.nxt.grid(row=2,column=1)

    def funcToTeacherHome(self):

        backToTeacherHome=TeachersHome(root,self.pid,0)


    def enterQues(self):

        self.call+=1
        if self.call == 1 :

            self.noOfQuesLabel.destroy()
            self.headLine.destroy()
            self.quesSpinBox.destroy()
            self.nxt.destroy()
            self.bacKToTeacher.destroy()
            self.quesGenerator()

        elif self.call>1 and self.call<=self.noOfQues :
            self.quesGenerator()


    def quesGenerator(self):

        try:
            self.button[2].destroy()
            self.questionCall()
        except:
            self.questionCall()

    def questionCall(self):

        self.quesNentryLabel = []
        self.entryValue = []
        self.button = []

        for i in range(8):

            if i == 0:
                self.quesNentryLabel.append(Label(self.f, text='Add question', font='Helvetica 25 bold', fg='#4A90E2'))
                self.quesNentryLabel[i].grid(row=i, column=0, columnspan=3, padx=5, pady=5)

            elif i in range(1, 7):
                if i == 1:
                    self.quesNentryLabel.append(Label(self.f, text='Q.'+str(i)+')', font='Helvetica 15 bold', fg='#4A90E2'))
                    self.quesNentryLabel[i].grid(row=i, column=0, sticky=W, padx=5, pady=5)

                    self.entryValue.append(Entry(self.f, width=35))
                    self.entryValue[i - 1].grid(row=i, column=1, columnspan=2, sticky=EW, padx=5, pady=5)

                elif i in range(2, 6):
                    self.quesNentryLabel.append(
                        Label(self.f, text='option ' + str(i - 1), font='Helvetica 15', fg='#4A90E2'))
                    self.quesNentryLabel[i].grid(row=i, column=0, sticky=W, padx=5)

                    self.entryValue.append(Entry(self.f))
                    self.entryValue[i - 1].grid(row=i, column=1, sticky=W, padx=5, pady=5)

                else:
                    self.quesNentryLabel.append(Label(self.f, text='ans', font='Helvetica 15', fg='#4A90E2'))
                    self.quesNentryLabel[i].grid(row=i, column=0, sticky=W, padx=5)

                    self.entryValue.append(Entry(self.f))
                    self.entryValue[i - 1].grid(row=i, column=1, sticky=W, padx=5, pady=5)

                    self.hint = Label(self.f, text='Enter option number ex.1', font='Helvetica 12')
                    self.hint.grid(row=i + 1, column=1, sticky=W)


            else:

                self.button.append(Button(self.f, image=self.backImg, command=self.allStartHere, fg='white'))
                self.button[0].grid(row=i + 2, column=0, padx=5, pady=5, sticky=W)

                self.saveImg = PhotoImage(file='saveButton.png')
                self.button.append(Button(self.f, image=self.saveImg, command=self.saveQuesAlert, fg='white',
                                          disabledforeground='white'))
                self.button[1].grid(row=i + 2, column=1, padx=5, pady=5)
                print(i+2)

    def saveQuesAlert(self):

        self.f1=Label(self.f,relief=RAISED)
        self.f1.grid(row=2,rowspan=4,column=0,columnspan=2)
        self.msg = Label(self.f1, text='Do you really want to save Your Question?', font='Helvetica 20 bold', fg='#4A90E2')
        self.msg.grid(row=0, column=0, columnspan=2, padx=5,pady=5)

        self.yesImg = PhotoImage(file='yesButton.png')
        self.yes = Button(self.f1, image=self.yesImg,command=self.yesQues)
        self.yes.grid(row=1, column=0, padx=5,pady=5)

        self.noImg = PhotoImage(file='noButton.png')
        self.no = Button(self.f1, image=self.noImg, command=self.noQues)
        self.no.grid(row=1, column=1, padx=5,pady=5)

    def yesQues(self):
        if self.call == self.noOfQues :
            self.yesFunction()
            self.button[2].destroy()
            self.prvwImg=PhotoImage(file='previewButton.png')
            self.preview=Button(self.f,image=self.prvwImg,command=self.previewFunc)
            self.preview.grid(row=9,columnspan=2)

        else :
            self.yesFunction()


    def yesFunction(self):

        if len(self.entryValue[0].get()) > 0 and len(self.entryValue[1].get()) > 0 and len(
                self.entryValue[2].get()) > 0 and len(self.entryValue[3].get()) > 0 and len(
                self.entryValue[4].get()) > 0 and len(self.entryValue[5].get()) == 1:

            if (self.entryValue[5].get()).isnumeric():

                if int(self.entryValue[5].get()) > 0 and int(self.entryValue[5].get()) < 5:
                    #--------append----------#
                    for i in range(6):
                        self.tempQues.append(self.entryValue[i].get())

                    #--------disabled-------#
                    for i in range(7):
                        self.quesNentryLabel[i].config(state=DISABLED)
                    for i in range(6):
                        self.entryValue[i].config(state=DISABLED)

                    self.quesContent.append(self.tempQues)
                    print(self.quesContent)

                    self.f1.destroy()
                    self.button[0].destroy()
                    self.button[1].destroy()

                    self.nextImg = PhotoImage(file='nextButton.png')
                    self.button.append(Button(self.f, image=self.nextImg, command=self.enterQues, fg='white'))
                    self.button[2].grid(row=7, column=2, padx=5, pady=5, sticky=E)

                else:
                    messagebox.showinfo('Invalid option', 'Option can be from 1 to 4')
            else:
                messagebox.showinfo('Invalid answer', 'Please enter numeric value')
        else:
            messagebox.showinfo('Entry is Empty', 'Please fill all text field')

    def noQues(self):
        self.f1.destroy()

    def previewFunc(self):

        for i in range(len(self.entryValue)):
            self.entryValue[i].destroy()

        for i in range(len(self.quesNentryLabel)):
            self.quesNentryLabel[i].destroy()

        self.hint.destroy()
        self.preview.destroy()

        self.quesList=[]

        self.quesList=list(self.quesContent)

        print(self.quesList)

        self.callOfOneQues = 0
        self.callOfTwoQues = 0
        self.callOfThreeQues = 0
        self.callOfPreview = 0

        self.saveImg = PhotoImage(file='saveButton.png')
        self.yesImg = PhotoImage(file='yesButton.png')
        self.noImg = PhotoImage(file='noButton.png')

        self.w = open('python.txt', 'a+')

        self.previewStartPage()

    def previewStartPage(self):

        self.callOfPreview += 1

        try:
            self.noQues.destroy()
            self.home.destroy()
            self.previewMainPage()

        except:
            self.previewMainPage()

    def previewMainPage(self):

        if self.callOfPreview > 0 and self.callOfOneQues == 0 and self.callOfTwoQues == 0 and self.callOfThreeQues == 0:

            self.preview.destroy()
            self.mainPageContent()

        elif self.callOfOneQues > 0:

            self.quesOneOfOne.config(state=NORMAL)

            self.quesOneOfOne.destroy()
            self.next.destroy()
            self.mainPageContent()

        elif self.callOfTwoQues > 0:

            self.quesTwoOfOne.config(state=NORMAL)
            self.quesTwoOfTwo.config(state=NORMAL)

            self.quesTwoOfOne.destroy()
            self.quesTwoOfTwo.destroy()
            self.next.destroy()
            self.mainPageContent()

        elif self.callOfThreeQues > 0:

            self.quesThreeOfOne.config(state=NORMAL)
            self.quesThreeOfTwo.config(state=NORMAL)
            self.quesThreeOfThree.config(state=NORMAL)

            self.quesThreeOfOne.destroy()
            self.quesThreeOfTwo.destroy()
            self.quesThreeOfThree.destroy()
            self.next.destroy()
            self.mainPageContent()

        self.w.seek(0)
        print(self.w.readlines())

    def mainPageContent(self):

        if int(len(self.quesList)) == 0:
            self.noQues = Label(self.f, text='No Question is entered by You..!!', font='Helvetica 18 bold',
                                fg='#4A90E2')
            self.noQues.grid(row=1, columnspan=3)
            self.pythonDisplay.destroy()
            self.displayHomeButton()
            self.home.grid(row=2, columnspan=3)

        elif int(len(self.quesList)) == 1:

            if self.callOfOneQues == 0:
                self.oneQuesDisplay(self.quesList[0])
            else:
                self.pythonDisplay.destroy()
                Label(self.f,text='All questions are succefully added',font='Helvetica 15 bold',fg='#4A90E2').grid(row=1,columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=2, columnspan=3)

        elif int(len(self.quesList)) == 2:

            if self.callOfTwoQues == 0:
                self.twoQuesDisplay(self.quesList[:2])
            else:
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=3, columnspan=3)

        elif int(len(self.quesList)) == 3:

            if self.callOfThreeQues == 0:
                self.threeQuesDisplay(self.quesList[:3])
            else:
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=4, columnspan=3)

        elif int(len(self.quesList)) == 4:

            if self.callOfThreeQues == 0 and self.callOfOneQues == 0:
                self.threeQuesDisplay(self.quesList[0:3])

            elif self.callOfThreeQues > 0 and self.callOfOneQues == 0:
                self.oneQuesDisplay(self.quesList[3:])

            elif self.callOfThreeQues > 0 and self.callOfOneQues > 0:
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=2, columnspan=3)

        elif int(len(self.quesList)) == 5:

            if self.callOfThreeQues == 0:
                self.threeQuesDisplay(self.quesList[0:3])

            elif self.callOfThreeQues != 0 and self.callOfTwoQues == 0:
                self.oneQuesDisplay(self.quesList[3:])

            elif self.callOfThreeQues != 0 and self.callOfTwoQues != 0:
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=3, columnspan=3)

        elif int(len(self.quesList)) == 6:

            if self.callOfThreeQues == 0:
                self.threeQuesDisplay(self.quesList[0:3])

            elif self.callOfThreeQues == 1:
                self.threeQuesDisplay(self.quesList[3:])

            elif self.callOfThreeQues > 1:
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=4, columnspan=3)


        elif int(len(self.quesList)) == 7:

            if self.callOfThreeQues == 0:
                self.threeQuesDisplay(self.quesList[0:3])

            elif self.callOfThreeQues == 1:
                self.threeQuesDisplay(self.quesList[3:6])

            elif self.callOfThreeQues > 1 and self.callOfOneQues == 0:
                self.oneQuesDisplay(self.quesList[6:])

            elif self.callOfThreeQues > 1 and self.callOfOneQues > 0:
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=2, columnspan=3)

        elif int(len(self.quesList)) == 8:

            if self.callOfThreeQues == 0:
                self.threeQuesDisplay(self.quesList[0:3])

            elif self.callOfThreeQues == 1:
                self.threeQuesDisplay(self.quesList[3:6])

            elif self.callOfThreeQues > 1 and self.callOfTwoQues == 0:
                self.twoQuesDisplay(self.quesList[6:])

            elif self.callOfThreeQues > 1 and self.callOfTwoQues > 0:
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=3, columspan=3)

        elif int(len(self.quesList)) == 9:

            if self.callOfThreeQues == 0:
                self.threeQuesDisplay(self.quesList[0:3])

            elif self.callOfThreeQues == 1:
                self.threeQuesDisplay(self.quesList[3:6])

            elif self.callOfThreeQues == 2:
                self.threeQuesDisplay(self.quesList[6:])

            elif self.callOfThreeQues > 2:
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=4, columnspan=3)

        elif int(len(self.quesList)) == 10:

            if self.callOfThreeQues == 0:
                self.threeQuesDisplay(self.quesList[0:3])

            elif self.callOfThreeQues == 1:
                self.threeQuesDisplay(self.quesList[3:6])

            elif self.callOfThreeQues == 2:
                self.threeQuesDisplay(self.quesList[6:9])

            elif self.callOfThreeQues > 2 and self.callOfOneQues == 0:
                self.oneQuesDisplay(self.quesList[9:])

            elif self.callOfThreeQues > 2 and self.callOfOneQues > 0:
                self.pythonDisplay.destroy()
                Label(self.f, text='All questions are succefully added', font='Helvetica 15 bold', fg='#4A90E2').grid(
                    row=1, columnspan=3)
                self.displayHomeButton()
                self.home.grid(row=2, columnspan=3)

    def title(self):
        self.pythonDisplay = Label(self.f, text='Python', font='Helvetica 18 bold', fg='#4A90E2')
        self.pythonDisplay.grid(row=0, columnspan=3, padx=5, pady=5)

    def oneQuesDisplay(self, localList):

        self.callOfOneQues += 1
        self.localList = localList
        self.varOneOfOne = IntVar()
        self.title()

        print(self.localList)

        self.quesOneOfOne = Checkbutton(self.f, text=str(self.localList[0]) + '\n' + str(
            self.localList[1]) + '\n' + str(self.localList[2]) + '\n' +
                                                     str(self.localList[3]) + '\n' + str(
            self.localList[4]) + '\n' + str(self.localList[5]) + '\n',
                                        font='helvetica 15', fg='#4A90E2', justify=LEFT, variable=self.varOneOfOne,
                                        offvalue=0, onvalue=1)
        self.quesOneOfOne.grid(row=1, columnspan=3, sticky=W, padx=5, pady=5)

        self.saveOfOne = Button(self.f, image=self.saveImg, command=self.saveAlertOfOne)
        self.saveOfOne.grid(row=2, columnspan=3, pady=5)

    def twoQuesDisplay(self, localList):

        self.callOfTwoQues += 1
        self.localList = localList
        self.varTwoOfOne = IntVar()
        self.varTwoOfTwo = IntVar()

        self.title()

        self.quesTwoOfOne = Checkbutton(self.f, text=str(self.localList[0][0]) + '\n' + str(
            self.localList[0][1]) + '\n' + str(self.localList[0][2]) + '\n' +
                                                     str(self.localList[0][3]) + '\n' + str(
            self.localList[0][4]) + '\n' + str(self.localList[0][5]),
                                        font='helvetica 15', fg='#4A90E2', justify=LEFT, variable=self.varTwoOfOne,
                                        offvalue=0, onvalue=1)
        self.quesTwoOfOne.grid(row=1, columnspan=3, sticky=W, padx=5, pady=5)

        self.quesTwoOfTwo = Checkbutton(self.f,
                                        text=str(self.localList[1][0]) + '\n' + str(self.localList[1][1]) + '\n' +
                                             str(self.localList[1][2]) + '\n' +
                                             str(self.localList[1][3]) + '\n' + str(self.localList[1][4]) + '\n' +
                                             str(self.localList[1][5]),
                                        font='helvetica 15', fg='#4A90E2', justify=LEFT, variable=self.varTwoOfTwo,
                                        offvalue=0, onvalue=1)
        self.quesTwoOfTwo.grid(row=2, columnspan=3, sticky=W, padx=5, pady=5)

        self.saveOfTwo = Button(self.f, image=self.saveImg, command=self.saveAlertOfTwo)
        self.saveOfTwo.grid(row=3, columnnspan=3, pady=5)

    def threeQuesDisplay(self, localList):

        self.callOfThreeQues += 1

        self.localList = localList
        self.varThreeOfOne = IntVar()
        self.varThreeOfTwo = IntVar()
        self.varThreeOfThree = IntVar()

        self.title()

        self.quesThreeOfOne = Checkbutton(self.f,
                                          text=str(self.localList[0][0]) + '\n' + str(self.localList[0][1]) + '\n' +
                                               str(self.localList[0][2]) + '\n' +
                                               str(self.localList[0][3]) + '\n' + str(self.localList[0][4]) + '\n' +
                                               str(self.localList[0][5]),
                                          font='helvetica 15', fg='#4A90E2', justify=LEFT,
                                          variable=self.varThreeOfOne,
                                          offvalue=0, onvalue=1)
        self.quesThreeOfOne.grid(row=1, columnspan=3, sticky=W, padx=5, pady=5)

        self.quesThreeOfTwo = Checkbutton(self.f,
                                          text=str(self.localList[1][0]) + '\n' + str(self.localList[1][1]) + '\n' +
                                               str(self.localList[1][2]) + '\n' +
                                               str(self.localList[1][3]) + '\n' + str(self.localList[1][4]) + '\n' +
                                               str(self.localList[1][5]),
                                          font='helvetica 15', fg='#4A90E2', justify=LEFT,
                                          variable=self.varThreeOfTwo,
                                          offvalue=0, onvalue=1)
        self.quesThreeOfTwo.grid(row=2, columnspan=3, sticky=W, padx=5, pady=5)

        self.quesThreeOfThree = Checkbutton(self.f, text=str(self.localList[2][0]) + '\n' + str(
            self.localList[2][1]) + '\n' +
                                                         str(self.localList[2][2]) + '\n' +
                                                         str(self.localList[2][3]) + '\n' + str(
            self.localList[2][4]) + '\n' +
                                                         str(self.localList[2][5]),
                                            font='helvetica 15', fg='#4A90E2', justify=LEFT,
                                            variable=self.varThreeOfThree,
                                            offvalue=0, onvalue=1)
        self.quesThreeOfThree.grid(row=3, columnspan=3, sticky=W, padx=5, pady=5)

        self.saveOfThree = Button(self.f, image=self.saveImg, command=self.saveAlertOfThree)
        self.saveOfThree.grid(row=4, columnspan=3, pady=5)

    def noOfAll(self):
        self.no = Button(self.f1, image=self.noImg, command=self.noFuncOfAll)

    def noFuncOfAll(self):
        self.f1.destroy()

    def saveAlertOfOne(self):
        self.f1 = Label(self.f, relief=RAISED)
        self.f1.grid(row=1, columnspan=2)
        self.saveLabelOfOne = Label(self.f1, text='Do you really want to save?', font='Helvetica 18 bold',
                                    fg='#4A90E2')
        self.saveLabelOfOne.grid(row=0, columnspan=2)
        self.yesOfOne = Button(self.f1, image=self.yesImg, command=self.yesFuncOfOne)
        self.yesOfOne.grid(row=1, column=0)
        self.noOfAll()
        self.no.grid(row=1, column=1)

    def saveAlertOfTwo(self):
        self.f1 = Label(self.f, relief=RAISED)
        self.f1.grid(row=1, columnspan=2)
        self.saveLabelOfTwo = Label(self.f1, text='Do you really want to save?', font='Helvetica 18 bold',
                                    fg='#4A90E2')
        self.saveLabelOfTwo.grid(row=0, columnspan=2)
        self.yesOfOne = Button(self.f1, image=self.yesImg, command=self.yesFuncOfTwo)
        self.yesOfOne.grid(row=1, column=0)
        self.noOfAll()
        self.no.grid(row=1, column=1)

    def saveAlertOfThree(self):
        self.f1 = Label(self.f, relief=RAISED)
        self.f1.grid(row=2, columnspan=2)
        self.saveLabelOfThree = Label(self.f1, text='Do you really want to save?', font='Helvetica 18 bold',
                                      fg='#4A90E2')
        self.saveLabelOfThree.grid(row=0, columnspan=2)
        self.yesOfOne = Button(self.f1, image=self.yesImg, command=self.yesFuncOfThree)
        self.yesOfOne.grid(row=1, column=0)
        self.noOfAll()
        self.no.grid(row=1, column=1)

    def yesFuncOfOne(self):

        self.quesOneOfOne.config(state=DISABLED)

        if self.varOneOfOne.get() > 0:
            for i in range(6):
                self.w.write(str(self.localList[i]) + '\n')

        self.f1.destroy()
        self.saveOfOne.destroy()
        self.displayNextButton()
        self.next.grid(row=2, columnspan=3, sticky=E)
        self.localList = []

    def yesFuncOfTwo(self):

        self.quesTwoOfOne.config(state=DISABLED)
        self.quesTwoOfTwo.config(state=DISABLED)

        if self.varTwoOfOne.get() > 0 and self.varTwoOfTwo.get() > 0:
            for i in range(2):
                for j in range(6):
                    self.w.write(str(self.localList[i][j]) + '\n')

        elif self.varTwoOfOne.get() > 0:
            for i in [0]:
                for j in range(6):
                    self.w.write(str(self.localList[i][j]) + '\n')

        elif self.varTwoOfTwo.get() > 0:
            for i in [1]:
                for j in range(6):
                    self.w.write(str(self.localList[i][j]) + '\n')

        self.f1.destroy()
        self.saveOfTwo.destroy()
        self.displayNextButton()
        self.next.grid(row=3, columnspan=3, sticky=E)
        self.localList = []

    def yesFuncOfThree(self):

        self.quesThreeOfOne.config(state=DISABLED)
        self.quesThreeOfTwo.config(state=DISABLED)
        self.quesThreeOfThree.config(state=DISABLED)

        if self.varThreeOfOne.get() > 0 and self.varThreeOfTwo.get() > 0 and self.varThreeOfThree.get() > 0:
            for i in range(3):
                for j in range(6):
                    self.w.write(str(self.localList[i][j]) + '\n')

        elif self.varThreeOfOne.get() > 0 and self.varThreeOfTwo.get() > 0:
            for i in [0, 1]:
                for j in range(6):
                    self.w.write(str(self.localList[i][j]) + '\n')

        elif self.varThreeOfTwo.get() > 0 and self.varThreeOfThree.get() > 0:
            for i in [1, 2]:
                for j in range(6):
                    self.w.write(str(self.localList[i][j]) + '\n')

        elif self.varThreeOfOne.get() > 0 and self.varThreeOfThree.get() > 0:
            for i in [0, 2]:
                for j in range(6):
                    self.w.write(str(self.localList[i][j]) + '\n')

        elif self.varThreeOfOne.get() > 0:
            for i in [0]:
                for j in range(6):
                    self.w.write(str(self.localList[i][j]) + '\n')

        elif self.varThreeOfTwo.get() > 0:
            for i in [1]:
                for j in range(6):
                    self.w.write(str(self.localList[i][j]) + '\n')

        elif self.varThreeOfThree.get() > 0:
            for i in [2]:
                for j in range(6):
                    self.w.write(str(self.localList[i][j]) + '\n')

        self.f1.destroy()
        self.saveOfThree.destroy()
        self.displayNextButton()
        self.next.grid(row=4, columnspan=3, sticky=E)
        self.localList = []

    def displayNextButton(self):
        self.nextImg = PhotoImage(file='nxtButton.png')
        self.next = Button(self.f, image=self.nextImg, command=self.previewMainPage)

    def displayHomeButton(self):
        self.homeImg = PhotoImage(file='homeButton.png')
        self.home = Button(self.f, image=self.homeImg, command=self.homeFunc)

    def homeFunc(self):
        backToTeachersHome=TeachersHome(root,self.pid,0)


class Performance:
    con = sqlite3.connect("mockTest.db")
    cur = con.cursor()
    def __init__(self,subject):
        self.subject = subject
        print(self.subject)
        self.creategraph()



    def creategraph(self):

        score=[]
        self.cur.execute('''Select score From {}'''.format(self.subject))
        p = self.cur.fetchall()

        if(len(p)!=0):
            for j in range(len(p)):
                score.append(j)
            self.s40, self.s50, self.s60, self.s70, self.s80 = 0, 0, 0, 0, 0
            for i in range(len(p)):
                if (score[i] <= 4):
                    self.s40 += 1
                if (score[i] > 4 and score[i] <= 5):
                    self.s50 += 1
                if (score[i] > 5 and score[i] <= 6):
                    self.s60 += 1
                if (score[i] > 6 and score[i] <= 7):
                    self.s70 += 1
                if (score[i] >= 8):
                    self.s80 += 1
            perscore = [self.s40, self.s50, self.s60, self.s70, self.s80]
            label = ["40% and below", "40% to 50%", "50% to 60%", "60% to 70%", "80% and above"]
            color = ['red', 'yellowgreen', 'lightcoral', 'lightskyblue', 'green']
            plt.pie(perscore, labels=label, colors=color, autopct='%.2f%%', startangle=120)
            plt.show()
            score = []
        elif(len(p)==0):
            a = messagebox.showinfo("Insufficient Data", "Test is not yet set for this subject")
        print(score)


class StudentPage():
    now=0
    now1=0
    n=0
    def __init__(self, screen, pid):

        self.con = sqlite3.connect('mockTest.db')
        self.cur = self.con.cursor()
        self.pid = pid

        self.root = root
        background = PhotoImage(file="background.png")
        self.backframe = Frame(self.root)
        backround = Label(self.backframe, image=background)
        backround.grid(row=0, sticky='nsew')
        backholdframe = Frame(self.backframe)
        self.backholdframe = Frame(backholdframe, bg='white', relief='raised', bd=2)
        self.marks = 0
        self.cur.execute("create table if not exists AM4(pid varchar(30) unique,score int)")
        self.cur.execute("create table if not exists CN(pid varchar(30) unique,score int)")
        self.cur.execute("create table if not exists OS(pid varchar(30) unique,score int)")
        self.cur.execute("create table if not exists COA(pid varchar(30) unique,score int)")
        self.cur.execute("create table if not exists AT(pid varchar(30) unique,score int)")
        self.cur.execute("create table if not exists Python(pid varchar(30) unique,score int)")
        self.clock = Label(self.backframe, bg="#4a90e2")

        self.call = 0
        self.studentPage()

        self.backholdframe.grid(row=1, column=1, sticky='news')
        self.backholdframe.rowconfigure(0, weight=1)

        self.backholdframe.columnconfigure(0, weight=1)

        backholdframe.grid(row=0, column=0)
        backholdframe.rowconfigure(0, weight=1)
        backholdframe.rowconfigure(1, weight=5)
        backholdframe.rowconfigure(2, weight=1)
        backholdframe.columnconfigure(0, weight=1)
        backholdframe.columnconfigure(1, weight=5)
        backholdframe.columnconfigure(2, weight=1)
        self.backframe.grid(row=0, sticky='nsew')
        self.backframe.rowconfigure(0, weight=1)
        self.backframe.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        root.mainloop()

    def studentPage(self):
        self.subjects = ['AM4', 'CN', 'OS', 'COA', 'AT', 'Python']
        self.a = []
        self.na = []
        self.info = []

        self.clickOfAttmpt = 0

        for i in self.subjects:

            self.cur.execute('''select pid,score from {a} where pid = {b}'''.format(a=i, b=self.pid))

            for r in self.cur:
                self.info.append(r)
            if len(self.info) != 0:
                self.a.append(i)
                self.info = []
            else:
                self.na.append(i)
                self.info = []

        try:
            self.f2.destroy()

            self.f = Label(self.backholdframe)
            self.f.grid(row=0, rowspan=15, column=0)

            self.notAttmpt = PhotoImage(file='notAttempted.png')
            self.natp = Button(self.f, image=self.notAttmpt, command=self.notAttmptFunc, relief=FLAT)
            self.natp.grid(row=0, column=0, padx=5, pady=10)
            backbutton = PhotoImage(file="backButtonIcon.png")
            goback = Button(self.f,image = backbutton,command = lambda:StudentHome(root,self.pid),relief="flat")
            goback.grid(row=7,columnspan=2,sticky='s')

            self.Attmpt = PhotoImage(file='Attempted.png')
            self.atp = Button(self.f, image=self.Attmpt, command=self.attmptFunc, relief=FLAT)
            self.atp.grid(row=0, column=1, padx=5, pady=10)

        except:
            self.f = Label(self.backholdframe)
            self.f.grid(row=0, rowspan=15, column=0)

            self.notAttmpt = PhotoImage(file='notAttempted.png')
            self.natp = Button(self.f, image=self.notAttmpt, command=self.notAttmptFunc, relief=FLAT)
            self.natp.grid(row=0, column=0, padx=5, pady=10)

            self.Attmpt = PhotoImage(file='Attempted.png')
            self.atp = Button(self.f, image=self.Attmpt, command=self.attmptFunc, relief=FLAT)
            self.atp.grid(row=0, column=1, padx=5, pady=10)

    def attmptFunc(self):

        self.clickOfAttmpt += 1

        if self.clickOfAttmpt % 2 == 1:
            self.atp.config(relief=RAISED)
            try:
                self.am.destroy()
                self.cn.destroy()
                self.os.destroy()
                self.coa.destroy()
                self.at.destroy()
                self.py.destroy()
                self.contentOfAttmpt()
                self.backbutton = PhotoImage(file="backButtonIcon.png")
                goback = Button(self.f, image=self.backbutton, command=lambda: StudentHome(root, self.pid), relief="flat")
                goback.grid(row=7, columnspan=2, sticky='s')

            except:
                self.backbutton = PhotoImage(file="backButtonIcon.png")
                goback = Button(self.f, image=self.backbutton, command=lambda: StudentHome(root, self.pid), relief="flat")
                goback.grid(row=7, columnspan=2, sticky='s')
                self.contentOfAttmpt()

    def contentOfAttmpt(self):

        if int(len(self.a)) != 0:
            self.indexOfScore = 0
            self.ninfo = []
            self.labelOfScore = []
            for i in self.subjects:
                self.cur.execute('''select pid,score from {t} where pid={b}'''.format(t=i, b=self.pid))
                for r in self.cur:
                    self.ninfo.append(r)
                    self.ninfo.insert(0, i)

            self.labelOfScore.append(Label(self.f, text='Marks', font='Helvetica 20 bold', fg='#4A90E2'))
            self.labelOfScore[0].grid(row=1, columnspan=2)

            while self.indexOfScore < int(len(self.ninfo)) - 1:
                self.labelOfScore.append(Label(self.f, text=str(self.ninfo[self.indexOfScore]) + " - " + str(
                    self.ninfo[self.indexOfScore + 1][1]), font='Helvetica 16 bold', fg='#4A90E2'))
                self.labelOfScore[self.indexOfScore + 1].grid(row=self.indexOfScore + 2, columnspan=2)
                self.indexOfScore += 1
        else:
            self.txta = Label(self.f, text='You didnt attmept any Test till Yet', font='Helvetica 20 bold',
                              fg='#4A90E2')
            self.txta.grid(row=1, column=0, columnspan=2)

    def notAttmptFunc(self):

        self.natp.config(relief=RAISED)

        try:
            self.am.destroy()
            self.cn.destroy()
            self.os.destroy()
            self.coa.destroy()
            self.at.destroy()
            self.py.destroy()
            for i in range(len(self.labelOfScore)):
                self.labelOfScore[i].destroy()
            self.contentOfnoattmpt()
            backbutton = PhotoImage(file="backButtonIcon.png")
            goback = Button(self.f, image=backbutton, command=lambda: StudentHome(root, self.pid), relief="flat")
            goback.grid(row=8, columnspan=2, sticky='s')
            self.txta.destroy()

        except:
            self.contentOfnoattmpt()
            backbutton = PhotoImage(file="backButtonIcon.png")
            goback = Button(self.f, image=backbutton, command=lambda: StudentHome(root, self.pid), relief="flat")
            goback.grid(row=8, columnspan=2, sticky='s')
            self.txta.destroy()


    def contentOfnoattmpt(self):
        if len(self.na) != 0:
            c = 0
            for self.b in self.na:
                if self.b == 'AM4':
                    self.amImg = PhotoImage(file='am4Button.png')
                    self.am = Button(self.f, image=self.amImg, command=self.startAlertOfOther)
                    self.am.grid(row=c + 1, column=0, columnspan=2, padx=5, pady=10)

                elif self.b == 'CN':
                    self.cnImg = PhotoImage(file='cnButton.png')
                    self.cn = Button(self.f, image=self.cnImg, command=self.startAlertOfOther)
                    self.cn.grid(row=c + 1, column=0, padx=5, columnspan=2, pady=10)

                elif self.b == 'OS':
                    self.osImg = PhotoImage(file='osButton.png')
                    self.os = Button(self.f, image=self.osImg, command=self.startAlertOfOther)
                    self.os.grid(row=c + 1, column=0, padx=5, columnspan=2, pady=10)

                elif self.b == 'COA':
                    self.coaImg = PhotoImage(file='coaButton.png')
                    self.coa = Button(self.f, image=self.coaImg, command=self.startAlertOfOther)
                    self.coa.grid(row=c + 1, column=0, padx=5, columnspan=2, pady=10)

                elif self.b == 'AT':
                    self.atImg = PhotoImage(file='atButton.png')
                    self.at = Button(self.f, image=self.atImg, command=self.startAlertOfOther)
                    self.at.grid(row=c + 1, column=0, padx=5, columnspan=2, pady=10)

                elif self.b == 'Python':
                    self.pyImg = PhotoImage(file='pyButton.png')
                    self.py = Button(self.f, image=self.pyImg, command=self.startAlertOfPy)
                    self.py.grid(row=c + 1, column=0, padx=5, columnspan=2, pady=10)

                c += 1
            self.txta.destroy()
        else:
            self.txtna = Label(self.f, text='You have attempted all Test', font='Helvetica 18 bold', fg='#4A90E2')
            self.txtna.grid(row=1, column=0, columnspan=2, padx=5, pady=10)

    def startAlertOfOther(self):

        self.f.config(state=DISABLED)
        self.f1 = Label(self.f, relief=RAISED)
        self.f1.grid(row=3, column=0, columnspan=2)
        self.msg = Label(self.f1, text='Test has not yet set..!!', font='Helvetica 20 bold', fg='#4A90E2')
        self.msg.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.okImg = PhotoImage(file='okButton.png')
        self.ok = Button(self.f1, image=self.okImg, command=self.otherOfOk)
        self.ok.grid(row=1, columnspan=2, padx=5, pady=5)

    def otherOfOk(self):
        self.f.config(state=NORMAL)
        self.f1.destroy()

    def startAlertOfPy(self):

        self.f.config(state=DISABLED)
        self.f1 = Label(self.f, relief=RAISED)
        self.f1.grid(row=3, column=0, columnspan=2)
        self.msg = Label(self.f1, text='Do you really want to start the test?', font='Helvetica 20 bold', fg='#4A90E2')
        self.msg.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.yesImg = PhotoImage(file='yesButton.png')
        self.yes = Button(self.f1, image=self.yesImg, command=self.startTestOfPy)
        self.yes.grid(row=1, column=0, padx=5, pady=5)

        self.noImg = PhotoImage(file='noButton.png')
        self.no = Button(self.f1, image=self.noImg, command=self.noOfPy)
        self.no.grid(row=1, column=1, padx=5, pady=5)

        self.r = open('python.txt', 'r+')

        self.usrAns = []
        self.Ans = []
        self.quesNo = 1
        self.appendToMainList()

    def noOfPy(self):
        self.f.config(state=NORMAL)
        self.f1.destroy()

    def appendToList(self):
        self.nxt = 0
        while True:
            if self.r.read(1) == '\n':
                break
            self.nxt += 1
        self.r.seek(self.prv)
        self.l.append(self.r.read(self.nxt))
        self.prv = self.prv + self.nxt + 1
        self.r.seek(self.prv)

    def callForAppend(self):
        self.l = []
        for x in range(6):
            self.appendToList()

    def appendToMainList(self):
        self.prv = 0
        self.quesList = []
        for i in range(50):
            self.callForAppend()
            self.quesList.append(self.l)
        self.randomGenerator()

    def randomGenerator(self):
        self.indx = []
        while (len(self.indx) < 10):
            p = []
            for i in range(10):
                p.append(random.randint(0, 49))
                self.indx = set(p)

        self.indxList = []

        for i in self.indx:
            self.indxList.append(i)


    def startTestOfPy(self):

        self.f.destroy()
        self.f1.destroy()
        if self.call == 0:
            self.f2 = Label(self.backholdframe)
            self.f2.grid(row=0, rowspan=17, column=0)
            self.ques(self.indxList[:3])
            self.time = Label(self.clock, text=" ", font="Helvetica 24 bold",fg='white',bg="#034DA4")
            self.time.grid(row=0, column=20)
            self.clock.grid(row=0, sticky="n", padx=10, pady=80)
            self.update_clock()

        elif self.call == 1:
            self.f2.destroy()
            self.f2 = Label(self.backholdframe)
            self.f2.grid(row=0, rowspan=17, column=0)
            self.ques(self.indxList[3:6])

        elif self.call == 2:
            self.f2.destroy()
            self.f2 = Label(self.backholdframe)
            self.f2.grid(row=0, rowspan=17, column=0)
            self.ques(self.indxList[6:9])

        elif self.call == 3:
            self.f2.destroy()
            self.f2 = Label(self.backholdframe)
            self.f2.grid(row=0, rowspan=17, column=0)
            self.ques(self.indxList[9:])

        self.call += 1

    def ques(self, finalIndex):
        self.finalIndex = finalIndex

        self.question = []
        self.option = []
        x = 0
        y = 0
        z = 1

        Label(self.f2, text='Python', font='Helvetica 18 bold', fg='#4A90E2').grid(row=0, column=0)

        if self.call != 3:

            self.r1 = IntVar()
            self.r2 = IntVar()
            self.r3 = IntVar()

            for i in finalIndex:

                for j in range(6):

                    if j == 0:
                        self.question.append(
                            Label(self.f2, text=str(self.quesNo) + '.' + self.quesList[i][j], font='Helvetica 13 bold',
                                  fg='#4A90E2'))
                        self.question[x].grid(row=z + j, column=j, sticky=W, padx=5)

                    elif j == 5:
                        self.Ans.append(self.quesList[i][j])

                    else:
                        if z == 1:
                            self.option.append(
                                Radiobutton(self.f2, text=self.quesList[i][j], font='Helvetica 12', fg='#4A90E2',
                                            variable=self.r1, value=j))
                            self.option[y].grid(row=z + j, column=0, sticky=W, padx=5, pady=5)
                        elif z == 6:
                            self.option.append(
                                Radiobutton(self.f2, text=self.quesList[i][j], font='Helvetica 12', fg='#4A90E2',
                                            variable=self.r2, value=j))
                            self.option[y].grid(row=z + j, column=0, sticky=W, padx=5)
                        elif z == 11:
                            self.option.append(
                                Radiobutton(self.f2, text=self.quesList[i][j], font='Helvetica 12', fg='#4A90E2',
                                            variable=self.r3, value=j))
                            self.option[y].grid(row=z + j, column=0, sticky=W, padx=5)

                        y += 1
                x += 1
                z += 5
                self.quesNo += 1

            self.saveImg = PhotoImage(file='saveButton.png')
            self.save = Button(self.f2, image=self.saveImg, command=self.saveAnsAlert)
            self.save.grid(row=17, columnspan=2)

        else:
            self.r4 = IntVar()

            Label(self.f2, text='Python', font='Helvetica 18 bold', fg='#4A90E2').grid(row=0, column=0)

            for i in finalIndex:

                for j in range(6):

                    if j == 0:
                        self.question.append(
                            Label(self.f2, text=str(self.quesNo) + '.' + self.quesList[i][j], font='Helvetica 13 bold',
                                  fg='#4A90E2'))
                        self.question[x].grid(row=z, column=j, sticky=W, padx=5)

                    elif j == 5:
                        self.Ans.append(self.quesList[i][j])

                    else:

                        if z == 1:
                            self.option.append(
                                Radiobutton(self.f2, text=self.quesList[i][j], font='Helvetica 12', fg='#4A90E2',
                                            variable=self.r4, value=j))
                            self.option[y].grid(row=z + j, column=0, sticky=W, padx=5, pady=5)

                        y += 1

            self.saveImg = PhotoImage(file='saveButton.png')
            self.save = Button(self.f2, image=self.saveImg, command=self.saveLastAnsAlert)
            self.save.grid(row=6)

    def saveAnsAlert(self):

        self.f3 = Label(self.f2, relief=RAISED)
        self.f3.grid(row=6, rowspan=3, column=0, columnspan=2)
        self.msg = Label(self.f3, text='Do you really want to save Your Answer?', font='Helvetica 20 bold',
                         fg='#4A90E2')
        self.msg.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.yesImg = PhotoImage(file='yesButton.png')
        self.yes = Button(self.f3, image=self.yesImg, command=self.yesOfStart)
        self.yes.grid(row=7, column=0, padx=5, pady=5)

        self.noImg = PhotoImage(file='noButton.png')
        self.no = Button(self.f3, image=self.noImg, command=self.noOfStart)
        self.no.grid(row=7, column=1, padx=5, pady=5)

    def noOfStart(self):
        self.f3.destroy()

    def yesOfStart(self):

        if self.r1.get() > 0 and self.r2.get() > 0 and self.r3.get() > 0:
            self.usrAns.append(self.r1.get())
            self.usrAns.append(self.r2.get())
            self.usrAns.append(self.r3.get())

            self.f3.destroy()
            self.save.destroy()

            self.f2.config(state=DISABLED)

            for i in range(3):
                self.question[i].config(state=DISABLED)

            for i in range(12):
                self.option[i].config(state=DISABLED)

            self.nxtImg = PhotoImage(file='nxtButton.png')
            self.nxt = Button(self.f2, image=self.nxtImg, command=self.startTestOfPy)
            self.nxt.grid(row=17, columnspan=2, sticky=E)

        elif self.r2.get() > 0 and self.r3.get() > 0:
            messagebox.showinfo('select option', 'please select ans for option 1')
        elif self.r1.get() > 0 and self.r3.get() > 0:
            messagebox.showinfo('select option', 'please select ans for option 2')
        elif self.r1.get() > 0 and self.r2.get() > 0:
            messagebox.showinfo('select option', 'please select ans for option 3')
        else:
            messagebox.showinfo('select option', 'please select all answer')

    def saveLastAnsAlert(self):

        self.f3 = Label(self.f2, relief=RAISED)
        self.f3.grid(row=2, rowspan=3, column=0, columnspan=2)
        self.msg = Label(self.f3, text='Do you really want to save Your Answer?', font='Helvetica 20 bold',
                         fg='#4A90E2')
        self.msg.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        self.yesImg = PhotoImage(file='yesButton.png')
        self.yes = Button(self.f3, image=self.yesImg, command=self.lastYes)
        self.yes.grid(row=1, column=0, padx=5, pady=5)

        self.noImg = PhotoImage(file='noButton.png')
        self.no = Button(self.f3, image=self.noImg, command=self.lastNo)
        self.no.grid(row=1, column=1, padx=5, pady=5)

    def lastNo(self):
        self.f3.destroy()

    def lastYes(self):

        if self.r4.get() > 0:

            self.f3.destroy()
            self.save.destroy()

            self.usrAns.append(self.r4.get())
            self.f2.config(state=DISABLED)

            self.question[0].config(state=DISABLED)

            for i in range(4):
                self.option[i].config(state=DISABLED)

            self.scoreImg = PhotoImage(file='scoreButton.png')
            self.score = Button(self.f2, image=self.scoreImg, command=self.displayScore)
            self.score.grid(row=6)

        else:
            messagebox.showinfo('select option', 'please select the any option')

    def displayScore(self):
        self.marks = 0
        for i in range(10):
            if self.usrAns[i] == int(self.Ans[i]):
                self.marks += 1
        self.cur.execute('insert into Python(pid,score) values(?,?)', (self.pid, self.marks))
        self.score.destroy()

        self.scoreTxt = Label(self.f2, text='Your Score is ' + str(self.marks), font='Helvetica 18 bold', fg='#4A90E2')
        self.scoreTxt.grid(row=6)

        self.con.commit()
        self.homeImg = PhotoImage(file='homeButton.png')

        self.home = Button(self.f2, image=self.homeImg, command=self.studentPage)
        self.home.grid(row=7)

    def update_clock(self):


        self.now1 = self.now1 + 0.01
        a = float("{0:.2f}".format(self.now1))
        if (a == 00.59):
            self.now += 1
            self.now1 = 0

        if (self.n == 18):
            print("time up")


        timing = float("{0:.2f}".format(self.now)) + float("{0:.2f}".format(self.now1))
        timing1 = "{0:.2f}".format(timing)


        # self.now = time.strftime("%H:%M:%S")

        j=0

        if(timing1=="0.50"):
            self.time.config(font='Helvetica 26 bold',fg='red')

        self.time.config(text=timing1)

        if(timing1=="1.01"):
            for i in range(len(self.usrAns)):
                if self.usrAns[i] == int(self.Ans[i]):
                    self.marks += 1
                j+=1
            if self.option[0]==self.Ans[j] :
                self.marks += 1
            if self.option[1]==self.Ans[j+1] :
                self.marks += 1
            if self.option[2] == self.Ans[j+1] :
                self.marks += 1

            self.cur.execute('insert into Python(pid,score) values(?,?)', (self.pid, self.marks))
            self.con.commit()
            messagebox.showinfo("Time UP","Time up\nYour score is :" + str(self.marks))
            a=StudentHome(root,self.pid)

        self.clock.after(1000, self.update_clock)



class StudentHome:
    p = 0
    def logout(self):
        self.p+=1
        if(self.p%2==1):
            self.logoutbutton = Button(self.frontframe,text="Logout",command = lambda:Frontpage(root),bg="white",relief='flat',fg="#4a90e2",font="Helvetica 15")
            self.logoutbutton.grid(row=0,column=2,padx=10)
        else:
            self.logoutbutton.destroy()


    def __init__(self, root,pid):
        con = sqlite3.connect("mockTest.db")
        self.cur = con.cursor()
        self.pid=pid
        self.root = root
        background = PhotoImage(file="background.png")
        self.backframe = Frame(self.root)
        backround = Label(self.backframe, image=background)
        backround.grid(row=0, sticky='nsew')
        backholdframe = Frame(self.backframe)
        self.frontframe = Frame(backholdframe, bg='white', relief='raised', bd=2)

        studenticon = PhotoImage(file="studentIcon.png")
        self.studentButton = Button(self.frontframe,image=studenticon,bg="white",relief='flat')
        self.studentButton.grid(row=0,column=0,sticky='nsew',pady=10,ipadx=20,ipady=10)
        self.cur.execute('''Select sname from Studentdetails where pid = {}'''.format(self.pid))
        l = []
        for r in self.cur:
            l.append(r)
            print(l)
        name = "Hello " + l[0][0]
        # var = StringVar()
        #  var.set("Welcome " + " ".join(l))
        self.welcomemsg = Button(self.frontframe, text=name, font="Helvetica 16 ", bg="white", fg="#4a90e2",
                                 command=self.logout, relief="flat")
        self.welcomemsg.grid(row=0, column=1, padx=5, pady=10)

        attemptpaperIcon = PhotoImage(file="startTest.png")
        self.startTest = Button(self.frontframe,image=attemptpaperIcon,bg='white',relief='flat',command=lambda:StudentPage(root,self.pid))
        self.startTest.grid(row=1,columnspan=2,pady=10)
        checkperformance = PhotoImage(file="studentPerformance.png")
        self.startTest = Button(self.frontframe, image=checkperformance, bg='white', relief='flat',command=lambda:StudentPerformace(root,self.pid))
        self.startTest.grid(row=2, columnspan=2, pady=10)
        self.frontframe.grid(row=1, column=1, sticky='news')
        self.frontframe.rowconfigure(0, weight=1)
        self.frontframe.rowconfigure(1, weight=1)
        self.frontframe.rowconfigure(2, weight=1)
        self.frontframe.rowconfigure(3, weight=1)
        self.frontframe.rowconfigure(4, weight=1)
        self.frontframe.rowconfigure(5, weight=1)

        self.frontframe.columnconfigure(0, weight=1)
        self.frontframe.columnconfigure(1, weight=1)

        backholdframe.grid(row=0, column=0)
        backholdframe.rowconfigure(0, weight=1)
        backholdframe.rowconfigure(1, weight=5)
        backholdframe.rowconfigure(2, weight=1)
        backholdframe.columnconfigure(0, weight=1)
        backholdframe.columnconfigure(1, weight=5)
        backholdframe.columnconfigure(2, weight=1)
        self.backframe.grid(row=0, sticky='nsew')
        self.backframe.rowconfigure(0, weight=1)
        self.backframe.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.columnconfigure(0, weight=1)
        root.mainloop()


class StudentPerformace:
    def __init__(self,root,pid):
        self.pid = pid
        self.root = root
        background = PhotoImage(file="background.png")
        self.backframe = Frame(self.root)
        backround = Label(self.backframe, image=background)
        backround.grid(row=0, sticky='nsew')
        backholdframe = Frame(self.backframe)
        self.frontframe = Frame(backholdframe, bg='white', relief='raised', bd=2)


        var = StringVar()
        var.set("Please select a subject")
        self.selectsubject = Spinbox(self.frontframe, values=('Python', 'CN', 'COA','AM4','AT','OS'), bg='white')
        self.selectsubject.grid(row=0, columnspan=2, pady=20,padx=20, sticky='ns')
        submit = PhotoImage(file="submitButtonIcon.png")
        self.selectsubjected = Button(self.frontframe, image=submit, bg='white', relief='flat',
                                      command=self.checkPerformance)
        self.selectsubjected.grid(row=2, columnspan=2, pady=20,padx=20)
        self.backicon = PhotoImage(file="backButtonIcon.png")
        self.back = Button(self.frontframe, image=self.backicon, bg='white', relief='flat', command=lambda:StudentHome(root,self.pid))
        self.back.grid(row=3, columnspan=2)

        self.frontframe.grid(row=1, column=1, sticky='news')
        self.frontframe.rowconfigure(0, weight=1)
        self.frontframe.rowconfigure(1, weight=1)
        self.frontframe.rowconfigure(2, weight=1)
        self.frontframe.rowconfigure(3, weight=1)
        self.frontframe.rowconfigure(4, weight=1)
        self.frontframe.rowconfigure(5, weight=1)

        self.frontframe.columnconfigure(0, weight=1)
        self.frontframe.columnconfigure(1, weight=1)
        self.frontframe.columnconfigure(2, weight=1)
        backholdframe.grid(row=0, column=0)
        backholdframe.rowconfigure(0, weight=1)
        backholdframe.rowconfigure(1, weight=5)
        backholdframe.rowconfigure(2, weight=1)
        backholdframe.columnconfigure(0, weight=1)
        backholdframe.columnconfigure(1, weight=5)
        backholdframe.columnconfigure(2, weight=1)
        self.backframe.grid(row=0, sticky='nsew')
        self.backframe.rowconfigure(0, weight=1)
        self.backframe.columnconfigure(0, weight=1)
        root.mainloop()
    def checkPerformance(self):
        con = sqlite3.connect("mockTest.db")
        self.cur = con.cursor()
        subject = self.selectsubject.get()

        self.cur.execute(''' SELECT  score FROM {a} WHERE pid = {b}'''.format(a=str(subject),b=self.pid))
        self.l=self.cur.fetchall()
        print(self.l)

        if(len(self.l)!=0):
            print("hi")
            objects = ('Correct Answers', "Incorrect Answers")

            print(self.l)
            for x in range(0, 10):
                self.l.append(x)
            y_pos = np.arange(len(objects))
            score = self.l[0][0]
            performance = [score, 10 - score]

            plt.bar(y_pos, performance, align='center', alpha=0.5)
            plt.xticks(y_pos, objects)
            plt.ylabel('Score')
            plt.title('Python')
            plt.show()
            self.l=[]
            print(len(self.l))

        elif(len(self.l)==0):
            print("hi")
            b = messagebox.showerror("Error","You have not attempted this test")



root = Tk()
root.title("Mock Test")
root.geometry('720x1280')
root.config(bg='cyan')
root.rowconfigure(0, weight=1)
root.columnconfigure(0,weight=1)
con = sqlite3.connect("mockTest.db")



#a=Reset(root)
b=Welcome(root)
#b.viewtable()



