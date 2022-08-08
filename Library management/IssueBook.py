from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pymysql
mypass = 'toor'
mydatabase = '*****'

con = pymysql.connect(host='*******', user='*****', password='*****', port=****, database='******')
cur = con.cursor()

issueTable = "books_issued"
bookTable = "books"

allBid = []


def issue():

    global issueBtn, labelFrame, lb1, inf1, inf2, quitBtn, root, Canvas1, status

    bid =inf1.get()
    issueto = inf2.get()

    issueBtn.destroy()
    labelFrame.destroy()
    lb1.destroy()
    inf1.destroy()
    inf2.destroy()

    extractBid = "select bid from " +bookTable
    try:
        cur.execute(extractBid)
        con.commit()
        for i in cur:
            allBid.append(i[0])

        if bid in allBid:
            checkAvail = "slelct status from "+bookTable+"where bid = '"+bid+"'"
            cur.execute(checkAvail)
            con.commit()
            for i in cur:
                check = i[0]

                if check == True:
                    status = True
                else:
                    status = False

        else:
            messagebox.showinfo("Error","Book ID not present")
    except:
        messagebox.showinfo("Error","Can't fetch Book Ids")
    issueSQL = "insert into "+issueTable+"values('"+bid+"'.'"+issueto+"')"
    show = "select * from "+issueTable

    updateStatus = "update"+bookTable+"set Status = 'issued' where bid ='"+bid+"'"
    try:
        if bid in allBid and status == True:
            cur.execute(issueSQL)
            con.commit()
            cur.execute(updateStatus)
            con.commit()
            messagebox.showinfo('Success','Book Issued Successfully')
            root.destroy()
        else:
            allBid.clear()
            messagebox.showinfo('Message','Book Already issued')
            root.destroy()
            return
    except:
        messagebox.showinfo('Search Error','The value entered is wrong, try again')

    print(bid)
    print(issueto)

    allBid.clear()


def issueBook():
    global labelFrame,inf1,inf2,root,Canvas1,status

    root =Tk()
    root.title('Library')
    root.minsize(width=400,height=400)
    root.geometry("600x500")

    Canvas1 = Canvas(root)
    Canvas1.config(bg='#D6ED17')
    Canvas1.pack(expand=True,fill=BOTH)

    headingFrame = Frame(root,bg='#FFBB00',bd=5)
    headingFrame.place(relx=0.25,rely=0.1,relwidth=0.5,relheight=0.13)

    headingLabel = Label(headingFrame,text="Issue Book",bg='black',fg='white',font=('courier',15))
    headingLabel.place(relx=0,rely=0,relwidth=1,relheight=1)

    labelFrame = Frame(root,bg='black')
    labelFrame.place(relx=0.1,rely=0.3,relwidth=0.8,relheight=0.5)

    Label(labelFrame,text="BooK ID:",bg='black',fg='white').place(relx=0.05,rely=0.2)

    inf1 =Entry(labelFrame)
    inf1.place(relx=0.05,rely=0.4)

    Label(labelFrame,text="Issued To:",bg='black',fg='white').place(relx=0.05,rely=0.4)

    inf2 = Entry(labelFrame)
    inf2.place(relx=0.3,rely=0.4)

    issueBtn = Button(root,text="Issue",bg='#d1cc0',fg='black',command=issue)
    issueBtn.place(relx=0.28,rely=0.9,relwidth=00.18,relheight=0.08)

    quitBtn = Button(root,text="Quit",bg='#aaa69d',fg='black',command=root.destroy)
    quitBtn.place(relx=0.53,rely=0.9,relwidth=0.10,relheight=0.08)

    root.mainloop()


