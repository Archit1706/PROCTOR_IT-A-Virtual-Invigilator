# Importing the required packages
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import numpy
import mysql.connector
import webbrowser
import about
import details
import doubts
from ExamOptions import *
# from Login import Login


# creating a class HomePage


class HomePage:

    # taking root or instance of Tk() as an input creating a home Page
    def __init__(self, root, username) -> None:

        self.username = username
        self.root = root
        self.root.title("Home Page")
        self.root.wm_attributes("-fullscreen", True)
        self.root.resizable(False, False)

        # creating a frame on the self.window
        self.frame = Frame(self.root, width=1280, height=725)
        self.frame.place(x=0, y=0)

        # Create an object of tkinter ImageTk for background image
        # self.img = ImageTk.PhotoImage(Image.open(file="resources/homeBack2.jpg"))
        self.img = ImageTk.PhotoImage(file="resources/homeBack2.jpg")

        # Create a Label Widget to display the Background Image
        self.label = Label(self.frame, image=self.img)
        self.label.place(x=0, y=0, relwidth=1, relheight=1)

        # Adding the required widgets of the home page
        self.homePage_contents()

    def homePage_contents(self):
        '''It adds the required widgets to the home page'''

        # Adding a welcome label on the navigation bar as per the user who logged in
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234567",
                database="proctor_it"
            )
            # print(self.username)
            self.u_name = [self.username]
            mycursor = mydb.cursor()
            query = "SELECT Name FROM register WHERE Username = %s"
            mycursor.execute(query, self.u_name)
            myresult = mycursor.fetchone()
            self.name = myresult[0]
            # print(self.name)

        except Exception as ep:
            messagebox.showerror('error', ep, parent=self.root)
        # self.name = "Archit Rathod"
        self.welcome_message = "Welcome " + self.name + "!"
        self.welcome = Label(self.frame, text=self.welcome_message, font=(
            "Arial", 20, "bold"), bg="white", fg="black").place(x=480, y=5)

        # Adding a button1 = see_profile to the self.window
        self.see_profile_button = Button(self.frame, text="See Details", bg="white", fg="black", font=(
            "Arial", 20, "bold"), command=self.see_profile).place(x=180, y=250)

        # Adding a button2 = check_marks to the self.window
        self.check_marks_button = Button(self.frame, text="Check Marks", bg="white",
                                         fg="black", font=("Arial", 20, "bold"), command=self.check_marks).place(x=540, y=250)

        # Adding a button3 = give_test to the self.window
        self.give_test_button = Button(self.frame, text="Give Test", bg="white",
                                       fg="black", font=("Arial", 20, "bold"), command=self.give_test).place(x=940, y=250)

        # Adding a button4 = doubts to the self.window
        self.doubts_button = Button(self.frame, text="Doubts/Help", bg="white",
                                    fg="black", font=("Arial", 20, "bold"), command=self.doubts).place(x=180, y=600)

        # Adding a button5 = about_us to the self.window
        self.about_us_button = Button(self.frame, text="About Us", bg="white", fg="black", font=(
            "Arial", 20, "bold"), command=self.about_us).place(x=570, y=600)

        # Adding a button6 = logout to the self.window
        self.logout_button = Button(self.frame, text="Logout", bg="white", fg="black", font=(
            "Arial", 20, "bold"), command=self.logout).place(x=940, y=600)

        # self.frame.mainloop()

    # ------------------------ Adding functionalities to the home page -----------------------

    # -------------------------------- profile details --------------------------------

    def see_profile(self):

        self.win = Toplevel(self.root)
        details.Details(self.win, self.username)

    # ---------------------------Show marks -----------------------------------

    def check_marks(self):
        '''Shows the marks of the student as a table'''

        pass

    # --------------------------------- Give Test ------------------------------------

    def give_test(self):
        '''Shows the instruction page for the student'''

        # self.win3 = Toplevel(self.root)
        # self.win3.title("Rules")
        # self.win3.geometry("960x600+130+60")
        # self.win3.resizable(False, False)
        # self.bg = ImageTk.PhotoImage(file="resources/instructions.jpg")
        # self.bg_image = Label(self.win, image=self.bg).place(x=0, y=0, relheight=1,
        #                                                      relwidth=1)

        # self.tnc = Checkbutton(self.win3, text="I agree to the terms and conditions", font=("Arial", 14), bg="white", fg="black", variable=self.tnc_var)
        # self.tnc.place(x=50, y=550)

        # exec(open("quiz.py").read())
        self.win = Toplevel(self.root)
        ChooseExam(self.win, self.username)

    # ----------------------------------- Doubts and FeedBack -------------------------

    def doubts(self):

        self.win = Toplevel(self.root)
        doubts.Doubts(self.win, self.username)

    # --------------------------------------About Us page ------------------------------

    def about_us(self):
        self.win = Toplevel(self.root)
        about.About(self.win)

    # ------------------------------ Logout ------------------------------------------

    def logout(self):
        '''Logs out the student and returns to the login page'''
        answer = messagebox.askquestion(
            "Logout", "Are you sure you want to logout?")
        if answer == "yes":
            # self.root.destroy()
            self.root.destroy()
            exec(open("Project\Login.py").read())
            # win = Tk()
            # Login(win)


# root = Tk()
# obj = HomePage(root, "admin123")
# Button(root, text="Quit", command=root.destroy).pack()
# root.mainloop()
