from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import cv2
import numpy as np


# Load predefined data

face_classifier = cv2.CascadeClassifier(
    "resources/haarcascade_frontalface_default.xml")


def face_cropped(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    # here scaling factor = 1.3 and minNeighbors = 5
    if faces is ():
        return None
    for (x, y, w, h) in faces:
        cropped_face = img[y:y+h, x:x+w]
    return cropped_face


name = "Archit_Rathod"
cap = cv2.VideoCapture(0)
img_id = 0
while True:
    ret, imgFrame = cap.read()
    if face_cropped(imgFrame) is not None:
        img_id += 1

        face = cv2.resize(face_cropped(imgFrame), (500, 500))
        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f"students/{name}/user." + str(img_id) + ".jpg", face)
        cv2.putText(img=face, org=(50, 50), text=str(
            img_id), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=2, color=(0, 255, 255), thickness=2)
        cv2.imshow("Cropped Face", face)

    if cv2.waitKey(1) == 27 or int(img_id) == 30:
        break

cap.release()
cv2.destroyAllWindows()
messagebox.showinfo("Success", "Images Captured Successfully")


# class PhotoSample:

#     def __init__(self, username):
#         self.face_classifier = cv2.CascadeClassifier(
#             "resources/haarcascade_frontalface_default.xml")
#         self.username = username

#     def face_cropped(img):
#         gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#         faces = self.face_classifier.detectMultiScale(gray, 1.3, 5)
#         # here scaling factor = 1.3 and minNeighbors = 5
#         if faces is ():
#             return None
#         for (x, y, w, h) in faces:
#             cropped_face = img[y:y+h, x:x+w]
#         return cropped_face

#     def run(self):
#         self.name = "Archit_Rathod"
#         cap = cv2.VideoCapture(0)
#         self.img_id = 0
#         while True:
#             ret, imgFrame = cap.read()
#             if self.face_cropped(imgFrame) is not None:
#                 self.img_id += 1
#                 face = cv2.resize(self.face_cropped(imgFrame), (500, 500))
#                 face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
#                 cv2.imwrite(f"students/{self.name}/user." +
#                             str(self.img_id) + ".jpg", face)
#                 cv2.putText(img=face, org=(50, 50), text=str(
#                     self.img_id), fontFace=cv2.FONT_HERSHEY_COMPLEX, fontScale=2, color=(0, 255, 255), thickness=2)
#                 cv2.imshow("Cropped Face", face)
#             if cv2.waitKey(1) == 27 or int(self.img_id) == 30:
#                 break
#         cap.release()
#         cv2.destroyAllWindows()
#         messagebox.showinfo("Success", "Images Captured Successfully")


# ps = PhotoSample("Archit_Rathod")
# ps.run()
