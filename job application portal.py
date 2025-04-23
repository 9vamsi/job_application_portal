from tkinter import *
from tkinter import messagebox
import os

class JobPortal:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("600x500")
        self.root.config(bg="lightblue")

        self.email_text = StringVar()
        self.password_text = StringVar()

        Label(self.root, text="Login Form", font=("times new roman", 20, "bold"), bg="lightblue").place(x=220, y=30)

        Label(self.root, text="Email", font=("times new roman", 15), bg="lightblue").place(x=120, y=100)
        Entry(self.root, textvariable=self.email_text, font=("times new roman", 15)).place(x=200, y=100, width=200)

        Label(self.root, text="Password", font=("times new roman", 15), bg="lightblue").place(x=120, y=150)
        Entry(self.root, textvariable=self.password_text, show="*", font=("times new roman", 15)).place(x=200, y=150, width=200)

        Button(self.root, text="Login", command=self.login_function, font=("times new roman", 15), bg="green", fg="white").place(x=250, y=200, width=100)
        Button(self.root, text="New user? Register here", command=self.register_form, font=("times new roman", 10), bg="lightblue", fg="blue").place(x=220, y=250)

        if not os.path.exists("users.txt"):
            open("users.txt", "w").close()

    def login_function(self):
        email = self.email_text.get().strip()
        password = self.password_text.get().strip()

        if email == "" or password == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return

        with open("users.txt", "r") as file:
            for line in file:
                user_email, user_pass = line.strip().split(",")
                if email == user_email and password == user_pass:
                    messagebox.showinfo("Success", f"Welcome {email}!", parent=self.root)
                    self.job_list()
                    return

        messagebox.showerror("Error", "Invalid Email or Password", parent=self.root)

    def register_form(self):
        self.new_window = Toplevel(self.root)
        self.new_window.title("Register")
        self.new_window.geometry("500x400")
        self.new_window.config(bg="lightgreen")

        self.reg_email_text = StringVar()
        self.reg_pass_text = StringVar()

        Label(self.new_window, text="Register", font=("times new roman", 20, "bold"), bg="lightgreen").place(x=200, y=30)

        Label(self.new_window, text="Email", font=("times new roman", 15), bg="lightgreen").place(x=100, y=100)
        Entry(self.new_window, textvariable=self.reg_email_text, font=("times new roman", 15)).place(x=200, y=100, width=200)

        Label(self.new_window, text="Password", font=("times new roman", 15), bg="lightgreen").place(x=100, y=150)
        Entry(self.new_window, textvariable=self.reg_pass_text, show="*", font=("times new roman", 15)).place(x=200, y=150, width=200)

        Button(self.new_window, text="Submit", command=self.new_register, font=("times new roman", 15), bg="blue", fg="white").place(x=200, y=200)

    def new_register(self):
        email = self.reg_email_text.get().strip()
        password = self.reg_pass_text.get().strip()

        if email == "" or password == "":
            messagebox.showerror("Error", "All fields are required", parent=self.new_window)
            return

        with open("users.txt", "r") as file:
            for line in file:
                user_email, _ = line.strip().split(",")
                if email == user_email:
                    messagebox.showerror("Error", "User already exists", parent=self.new_window)
                    return

        with open("users.txt", "a") as file:
            file.write(f"{email},{password}\n")

        messagebox.showinfo("Success", "Registration successful", parent=self.new_window)
        self.new_window.destroy()

    def job_list(self):
        self.job_portal = Toplevel(self.root)
        self.job_portal.title("Job Portal")
        self.job_portal.geometry("500x500")
        self.job_portal.config(bg="lightyellow")

        Label(self.job_portal, text="Job List", font=("times new roman", 20, "bold"), bg="lightyellow").pack(pady=20)

        jobs = ["Software Engineer", "Data Analyst", "Web Developer"]
        y = 80
        for job in jobs:
            Label(self.job_portal, text=job, font=("times new roman", 15), bg="lightyellow").place(x=100, y=y)
            Button(self.job_portal, text="APPLY", command=self.job_form, font=("times new roman", 10), bg="blue", fg="white").place(x=300, y=y)
            y += 40

    def job_form(self):
        self.application_form = Toplevel(self.root)
        self.application_form.title("Job Application")
        self.application_form.geometry("400x400")
        self.application_form.config(bg="lightgray")

        self.name_text = StringVar()
        self.email_text_form = StringVar()
        self.phone_text = StringVar()
        self.terms_var = IntVar()

        Label(self.application_form, text="Job Application Form", font=("times new roman", 18, "bold"), bg="lightgray").pack(pady=10)

        leftframe = Frame(self.application_form, bg="lightgray")
        leftframe.place(x=20, y=60, width=360, height=300)

        Label(leftframe, text="Name", font=("times new roman", 12), bg="lightgray").place(x=10, y=30)
        Entry(leftframe, textvariable=self.name_text, bg="white").place(x=85, y=30)

        Label(leftframe, text="Email", font=("times new roman", 12), bg="lightgray").place(x=10, y=70)
        Entry(leftframe, textvariable=self.email_text_form, bg="white").place(x=85, y=70)

        Label(leftframe, text="Phone", font=("times new roman", 12), bg="lightgray").place(x=10, y=110)
        Entry(leftframe, textvariable=self.phone_text, bg="white").place(x=85, y=110)

        Checkbutton(leftframe, text="I agree to terms and conditions", variable=self.terms_var, onvalue=1, offvalue=0, bg="lightgray").place(x=10, y=150)

        Button(self.application_form, text="Submit", command=self.submit_form, font=("times new roman", 12), bg="green", fg="white").place(x=150, y=350)

    def submit_form(self):
        if self.name_text.get().strip() == "" or self.email_text_form.get().strip() == "" or self.phone_text.get().strip() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.application_form)
        elif self.terms_var.get() != 1:
            messagebox.showerror("Error", "You must agree to the terms and conditions", parent=self.application_form)
        else:
            messagebox.showinfo("Success", "Application submitted successfully!", parent=self.application_form)
            self.application_form.destroy()


root = Tk()
obj = JobPortal(root)
root.mainloop()
