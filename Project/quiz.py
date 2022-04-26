from re import L
from tkinter import *
from tkinter import messagebox
import json
import cv2
import PIL.Image
import PIL.ImageTk
import time
import mysql.connector
# from ExamOptions import FaceRecognition


class Quiz:

    def __init__(self, root, username, subject):

        self.root = root
        self.username = username
        self.subject = subject
        if self.subject == "Operating System":
            self.subject = "OS"
        # self.root.geometry("800x450")
        self.root.title("Quiz")
        self.root.wm_attributes("-fullscreen", "true")

        
        with open(f'data\{self.subject}.json') as f:
            self.data = json.load(f)

        self.question = (self.data['question'])
        self.options = (self.data['options'])
        self.answer = (self.data['answer'])

        self.q_no = 0

        self.display_title()
        self.display_question()

        self.opt_selected = IntVar()
        self.opts = self.radio_buttons()

        self.display_options()
        self.buttons()
        self.data_size = len(self.question)
        self.correct_ans = 0

    def display_result(self):

        self.wrong_count = self.data_size - self.correct_ans
        self.correct = f"Correct: {self.correct_ans}"
        self.wrong = f"Wrong: {self.wrong_count}"

        self.score = int(self.correct_ans / self.data_size * 100)
        self.result = f"Score: {self.score}%"

        messagebox.showinfo("Result", f"{self.result}\n{self.correct}\n{self.wrong}")


    def check_ans(self, q_no):
        self.q_no = q_no
        if self.opt_selected.get() == self.answer[self.q_no]:
            return True

    def next_btn(self):

        if self.check_ans(self.q_no):
            self.correct_ans += 1

        self.q_no += 1

        if self.q_no == self.data_size - 1:
            self.next_btn['text'] = 'Submit'

        if self.q_no == self.data_size:

            self.display_result()
            self.update_database()
            self.root.destroy()
        else:
            self.display_question()
            self.display_options()
    
    def update_database(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="1234567",
                database="proctor_it"
            )
            mycursor = mydb.cursor()
            query = "INSERT INTO marks VALUES (%s, %s, %s, %s, %s, %s, %s)"
            currDate = time.strftime("%d/%m/%Y")
            currTime = time.strftime("%H:%M:%S")
            currDate_Time = currDate + " " + currTime
            val = (self.username, self.subject, self.data_size, self.correct_ans, self.wrong_count, self.score, currDate_Time)
            mycursor.execute(query, val)
            mydb.commit()
            
        except Exception as e:
            print(e)


    def buttons(self):
        self.next_button = Button(self.root, text="Next", command=self.next_btn,
                             width=10, bg="#4152b3", fg="white", font=("ariel", 20, "bold"))
        self.next_button.place(x=350, y=380)

        # quit_button = Button(self.root, text="Quit", command=self.root.destroy,
        #  width=5, bg="black", fg="white", font=("ariel", 16, " bold"))
        # quit_button.place(x=700, y=50)

    def display_options(self):
        val = 0
        self.opt_selected.set(0)
        for option in self.options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    def display_question(self):
        Label(self.root, text=self.question[self.q_no], width=60,
              font=('Arial', 22, 'bold'), anchor='w').place(x=70, y=100)

    def display_title(self):
        title = Label(self.root, text="QUIZ",
                      width=80, bg="#4152b3", fg="white", font=("ariel", 20, "bold"))
        title.place(x=0, y=2)

    def radio_buttons(self):
        q_list = []
        y_pos = 150

        while len(q_list) < 4:
            radio_btn = Radiobutton(self.root, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14))
            q_list.append(radio_btn)
            radio_btn.place(x=100, y=y_pos)
            y_pos += 40

        return q_list


class FaceRecognition(Quiz):

    def face_recognition(self):

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_img, scaleFactor, minNeighbors)
            coords = []
            # drawing rectangle around the feature and labeling it
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                
                id, predict = clf.predict(gray_img[y:y + h, x:x + w])
                confidence = int(100 * (1 - (predict / 300)))

            try:

                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234567",
                    database="proctor_it"
                )
                mycursor = mydb.cursor()
                query = "SELECT * FROM register WHERE username = %s"
                val = (self.username)
                mycursor.execute(query, val)
                myresult = mycursor.fetchone()
                for x in myresult:
                    name = x[0]
                    roll = x[1]

                mydb.close()
               
            except Exception as e:
                messagebox.showerror('error', e, parent=self.root)

                if confidence > 80:
                    cv2.putText(
                        img, f"Name: {name}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Roll No: {roll}", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(
                        img(x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(
                        img, "Unknown Face", (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3)

                coords = [x, y, w, h]

            return coords

        def detect(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1,
                                  10, (0, 255, 0), "Face", clf)
            return img

        faceCascade = cv2.CascadeClassifier(
            "resources/haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, frame = video_cap.read()
            img = detect(frame, clf, faceCascade)
            cv2.imshow("Face Recognition", img)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_cap.release()
        cv2.destroyAllWindows()

# root = Tk()
# subject = "Operating System"
# username = "admin123"
# obj = Quiz(root, username, subject)
# root.mainloop()
