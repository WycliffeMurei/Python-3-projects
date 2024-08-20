from tkinter import*
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
import mysql.connector
#from PIL import PhotoImage
#from pypdf import pdfileReader,FileWritter




splash_base = Tk()
splash_base.geometry('150x100')
splash_base.eval('tk::PlaceWindow . center')

splash_base.overrideredirect(True)
splash_base.title("Shine Tech database")
splash_base.configure(bg="orange")
splash_label =Label(splash_base,text="SHINE TECH Dbs",font=("Helvitica",10))
splash_label.pack(pady=20)




def main_window():
                splash_label.destroy()


                base = Tk()

                base.geometry('600x450')
                base.configure(bg="brown")
                base.title("Shine Tech  Database system")
                base.resizable(False,False)
               # image_icon=PhotoImage(file="Screenshot_20230611-,210849_Computer Launcher.jpg")
                #base.iconphoto(False,image_icon)
                labl_0 = Label(base, text="Registration system", width=20, font=("bold", 20))
                labl_0.place(x=90, y=53)
                list=[]
                connection = mysql.connector.Connect(host='localhost',user='root',password='kibet',port=3306,database='shine Tech')

                c = connection.cursor()







                def register ():
                    studentname =entry_1.get()
                    regno = entry_02.get()
                    course = entry_04.get()
                    semester = entry_05.get()
                    age = entry_06.get()
                    #insert_query = "INSERT INTO "'DETAILS'('Name','admission','study','course')
                    #VALUE = ("%S,%S,%S,%S,%S")


                    #vals = (studentname, regno, course,semester, age)
                    #c.execute(insert_query, vals)
                    #connection.commit()
                    with mysql.connect("Shine Tech") as connection:
                         c = connection.cursor()
                         line = "INSERT INTO Details Values('" + studentname  + '",' "" + str(regno) +'" ,' "" + course +"", + semester + '",' "" "" +str(age) +")"
                         c.execute(line)
                         c.commit()
                         c.close()
                    

                    if studentname =="" and regno=="":
                        messagebox.showerror("Blank", "Blank field!")

                    elif len(studentname) >= 16:
                            messagebox.showerror("Blank","inalid length")


                    elif  len(regno)   > 10 and not IntVar :
                        messagebox.showerror("showeerror","invalid input")
                        messagebox.showerror("showerror", "Blank field!")



                    elif studentname  == True and age == True:
                        list.append(studentname and regno)



                    if  course =="" and semester and age =="":
                        messagebox.showerror("Blank", "Blank field!", )

                    elif len(studentname) >= 16:
                            messagebox.showerror("Blank", "inalid length")

                    elif len(age) > 2 and not int and age < 18 :
                            messagebox.showerror("Blank", "invalid input")




                    else:

                          course == True and semester == True
                          list.append(course and semester)
                    messagebox.showinfo("success", "success Registration")




                def add ():
                    studentname=entry_1.get()
                    regno= entry_02.get()
                    course= entry_04.get()
                    semester= entry_05.get()
                    age= entry_06.get()
                    if studentname =="" and regno=="":
                        messagebox.showerror("showerror", "Blank field!")

                    elif len(studentname) >= 16:
                            messagebox.showerror("showerror","inalid length")


                    elif len(regno) > 10 and not int :
                        messagebox.showerror("showeerror","invalid input")
                        messagebox.showerror("showerror", "Blank field!")



                    elif studentname  == True and age == True:
                        list.append(studentname and regno)



                    if  course =="" and semester and age =="":
                        messagebox.showerror("showerror", "Blank field!", )

                    elif len(studentname) >= 16:
                            messagebox.showerror("showerror", "inalid length")

                    elif len(age) > 2 and not int and age < 18 :
                            messagebox.showerror("showeerror", "invalid input")




                    else:

                          course == True and semester == True
                          list.append(course and semester)
                    messagebox.showinfo("showinfo", "success record addition")









                def update ():
                    studentname=entry_1.get()
                    regno= entry_02.get()
                    course= entry_04.get()
                    semester= entry_05.get()
                    age= entry_06.get()
                    if studentname == "" and regno == "":
                        messagebox.showerror("showerror", "Blank field!")

                    elif len(studentname) >= 16:
                        messagebox.showerror("showerror", "inalid length")


                    elif len(regno) > 10 and not int:
                        messagebox.showerror("showeerror", "invalid input")
                        messagebox.showerror("showerror", "Blank field!")



                    elif studentname == True and age == True:
                        list.append(studentname and regno)

                    if course == "" and semester and age == "":
                        messagebox.showerror("showerror", "Blank field!", )

                    elif len(studentname) >= 16:
                        messagebox.showerror("showerror", "inalid length")

                    elif len(age) > 2 and not int and age < 18:
                        messagebox.showerror("showeerror", "invalid input")




                    else:

                        course == True and semester == True
                        list.append(course and semester)
                    messagebox.showinfo("showinfo", "success update!")

                def search():

                    messagebox.showinfo("showinfo","Enter element to search")
                    label_7 =Label(base,text="search",width="20",textvariable="search",font=("italic",10))
                    label_7.place(x=200,y=350)



                    if element in list:
                        messagebox.showinfo("showinfo","element found")
                    else:
                        messagebox.error("showerror","Record not found")
                def delete():
                    messagebox.showwarning("showwarning","Are you sure")
                    register().destroy()





                def view():
                    username = str()
                    pwd = str()
                    username = "kibet"
                    pwd = "kibet"
                    label_8 = Label(base, text="username", width="20", textvariable="search", font=("italic", 10))
                    label_8.place(x=390, y=240)

                    label_9 = Label(base, text="paswword", width="20", textvariable="pwd", font=("italic", 10))
                    label_9.place(x=390, y=260)

                    if username and pwd =="":
                        messagebox.showerror("showerror","cannot be blank")
                    elif  not pwd and username:
                        messagebox.showerror("showerror", "check pasword or username")
                    else:
                        pass











                    studentname = IntVar()
                    regno = IntVar()
                    course= IntVar()
                    age = IntVar()
                    search = IntVar()
                    global entry_1
                    global entry_02
                    global entry_03
                    global entry_04
                    global entry_05
                    global entry_06

                labl_1 = Label(base, text="Student Name",width=20, font=("bold", 10))
                labl_1.place(x=68, y=130)


                entry_1 = Entry(base)
                entry_1.place(x=250, y=130)

                labl_2 = Label(base, text="Reg No.", width=20, font=("bold", 10))
                labl_2.place(x=68, y=180)


                entry_02 = Entry(base)
                entry_02.place(x=250, y=180)

                labl_3 = Label(base, text="Gender", width=20, font=("bold", 10))
                labl_3.place(x=70, y=230)

                Radiobutton(base, text="Male", padx=5, value=1).place(x=250, y=230)
                Radiobutton(base, text="Female", padx=5,  value=2).place(x=310, y=230)

                labl_4 = Label(base, text="course:", width=20, font=("bold", 10))
                labl_4.place(x=70, y=280)


                entry_04 = Entry(base)
                entry_04.place(x=250, y=280)

                labl_5 = Label(base, text="semester:", width=20, font=("bold", 10))
                labl_5.place(x=70, y=280)


                entry_05= Entry(base)
                entry_05.place(x=250, y=280)

                labl_6 = Label(base, text="Age:", width=20, font=("bold", 10))
                labl_6.place(x=70, y=280)


                entry_06 = Entry(base)
                entry_06.place(x=250, y=280)

                Button(base, text='Submit', width=20, bg='brown', fg='white',command=register).place(x=400, y=380)
                Button(base, text="Add", width=20,  bg='red', fg='white', command=add).place(x=220,y=380)
                Button(base, text="update", width=20,  bg='blue', fg='white', command=update).place(x=40,y=380)
                Button(base,text="search",width=20, bg='pink',fg='whitesmoke',command=search).place(x=200,y=350)
                Button(base, text="delete", width=20, bg='Darkviolet', fg='pink', command=delete).place(x=200, y=420)
                Button(base, text="view", width=20, bg='pink', fg='white', command=view).place(x=400, y=200)
# it will be used for displaying the registration form onto the window






splash_label.after(3000,main_window)
mainloop()
print("Registration form is created seccussfully...")

