from tkinter import *
from quiz_brain import QuizBrain

# For the User Interface using Tkinter
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        # I just tapped into the QuizBrain Class

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some question text", fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        false_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=false_image, highlightthickness=0, command=self.wrong)
        self.wrong_button.grid(row=2, column=0)

        true_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=true_image, highlightthickness=0, command=self.correct)
        self.correct_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz Over")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def wrong(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def correct(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
