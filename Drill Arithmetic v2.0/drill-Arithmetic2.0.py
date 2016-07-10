#Colby J. Conklling
#Drill Arithmetic v2.0
#Intro to Programming Course
#University of Central Arkansas

import tkinter as tk
import tkinter.messagebox
import time
import sys
import random
import os
root = tk.Tk()

class Window(tk.Frame):
    #Creating variables and instances of tk
    name=" "
    entry= tk.Entry()
    rentry1 = tk.Entry()
    rentry2 = tk.Entry()
    totalcorrect = 0
    questioncount = 0
    output = ""
    numberofquestions = 5
    userloggedin = ""
    output = tk.StringVar()
    checkoption = tk.IntVar()
    qnumber = tk.StringVar()
    qnumber.set("5")
    operand1 = 1
    operand2 = 10
    loggedin = False
    loginattempts = 0
    t = tk
    m = tk
    r = tk
    rw = tk
    ra = tk
    o = tk
    asettings = tk

#Loads users into array from users.txt to be manipulated
    def load(self):
        filename = ("users.txt")
        infile = open(filename, 'r')
        data = []
        line = infile.readline()
        data.append(line.split())
        while line != '':
            line = infile.readline()
            data.append(line.split())
            
        return data

    def loadperf(self):
        filename = ("drillArch.dat")
        infile = open(filename, 'r')
        data=[]
        line = infile.readline()
        data.append(line.split())
        while line != '':
            line = infile.readline()
            data.append(line.split())

        return data

    #Searches through users to authenticate login
    def search(self, event=None):
        founduser = False
        users = self.load()
        for i in users:              
            if self.E1.get() in i:
                founduser = True
                if (self.E2.get() == users[users.index(i)][1]):
                    Window.userloggedin = (self.E1.get())
                    self.E1.delete(0, 'end')
                    self.E2.delete(0, 'end')
                    self.E1.focus()
                    root.withdraw()
                    self.menu()
                else:
                    tk.messagebox.showwarning("Login Error.", "Username/Password Combination Not Found!")
                    Window.loginattempts +=1
                    self.E1.delete(0, 'end')
                    self.E2.delete(0, 'end')
                    self.E1.focus()
        if (founduser == False):
            tk.messagebox.showwarning("Login Error.", "User Not Found!")
            Window.loginattempts += 1
            self.E1.delete(0, 'end')
            self.E2.delete(0, 'end')
            self.E1.focus()
        if (Window.loginattempts >= 3):
            if tk.messagebox.askyesno("Login Error", "You have had 3 failed login attempts.  Would you like to create an account?"):
                self.registerwindow()
                Window.loginattempts = 0
                self.E1.delete(0, 'end')
                self.E2.delete(0, 'end')
            else:
                root.destroy()
            return
                
    #Centers tk windows based on screen size
    def center(self, toplevel):
        toplevel.update_idletasks()
        w = toplevel.winfo_screenwidth()
        h = toplevel.winfo_screenheight()
        size = tuple(int(_) for _ in toplevel.geometry().split('+')[0].split('x'))
        x = w/2 - size[0]/2
        y = h/2 - size[1]/2
        toplevel.geometry("%dx%d+%d+%d" % (size + (x, y)))

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

     #Root window   
    def init_window(self):
        self.master.title("Please Login")
        self.pack(fill=tk.BOTH, expand=1)
        photo = tk.PhotoImage(file="header.gif")
        label = tk.Label(image=photo)
        label.image = photo
        label.place(x=80, y=10)
        L1 = tk.Label(text="Username:", font=("Century Gothic", 10))
        L1.place(x=15, y=78)
        self.E1 = tk.Entry(self, font=("Century Gothic", 10), bd=2)
        self.E1.place(x=92, y=80)
        L2 = tk.Label(text="Password:", font=("Century Gothic", 10))
        L2.place(x=15, y=118)
        self.E2 = tk.Entry(self, show = "•", font=("Century Gothic", 10), bd=2)
        self.E2.place(x=92, y=120)
        loginButton = tk.Button(self, text="Login", font=("Century Gothic", 10), command=self.search)
        loginButton.place(x=175, y=155)
        registerbutton = tk.Button(self, text="Register", font=("Century Gothic", 10), command=self.registerwindow)
        registerbutton.place(x=95, y=155)
        removeaccountbutton = tk.Button(self,text=" Account \n Settings",font=("Century Gothic", 8), command= self.accountsettingswindow)
        removeaccountbutton.place(x=15, y=150)
        L3 = tk.Label(text="Colby J. Conkling 2016. v2.0",font=("Century Gothic", 7))
        L3.place(x=60, y=200)
        self.center(root)
        root.bind('<Return>', self.search)
        self.E1.focus()
    
    def accountsettingswindow(self, event=None):
        Window.asettings = tk.Toplevel(self)
        Window.asettings.wm_title("Account Settings")
        Window.asettings.protocol("WM_DELETEWINDOW", on_closing)
        Window.asettings.geometry("285x250")
        Window.asettings.focus_force()
        self.center(Window.asettings)
        L1 = tk.Label(Window.asettings, text="Account Settings", font=("Century Gothic", 15))
        L1.place(x=55, y =10)
        generatereportbutton = tk.Button(Window.asettings, text="Generate Accounts Report",  font=("Century Gothic", 10), command=self.generateusersreport)
        generatereportbutton.place(x=53, y=60)
        removeaccountbutton = tk.Button(Window.asettings, text="Remove an Account", font=("Century Gothic", 10), command=self.removeaccountwindow)
        removeaccountbutton.place(x=66, y=110)
        getdataforuserbutton = tk.Button(Window.asettings, text="Generate Performance Report for User",  font=("Century Gothic", 10), command=self.generateperformancereport)
        getdataforuserbutton.place(x=15, y=160)

    #Generates a report of active users and displays it as a text document opening with the default os program
    def generateusersreport(self, event=None):
        filename = ("User Accounts Report.txt")
        file = open(filename, 'w')
        file.write("Drill Arithmetic User Accounts Summary\n\nReport Generated On: " + time.strftime("%c"))
        data = self.load()
        file.write("\n\nNumber of Accounts: " + str(len(data) - 1))
        file.write("\n\nActive Users:\n")
        for x in range(len(data)-1):
            file.write("\n"+data[x][0])
        os.startfile("User Accounts Report.txt")
        Window.asettings.destroy()

    def generateperformancereport(self, event=None):
        tk.messagebox.showinfo("Error.", "This feature is not yet available.  Sorry. :(")
        Window.asettings.focus_force()
            
    #Creates a window to remove a user's account
    def removeaccountwindow(self, event=None):
        Window.ra = tk.Toplevel(self)
        Window.ra.wm_title("Remove Account")
        Window.ra.protocol("WM_DELETEWINDOW", on_closing)
        Window.ra.geometry("285x250")
        Window.ra.focus_force()
        self.center(Window.ra)
        L1 = tk.Label(Window.ra, text="Username:", font=("Century Gothic", 10))
        L1.place(x=15, y=58)
        Window.E1Remove = tk.Entry(Window.ra, font=("Centry Gothic", 10), bd=2)
        Window.E1Remove.place(x=120, y=60)
        L2 = tk.Label(Window.ra, text="Password:", font=("Century Gothic", 10))
        L2.place(x=15, y=98)
        Window.E2Remove = tk.Entry(Window.ra, show = "•", font=("Century Gothic", 10), bd=2)
        Window.E2Remove.place(x=120, y=100)
        L3 = tk.Label(Window.ra, text="Enter the info below to remove your account.", font=("Century Gothic", 8))
        L3.place(x=14, y=15)
        removeaccountbutton = tk.Button(Window.ra, text="Remove Account", font=("Century Gothic", 10), command=self.removeaccount)
        removeaccountbutton.place(x=85, y=190)
        Window.E1Remove.focus()
        Window.ra.bind('<Return>', self.removeaccount)

    #Creates registration window
    def registerwindow(self):
        Window.rw = tk.Toplevel(self)
        Window.rw.wm_title("Registration")
        Window.rw.protocol("WM_DELETEWINDOW", on_closing)
        Window.rw.geometry("285x250")
        Window.rw.focus_force()
        self.center(Window.rw)
        L1 = tk.Label(Window.rw, text="Username:", font=("Century Gothic", 10))
        L1.place(x=15, y=58)
        Window.E1R = tk.Entry(Window.rw, font=("Centry Gothic", 10), bd=2)
        Window.E1R.place(x=120, y=60)
        L2 = tk.Label(Window.rw, text="Password:", font=("Century Gothic", 10))
        L2.place(x=15, y=98)
        Window.E2R = tk.Entry(Window.rw, show = "•", font=("Century Gothic", 10), bd=2)
        Window.E2R.place(x=120, y=100)
        L3 = tk.Label(Window.rw, text="Confirm Psswd:", font=("Century Gothic", 10))
        L3.place(x=15, y=140)
        L4 = tk.Label(Window.rw, text="Enter the information below to create an account.", font=("Century Gothic", 8))
        L4.place(x=4, y=15)
        Window.E3R = tk.Entry(Window.rw, show = "•", font=("Century Gothic", 10), bd=2)
        Window.E3R.place(x=120, y=140)
        registerbutton = tk.Button(Window.rw, text="Create Account", font=("Century Gothic", 10), command=self.register)
        registerbutton.place(x=85, y=190)
        Window.E1R.focus()
        Window.rw.bind('<Return>', self.register)

    #Registers a new user and places credentials into users.txt if that user does not already exist.
    def register(self, event=None):
        users = self.load()
        accountfound = False
        for i in users:
            if Window.E1R.get() in i:
                accountfound = True
        if accountfound == True:
            tk.messagebox.showwarning("Account Creation Error", "Sorry, that username is already taken.")
            Window.E1R.delete(0, 'end')
            Window.E2R.delete(0, 'end')
            Window.E3R.delete(0, 'end')
            Window.rw.focus_force()
            Window.E1R.focus()
        elif (Window.E2R.get() != Window.E3R.get()):
            tk.messagebox.showwarning("Account Creation Error", "Passowrds do not match.  Please try again.")
            Window.E2R.delete(0, 'end')
            Window.E3R.delete(0, 'end')
            Window.rw.focus_force()
            Window.E2R.focus()
        else:
            with open("users.txt", "a") as file:
                file.write(Window.E1R.get() + " " + Window.E2R.get() + "\n")
            tk.messagebox.showinfo("Success", "Your account has been created.  You can now login.")
            Window.rw.withdraw()
            Window.rw.destroy()

    #Removes account from users.txt if user found and password correct
    def removeaccount(self, event=None):
        users = self.load()
        accountfound = False
        for i in users:
            if Window.E1Remove.get() in i:
                if (Window.E2Remove.get() == users[users.index(i)][1]):
                    accountfound = True
                    accountindex = users.index(i)
        if accountfound == True:
            users.pop(accountindex)
            with open("users.txt", "w") as file:
                for x in range(len(users) - 1):
                    file.write(users[x][0])
                    file.write(" ")
                    file.write(users[x][1])
                    file.write("\n")
            tk.messagebox.showinfo("Success", "Your account has been deleted.  We're sorry to see you go.")
            Window.ra.withdraw()
            Window.ra.destroy()
            Window.asettings.destroy()
        else:
            tk.messagebox.showwarning("Error Removing Account", "Username or Password Incorrect.  Please try again.")
            Window.E1Remove.delete(0, 'end')
            Window.E2Remove.delete(0, 'end')
            Window.ra.focus_force()
            Window.E1Remove.focus()
                            
    #Window where user selects what arithmetic operation to drill
    def menu(self):
        Window.t = tk.Toplevel(self)
        Window.t.wm_title("Drill Arithmetic  Logged In: " + Window.userloggedin)
        Window.t.wm_iconbitmap('icon.ico')
        Window.t.protocol("WM_DELETE_WINDOW", on_closing)
        Window.t.geometry("500x200")
        Window.t.focus_force()
        self.center(Window.t)
        inst = tk.Label(Window.t, text= "What skill would you like to practice today?", font=("Century Gothic", 16))
        inst.place(x=23, y=45)
        addButton = tk.Button(Window.t, text="Addition", font=("Century Gothic", 10), command=self.add)
        addButton.place(x=55, y=130)
        subButton = tk.Button(Window.t, text="Subtraction", font=("Century Gothic", 10), command=self.sub)
        subButton.place(x=145, y=130)
        multButton = tk.Button(Window.t, text="Multiplication", font=("Century Gothic", 10), command=self.mult)
        multButton.place(x=255, y=130)
        divisButton = tk.Button(Window.t, text="Division", font=("Century Gothic", 10), command=self.divis)
        divisButton.place(x=380, y=130)

    #Drill Button Methods
    def add(self):
        Window.name = "Addition"
        self.options_page()
    def sub (self):
        Window.name = "Subtraction"
        self.options_page()
    def mult (self):
        Window.name = "Multiplication"
        self.options_page()
    def divis (self):
        Window.name = "Division"
        self.options_page()

    #Determines if answer is correct and calls next question from the nexquestion() method
    def nextq(self, event=None):
        if (Window.entry.get() == ""):
            tk.messagebox.showwarning("No Answer!", "Please type in a number before submitting.")
            Window.m.focus_force()
            Window.entry.focus()
        else:
            if (Window.checkoption.get() == 1):
                if tk.messagebox.askyesno("Confirm", "Are you sure your answer is " + Window.entry.get() + "?"):
                    self.nextquestion(Window.entry.get())
                Window.m.focus_force()
                Window.entry.focus()
                Window.entry.delete(0, 'end')
            else:
                self.nextquestion(Window.entry.get())
                Window.entry.delete(0, 'end')
            
    #Main window where users answer arithmetic problems
    def main(self):
        Window.operand1 = int(Window.rentry1.get())
        Window.operand2 = int(Window.rentry2.get())
        if (Window.qnumber.get()== "10"):
            Window.numberofquestions = 10
        if (Window.qnumber.get()== "15"):
            Window.numberofquestions = 15
        if (Window.qnumber.get()== "20"):
            Window.numberofquestions = 20
        Window.o.withdraw()
        Window.questioncount = 0
        Window.totalcorrect = 0
        Window.t.withdraw()
        Window.m = tk.Toplevel(self)
        Window.m.wm_title("Logged In: " + Window.userloggedin)
        Window.m.wm_iconbitmap('icon.ico')
        Window.m.protocol("WM_DELETE_WINDOW", on_closing)
        Window.m.geometry("320x200")
        Window.m.focus_force()
        self.center(Window.m)
        tk.Label(Window.m, textvariable=Window.output, font=("Century Gothic", 16)).place(x=36,y=38)
        Window.output.set("Loading...")
        L1 = tk.Label(Window.m, font=("Century Gothic", 10), text="Your Answer: ")
        L1.place(x=38, y=107)
        Window.entry = tk.Entry(Window.m, bd=2)
        Window.entry.place(x=132, y=109)
        submitButton = tk.Button(Window.m, text="Submit", font=("Century Gothic", 10), command=self.nextq)
        submitButton.place(x=132, y=150)
        Window.m.bind('<Return>', self.nextq)
        Window.entry.focus()
        if (Window.name == "Addition"):
            self.addition()
        if (Window.name == "Subtraction"):
            self.subtraction()
        if (Window.name == "Multiplication"):
            self.multiplication()
        if (Window.name == "Division"):
            self.division()

    #Options page that is brought up before user starts drilling
    def options_page(self):
        Window.t.withdraw()
        Window.o = tk.Toplevel(self)
        Window.o.wm_title("Drill Arithmetic Options")
        Window.o.wm_iconbitmap('icon.ico')
        Window.o.protocol("WM_DELETE_WINDOW", on_closing)
        Window.o.geometry("320x230")
        Window.o.focus_force()
        self.center(Window.o)
        L1 = tk.Label(Window.o, font=("Century Gothic", 18), text="OPTIONS")
        L1.place(x=110, y=5)
        Window.rentry1 = tk.Entry(Window.o, bd=2)
        Window.rentry1.place(x=190, y=100, width=20)
        Window.rentry1.insert(0, "1")
        Window.rentry2 = tk.Entry(Window.o, bd=2)
        Window.rentry2.place(x=255, y=100, width=20)
        Window.rentry2.insert(0, "10")
        L2 = tk.Label(Window.o, font=("Century Gothic", 10), text="Operands Between:")
        L2.place(x=50, y=98)
        L3 = tk.Label(Window.o, font=("Century Gothic", 10), text="and")
        L3.place(x=215, y=100)
        L2 = tk.Label(Window.o, font=("Century Gothic", 10), text="Number of Questions:")
        L2.place(x=10, y=140)
        c = tk.Checkbutton(Window.o, text="Confirm Answers Before Submission", variable=Window.checkoption)
        c.place(x=50,y=55)
        r1 = tk.Radiobutton(Window.o, text="5 ", variable=Window.qnumber, value="5", indicatoron=0)
        r1.place(x=162,y=140)
        r2 = tk.Radiobutton(Window.o, text="10", variable=Window.qnumber, value="10", indicatoron=0)
        r2.place(x=200,y=140)
        r3 = tk.Radiobutton(Window.o, text="15", variable=Window.qnumber, value="15", indicatoron=0)
        r3.place(x=240,y=140)
        r4 = tk.Radiobutton(Window.o, text="20", variable=Window.qnumber, value="20", indicatoron=0)
        r4.place(x=280,y=140)
        StartButton = tk.Button(Window.o, text="Start Drilling", font=("Century Gothic", 10), command=self.main)
        StartButton.place(x=120, y=185)

    #Gives the results for the current drill to the user, including number of questions answered correctly,
    #number of questionsanswered incorrectly, and the percentage and letter grade.
    def results_page(self):
        Window.m.withdraw()
        Window.r = tk.Toplevel(self)
        Window.r.wm_title("Results for User: " + Window.userloggedin)
        Window.r.wm_iconbitmap('icon.ico')
        Window.r.protocol("WM_DELETE_WINDOW", on_closing)
        Window.r.geometry("340x260")
        Window.r.focus_force()
        self.center(Window.r)
        L1 = tk.Label(Window.r, text="Skill: " + Window.name, font=("Century Gothic", 15))
        L1.place(x=5, y=20)
        L2 = tk.Label(Window.r, text="Questions Answered Correctly: " + str(Window.totalcorrect), font=("Century Gothic", 15))
        L2.place(x=5, y=60)
        L3 = tk.Label(Window.r, text="Questions Answered Wrong: " + str(Window.numberofquestions - Window.totalcorrect), font=("Century Gothic", 15))
        L3.place(x=5, y=100)
        percentage = ((Window.totalcorrect / Window.numberofquestions)*100)
        if   (percentage >=90):
            grade = "A"
        elif (percentage >=80):
            grade = "B"
        elif (percentage >=70):
            grade = "C"
        elif (percentage >=60):
            grade = "D"
        else:
            grade = "F"
        L4 = tk.Label(Window.r, text="Percentage: " + str(percentage) + "%", font=("Century Gothic", 15))
        L4.place(x=5, y=140)
        L5 = tk.Label(Window.r, text="Grade: " + grade, font=("Century Gothic", 15))
        L5.place(x=5, y=180)
        againButton = tk.Button(Window.r, text="Practice Some More", font=("Century Gothic", 10), command=self.playagain)
        againButton.place(x=120, y=220)
        logoutButton = tk.Button(Window.r, text="Logout", font=("Century Gothic", 10), command=self.logout)
        logoutButton.place(x=50, y=220)

    #Closes result page and returns to initial window
    def logout(self, event=None):
        Window.r.withdraw()
        root.deiconify()
        self.E1.focus()
        
    #Called to drill another skill after comopletion
    def playagain(self, event=None):
        Window.r.withdraw()
        Window.r.destroy()
        self.menu()

   #Calls another question or delivers results page if all questions answered 
    def nextquestion(self, answer):
        Window.questioncount +=1
        if (answer == Window.correctanswer):
            Window.totalcorrect +=1
            Window.output.set("             Correct!")
            Window.m.update()
            time.sleep(1)
        else:
            Window.output.set("Wrong. The answer is " + str(Window.correctanswer) +".")
            Window.m.update()
            time.sleep(1.5)
        if (Window.questioncount == Window.numberofquestions):        
            self.results_page()
        else:
            if (Window.name == "Addition"):
                self.addition()
            if (Window.name == "Subtraction"):
                self.subtraction()
            if (Window.name == "Multiplication"):
                self.multiplication()
            if (Window.name == "Division"):
                 self.division()

   #Arithmetic question methods       
    def addition(self):
        number1 = random.randrange(Window.operand1, Window.operand2)
        number2 = random.randrange(Window.operand1, Window.operand2)
        Window.output.set("Please calculate " + str(number1) + " + " + str(number2))
        Window.correctanswer = str(number1 + number2)

    def multiplication(self):
        number1 = random.randrange(Window.operand1, Window.operand2)
        number2 = random.randrange(Window.operand1, Window.operand2)
        Window.output.set("Please calculate " + str(number1) + " x " + str(number2) + ":\n")
        Window.correctanswer = str(number1 * number2)

    def subtraction(self):
        number1 = -1
        number2 = 0
        while(number1 < number2): #Ensures that the 1st number is greater than the 2nd.
            number1 = random.randrange(Window.operand1, Window.operand2)
            number2 = random.randrange(Window.operand1, Window.operand2)
        Window.output.set("Please calculate " + str(number1) + " - " + str(number2) + ":\n")
        Window.correctanswer = str(number1 - number2)
    
    def division(self):
        number1 = random.randrange(Window.operand1, Window.operand2)
        number2 = random.randrange(Window.operand1, Window.operand2)
        Window.output.set("Please calculate " + str(number1*number2) + " ÷ " + str(number1) + ":\n")
        Window.correctanswer = str(int((number1*number2) / number1))

#Ensures that the program does not continue to run after windows are closed
def on_closing():
    root.destroy()

#Sets dimensions, icon for main window, and starts mainloop     
root.wm_iconbitmap('icon.ico')
root.protocol("WM_DELETE_WINDOW", on_closing)
root.geometry("250x220")
app = Window(root)
root.mainloop()

 
