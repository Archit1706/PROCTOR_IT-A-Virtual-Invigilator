# Importing the required packages
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from numpy import roll
import mysql.connector
import cv2
# from quiz import *
import Multiprocessing


class ChooseExam:

    def __init__(self, root, username) -> None:
        '''Shows a page where student can choose the exam subject'''
        # self.root = root
        self.username = username
        self.win5 = root
        self.win5.title("Doubts/Help")
        self.win5.geometry("960x600+150+20")
        self.win5.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="resources/instructions.jpg")
        self.bg_image = Label(self.win5, image=self.bg).place(x=0, y=0, relheight=1,
                                                              relwidth=1)
        # self.win5.wm_attributes('-transparentcolor', '#4152b3')

        self.exam_widgets()

    def exam_widgets(self):
        '''Adds the widgets to the page'''

        self.tnc_var = IntVar()
        self.paper_var = StringVar()

        # check button for terms and conditions
        self.tnc_check_button = Checkbutton(self.win5, text="Have you read the instructions properly", variable=self.tnc_var,
                                            onvalue=1, offvalue=0, height=1,
                                            width=32, font=("Arial", 14))
        self.tnc_check_button.pack()
        self.tnc_check_button.place(x=250, y=550)

        # paper
        # label for paper
        self.paper_label = Label(self.win5, text="Subject", font=("Arial", 14, "bold"), fg="#4152b3",
                                 bg="white").place(x=80, y=290)
        # optionmenu for paper
        self.options = ["Operating System",
                        "Computer Networks",
                        "Computer Architecture",
                        "Data Structures",
                        "Database Management System"]
        # initial menu text
        self.paper_var.set("Choose a subject")
        # Create Dropdown menu
        self.paper_om = OptionMenu(
            self.win5, self.paper_var, *self.options)
        self.paper_om.config(bg="#f5f5f5", font=("Arial", 10), width=20)
        self.paper_om.pack()
        self.paper_om.place(x=710, y=490)
        self.paper_om.config(width=25)

        self.start_test_button = Button(self.win5, text="Start Exam", bg="#4152b3",
                                        fg="white", font=("Arial", 20, "bold"), command=self.start_test).place(x=730, y=530)

    def start_test(self):
        self.subject = self.paper_var.get()
        self.tnc = self.tnc_var.get()
        if self.tnc == 0:
            messagebox.showwarning(
                'error', "Please read the instructions properly", parent=self.win5)
        elif self.subject == "Choose a subject":
            messagebox.showwarning(
                'error', "Please choose a subject", parent=self.win5)
        else:
            self.win5.destroy()
            # self.win6 = Tk()
            # Quiz(self.win6, self.username, self.subject)
            # x = FaceRecognition(self.username)
            # x.face_recognition()
            # exec(open("Project/Multiprocessing.py").read())
            Multiprocessing.run_both()


            # self.exam_widgets()


# root = Tk()
# obj = ChooseExam(root, "admin123")
# Button(root, text="Quit", command=root.destroy).pack()
# root.mainloop()
