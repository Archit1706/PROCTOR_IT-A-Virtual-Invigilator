# importing the required libraries
from tkinter import *
from tkinter import messagebox
# import mtTkinter
from PIL import ImageTk
import mysql.connector
from HomePage import HomePage


# creating a class login
class Login:

    # creating a simple tkinter window
    def __init__(self, root):
        # creating a window
        self.root = root
        self.root.title("Login System")
        # self.root.geometry("1000x600+150+20")
        self.root.wm_attributes("-fullscreen", True)
        self.root.resizable(False, False)

        # adding background image to the window and the login button
        self.bg = ImageTk.PhotoImage(file="resources/loginBg.png")
        # self.login_btn = PhotoImage(file="Login.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relheight=1,
                                                              relwidth=1)
        self.name_var = StringVar()
        self.password_var = StringVar()
        self.login()

    # adding widgets to the login window
    def login(self):
        # Creating a login frame
        self.Frame_Login = Frame(self.root, bg="#4152b3")
        self.Frame_Login.place(x=675, y=140, height=500, width=600)

        #  Giving a title to the login page
        self.title = Label(self.Frame_Login, text="Student Login", font=(
            "Helvetica", 40, "bold"), bg="#4152b3", fg="white").place(x=110, y=20)

        # Username
        # label
        self.username_label = Label(self.Frame_Login, text="Username", font=("Helvetica", 16), bg="#4152b3",
                                    fg="white")
        self.username_label.place(x=180, y=150)

        # entry
        self.user_input = Entry(self.Frame_Login, font=(
            "Helvetica", 14), textvariable=self.name_var)
        self.user_input.place(x=180, y=180)
        self.user_input.focus()

        # Password
        # label
        self.password_label = Label(self.Frame_Login, text="Password", font=("Helvetica", 16), bg="#4152b3",
                                    fg="white")
        self.password_label.place(x=180, y=220)
        # entry
        self.pass_input = Entry(self.Frame_Login, font=(
            "Helvetica", 14), textvariable=self.password_var, show="*")
        self.pass_input.place(x=180, y=250)

        # login Button
        self.login = Button(self.Frame_Login, text="Login", font=("Helvetica", 25), bg="white", fg="#4152b3",
                            highlightthickness=0, height=1, width=11, borderwidth=0, command=self.check).place(x=180, y=320)

        # For new students
        # label
        self.no_account = Label(self.Frame_Login, text="Don't have an account?", font=(
            "Helvetica", 10), bg="#4152b3", fg="white").place(x=180, y=430)

        # button
        self.signup = Button(self.Frame_Login, text="SignUp", font=("Helvetica", 10, "underline"), bg="#4152b3", fg="white", height=1, width=8, command=self.signup,
                             highlightthickness=0, bd=0).place(x=320, y=430)

    # function for signup
    def signup(self):
        self.root.destroy()
        exec(open("Project\Signup.py").read())

    # function for checking the credentials of the user and opening the main window

    def check(self):
        # getting the values from the entry fields
        self.username = self.name_var.get()
        self.password = self.password_var.get()
        # print(username)
        # print(password)

        # if anyone or both the fields are empty
        if self.username == "" or self.password == "":
            msg = 'Username and Password cannot be empty!'
            messagebox.showwarning('message', msg, parent=self.root)

        # if the username is not alphanumeric
        # elif not(any(ch.isdigit() for ch in self.username)) or not(any(ch.isalpha() for ch in self.username)):
        #     msg = 'Username should be Alpha-Numeric\n Eg. admin123'
        #     messagebox.showwarning('message', msg, parent=self.root)

        # if username is very small
        elif len(self.username) <= 4:
            msg = 'Username is too short. Username should be 5 to 15 characters long'
            messagebox.showwarning('message', msg, parent=self.root)

        # if username is very long
        elif len(self.username) > 16:
            msg = 'Username is too long. Username should be 5 to 15 characters long'
            messagebox.showwarning('message', msg, parent=self.root)

        # if everything is fine start database connection and check the credentials
        else:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234567",
                    database="proctor_it"
                )

                mycursor = mydb.cursor()
                mycursor.execute(
                    "SELECT * FROM login WHERE username = %s AND password = %s", (self.username, self.password))
                myresult = mycursor.fetchall()

                for row in myresult:
                    if row[0] == self.username and row[1] == self.password:
                        msg = 'Login Successful'
                        messagebox.showinfo('message', msg, parent=self.root)
                        # exec(open("HomePage.py").read())
                        # self.root.destroy()
                        # win = Tk()
                        # self.win = Toplevel(self.root)
                        # self.win = Toplevel()
                        # self.root.quit()
                        self.user_input.delete(0, END)
                        self.pass_input.delete(0, END)

                        HomePage(self.root, self.username)

                        # self.root.quit()

                        # print("login success")
                        # self.home()
                    else:
                        # continue
                        msg = 'Invalid Username or Password'
                        messagebox.showwarning(
                            'message', msg, parent=self.root)
                        self.user_input.delete(0, END)
                        self.pass_input.delete(0, END)

            # if error occurs in the database connection then show the error message
            except Exception as ep:
                messagebox.showwarning('error', ep, parent=self.root)

    # def home(self):
    #     self.root.destroy()
    #     exec(open("HomePage.py").read())


# creating an instance of the class Tk()
# root = Tk()
# # creating an instance of the class Login()
# obj = Login(root)
# # Button(root, text="Quit", command=root.destroy).pack()
# root.mainloop()
