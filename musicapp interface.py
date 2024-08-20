from tkinter import*
from tkinter import messagebox
from tkinter import PhotoImage
root = Tk()
root.configure(bg="maroon")
root.geometry('100x100')
root.resizable(False,False)
root.eval('tk::PlaceWindow . center')
root.overrideredirect(True)
#photo=PhotoImage(file="Screenshot_20230611-210849_Computer Launcher.jpg")
#root.iconphoto(False,photo)
root.title("dunda beat")
root =Label(root,text="NDUNDA BEAT",font=("Helvitica",6 ))
root.pack(pady=20)



def main_window():
    root.destroy()

    base = Tk()

    base.geometry('350x500')
    base.configure(bg="grey")
    base.title("Dunda beat play")
    base.resizable(False, False)
    frame_1 = Frame(root,bg="blue" ,width=340,height=100)
    frame_1.place(x=0,y=400)

root.after(3000,main_window)
mainloop()


