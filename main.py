from tkinter import *
from random import shuffle
from words import words

text_color = "#48F598"
background_color = "#0D1E44"
FONT_NAME = "Courier"

list_of_words = words.split(" ")
timer = None


class TypingSpeedometer:
    def __init__(self):
        self.example_words = []
        self.words_per_minute = 0

    def start(self):
        self.words_per_minute = 0
        shuffle(list_of_words)
        self.example_words = list_of_words[:130]
        test_words.delete('1.0', END)
        test_words.insert(END, self.example_words)

        text_label.destroy()
        start_btn.destroy()

        timer_label.grid(column=0, row=1, columnspan=2)
        test_words.grid(column=0, row=2)
        user_text.delete('1.0', END)
        user_text.focus()
        user_text.grid(column=1, row=2)
        self.count_down(59)

    def count_down(self, count):
        timer_label.config(text=f"00:{count}")
        if count < 10:
            timer_label.config(text=f"00:0{count}")
        if count > 0:
            global timer
            timer = window.after(1000, self.count_down, count - 1)
        else:
            timer_label.config(text=f"00:00")
            self.count_words()

    def count_words(self):
        user_words = user_text.get("1.0", END).strip("\n").split(" ")
        for n in range(len(user_words)):
            if user_words[n] == self.example_words[n]:
                self.words_per_minute += 1

        self.show_results()

    def show_results(self):
        new_window = Toplevel()
        new_window.config(padx=100, pady=50, bg=background_color)
        results_label = Label(
            new_window,
            text=f"Your results: {self.words_per_minute} words per minute!",
            font=(FONT_NAME, 25),
            bg=background_color,
            fg=text_color,
            pady=50
        )
        results_label.grid()
        try_again_btn = Button(new_window, image=try_again_img, highlightthickness=0, bd=0, command=self.start)
        try_again_btn.grid()


speedometer = TypingSpeedometer()

# GUI
window = Tk()
window.title("Typing Speedometer")
window.config(padx=100, pady=50, bg=background_color)

title_img = PhotoImage(file="images/title.png")
title_label = Label(image=title_img)
title_label.config(bg=background_color)
title_label.grid(column=0, columnspan=2)

text_img = PhotoImage(file="images/text.png")
text_label = Label(image=text_img)
text_label.config(bg=background_color)
text_label.grid()

start_btn_img = PhotoImage(file="images/button_start.png")
try_again_img = PhotoImage(file="images/button_try-again.png")
start_btn = Button(image=start_btn_img, highlightthickness=0, bd=0, command=speedometer.start)
start_btn.grid()

test_words = Text(width=42, height=17, font=(FONT_NAME, 18), bg=background_color, fg="#a4e2c0", wrap="word")
test_words.config(highlightbackground=text_color, highlightcolor=text_color, highlightthickness=1)

user_text = Text(width=42, height=17, font=(FONT_NAME, 18), bg=background_color, fg=text_color, wrap="word")
user_text.config(highlightbackground=text_color, highlightcolor=text_color, highlightthickness=1)

timer_label = Label(text="00:00", font=(FONT_NAME, 25), bg=background_color, fg=text_color)

window.mainloop()
