from tkinter import*
from tkinter import messagebox
from tkinter import ttk
name=str()
empno = str()
gender= str()
specy=str()
email= str()
'''import mysql.connector'''
'''import mysql.connector'''
'''mydb= mysql.connector.connect(
        host='localhost',
        user='root',
        password='kibet',
        port='3306',
        database='record')
mycursor = mydb.cursor()'''

root = Tk()





root.resizable(False,False)
root.title('School Reporting Assesment System')
root.geometry('700x400')
root.configure(bg='purple')
labl_0 = Label(root, text="Human Resource Reporting  System", width=30, font=("bold", 20))
labl_0.place(x=90, y=53)

frame_1 = Frame(root,bg='white',width="300",height="200")
frame_1.place(x=20,y=135)
label_1 = Label(frame_1,text="Teachers Report schedule" ,font=('bold',15))
label_1.place(x=40, y=40)

frame_2 = Frame(root,bg='violet',width="300",height="200")
frame_2.place(x=350,y=135)

label_2 = Label(frame_2,text="Non_staff Report schedule" ,font=('bold',15))
label_2.place(x=40, y=40)
#frame_rpt = Frame(base,bg='grey',width=50,height=50)

global rpt



class staff:
 def __init__(self, name,empno ,gender,specy,email):
    self.name = name
    self.empno = empno
    self.gender = gender
    self.specy = specy
    self.email = email


 

 def rpt (name=None):




      base = Toplevel(root)
      base.configure(bg='indigo')
      base.geometry('500x400')
      base.title('Staff Report')
      base.resizable(False, False)
      #base.place(side=RIGHT)
      frame_rpt = Frame(base,bg='orange',width=400,height=350)
      frame_rpt.place(x=50, y=40)



      label_0 = Label(frame_rpt, text="Teachers Report schedule", font=('bold', 15))
      label_0.place(x=70, y=40)

      labl_1 = Label(frame_rpt, text="Teachers Name", width=20, font=("bold", 10))
      labl_1.place(x=1, y=80)

      entry_1 = Entry(frame_rpt)
      entry_1.place(x=180, y=80)

      labl_2 = Label(frame_rpt, text="    Employment No.", width=20, font=("bold", 10))
      labl_2.place(x=1, y=100)

      entry_02 = Entry(frame_rpt)
      entry_02.place(x=180, y=100)

      labl_3 = Label(frame_rpt, text="Gender", width=20, font=("bold", 10))
      labl_3.place(x=1, y=120)


      Radiobutton(frame_rpt, text="Male", padx=5, value=1).place(x=180, y=120)
      Radiobutton(frame_rpt, text="Female", padx=5, value=2).place(x=230, y=120)

      labl_4 = Label(frame_rpt, text="specification Field:", width=20, font=("bold", 10))
      labl_4.place(x=1, y=140)

      entry_04 = Entry(frame_rpt)
      entry_04.place(x=180, y=140)

      labl_5 = Label(frame_rpt, text="Department:", width=20, font=("bold", 10))
      labl_5.place(x=1, y=160)

      entry_05 = Entry(frame_rpt)
      entry_05.place(x=180, y=160)

      labl_6 = Label(frame_rpt, text="Email:", width=20, font=("bold", 10))
      labl_6.place(x=1, y=180)

      entry_06 = Entry(frame_rpt)
      entry_06.place(x=180, y=180)

      def submit():
          global base






          name = entry_1.get()
          empno = entry_02.get()
          gender=entry_04.get()
          specy = entry_05.get()
          email = entry_06.get()


          #insert_query = "INSERT INTO ", 'human resource record', ('Name', 'Emp no', 'specification','Department')

          #values = ('name=','employ','gender','spec','email',)

          #mycursor.execute(insert_query, values)
          #mydb .commit()


          if name or empno or  gender or specy or email=="":
              messagebox.showerror("error","Empty fields not allowed")
          else:
               blank= messagebox.RETRY

          sub = messagebox.showinfo("success", "your report is being validated , check the response in your Email account")

          if sub == 1:
              sub = messagebox.OK

      Button(frame_rpt, text="Submit", command=submit).place(x=150, y=220)
      base.destroy



      base.mainloop()

def rpt_staff():

          staffbase = Toplevel(root)
          staffbase.configure(bg='maroon')
          staffbase.geometry('500x400')
          staffbase.title('Staff Report')
          staffbase.resizable(False, False)
          # base.place(side=RIGHT)
          frame_rptstaff = Frame(staffbase, bg='white', width=400, height=350)
          frame_rptstaff.place(x=50, y=40)

          label_0 = Label(frame_rptstaff, text="Non_staff Report schedule", font=('bold', 15))
          label_0.place(x=70, y=40)

          labl_1 = Label(frame_rptstaff, text="Employee  Name.", width=20, font=("bold", 10))
          labl_1.place(x=1, y=80)

          entry_1 = Entry(frame_rptstaff)
          entry_1.place(x=180, y=80)

          labl_2 = Label(frame_rptstaff, text="Employment No.", width=20, font=("bold", 10))
          labl_2.place(x=1, y=100)

          entry_02 = Entry(frame_rptstaff)
          entry_02.place(x=180, y=100)

          labl_3 = Label(frame_rptstaff, text="Gender", width=20, font=("bold", 10))
          labl_3.place(x=1, y=120)

          Radiobutton(frame_rptstaff, text="Male", padx=5, value=1).place(x=180, y=120)
          Radiobutton(frame_rptstaff, text="Female", padx=5, value=2).place(x=230, y=120)

          labl_4 = Label(frame_rptstaff, text="specification Field:", width=20, font=("bold", 10))
          labl_4.place(x=1, y=140)

          entry_04 = Entry(frame_rptstaff)
          entry_04.place(x=180, y=140)

          labl_5 = Label(frame_rptstaff, text="Department:", width=20, font=("bold", 10))
          labl_5.place(x=1, y=160)

          entry_05 = Entry(frame_rptstaff)
          entry_05.place(x=180, y=160)

          labl_6 = Label(frame_rptstaff, text="Email:", width=20, font=("bold", 10))
          labl_6.place(x=1, y=180)

          entry_06 = Entry(frame_rptstaff)
          entry_06.place(x=180, y=180)

          def submit():
              global staff

              name = entry_1.get()
              empno = entry_02.get()
              gender = entry_04.get()
              specy = entry_05.get()
              email = entry_06.get()

              # insert_query = ("INSERT INTO ", 'users', ('name', 'adm', 'age')
              # VALUES ("%s","%s","%s")
              # vals = ('studentname', 'regno','age')

              # mycursor.execute(insert_query, vals)
              # mydb.commit()
              if name or gender or specy or email == "":
                  messagebox.showerror("error", "Empty fields not allowed")
              else:
                blank = messagebox.RETRY
                sub = messagebox.showinfo("success","your report is being validated , check the response in your Email account")

              if sub == 1:
                          messagebox.OK

          button = Button(frame_rptstaff, text="Submit", command=submit).place(x=150, y=220)
          staffbase.destroy

          staffbase.mainloop()






def repot():
    response = messagebox.askyesno("reporting","Report")
    if response == 1:


        ok =messagebox.showinfo("report","reporting..." ,command= rpt())
        if ok == True:
            Toplevel(root).destroy()






    if response == 0:
        res =messagebox.askyesno("No report","Are you sure")
        if res == 1:
            messagebox.ABORT
        if res == 0:
           if  response == False:
            messagebox.showwarning("warn","make sure you report!",command=repot())
def repotstaff():
    response = messagebox.askyesno("reporting","Report")
    if response == 1:


        ok =messagebox.showinfo("report","reporting..." ,command= rpt_staff())
        if ok == True:
            Toplevel(root).destroy()






    if response == 0:
        res =messagebox.askyesno("No report","Are you sure")
        if res == 1:
            messagebox.ABORT
        if res == 0:
           if  response == False:
            messagebox.showwarning("warn","make sure you report!",command=rpt_staff())









button1= Button(frame_1,text="Report",width=20, bg='brown', fg='white',command=repot).place(x=40, y=100)

button2= Button(frame_2,text="Report",width=20, bg='brown', fg='white',command=repotstaff).place(x=40, y=100)


















mainloop()
