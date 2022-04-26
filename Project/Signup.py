# importing the required modules
from this import d
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
# import tkinter.font
import cv2
import numpy as np
import re
import os
import time
from Login import Login


# creating a class Signup
class Signup:

    # taking root or instance of Tk() as an input creating a signup page
    def __init__(self, root):
        # creating a window
        self.roll_var = StringVar()
        self.root = root
        self.root.title("Signup")
        self.root.geometry("1000x600+150+20")
        self.root.wm_attributes("-fullscreen", True)
        self.root.resizable(False, False)
        self.bg = ImageTk.PhotoImage(file="resources/Signup.png")
        self.bg_image = Label(self.root, image=self.bg).place(x=0, y=0, relheight=1,
                                                              relwidth=1)
        self.signup_contents()

    def signup_contents(self):
        '''Function to add all the required widgets to the signup page'''

        # creating a signup frame
        self.Frame_Signup = Frame(self.root, bg="white")
        self.Frame_Signup.place(x=560, y=30, height=700, width=700)
        #  Giving a title to the signup page
        self.title = Label(self.Frame_Signup, text="Student Signup", font=(
            "Arial", 40, "bold"), fg="#4152b3", bg="white").place(x=150, y=30)

        self.name_var = StringVar()
        self.username_var = StringVar()
        self.passw_var = StringVar()
        self.cpass_var = StringVar()
        self.email_var = StringVar()
        self.branch_var = StringVar()
        self.gradYear_var = StringVar()

        # first name
        # label for name
        self.name_label = Label(self.Frame_Signup, text="Name", font=("Arial", 14, "bold"), fg="#4152b3", bg="white").place(
            x=80, y=150)
        # entry for name
        self.name_input = Entry(self.Frame_Signup, bg="#f5f5f5", font=(
            "Arial", 12), textvariable=self.name_var)
        self.name_input.place(x=80, y=180)
        self.name_input.focus()

        # last name
        # label for user name
        self.username_label = Label(self.Frame_Signup, text="User Name", font=("Arial", 14, "bold"), fg="#4152b3",
                                    bg="white").place(x=400, y=150)
        # entry for user name
        self.username_input = Entry(self.Frame_Signup, bg="#f5f5f5", font=(
            "Arial", 12), textvariable=self.username_var)
        self.username_input.place(x=400, y=180)

        # ROLL_NO
        # label for roll no
        self.roll_no_label = Label(self.Frame_Signup, text="Roll No", font=("Arial", 14, "bold"), fg="#4152b3",
                                   bg="white").place(x=80, y=220)
        # entry for roll no
        self.roll_no_input = Entry(self.Frame_Signup, bg="#f5f5f5", font=(
            "Arial", 12), textvariable=self.roll_var)
        self.roll_no_input.place(x=80, y=250)

        # EMAIL
        # label for email
        self.email_label = Label(self.Frame_Signup, text="Email", font=("Arial", 14, "bold"), fg="#4152b3",
                                 bg="white").place(x=400, y=220)
        # entry for email
        self.email_input = Entry(self.Frame_Signup, bg="#f5f5f5", font=(
            "Arial", 12), textvariable=self.email_var)
        self.email_input.place(x=400, y=250)

        # BRANCH
        # label for branch
        self.branch_label = Label(self.Frame_Signup, text="Branch", font=("Arial", 14, "bold"), fg="#4152b3",
                                  bg="white").place(x=80, y=290)
        # optionmenu for branch
        self.options = ["AI&DS",
                        "Computer Science",
                        "IT",
                        "EXTC",
                        "BIOMEDICAL"]
        # initial menu text
        self.branch_var.set("Branch")
        # Create Dropdown menu
        self.branch_om = OptionMenu(
            self.Frame_Signup, self.branch_var, *self.options)
        self.branch_om.config(bg="#f5f5f5", font=("Arial", 10), width=20)
        self.branch_om.pack()
        self.branch_om.place(x=80, y=320)

        # graduation Year
        # label for gradYear
        self.gradYear_label = Label(self.Frame_Signup, text="Graduation Year", font=("Arial", 14, "bold"), fg="#4152b3",
                                    bg="white").place(x=400, y=290)
        # entry for email
        self.gradYear_input = Entry(self.Frame_Signup, bg="#f5f5f5", font=(
            "Arial", 12), textvariable=self.gradYear_var)
        self.gradYear_input.place(x=400, y=320)

        # Password
        # label for password
        self.password_label = Label(self.Frame_Signup, text="Password", font=("Arial", 14, "bold"), fg="#4152b3", bg="white").place(
            x=80, y=370)
        # entry for password
        self.password_input = Entry(self.Frame_Signup, bg="#f5f5f5", font=(
            "Arial", 12), textvariable=self.passw_var, show="*")
        self.password_input.place(x=80, y=400)

        # Confirm Password
        # label for confirm password
        self.confirm_password_label = Label(self.Frame_Signup, text="Confirm Password", font=("Arial", 14, "bold"), fg="#4152b3",
                                            bg="white").place(x=400, y=370)
        # entry for confirm password
        self.confirm_password_input = Entry(self.Frame_Signup, bg="#f5f5f5", font=(
            "Arial", 12), textvariable=self.cpass_var, show="*")
        self.confirm_password_input.place(x=400, y=400)

        # check button for terms and conditions
        self.tnc_var = IntVar()
        self.tnc_check_button = Checkbutton(self.Frame_Signup, text="Terms & Conditions", variable=self.tnc_var,
                                            onvalue=1, offvalue=0, height=1,
                                            width=14, bg="white")
        self.tnc_check_button.pack()
        self.tnc_check_button.place(x=270, y=450)

        # Signup Button
        self.signup_button = Button(self.Frame_Signup, text="Create an account", font=("Arial", 25, "bold"), bg="#4152b3", fg="white",
                                    highlightthickness=0, height=1, width=15, command=self.check).place(
            x=180, y=510)

        # For registered students
        self.have_account = Label(self.Frame_Signup, text="Already have an account", font=(
            "Arial", 10), fg="#4152b3", bg="white").place(x=220, y=600)
        self.login_button = Button(self.Frame_Signup, text="Login", font=("Arial", 10, "underline"), bg="white", fg="#4152b3",
                                   height=1, width=8, command=self.login,
                                   highlightthickness=0, bd=0).place(x=370, y=600)

    def check(self):
        self.name = self.name_var.get()
        self.username = self.username_var.get()
        self.password = self.passw_var.get()
        self.confpass = self.cpass_var.get()
        self.roll_no = self.roll_var.get()
        self.email = self.email_var.get()
        self.branch = self.branch_var.get()
        self.gradYear = self.gradYear_var.get()
        self.tnc = self.tnc_var.get()

        self.regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

        if self.name == "" or self.username == "" or self.password == "" or self.confpass == "" or self.roll_no == "" or self.email == "" or self.branch == "" or self.gradYear == "":
            msg = 'No Empty blanks allowed!'
            messagebox.showwarning('message', msg, parent=self.root)

        # elif not(any(ch.isdigit() for ch in self.username)) or not(any(ch.isalpha() for ch in self.username)):
        #     msg = 'Username should be Alpha-Numeric\n Eg. admin123'
        #     messagebox.showwarning('message', msg, parent=self.root)

        elif len(self.username) <= 4:
            msg = 'Username is too short. Username should be 5 to 15 characters long'
            messagebox.showwarning('message', msg, parent=self.root)

        # if username is very long
        elif len(self.username) > 16:
            msg = 'Username is too long. Username should be 5 to 15 characters long'
            messagebox.showwarning('message', msg, parent=self.root)

        elif self.confpass != self.password:
            msg = 'Confirmed Password does not match the Password'
            messagebox.showwarning('message', msg, parent=self.root)

        elif any(ch.isalpha() for ch in self.roll_no):
            msg = 'Roll no should be in Numeric Format'
            messagebox.showwarning('message', msg, parent=self.root)

        elif (re.fullmatch(self.regex, self.email) == None):
            msg = 'Email should be in proper format \n Eg. admin123@gmail.com'
            messagebox.showwarning('message', msg, parent=self.root)

        elif self.branch == "Branch":
            msg = 'Please select a branch'
            messagebox.showwarning('message', msg, parent=self.root)

        elif any(ch.isalpha() for ch in self.gradYear):
            msg = 'Graduation Year should be in Numeric Format\n Eg. 2022'
            messagebox.showwarning('message', msg, parent=self.root)

        elif len(self.gradYear) != 4:
            msg = 'Graduation Year should be 4 digits'
            messagebox.showwarning('message', msg, parent=self.root)

        elif self.tnc_var.get() == 0:
            msg = 'Please accept the terms and conditions'
            messagebox.showwarning('message', msg, parent=self.root)

        else:
            self.update_database()
            pass

    def update_database(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234567",
                database="proctor_it"
            )
            mycursor = mydb.cursor()
            # query1 = ("SELECT * FROM register WHERE username = %s")
            # value = [self.username]
            # mycursor.execute(query1, value)
            # row = mycursor.fetchone()
            # if row != None:
            #     messagebox.showwarning('message', 'Username already exists', parent=self.root)
            # else:
            query1 = "INSERT INTO register VALUES (%s, %s, %s, %s, %s, %s, %s)"
            query2 = "INSERT INTO login VALUES (%s, %s)"
            mycursor.execute(query1, (self.name, self.roll_no, self.email,
                                     self.username, self.password, self.branch, self.gradYear))
            mycursor.execute(query2, (self.username, self.password))
            mydb.commit()
            mydb.close()
            msg = 'Student Account Created Successfully'
            messagebox.showinfo('message', msg, parent=self.root)
            messagebox.showinfo(
                'message', 'Now we will collect face samples', parent=self.root)
            # self.root.destroy()
            time.sleep(1)
            self.generate_dataset()
            # exec(open("Project/PhotoSample.py").read())
            time.sleep(1)
            self.train_classifier()
            self.root.quit()
            win = Tk()
            Login(win)
            # exec(open("Project\Login.py").read())

        # if error occurs in the database connection then show the error message
        except Exception as ep:
            messagebox.showwarning('error', ep, parent=self.root)
            self.name_input.delete(0, END)
            self.username_input.delete(0, END)
            self.password_input.delete(0, END)
            self.confirm_password_input.delete(0, END)
            self.email_input.delete(0, END)
            self.roll_no_input.delete(0, END)
            self.branch_var.set("Branch")
            self.gradYear_input.delete(0, END)

    def generate_dataset(self):
        self.face_classifier = cv2.CascadeClassifier(
            "resources/haarcascade_frontalface_default.xml")

        os.mkdir(f"students/{self.username}")

        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234567",
                database="proctor_it"
            )
            mycursor = mydb.cursor()
            query = "SELECT COUNT(name) FROM register; "
            mycursor.execute(query)
            row = mycursor.fetchone()
            self.count = row[0]
            mydb.close()
        except Exception as ep:
            messagebox.showwarning('error', ep, parent=self.root)

        cap = cv2.VideoCapture(0)
        img_id = 0
        while True:
            ret, imgFrame = cap.read()
            if self.face_cropped(imgFrame) is not None:
                img_id += 1

                face = cv2.resize(self.face_cropped(imgFrame), (500, 500))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

                cv2.imwrite(f"students/{self.username}/user." + str(self.count + 1) + "." +
                            str(img_id) + ".jpg", face)
                cv2.putText(img=face, org=(50, 50), text=str(
                    img_id), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=2, color=(0, 255, 255), thickness=2)
                cv2.imshow("Cropped Face", face)

            if cv2.waitKey(1) == 27 or int(img_id) == 30:
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Success", "Images Captured Successfully")

    def face_cropped(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_classifier.detectMultiScale(gray, 1.3, 5)
        # here scaling factor = 1.3 and minNeighbors = 5
        if faces is ():
            return None
        for (x, y, w, h) in faces:
            cropped_face = img[y:y+h, x:x+w]
        return cropped_face

    def login(self):
        self.root.destroy()
        # exec(open("Project\Login.py").read())
        win = Tk()
        Login(win)

    def train_classifier(self):
        data_dir = ("students/" + self.username)
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert("L")
            img_numpy = np.array(img, "uint8")
            id = int(os.path.split(image)[1].split(".")[1])
            faces.append(img_numpy)
            ids.append(id)
            cv2.imshow("Training", img_numpy)
            cv2.waitKey(1) == 13

        ids = np.array(ids)

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Success", "Classifier Trained Successfully")


        # recognizer = cv2.face.LBPHFaceRecognizer_create()
        # detector = cv2.CascadeClassifier("resources/haarcascade_frontalface_default.xml")
        # def getImagesAndLabels(path):
        #     imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
        #     faceSamples = []
        #     ids = []
        #     for imagePath in imagePaths:
        #         PIL_img = Image.open(imagePath).convert('L')
        #         img_numpy = np.array(PIL_img, 'uint8')
        #         id = int(os.path.split(imagePath)[-1].split(".")[1])
        #         faces = detector.detectMultiScale(img_numpy)
        #         for (x, y, w, h) in faces:
        #             faceSamples.append(img_numpy[y:y+h, x:x+w])
        #             ids.append(id)
        #     return faceSamples, ids
root = Tk()
obj = Signup(root)
# Button(root, text="Quit", command=root.destroy).pack()
root.mainloop()
