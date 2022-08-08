from tkinter import *
from PIL import ImageTk,Image
import pymysql
from AddBook import *
from DeleteBook import *
from ViewBooks import *
from ReturnBook import *
from IssueBook import *
mypass = '****'
mydatabase ='****'

con = pymysql.connect(host='******',user='******',password='****',port=****,database='****')
cur = con.cursor()

root = Tk()
root.title("Library")
root.minsize(width=400,height=400)
root.geometry("600x500")

same =True
n=0.25
background_image = Image.open('*********lib.jpg')
[imageSizeWidth, imageSizeHeight]= background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth,newImageSizeHeight),Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

Canvas1 = Canvas(root)
Canvas1.create_image(300,400,image = img)
Canvas1.config(bg="white",width=newImageSizeWidth,height=newImageSizeHeight)
Canvas1.pack(expand=True,fill=BOTH)

headingFrame1 = Frame(root,bg="#FFBB00",bd=5)
headingFrame1.place(relx=0.2,rely=0.1,relwidth=0.6,relheight=0.16)

headinglabel = Label(headingFrame1,text='Welcome to Library Management',bg='black',fg='white',font=('Courier',15))
headinglabel.place(relx=0,rely=0,relheight=1,relwidth=1)

Button(root,text="Add Book Details",bg='black',fg='white',command=addBook).place(relx=0.28,rely=0.4,relwidth=0.45,relheight=0.1)
Button(root,text="Delete",bg='black',fg='white',command=deleteBook).place(relx=0.28,rely=0.5,relwidth=0.45,relheight=0.1)
Button(root,text="View Book Lists",bg='black',fg='white',command=View).place(relx=0.28,rely=0.6,relwidth=0.45,relheight=0.1)
Button(root,text="Issue Book to Student",bg='black',fg='white',command=issueBook).place(relx=0.28,rely=0.7,relwidth=0.45,relheight=0.1)
Button(root,text="Return Book",bg='black',fg='white',command=returnBook).place(relx=0.28,rely=0.8,relwidth=0.45,relheight=0.1)

root.mainloop()
