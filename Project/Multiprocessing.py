from multiprocessing import Process
from FaceDetection import FaceRecognition
from quiz import Quiz
from tkinter import *


def quiz_process(root, username, subject):
    # window = Tk()
    # Quiz(window, "admin123", "Operating System")
    # exec(open("Project/quiz.py").read())
    root = Tk()
    subject = "Operating System"
    username = "admin123"
    obj = Quiz(root, username, subject)
    root.mainloop()


def proctor_process(username):
    x = FaceRecognition("admin123")
    x.face_recognition()


# if __name__ == '__main__':

def run_both():

    my_process1 = Process(target=quiz_process, args=(
        "root", "username", "subject",))
    my_process2 = Process(target=proctor_process, args=('username',))
    my_process1.start()
    my_process2.start()

    # as of now the exam wil terminate as soon as there is no face in the screen
    while True:
        if not my_process2.is_alive():
            my_process1.terminate()
            my_process2.terminate()
            break
    # my_process1.join()
    # my_process2.join()
