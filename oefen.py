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
    window.configure(bg="#e5e5e5")
    titel = window.title("Blast")

    label = Label(text="Choose file",bg="#3e3e3e",fg="white",font="bold 15").place(relx=0.5, rely=0.015,
                                             anchor="center")

    button = Button(text="file",command=openFile).place(relx=0.5,
                                                        rely=0.05,
                                                        anchor="center")

    label_orf = Label(text="ORFfinder"+(" "*184),font="bold 18",bg="#3e3e3e",fg="white").place(x=30,y=110)
    lb_orf = Label(text="Minimale ORF length (nt)",bg="#e5e5e5").place(x=30,y=150)
    cl0 = IntVar()
    dr0 = OptionMenu(window, cl0, 30,75,150).place(x=200,y=150)

    lb0 = Label(text="BLAST"+(" "*190),font="bold 18",bg="#3e3e3e",fg="white").place(x=30,y=210)

    cl1 = StringVar()
    lb1 = Label(text="Database:",bg="#e5e5e5").place(x=30,y=270, anchor="sw")
    dr1 = OptionMenu(window,cl1,"NR","nog een","nog twee").place(x=120,
                                                                 y=247)
    radio = IntVar()
    lb2 = Label(text="Expected:",bg="#e5e5e5").place(x=30,y=325, anchor="sw")
    ch2 = Radiobutton(text="e-20",variable=radio, value=1).place(x=120,y=302)
    ch2_1 = Radiobutton(text="e-30",variable=radio, value=2).place(x=180,y=302)
    ch2_1 = Radiobutton(text="e-40",variable=radio, value=3).place(x=240, y=302)

    cl3 = IntVar()
    lb3 = Label(text="Word Size:",bg="#e5e5e5").place(x=30,y=375, anchor="sw")
    dr3 = OptionMenu(window,cl3,16,32,128).place(x=120, y=352)

    cl4 = StringVar()
    lb4 = Label(text="Matrix:",bg="#e5e5e5").place(x=30,y=425, anchor="sw")
    dr4 = OptionMenu(window, cl4, "PAM30","PAM70","BLOSUM80","BLOSUM45")\
        .place(x=120, y=402)

    cl5 = StringVar()
    lb5 = Label(text="Organism:",bg="#e5e5e5").place(x=30,y=475, anchor="sw")
    e5 = OptionMenu(window, cl5, "Eukaryote","Prokaryote","Archaea","Yeast","Fungi").place(x=120,y=452)

    cl6 = IntVar()
    lb6 = Label(text="Hitlist lenght:",bg="#e5e5e5").place(x=30,y=525, anchor="sw")
    ch6 = OptionMenu(window,cl6,10,50,100).place(x=120,y=502)

    cl7 = StringVar()
    lb7 = Label(text="MegaBlast:",bg="#e5e5e5").place(x=30,y=575, anchor="sw")
    dr7 = OptionMenu(window,cl7,"TRUE","FALSE").place(x=120,y=552)

    blast_B = Button(window,text="BLAST",bg="#3e3e3e").place(x=50,y=650)

    window.mainloop()
    return cl1,cl3,cl4,cl6,cl7

def get_Para(org):
    print(org)

if __name__ == '__main__':
    # parameters = gui()
    # get_Para()
    gui()