# Importing the required packages
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from numpy import roll
import mysql.connector
import webbrowser

class About:

    def __init__(self, root) -> None:
        '''Shows the about us page and link to download project source code'''

        self.gitProject = "https://github.com/Archit1706/PROCTOR-IT-A-Virtual-Invigilator"
        self.win5 = root
        self.win5.title("About Us")
        self.win5.geometry("640x400+350+100")
        self.win5.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="resources/about_us.jpg")
        self.bg_image = Label(self.win5, image=self.bg).place(x=0, y=0, relheight=1,
                                                              relwidth=1)
        self.download = Button(self.win5, text="Download", bg="#4152b3", fg="white", font=(
            "Arial", 10), command=self.download_code).place(x=270, y=345, width=100)


    def download_code(self):
        '''Opens GitHub in web browser to download the project source code'''
        webbrowser.open_new(self.gitProject)
        self.win5.destroy()


# root = Tk()
# obj = About(root)
# Button(root, text="Quit", command=root.destroy).pack()
# root.mainloop()
