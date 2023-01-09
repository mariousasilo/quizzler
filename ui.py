import tkinter
import random
import html
from tkinter import messagebox
from quiz import Quiz

FONT = ("Arial", 12, "normal")
THEME_COLOR = "#375362"


class Interface:

    def __init__(self):
        self.question_number: int
        self.quiz = Quiz()
        self.root = tkinter.Tk()
        self.root.title("Quizzler")
        self.root.config(padx=20, pady=20, background=THEME_COLOR)

        self.txt_score = tkinter.Label(text=f"Score: 0", background=THEME_COLOR, fg="white", font=FONT)
        self.txt_score.grid(row=0, column=1)

        self.canvas = tkinter.Canvas(width=300, height=250)
        self.txt_question = self.canvas.create_text(150, 125, text=f"sample", width=200, font=FONT)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        img_true = tkinter.PhotoImage(file="images/true.png")
        self.button_true = tkinter.Button(image=img_true, highlightthickness=0)
        self.button_true.grid(row=2, column=0)
        img_false = tkinter.PhotoImage(file="images/false.png")
        self.button_false = tkinter.Button(image=img_false, highlightthickness=0)
        self.button_false.grid(row=2, column=1)

        self.questioning()
        self.root.mainloop()

    def is_wrong(self):
        self.button_true.config(command=self.btn_pressed)
        self.button_false.config(command=self.btn_pressed)
        self.canvas.config(bg="red")
        self.quiz.questions_wrong.append(self.quiz.questions_list[self.question_number])
        self.quiz.questions_list.remove(self.quiz.questions_list[self.question_number])
        self.txt_score.config(text=f"Score: {len(self.quiz.questions_correct)}/"
                                   f"{len(self.quiz.questions_correct) + len(self.quiz.questions_wrong)}")
        self.delay()

    def is_correct(self):
        self.button_true.config(command=self.btn_pressed)
        self.button_false.config(command=self.btn_pressed)
        self.canvas.config(bg="green")
        self.quiz.questions_correct.append(self.quiz.questions_list[self.question_number])
        self.quiz.questions_list.remove(self.quiz.questions_list[self.question_number])
        self.txt_score.config(text=f"Score: {len(self.quiz.questions_correct)}/"
                                   f"{len(self.quiz.questions_correct)+len(self.quiz.questions_wrong)}")
        self.delay()

    def questioning(self):
        try:
            self.question_number = random.randint(0, len(self.quiz.questions_list) - 1)
            current_question = html.unescape(self.quiz.questions_dict["results"][self.question_number]["question"])
            current_answer = self.quiz.questions_dict["results"][self.question_number]["correct_answer"]
            self.canvas.itemconfig(self.txt_question, text=current_question)
            self.canvas.config(bg="white")
            if current_answer == "True":
                self.button_true.config(command=self.is_correct)
                self.button_false.config(command=self.is_wrong)
            elif current_answer == "False":
                self.button_true.config(command=self.is_wrong)
                self.button_false.config(command=self.is_correct)
        except ValueError:
            tkinter.messagebox.showinfo(message="There are no more questions left.")

    def delay(self):
        self.root.after(2000, self.questioning)

    def btn_pressed(self):
        pass
