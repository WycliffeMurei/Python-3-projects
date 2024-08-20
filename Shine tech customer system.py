import collections
import pickle
from functools import partial
from tkinter import *
from tkinter import messagebox

splash_Frame = Tk()
splash_Frame.geometry('300x200')
splash_Frame.eval('tk::PlaceWindow . center')

splash_Frame.overrideredirect(True)
splash_Frame.title("shine Tech customers system")
splash_Frame.configure(bg="violet")
splash_Frame =Label(splash_Frame,text="SHINE TECH MIS",font=("aerial back",18))
splash_Frame.pack(pady=20)




def add_contact_Window(self,master, customer_list, key):
    splash_Frame.destroy()
    Frame = Tk()
    Frame.geometry("600x450")
    Frame.title("sunshine database system")
    Frame.configure(bg="pink")
    labl_0 = Label(Frame, text="Shine tech customers system", width=20, font=("bold", 10))
    labl_0.place(x=68, y=130)


    self.master = master
    self.customer_list = customer_list



class crudmain:
    def _init_(self, master, cust):
        self.master = master
        self.customer_list = cust
        self.cust_frame = Frame(self.master)
        frame = Frame(self.master)
        Frame.master.title("contact list editor")
        self.label_1 = Label(frame, text='contact list').pack(side=LEFT)
        self.labl_0.place(x=68, y=130)
        self.update_customer()
        self.add_button = Button(frame, text="add contact", command=self.add_contact_window)
        self.add_button.pack(anchor='sw')
        frame.pack(anchor='nw')
        self.cust_frame.pack(anchor='w')

    def update_customer(self):
        for widget in self.cust_frame.winfo_children():
            widget.destroy()

            r = 0
            for key in self.customer_list:
                Button(self.cust_frame, text=key, command=partial(self.cust_info, key)).grid(row=1, column=r)
                r += 1

    def add_contact_window(self, master, customer_list, key):
        add_contact_Window(self.master, self.customer_list, key)

    def custinfo(self, key, root=None):
        self.custinfo(self.master, self.customer_list, key)

        class CustInfo:
            def __init__(self):
                self.info_window = None

            def _init_(self, master, cust, info_window, key):
                self.master = master
                self.cust = cust[key]
                self.info_window.title("contact information")
                Label(self.info_window, text=self.cust["first name"]).pack()
                Label(self.info_window, text=self.cust["last  name"]).pack()
                Label(self.info_window, text=self.cust["email"]).pack()
                Label(self.info_window, text=self.cust["adress"]).pack()
                Label(self.info_window, text=self.cust["phone"]).pack()

                Button(self.info_window, text="close", ).pack(anchor='s')

        class Addwindow:
            def _init_(self, master, main_window, cust):
                self.master = master
                self.cust = cust
                self.main_window = main_window
                self.add_window = Toplevel()
                self.add_window.title("Add contact")
                Label(self.add_window, text="First name").grid(row=0, column=0).place(x=250, y=130)
                Label(self.add_window, text="last name").grid(row=1, column=0).place(x=250, y=130)
                Label(self.add_window, text="Email Adress").grid(row=2, column=0).place(x=250, y=130)
                Label(self.add_window, text="living adree").grid(row=3, column=0).place(x=250, y=130)
                Label(self.add_window, text="phone number").grid(row=4, column=0).place(x=250, y=130)
                self.first_name() == StringVar()
                self.last_name() == StringVar()
                self.email() == StringVar()
                self.adress() == StringVar()
                self.phone() == StringVar()
                Button(self.add_window, text="submit", command=lambda: self.save(self.cust)).grid(row=5,
                                                                                                  column=0).place(x=250,
                                                                                                                  y=130)
                Button(self.add_window, text="cancel", command=lambda: self.add_window.destroy()).grid(row=6,
                                                                                                       column=0).place(
                    x=250, y=130)
                Entry(self.add_window, textvariable=self.first_name).grid(row=0, column=1).place(x=250, y=130)
                Entry(self.add_window, textvariable=self.last_name).grid(row=1, column=1).place(x=250, y=130)
                Entry(self.add_window, textvariable=self.email).grid(row=2, column=1).place(x=250, y=130)
                Entry(self.add_window, textvariable=self.adress).grid(row=3, column=1).place(x=250, y=130)
                Entry(self.add_window, textvariable=self.phone).grid(row=4, column=1).place(x=250, y=130)

            def save(self, customers, ):
                first_name = str(self.first_name.get())
                last_name = str(self.last_name.get())
                email = str(self.email.get())
                adress = str(self.adress.get())
                phone = str(self.phone.get())
                save = {'first_name': self.first_name, 'last_name': self.last_name, 'email': self.email,
                        'adress:': self.adress, 'phone:': self.phone}
                key = save['fist_name':first_name]
                key = save['last_name':last_name]
                key = save['email':email]
                key = save['adress':adress]
                key = save['phone':phone]
                customers[key] = save
                pickle.dump(customers, open('customer_file.dat', 'wb'))
                messagebox.showinfo("status", "information saved successfully!")
                self.add_window.destroy()
                self.main_window.update_customers()

            def main(self):
                try:
                    input_file = open("customer_file.dat", "rb")
                    customers = pickle.load(input_file)
                except (FileNotFoundError, IOError):
                    customers = collections.OrderedDict()



splash_Frame.after(5000,add_contact_Window)
mainloop()

