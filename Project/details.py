# Importing the required packages
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from numpy import roll
import mysql.connector
import webbrowser


class Details:

    def __init__(self, root, username) -> None:
        '''Shows a window with the profile details of the student'''
        # self.root = root
        self.username = username
        self.win = root
        # self.win = Toplevel(bg="#4152b3")
        self.win.title("Profile Details")
        self.win.geometry("960x600+130+60")
        self.win.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="resources/profile_details.jpg")
        self.bg_image = Label(self.win, image=self.bg).place(x=0, y=0, relheight=1,
                                                             relwidth=1)
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234567",
                database="proctor_it"
            )

            self.u_name = [self.username]
            mycursor = mydb.cursor()
            mycursor.execute(
                "SELECT * FROM register WHERE Username = %s", self.u_name)
            myresult = mycursor.fetchone()
            self.name = myresult[0]
            self.rollNo = str(myresult[1])
            self.email = myresult[2]
            self.username = myresult[3]
            self.password = myresult[4]
            self.branch = myresult[5]
            self.gradYear = str(myresult[6])

        except Exception as ep:
            messagebox.showwarning('error', ep, parent=self.root)

        # label to display name
        self.name_label = Label(self.win, text="Name: " + self.name, font=(
            "Arial", 22), bg="#f3f4ef", fg="black").place(x=100, y=40)

        # label to display rollNo
        self.rollNo_label = Label(self.win, text="Roll No: " + self.rollNo, font=(
            "Arial", 22), bg="#f3f4ef", fg="black").place(x=100, y=90)

        # label to display email
        self.email_label = Label(self.win, text="Email: " + self.email, font=(
            "Arial", 22), bg="#f3f4ef", fg="black").place(x=100, y=140)

        # label to display username
        self.username_label = Label(self.win, text="Username: " + self.username, font=(
            "Arial", 22), bg="#f3f4ef", fg="black").place(x=100, y=190)

        # label to display password
        self.password_label = Label(
            self.win, text="Password: " + "*******", font=("Arial", 22), bg="#f3f4ef", fg="black")
        self.password_label.place(x=100, y=250)

        # the button show password
        self.show_password_button = Button(self.win, text="👁", fg="#f3f4ef", bg="#4152b3", font=(
            "Arial", 14), command=self.show_password)
        self.show_password_button.place(x=450, y=250)

        # label to display branch
        self.branch_label = Label(self.win, text="Branch: " + self.branch, font=(
            "Arial", 22), bg="#f3f4ef", fg="black").place(x=100, y=300)

        # label to display graduation Year
        self.gradYear_label = Label(self.win, text="Graduation Year: " + self.gradYear, font=(
            "Arial", 22), bg="#f3f4ef", fg="black").place(x=100, y=350)

        # profile photo
        self.photo = Image.open(f"profile_pic\{self.username}.jpg")
        # antialias - converts high level image to low level image
        self.photo = self.photo.resize((190, 270), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(self.photo)
        self.fLabel = Label(self.win, image=self.photoimg1)
        self.fLabel.place(x=700, y=50, height=270, width=190)
    
    def see_profile(self):
        '''Extracts the profile details of the student from the database'''

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234567",
                database="proctor_it"
            )

            mycursor = mydb.cursor()
            mycursor.execute(
                "SELECT * FROM register WHERE Username = %s", self.u_name)
            myresult = mycursor.fetchone()
            self.name = myresult[0]
            self.rollNo = str(myresult[1])
            self.email = myresult[2]
            self.username = myresult[3]
            self.password = myresult[4]
            self.branch = myresult[5]
            self.gradYear = str(myresult[6])

            self.details_page()

        except Exception as ep:
            messagebox.showwarning('error', ep, parent=self.root)

    

    def show_password(self):
        '''Shows the password of the student'''
        self.passw = "Password: " + self.password
        # print(self.passw)
        self.password_label.config(text=self.passw)

# root = Tk()
# obj = Details(root, "admin123")
# Button(root, text="Quit", command=root.destroy).pack()
# root.mainloop()