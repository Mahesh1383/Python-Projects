from tkinter import *
import random
from tkinter import messagebox

target = 0
score = 0
guess = 0


def add():
    return "The sum of target and guess is" + str(guess+target)


def sub():
    return "The difference of target and guess is" + str(target-guess)


def multiplication():
    return "The product of target and guess is" + str(guess*target)


def division():
    return "The division of target by guess is " + str(target/guess)


def great_lesser():
    if target<guess:
        return 'Target is  less than guess'
    elif target>guess:
        return 'Target is greater than guess'


def clue():
    switcher = {
        0: add(),
        1: sub(),
        2: multiplication(),
        3: division(),
        4: great_lesser()
    }
    return switcher.get(random.randint(0, 4))


def generate_target_number():
    global target
    target = random.randint(0,10)
    messagebox.showinfo(message="Randon Number Generated; Started Guessing!! STARTING SCORE=10")
    random_number_button['state'] = DISABLED
    guess_button['STATE'] = NORMAL


def guess_and_score():
    global score
    global guess
    try:
        guess =0
        guess = int(guess_entry.get())
    except:
        messagebox.showerror(message="Enter a number to guess and to play")
        return
    if guess == target:
        messagebox.showinfo(message="Congratulations!!! you guess the number correct . Your score is "+str(score))
        random_number_button['state'] = NORMAL
        guess_button['state'] = DISABLED
        return
    elif score==0:
        messagebox.showwarning(message="Out of Guesses Buddy!  Better luck next time);")
        return
    else:
        score-=1
        message =clue()
        messagebox.showinfo(message=message)


window = Tk()
window.geometry('350x200')
window.title("Number Guessing Game")
title_label = Label(window, text="Number Guessing Game\n Guess a number between 1 to 50", font=('TimesnewRoamn', 12))
title_label.pack()
random_number_button = Button(window, text="Generate Random Number", command=generate_target_number)
guess_label = Label(window, text='Enter your guess:')
guess_label.pack()
guess_entry = Entry(window, width=5)
guess_entry.pack()
guess_button = Button(window, text="Guess Me", command=guess_and_score, state=DISABLED)
guess_button.pack()
window.mainloop()

