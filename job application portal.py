from tkinter import *
from tkinter import messagebox
class Login:
    def __init__(self, myw):
        self.myw = myw
        self.myw.title("ONLINE JOB PORTAL")
        self.myw.geometry('1199x600+60+40')
        myw.configure(bg='light blue')
        frame = Frame(self.myw, bg='white')
        frame.place(x=330, y=150, width=500, height=400)
        # title
        title = Label(frame, text="Login Here", font=(
            "Impact", 35, "bold"), fg="#6162FF", bg='white').place(x=60, y=30)
        sub_title = Label(frame, text="Members Login", font=(
            "Goudy old style", 15, "bold"), fg="green", bg='white').place(x=60, y=100)
        username = Label(frame, text="Username", font=(
            "Goudy old style", 15, "bold"), fg="grey", bg='white').place(x=60, y=140)
        self.username = Entry(frame, bg='white')
        self.username.place(x=60, y=170, width=320, height=35)
        password = Label(frame, text="Password", font=(
            "Goudy old style", 15, "bold"), fg="grey", bg='white').place(x=60, y=210)
        self.password = Entry(frame, bg='white')
        self.password.place(x=60, y=240, width=320, height=35)
        # button
        submit = Button(frame, command=self.check_function, cursor='hand2', text="Login", font=(
            "Goudy old style", 12, "bold"), fg="black", bg='white').place(x=190, y=320)
        new_account = Button(frame, text="Create New Account", cursor='hand2', bd=0, font=(
            "Goudy old style", 12, "bold"), fg="green", bg='white', command=self.open_new_window)
        new_account.place(x=140, y=280)

    def check_function(self):
        if self.username.get() == "" or self.password.get() == "":
            messagebox.showerror(
                "error", "All flieds are empty", parent=self.myw)
        elif self.username.get() == "1234" or self.password.get() == "sai":
            messagebox.showerror(
                "error", "Invalid Username or Password", parent=self.myw)
        else:
            messagebox.showinfo(
                "Welcome", "successfully logged in", parent=self.myw)
            self.open_new_portal()

    def open_new_window(self):
        self.new_window = Toplevel(self.myw)
        self.new_window.title("Register")
        self.new_window.geometry("800x400")
        self.name_text = StringVar()
        self.email_text = StringVar()
        self.password_text = StringVar()
        self.password1_text = StringVar()
        self.mobile_text = StringVar()
        self.age_text = StringVar()

        Label(self.new_window, text="Register here", bg='light green').pack()
        name = Label(self.new_window, text="Name:").place(x=100, y=50)
        self.name = Entry(self.new_window, bg='white', textvariable=self.name_text).place(
            x=140, y=50, width=250, height=25)
        age = Label(self.new_window, text="Age:").place(x=110, y=80)
        self.age = Entry(self.new_window, bg='white', textvariable=self.age_text).place(
            x=140, y=80, width=250, height=25)
        mobile = Label(self.new_window, text="Contact.No:").place(x=70, y=110)
        self.mobile = Entry(self.new_window, bg='white', textvariable=self.mobile_text).place(
            x=140, y=110, width=250, height=25)
        email = Label(self.new_window, text="email_id:").place(x=80, y=140)
        self.email = Entry(self.new_window, bg='white', textvariable=self.email_text).place(
            x=140, y=140, width=250, height=25)
        password = Label(
            self.new_window, text="Create password:").place(x=40, y=170)
        self.password = Entry(self.new_window, bg='white', textvariable=self.password_text).place(
            x=140, y=170, width=250, height=25)
        password1 = Label(
            self.new_window, text="Confirm password:").place(x=30, y=200)
        self.password1 = Entry(self.new_window, bg='white', textvariable=self.password1_text).place(
            x=140, y=200, width=250, height=25)
        chk=Checkbutton(self.new_window,text='I Agree the terms and Conditions',onvalue=1,offvalue=0,font=('times new roman',12)).place(x=90,y=250)
        register = Button(self.new_window, text="Register", cursor='hand2', font=("Times_New_Roman", 12, "bold"),
                          fg="black", bg='white', command=self.register_data).place(x=220, y=300)

    def register_data(self):
        if (self.name_text.get() == " ") or \
           (self.email_text.get() == "") or \
           (self.password_text.get() == "") or \
           (self.password1_text.get() == "") or \
           (self.mobile_text.get() == "") or \
           (self.age_text.get() == ""):

            messagebox.showerror(
                "ERROR", "All flieds are mandatory", parent=self.new_window)

        elif self.password_text.get() != self.password1_text.get():
            messagebox.showerror(
                "Error", "Password & confirm password should be same", parent=self.new_window)
        else:
            messagebox.showinfo(
                "Success", "Register successful", parent=self.new_window)
            self.open_new_portal()
    def open_new_portal(self):
            self.new_portal=Toplevel(self.myw)
            self.new_portal.title("job")
            self.new_portal.geometry('500x400')
            self.new_portal.title("JOBS SEARCH")
            apply = Button(self.new_portal, text="Post a job", cursor='hand2', font=("Comic sans ms", 19, "bold"),
                           fg="orange",bg='green', command=self.job_form).place(x=90, y=60)
            apply = Button(self.new_portal, text="Find a job", cursor='hand2', font=("Comic sans ms", 19, "bold"),
                           fg="black", bg='white', command=self.open_job_portal).place(x=90, y=150)




    def open_job_portal(self):
        self.job_portal = Toplevel(self.myw)
        self.job_portal.title("Job portal")
        self.job_portal.geometry("1199x600+60+40")
        self.job_portal.title("JOB APPLY")
        Label(self.job_portal, text="Job portal", bg='light blue',
              font=("Times_New_Roman", 23, "bold")).pack()
        Label(self.job_portal, text="Select The Job As Per Your Qualification ",
              bg='orange', font=("Times_New_Roman", 13, "bold")).pack()
        Label(self.job_portal, text="Company Name", font=(
            "times new roman", 12, "bold"), fg="black", bg='white').place(x=10, y=80)
        Label(self.job_portal, text="Location", font=(
            "times new roman", 12, "bold"), fg="black", bg='white').place(x=200, y=80)
        Label(self.job_portal, text="Salary", font=(
            "times new roman", 12, "bold"), fg="black", bg='white').place(x=350, y=80)
        Label(self.job_portal, text="Work Profile", font=(
            "times new roman", 12, "bold"), fg="black", bg='white').place(x=500, y=80)
        Label(self.job_portal, text="Job requirements", font=(
            "times new roman", 12, "bold"), fg="black", bg='white').place(x=750, y=80)
        Label(self.job_portal, text="Oracle").place(x=30, y=150)
        Label(self.job_portal, text="INFOSYS").place(x=30, y=200)
        Label(self.job_portal, text="Dell").place(x=30, y=250)
        Label(self.job_portal, text="Microsoft").place(x=30, y=300)
        Label(self.job_portal, text="Autodesk").place(x=30, y=350)
        Label(self.job_portal,text="Mahindra").place(x=30,y=400)
        Label(self.job_portal, text="Tata Moters").place(x=30, y=450)
        Label(self.job_portal, text="Airtel").place(x=30, y=500)
        Label(self.job_portal, text="Bangalore").place(x=200, y=150)
        Label(self.job_portal, text="HYDERABAD").place(x=200, y=200)
        Label(self.job_portal, text="MUMBAI").place(x=200, y=250)
        Label(self.job_portal, text="CHENNAI").place(x=200, y=300)
        Label(self.job_portal, text="VENICE").place(x=200, y=350)
        Label(self.job_portal,text='Punjab').place(x=200,y=400)
        Label(self.job_portal, text="Jharkhand").place(x=200,y=450)
        Label(self.job_portal, text="Manipur").place(x=200, y=500)
        Label(self.job_portal, text="30,000").place(x=350, y=150)
        Label(self.job_portal, text="49,000").place(x=350, y=200)
        Label(self.job_portal, text="70,000").place(x=350, y=250)
        Label(self.job_portal, text="80,000").place(x=350, y=300)
        Label(self.job_portal, text="50,000").place(x=350, y=350)
        Label(self.job_portal, text="54,900").place(x=350, y=400)
        Label(self.job_portal, text="43,330").place(x=350, y=450)
        Label(self.job_portal, text="67,000").place(x=350, y=500)

        Label(self.job_portal, text="Software Developer").place(x=500, y=150)
        Label(self.job_portal, text="Data scientist").place(x=500, y=200)
        Label(self.job_portal, text="Quality Analyst").place(x=500, y=250)
        Label(self.job_portal, text="Mobile Test Engineer").place(x=500, y=300)
        Label(self.job_portal, text="Back-end Developer").place(x=500, y=350)
        Label(self.job_portal, text="Marketing Management").place(x=500, y=400)
        Label(self.job_portal, text="Auditor").place(x=500, y=450)
        Label(self.job_portal, text="Retail Management").place(x=500, y=500)
        Label(self.job_portal, text="c,c++").place(x=750, y=150)
        Label(self.job_portal, text="HTML& CSS,Javascript ").place(x=750, y=200)
        Label(self.job_portal, text="Python,DATA STRUCTURE").place(x=750, y=250)
        Label(self.job_portal, text="Python,Java,c,c++").place(x=750, y=300)
        Label(self.job_portal, text="Java,c++").place(x=750, y=350)
        Label(self.job_portal, text="Mba,PG").place(x=750, y=400)
        Label(self.job_portal, text="B.com,Degree").place(x=750, y=450)
        Label(self.job_portal, text="Mba degree").place(x=750, y=500)

        apply = Button(self.job_portal, text="APPLY", cursor='hand2', font=("Goudy old style", 10, "bold"), fg="black",
                       bg='white', command=self.job_form).place(x=1000, y=140)
        apply = Button(self.job_portal, text="APPLY", cursor='hand2', font=("Goudy old style", 10, "bold"), fg="black",
                       bg='white', command=self.job_form).place(x=1000, y=190)
        apply = Button(self.job_portal, text="APPLY", cursor='hand2', font=("Goudy old style", 10, "bold"), fg="black",
                       bg='white', command=self.job_form).place(x=1000, y=240)
        apply = Button(self.job_portal, text="APPLY", cursor='hand2', font=("Goudy old style", 10, "bold"), fg="black",
                       bg='white', command=self.job_form).place(x=1000, y=290)
        apply = Button(self.job_portal, text="APPLY", cursor='hand2', font=("Goudy old style", 10, "bold"), fg="black",
                       bg='white', command=self.job_form).place(x=1000, y=340)
        apply = Button(self.job_portal, text="APPLY", cursor='hand2', font=("Goudy old style", 10, "bold"), fg="black",
                       bg='white', command=self.job_form).place(x=1000, y=390)
        apply = Button(self.job_portal, text="APPLY", cursor='hand2', font=("Goudy old style", 10, "bold"), fg="black",
                       bg='white', command=self.job_form).place(x=1000, y=390)
        apply = Button(self.job_portal, text="APPLY", cursor='hand2', font=("Goudy old style", 10, "bold"), fg="black",
                       bg='white', command=self.job_form).place(x=1000, y=440)
        apply = Button(self.job_portal, text="APPLY", cursor='hand2', font=("Goudy old style", 10, "bold"), fg="black",
                       bg='white', command=self.job_form).place(x=1000, y=490)
    def job_form(self):
        self.job_form = Toplevel(self.myw)
        self.job_form.title("APPLICATION PORTAL")
        self.job_form.geometry('1200x800')
        self.job_form.title("JOB APPLICATION")
        Label(self.job_form, text="Job requirements", font=(
            "times new roman", 12, "bold"), fg="black", bg='white').place(x=50, y=80)
        Label(self.job_form, text="APPLICATION FORM", font=(
            "times new roman", 12, "bold"), fg="black", bg='orange').place(x=540, y=10)
        Label(self.job_form, text="Please fill the form to apply", font=(
            "times new roman", 12, "bold"), fg="black", bd=0, bg='pink').place(x=530, y=40)
        leftframe = Frame(self.job_form, height=200,
                          width=500)
        leftframe.place(x=10, y=70)
        Label(self.job_form, text="Personal details:", font=12).place(x=10, y=30)
        self.l1_text = StringVar()
        self.l15_text = StringVar()
        self.l30_text = StringVar()
        self.l34_text = StringVar()
        self.l2_text = StringVar()
        self.l25_text = StringVar()
        self.l7_text = StringVar()
        l1 = Label(leftframe, text='First Name:')
        l1.place(x=13, y=30)
        self.l1 = Entry(leftframe, bg="white").place(x=85, y=32)
        l2 = Label(leftframe, text='Last name:')
        l2.place(x=13, y=60)
        self.l2 = Entry(leftframe, bg="white").place(x=85, y=62)
        l3 = Label(leftframe, text='Email id:')
        l3.place(x=24, y=90)
        self.l3 = Entry(leftframe, bg="white").place(x=85, y=92)
        l4 = Label(leftframe, text='Age:')
        l4.place(x=44, y=120)
        self.l4 = Entry(leftframe, bg="white").place(x=85, y=122)
        l5 = Label(leftframe, text='Pan Number:')
        l5.place(x=4, y=150)
        self.l5 = Entry(leftframe, bg="white").place(x=85, y=152)
        l6 = Label(leftframe, text='Middle Name:')
        l6.place(x=220, y=30)
        self.l6 = Entry(leftframe, bg="white").place(x=310, y=33)
        l7 = Label(leftframe, text='Mobile No:')
        l7.place(x=230, y=60)
        self.l7 = Entry(leftframe, bg="white").place(x=310, y=63)
        l8 = Label(leftframe, text='Date of Birth:')
        l8.place(x=220, y=90)
        self.l8 = Entry(leftframe, bg="white").place(x=310, y=93)
        l9 = Label(leftframe, text='Gender=M/F/T:')
        l9.place(x=212, y=120)
        self.l9 = Entry(leftframe, bg="white").place(x=310, y=123)
        l10 = Label(leftframe, text='Aadhar No:')
        l10.place(x=230, y=150)
        self.l10 = Entry(leftframe, bg="white").place(x=310, y=153)
        frame = Frame(self.job_form, height=300, width=500)
        frame.place(x=10, y=330)
        Label(self.job_form, text="Educational qualification:",
              font=12).place(x=10, y=300)
        l11 = Label(frame, text="Degree:")
        l11.place(x=15, y=15)
        self.l11 = Entry(frame, bg="white").place(x=80, y=15)
        l12 = Label(frame, text="start Date:")
        l12.place(x=10, y=50)
        self.l12 = Entry(frame, bg="white").place(x=80, y=50)
        l13 = Label(frame, text="End Date:")
        l13.place(x=10, y=85)
        self.l13 = Entry(frame, bg="white").place(x=80, y=85)
        l14 = Label(frame, text="Institute:")
        l14.place(x=10, y=120)
        self.l14 = Entry(frame, bg="white").place(x=80, y=120)
        l15 = Label(frame, text="Percentage:")
        l15.place(x=4, y=155)
        self.l15 = Entry(frame, bg="white").place(x=80, y=155)
        l16 = Label(frame, text="Degree:")
        l16.place(x=240, y=15)
        self.l16 = Entry(frame, bg="white").place(x=300, y=15)
        l17 = Label(frame, text="start Date:")
        l17.place(x=225, y=50)
        self.l17 = Entry(frame, bg="white").place(x=300, y=50)
        l18 = Label(frame, text="End Date:")
        l18.place(x=227, y=85)
        self.l18 = Entry(frame, bg="white").place(x=300, y=85)
        l19 = Label(frame, text="Institute:")
        l19.place(x=229, y=120)
        self.l19 = Entry(frame, bg="white").place(x=300, y=120)
        l20 = Label(frame, text="Percentage:")
        l20.place(x=215, y=155)
        self.l20 = Entry(frame, bg="white").place(x=300, y=155)
        l21 = Label(frame, text="Branch:")
        l21.place(x=233, y=190)
        self.l21 = Entry(frame, bg="white").place(x=300, y=190)
        rightframe = Frame(self.job_form, height=500, width=500)
        rightframe.place(x=600, y=90)
        Label(self.job_form, text="WORK EXPERIENCE",
               font="12").place(x=650, y=90)
        l22 = Label(rightframe, text='work section',bg='light green')
        l22.place(x=100, y=30)
        l23 = Label(rightframe, text='Total work experience:')
        l23.place(x=5, y=60)
        self.l23 = Entry(rightframe, bg="white").place(x=155, y=62)
        l24 = Label(rightframe, text='Reason for leaving:')
        l24.place(x=5, y=90)
        self.l24 = Entry(rightframe, bg="white").place(x=155, y=92)
        l25 = Label(rightframe, text="Internship",bg="light blue")
        l25.place(x=100, y=120)
        l26 = Label(rightframe, text='Company:')
        l26.place(x=20, y=150)
        self.l26 = Entry(rightframe, bg="white").place(x=155, y=152)
        l26 = Label(rightframe, text='Job title:')
        l26.place(x=20, y=180)
        self.l26 = Entry(rightframe, bg="white").place(x=155, y=182)
        l27 = Label(rightframe, text='Start date:')
        l27.place(x=20, y=210)
        self.l27 = Entry(rightframe, bg="white").place(x=155, y=212)
        l28 = Label(rightframe, text='End date:')
        l28.place(x=20, y=240)
        self.l28 = Entry(rightframe, bg="white").place(x=155, y=242)
        l29 = Label(rightframe, text='Skills:')
        l29.place(x=20, y=270)
        self.l29 = Entry(rightframe, bg="white").place(x=155, y=272)
        l30 = Label(rightframe, text='Language-1:')
        l30.place(x=15, y=300)
        self.l30 = Entry(rightframe, bg="white").place(x=155, y=302)
        l32 = Label(rightframe, text='Language-2:')
        l32.place(x=14, y=330)
        self.l32 = Entry(rightframe, bg="white").place(x=155, y=332)
        l33 = Label(rightframe, text='Current address:')
        l33.place(x=10, y=360)
        self.l33 = Entry(rightframe, bg="white").place(x=155, y=362)
        l34 = Label(rightframe, text='Permanent address:')
        l34.place(x=3, y=390)
        self.l34 = Entry(rightframe, bg="white").place(x=155, y=392)
        button1 = Button(rightframe, text="Submit",cursor="hand2", command=self.check_submit,font=(
            "times new roman", 12, "bold"), fg="black", bg='white')
        button1.place(x=150, y=450)

    def check_submit(self):
        if(self.l1_text.get() == " ") or \
                (self.l2_text.get() == "") or \
                (self.l30_text.get() == "") or \
                (self.l15_text.get() == "") or \
                (self.l34_text.get() == "") or \
                (self.l25_text.get() == "") or\
                (self.l14.get() == ""):
            messagebox.showerror(
                "ERROR", "All flieds are mandatory", parent=self.job_form)
        else:
            messagebox.showinfo("Success", "Register successful", parent=self.job_form)

myw = Tk()
obj = Login(myw)
myw.mainloop()