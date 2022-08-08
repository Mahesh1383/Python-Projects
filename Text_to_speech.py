from gtts import gTTS , lang
import os
from tkinter import *
from tkinter import messagebox
import speech_recognition as sr


def text_to_speech():
    text = text_entry..get("1,0","end-1c")
    language = accent_entry.get()
    if(len(text)<=1) | (len(language)<=0):
        messagebox.showerror(message="Enter the required details")
        return
    speech = gTTS(text=text,lang=language,slow=False)
    speech.save("text.mp3")


def list_languages():
    messagebox.showinfo(message=list(lang.tts_langs().items()))


def speech_to_text():
    recorder = sr.Recognizer()
    try:
        duration = int(duration_entry.get())
    except:
        messagebox.showerror("Enter the Duration")
        return
    messagebox.showinfo(message="Speak in the microphone and wait after finishing the recording")
    with sr.Microphone as mic:
        recorder.adjust_for_ambient_noise(mic)
        audio_input = recorder.listen(mic,duration=duration)
        try:
            text_output = recorder.recognize_google(audio_input)
            messagebox.showinfo(message="You said:\n"+text_output)
        except:
            messagebox.showerror(message="Couldn't process the audio input.")


window =Tk()
window.geometry('500x300')
window.title("Convert speech to text and Text to speech")
Label(window,text="Convert speech to text and Text to speech”).pack()
Label(window,text="Text:").place(x=10,y=20)
text_entry = Text(window,width=30,height=5).place(x=80,y=20)
Label(window,text="Accent:").place(x=10,y=110)
accent_entry = Entry(window,width=26).place(x=80,y=110)
Label(window,text="Duration:").place(x=10,y=140)
duration_entry = Entry(window,width=26).place(x=80,y=140)

Button(window,text="List Language",bg='Turquoise',fg='Red',command=list_languages).place(x=10,y=190)
Button(window,text="Convert Text to Speech",bg='Turquoise',fg='Red',command=text_to_speech).place(x=130,y=190)
Button(window,text="Convert Speech to Text",bg='Turquoise',fg='Red',command=speech_to_text).place(x=305,y=190)

window.mainloop()

