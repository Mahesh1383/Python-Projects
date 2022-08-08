﻿from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql


def bookRegister():
    bid = bookInfo1.get()
    title = bookInfo2.get()
    author = bookInfo3.get()
    status = bookInfo4.get()
    status = status.lower()

    insertBooks = "insert into table" + bookTable + " values ('" + bid + "','" + title + "','" + author + "');"
    try:
        cur.execute(insertBooks)
        con.commit()
        messagebox.showinfo('Success', 'Book Added Successfully')
    except:
        messagebox.showinfo("Error", "Can't add data into Database")

    print(bid)
    print(title)
    print(author)
    print(status)

    root.destroy()


def addBook():
    global bookInfo1, bookInfo2, bookInfo3, bookInfo4, Canvas1, con, cur, bookTable, root

    root = Tk()
    root.title("Library")
    root.minsize(height=400, width=400)
    root.geometry("600x500")

    con = pymysql.connect(host="*****", user='****', password='******', database='mahesh')
    cur = con.cursor()

    bookTable = "books"

    Canvas1 = Canvas(root)

    Canvas1.config(bg="Maroon")
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame1 = Frame(root,bg='#FFBB00',bd=5)
    headingFrame1.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headinglabel = Label(headingFrame1,text='Add Books',bg='black',fg='white',font=('courier',15))
    headinglabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.4,relwidth=0.8,relheight=0.4)

    lb1 = Label(labelFrame,text='Book Id:',bg='black',fg='white')
    lb1.place(relx=0.05,rely=0.2,relheight=0.08)

    bookInfo1 = Entry(labelFrame)
    bookInfo1.place(rely=0.2,relx=0.3,relwidth=0.62,relheight=0.08)

    lb2 = Label(labelFrame,text='Title:',bg='black',fg='white')
    lb2.place(relx=0.05,rely=0.35,relheight=0.08)

    bookInfo2 = Entry(labelFrame)
    bookInfo2.place(relx=0.3,rely=0.35,relheight=0.08)

    lb3 = Label(labelFrame,text='Author :',bg='black',fg='white')
    lb3.place(relx=0.05,rely=0.5,relheight=0.08)

    bookInfo3 = Entry(labelFrame)
    bookInfo3.place(relx=0.3,rely=0.5,relwidth=0.62,relheight=0.08)

    lb4 = Label(labelFrame)
    lb4.place(relx=0.08,rely=0.65,relheight=0.08)

    bookInfo4 =Entry(labelFrame)
    bookInfo4.place(relx=0.3,rely=0.65,relheight=0.08,relwidth=0.62)

    Button(root,text='Quit',bg='#f7f1e3',fg='black',command=root.destroy).place(relheight=0.08,relx=0.53,rely=0.9,relwidth=0.18)
    root.mainloop()



