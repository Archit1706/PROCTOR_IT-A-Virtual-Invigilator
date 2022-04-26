# Importing the required packages
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from numpy import roll
import mysql.connector
import webbrowser


class Doubts:
    
    def __init__(self, root, username) -> None:
        '''Shows the doubts page for the student'''
        # self.root = root
        self.username = username
        self.win4 = root
        self.win4.title("Doubts/Help")
        self.win4.geometry("640x400+350+120")
        self.win4.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="resources/doubts.jpg")
        self.bg_image = Label(self.win4, image=self.bg).place(x=0, y=0, relheight=1,
                                                              relwidth=1)
        self.win4.wm_attributes('-transparentcolor', '#4152b3')

        self.subject_label = Label(self.win4, text="Subject", font=(
            "Arial", 16, "bold"), fg="black").place(x=50, y=40)

        self.subject_entry = Entry(self.win4, font=("Arial", 14), fg="black")
        self.subject_entry.focus()
        self.subject_entry.place(x=50, y=80, height=30, width=400)

        self.message_label = Label(self.win4, text="Message", font=(
            "Arial", 16, "bold"), fg="black").place(x=200, y=140)

        self.message_entry = Text(self.win4, font=("Arial", 14), fg="black")
        self.message_entry.place(x=200, y=180, height=150, width=360)

        self.send_button = Button(self.win4, text="Send", bg="white", fg="black", font=(
            "Arial", 14), command=self.send_doubts).place(x=560, y=360)
        # return self.win4

    def send_doubts(self):
        '''Sends the doubts to the admin/database'''
        self.subject = self.subject_entry.get()
        self.message = self.message_entry.get("1.0", END)

        if self.subject == "" or self.message == "":
            messagebox.showwarning(
                'error', "Please fill all the fields", parent=self.win4)

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
                    f"INSERT INTO doubts (Username, Subject, Message) VALUES ('{self.username}','{self.subject}', '{self.message}')")
                mydb.commit()
                messagebox.showinfo(
                    'Success', 'Your message has been sent to the admin', parent=self.win4)
                self.win4.destroy()
            except Exception as ep:
                messagebox.showerror('error', ep, parent=self.win4)


# root = Tk()
# obj = Doubts(root, "admin123")
# Button(root, text="Quit", command=root.destroy).pack()
# root.mainloop()
