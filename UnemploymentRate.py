from tkinter import *
import tkinter.messagebox as MessageBox
import mysql.connector as mysql

def insert():

    ID = e_ID.get()
    States = e_States.get()
    Rate = e_Rate.get()

    if (ID == "" or States == "" or Rate ==""):
        MessageBox.showinfo("Insert Status", "All Fields are required")
    else:
        con = mysql.connect(host ="35.223.140.107", user ="root", password = "1234", database= "izzydb")
        cursor = con.cursor()
        cursor.execute("insert into UnemploymentRateQ3_2017 values('"+ID+"', '"+States+"', '"+Rate+"')")
        cursor.execute("commit")

        e_ID.delete(0, 'end')
        e_States.delete(0, 'end')
        e_Rate.delete(0, 'end')
        show()

        MessageBox.showinfo("Insert Status", "Inserted Successfully")
        con.close()

def delete():
    if (e_ID.get() == ""):
        MessageBox.showinfo("Delete Status", "ID is compulsory for delete")
    else:
        con = mysql.connect(host="35.223.140.107", user="root", password="1234", database="izzydb")
        cursor = con.cursor()
        cursor.execute("delete from UnemploymentRateQ3_2017 where ID = '"+e_ID.get() + "'")
        cursor.execute("commit")

        e_ID.delete(0, 'end')
        e_States.delete(0, 'end')
        e_Rate.delete(0, 'end')
        show()

        MessageBox.showinfo("Delete Status", "Deleted Successfully")
        con.close()

def update ():
    ID = e_ID.get()
    States = e_States.get()
    Rate = e_Rate.get()

    if (ID == "" or States == "" or Rate == ""):
        MessageBox.showinfo("Update Status", "All Fields are required")
    else:
        con = mysql.connect(host="35.223.140.107", user="root", password="1234", database="izzydb")
        cursor = con.cursor()
        cursor.execute("update UnemploymentRateQ3_2017 set States= '"+ States +"', Rate = '"+ Rate +"' where ID = '"+ ID +"'")
        cursor.execute("commit")

        e_ID.delete(0, 'end')
        e_States.delete(0, 'end')
        e_Rate.delete(0, 'end')
        show()

        MessageBox.showinfo("Update Status", "Updated Successfully")
        con.close()

def get():
    if (e_ID.get() == ""):
        MessageBox.showinfo("Fetch Status", "ID is compulsory for delete")
    else:
        con = mysql.connect(host="35.223.140.107", user="root", password="1234", database="izzydb")
        cursor = con.cursor()
        cursor.execute("select * from UnemploymentRateQ3_2017 where ID= '"+e_ID.get()+"'")
        rows = cursor.fetchall()

        for row in rows:
            e_States.insert(0, row[1])
            e_Rate.insert(0, row[2])


        con.close()

def show ():
    con = mysql.connect(host="35.223.140.107", user="root", password="1234", database="izzydb")
    cursor = con.cursor()
    cursor.execute("select * from UnemploymentRateQ3_2017")
    rows = cursor.fetchall()
    list.delete(0, list.size())

    for row in rows:
        insertData = str(row [0])+ '         '+row[1] # +'       '+str(row[2])
        list.insert (list.size()+1, insertData)

    con.close()



root = Tk()
root.geometry("600x300")
root.title("Unemployment Rate Q3 2017")


ID = Label(root, text ="Enter ID", font = ("bold", 10))
ID.place(x=20, y=30)

States = Label(root, text ="Enter State", font = ("bold", 10))
States.place(x=20, y=60)

Rate = Label(root, text ="Enter Rate", font = ("bold", 10))
Rate.place(x=20, y=90)


e_ID = Entry()
e_ID.place(x=150, y=30)

e_States = Entry()
e_States.place(x=150, y=60)

e_Rate = Entry()
e_Rate.place(x=150, y=90)


insert = Button (root, text="Insert", font=("Arial", 10), bg="white", command=insert)
insert.place(x=20, y =140)

delete = Button (root, text="Delete", font=("Arial", 10), bg="white", command=delete)
delete.place(x=70, y =140)

update = Button (root, text="Update", font=("Arial", 10), bg="white", command=update)
update.place(x=130, y =140)

get = Button (root, text="Get", font=("Arial", 10), bg="white", command=insert)
get.place(x=190, y =140)


list = Listbox(root)
list.place(x = 400, y = 30)
show()

root.mainloop()