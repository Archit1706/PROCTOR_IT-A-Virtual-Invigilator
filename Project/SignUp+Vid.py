from inspect import Attribute
from tkinter import *
from tkinter import messagebox
import cv2
import PIL.Image
import PIL.ImageTk
import time
import json


class App:


    def __init__(self, root, video_source=0):
        self.root = root
        self.root.title("Exam")
        self.root.resizable(width=False, height=False)
        self.root.wm_attributes("-fullscreen", True)
        self.video_source = video_source
        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)
        # Create a canvas that can fit the above video source size
        self.canvas = Canvas(
            self.root, width=self.vid.width, height=self.vid.height)
        self.canvas.place(x=650, y=20)
        # Button that lets the user take a snapshot
        # self.btn_snapshot = Button(
        #     root, text="Snapshot", width=50, command=self.snapshot)
        # self.btn_snapshot.pack(anchor=CENTER, expand=True)
        # After it is called once, the update method will be automatically called every laymilliseconds
        self.delay = 15
        self.update()
        with open('data/OS.json') as f:
            self.data = json.load(f)

        self.question = (self.data['question'])
        self.options = (self.data['options'])
        self.answer = (self.data['answer'])

        # set self.question number to 0
        self.q_no = 0
        # assigns ques to the display_self.question function to update later.
        self.display_title()
        self.display_question()
        # opt_selected holds an integer value which is used for
        # selected option in a self.question.
        self.opt_selected = IntVar()
        # displaying radio button for the current self.question and used to
        # display self.options for the current self.question
        self.opts = self.radio_buttons()
        # display self.options for the current self.question
        self.display_options()
        # displays the button for next and exit.
        self.buttons()
        # no of self.questions
        self.data_size = len(self.question)
        # keep a counter of self.correct answers
        self.correct = 0

    # This method is used to display the result
    # It counts the number of self.correct and wrong answers
    # and then display them at the end as a message Box
    def display_result(self):

        # calculates the wrong count
        self.wrong_count = self.data_size - self.correct
        self.correct = f"Correct: {self.self.correct}"
        self.wrong = f"Wrong: {self.wrong_count}"

        # calcultaes the percentage of self.correct answers
        self.score = int(self.correct / self.data_size * 100)
        self.result = f"Score: {self.score}%"

        # Shows a message box to display the result
        messagebox.showinfo("Result", f"{self.result}\n{self.correct}\n{self.wrong}")

        self.root.mainloop()


    # This method checks the Answer after we click on Next.
    def check_ans(self, q_no):

        # checks for if the selected option is self.correct
        if self.opt_selected.get() == self.answer[self.q_no]:
            # if the option is self.correct it return true
            return True

    # This method is used to check the self.answer of the
    # current self.question by calling the check_ans and self.question no.
    # if the self.question is self.correct it increases the count by 1
    # and then increase the self.question number by 1. If it is last
    # self.question then it calls display result to show the message box.
    # otherwise shows next self.question.
    def next_btn(self):

        # Check if the self.answer is self.correct
        if self.check_ans(self.q_no):
            # if the self.answer is self.correct it increments the self.correct by 1
            self.correct += 1

        # Moves to next self.Question by incrementing the self.q_no counter
        self.q_no += 1

        # checks if the self.q_no size is equal to the self.data size
        if self.q_no == self.data_size:

            # if it is self.correct then it displays the score
            self.display_result()

            # destroys the self.root
            self.root.destroy()
        else:
            # shows the next self.question
            self.display_question()
            self.display_options()

    # This method shows the two buttons on the screen.
    # The first one is the next_button which moves to next self.question
    # It has properties like what text it shows the functionality,
    # size, color, and property of text displayed on button. Then it
    # mentions where to place the button on the screen. The second
    # button is the exit button which is used to close the self.root without
    # completing the quiz.
    def buttons(self):

        # The first button is the Next button to move to the
        # next self.Question
        next_button = Button(self.root, text="Next", command=self.next_btn,
                             width=10, bg="blue", fg="white", font=("ariel", 16, "bold"))

        # placing the button on the screen
        next_button.place(x=350, y=380)

        # This is the second button which is used to Quit the self.root
        quit_button = Button(self.root, text="Quit", command=self.root.destroy,
                             width=5, bg="black", fg="white", font=("ariel", 16, " bold"))

        # placing the Quit button on the screen
        quit_button.place(x=700, y=50)

    # This method deselect the radio button on the screen
    # Then it is used to display the self.options available for the current
    # self.question which we obtain through the self.question number and Updates
    # each of the self.options for the current self.question of the radio button.
    def display_options(self):
        val = 0

        # deselecting the self.options
        self.opt_selected.set(0)

        # looping over the self.options to be displayed for the
        # text of the radio buttons.
        for option in self.options[self.q_no]:
            self.opts[val]['text'] = option
            val += 1

    # This method shows the current self.Question on the screen
    def display_question(self):

        # setting the self.Question properties
        Label(self.root, text=self.question[self.q_no], width=60,
              font=('ariel', 16, 'bold'), anchor='w').place(x=70, y=100)

    # This method is used to Display Title
    def display_title(self):

        # The title to be shown
        title = Label(self.root, text="QUIZ",
                      width=80, bg="#4152b3", fg="white", font=("ariel", 20, "bold"))

        # place of the title
        title.place(x=0, y=2)

    # This method shows the radio buttons to select the self.Question
    # on the screen at the specified position. It also returns a
    # list of radio button which are later used to add the self.options to
    # them.
    def radio_buttons(self):

        # initialize the list with an empty list of self.options
        q_list = []

        # position of the first option
        y_pos = 150

        # adding the self.options to the list
        while len(q_list) < 4:
            # setting the radio button properties
            radio_btn = Radiobutton(self.root, text=" ", variable=self.opt_selected,
                                    value=len(q_list) + 1, font=("ariel", 14))

            # adding the button to the list
            q_list.append(radio_btn)

            # placing the button
            radio_btn.place(x=100, y=y_pos)

            # incrementing the y-axis position by 40
            y_pos += 40

        # return the radio buttons
        return q_list


    def snapshot(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            cv2.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") +
                        ".jpg", cv2.cvtColor(frame, cv2.COLOR_RGB2BGR))

    def update(self):
        # Get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(
                image=PIL.Image.fromarray(frame))
            self.canvas.create_image(
                0, 0, image=self.photo, anchor=NW)
        self.root.after(self.delay, self.update)


class MyVideoCapture:

    
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        self.change_res(self.vid, 120, 70)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)
        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

        # self.window = Tk()
        # self.window.overrideredirect(0)
        # App(self.window, "Face")

    def change_res(self, vid, width, height):
        vid.set(3, width)
        vid.set(4, height)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed

    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()


# Create a root and pass it to the Application object
root = Tk()
obj = App(root)
Button(root, text="Quit", command=root.destroy).place(x=0, y=200)
