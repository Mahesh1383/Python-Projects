

from tkinter import *
from tkinter.font import BOLD
import mysql.connector
from tkinter import messagebox

db = mysql.connector.connect(host='****', user='****', password='****', port=****, database='****')
cursor = db.cursor()

window = Tk()
window.title("Blood Bank Management System")


def Donate_dbase():
    global bgrp
    global bunits
    units = bunits.get()

    dbase = mysql.connector.connect(host='*****', user='****', password='****', port=*****, database='****')
    cursor = dbase.cursor()

    print(bgrp)
    print(units)

    sqlquery = "Select units from BloodBank where Blood_Grp = '" + bgrp + "';"
    cursor.execute(sqlquery)

    for i in cursor:
        print(i[0])
        units = str(int(i[0]) + int(units))
        print(units)

    sqlquery = "Update BloodBank set units='" + units + "'where Blood_Grp='" + bgrp + "';"
    print(sqlquery)

    try:
        cursor.execute(sqlquery)
        dbase.commit()
        messagebox.showinfo('Success', 'Blood Donated Successfully')
    except:
        messagebox.showinfo('Error', 'Cannot Access Database')


def donate(*args, **kwargs):
    global bgrp
    global bunits

    bgrp = args[0]
    print(bgrp)

    window = Tk()
    window.title("Blood Donation Management System")
    Label(window, font=('arial', 10, 'bold'), text="Donate Blood").grid(rowspan=0, columnspan=3)

    Label(window, font=('arial', 10, 'bold'), text="Enter No of units ").grid(row=4, column=1)
    Label(window, font=('arial', 10, 'bold'), text=" ").grid(row=4, column=2)

    bunits = Entry(window, width=5, font=('arial', 10))
    bunits.grid(row=4, column=3)


Button(window, text="Submit", command=Donate_dbase, bg='DodgerBlue2', fg='White', font=('arial', 10)).grid(row=8,
                                                                                                           columnspan=3)

print('Donate')


def Request_dbase():
    global bgrp
    global bunits

    units = bunits.get()

    dbase = mysql.connector.connect(host='localhost', user='root', password='toor', port=3306, database='mahesh')
    cursor = dbase.cursor()

    print(bgrp)
    print(units)

    sqlquery = "Select units from BloodBank where Blood_Grp='" + bgrp + "' ;"
    cursor.execute(sqlquery)

    for i in cursor:
        if int(i[0]) >= int(units):
            units = str(int(i[0]) - int(units))
            print(units)

            sqlquery = "update BloodBank set units='" + units + "'  where Blood_Grp='" + bgrp + "';"
            print(sqlquery)

            try:
                cursor.execute(sqlquery)
                dbase.commit()
                messagebox.showinfo('Success', 'Blood Donated Successfully')
            except:
                messagebox.showinfo('Error', 'Cannot Access Databases')
        else:
            messagebox.showinfo("Error", "Not Available")


def request(*args, **kwargs):
    global bgrp
    global bunits

    bgrp = args[0]
    print(bgrp)

    window = Tk()
    window.title('Blood Donation Management System')

    Label(window, font=('arial', 20, 'bold'), text='Request Blood').grid(row=0, columnspan=3)
    Label(window, font=('arial', 10, 'bold'), text="Enter Units Required:").grid(row=4, columnspan=1)
    Label(window, font=('arial', 10, 'bold'), text=" ").grid(row=4, columnspan=2)

    bunits = Entry(window, width=5, font=('arial', 10, 'bold'))
    bunits.grid(row=4, column=3)


Button(window, text='Submit', font=('arial', 10), command=Request_dbase, bg='DodgerBlue2', fg='white').grid(row=8,
                                                                                                            columnspan=3)

print("Request")

sqlquery = ' select * from BloodBank;'

try:
    cursor.execute(sqlquery)

    Label(window, font=('arial', 20, 'bold'), text="%-20s%-20s" % ("Blood group", "Units")).grid(row=1, column=1)
    x = 4
    for i in cursor:
        Label(window, font=('arial', 10), text="%-20s%-20s" % (i[0], i[1])).grid(row=x, column=1)
        bgrp = i[0]

        Button(window, text='Donate', command=lambda arg=i[0], kw='donate': donate(arg, o1=kw), padx=10, pady=10,
               bg='DodgerBlue2', fg='White', font=('arial', 15)).grid(row=x, column=2)
        Button(window, text='Request', command=lambda arg=i[0], kw='request': request(arg, o1=kw), pady=10, padx=10,
               bg='DodgerBlue2', fg='White', font=('arial', 15)).grid(row=x, column=3)

        x += 1
except:
    messagebox.showinfo("Error", "Cannot Fetch Data")

mainloop()



