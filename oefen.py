from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="/Users/ozlemseyrani/desktop",
                                          title="Open file okay?")

    file = open(filepath,'r')
    print(file.read())
    file.close()


def gui():
    window = Tk()
    window.geometry('1000x1000')
    # window.configure(bg="#e5e5e5")
    titel = window.title("Blast")

    label = Label(text="Choose file:").place(relx=0.5, rely=0.01,
                                             anchor="center")

    button = Button(text="file",command=openFile).place(relx=0.5,
                                                        rely=0.03,

                                                        anchor="center")
    canvas = Canvas(window)
    # canvas.pack()
    canvas.config(width=300,height=20)

    line=canvas.create_line(10,10,10,10,fill="black",width=20)


    cl1 = StringVar()
    lb1 = Label(text="Database:").place(x=30,y=170, anchor="sw")
    dr1 = OptionMenu(window,cl1,"NR","nog een","nog twee").place(x=120,
                                                                 y=147)

    lb2 = Label(text="Expected:").place(x=30,y=225, anchor="sw")
    ch2 = Checkbutton(text="e-20").place(x=120,y=202)
    ch2_1 = Checkbutton(text="e-30").place(x=180,y=202)
    ch2_1 = Checkbutton(text="e-40").place(x=240, y=202)

    cl3 = IntVar()
    lb3 = Label(text="Word Size:").place(x=30,y=275, anchor="sw")
    dr3 = OptionMenu(window,cl3,2,3,6).place(x=120, y=252)

    cl4 = StringVar()
    lb4 = Label(text="Matrix:").place(x=30,y=325, anchor="sw")
    dr4 = OptionMenu(window, cl4, "PAM30","PAM70","BLOSUM80","BLOSUM45")\
        .place(x=120, y=302)

    lb5 = Label(text="Organism:").place(x=30,y=375, anchor="sw")
    e5 = Entry().place(x=120,y=352)

    cl6 = IntVar()
    lb6 = Label(text="Hitlist lenght:").place(x=30,y=425, anchor="sw")
    ch6 = Checkbutton(text="").place(x=120,y=402)

    cl7 = StringVar()
    lb7 = Label(text="MegaBlast:").place(x=30,y=475, anchor="sw")
    dr7 = OptionMenu(window,cl7,"TRUE","FALSE").place(x=120,y=452)

    blast_B = Button(text="BLAST").place(x=50,y=550)

    window.mainloop()
    return cl1,cl3,cl4,cl6,cl7

def get_Para(org):
    print(org)

if __name__ == '__main__':
    # parameters = gui()
    # get_Para()
    gui()