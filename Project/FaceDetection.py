from tkinter import *
from tkinter import messagebox
import json
import cv2
import PIL.Image
import PIL.ImageTk
import time
import mysql.connector
# from ExamOptions import FaceRecognition


class FaceRecognition:

    def __init__(self, username) -> None:
        self.username = username

    def face_recognition(self):
        self.n = "Admin Admin"
        self.r = "0"

        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            # Converting the test image to gray-scale
            gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # detecting features in gray-scale image, returns coordinates, width and height of features
            features = classifier.detectMultiScale(
                gray_img, scaleFactor, minNeighbors)
            coords = []
            # drawing rectangle around the feature and labeling it
            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # cv2.putText(img, text, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 3)

                id, predict = clf.predict(gray_img[y:y + h, x:x + w])

                confidence = int(100 * (1 - (predict / 300)))

            try:

                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="1234567",
                    database="proctor_it"
                )
                # mycursor = mydb.cursor()
                # query = "SELECT name FROM register WHERE username = %s"
                # val = (self.username)
                # mycursor.execute(query, val)
                # self.n = mycursor.fetchone()
                # self.n = "+".join(self.n)

                # query = "SELECT RollNo FROM register WHERE username = %s"
                # val = (self.username)
                # mycursor.execute(query, val)
                # self.r = mycursor.fetchone()
                # self.r = "+".join(self.r)

                mycursor = mydb.cursor()
                query = "SELECT Name, RollNo FROM register WHERE username = %s"
                val = (self.username)
                mycursor.execute(query, val)
                result = mycursor.fetchone()
                self.n = result[0]
                self.r = result[1]
                self.n = "+".join(self.n)

                # for x in myresult:
                #     self.name = x[0]
                #     self.roll = x[1]

                # print(name)
                # print(roll)
                # cv2.putText(img, name, (x, y - 4), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 3)
                # cv2.putText(img, roll, (x, y + h + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 3)
                # cv2.putText(img, str(confidence), (dx, y + h + 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 3)
                # mydb.close()

            except Exception as e:
                # messagebox.showerror('error', e, parent=self.win6)
                print(e)

                if confidence > 80:
                    cv2.putText(
                        img, f"Name: {self.n}", (x, y - 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                    cv2.putText(
                        img, f"Roll No: {self.r}", (x, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 3)
                else:
                    cv2.rectangle(
                        img, (x, y), (x + w, y + h), (0, 0, 255), 3)
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


# x = FaceRecognition("admin123")
# x.face_recognition()
# x = FaceRecognition("fsdaf")
# x.face_recognition()


# x = FaceRecognition("sanddd")
# x.face_recognition()
