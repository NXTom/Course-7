from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import main_app


def openFile():
    """
    Opens a chosen file based on the filepath
    :return: filepath
    """
    global filepath
    filepath = filedialog.askopenfilename()
    file = open(filepath, "r")
    file.close()


def gui():
    """
    GUI, made for getting the all the paramaters. Used for BLAST and ORF
    :return: cl0, cl1, radio, cl3, cl4, cl6, cl7
    """
    window = Tk()
    window.geometry('1000x1000')
    window.configure(bg="#e5e5e5")
    titel = window.title("Blast")

    # Makes label and button for the GUI
    label = Label(text="Choose file", bg="#3e3e3e", fg="white",
                  font="bold 15").place(relx=0.5, rely=0.015,
                                        anchor="center")

    button = Button(text="file", command=openFile).place(relx=0.5,
                                                         rely=0.05,
                                                         anchor="center")

    # labels for structure in the GUI
    label_orf = Label(text="ORFfinder" + (" " * 184), font="bold 18",
                      bg="#3e3e3e", fg="white").place(x=30, y=110)

    lb0 = Label(text="BLAST" + (" " * 190), font="bold 18",
                bg="#3e3e3e", fg="white").place(x=30, y=210)

    # visualized option menu for the BLAST parameters
    # DropdownMenu and Label for ORF min Length
    global cl0
    cl0 = IntVar()
    cl0.set(150)
    lb_orf = Label(text="Minimale ORF length (nt)", bg="#e5e5e5") \
        .place(x=30, y=150)
    dr0 = OptionMenu(window, cl0, 30, 75, 150).place(x=200, y=150)

    # DropdownMenu for the Databases
    global cl1
    cl1 = StringVar()
    cl1.set("nr")
    lb1 = Label(text="Database:", bg="#e5e5e5").place(x=30, y=270,
                                                      anchor="sw")
    dr1 = OptionMenu(window, cl1, "nr", "refseq_select", "PDB") \
        .place(x=120, y=247)

    # Entry for Expected E value
    lb2 = Label(text="Expected:       1e-", bg="#e5e5e5").place(x=30,
                                                                y=325,
                                                                anchor="sw")
    global entry1
    entry1 = Entry(window)
    entry1.place(x=150, y=300)

    # DropdownMenu for the Word size.
    global cl3
    cl3 = IntVar()
    cl3.set(32)
    lb3 = Label(text="Word Size:", bg="#e5e5e5").place(x=30, y=375,
                                                       anchor="sw")
    dr3 = OptionMenu(window, cl3, 16, 32, 128).place(x=120, y=352)

    # DropdownMenu for the organism name/taxID
    global cl5
    cl5 = StringVar()
    cl5.set("Eukaryote")
    lb5 = Label(text="Organism:", bg="#e5e5e5").place(x=30, y=425,
                                                      anchor="sw")
    e5 = OptionMenu(window, cl5, "Eukaryote", "Prokaryote", "Archaea",
                    "Yeast", "Fungi").place(x=120, y=402)

    # DropdownMenu for the hitlist length
    global cl6
    cl6 = IntVar()
    cl6.set(10)
    lb6 = Label(text="Hitlist length:", bg="#e5e5e5").place(x=30, y=475,
                                                            anchor="sw")
    ch6 = OptionMenu(window, cl6, 10, 50, 100).place(x=120, y=452)

    # DropdownMenu for MegaBlast options
    global cl7
    cl7 = StringVar()
    cl7.set(True)
    lb7 = Label(text="MegaBlast:", bg="#e5e5e5").place(x=30, y=525,
                                                       anchor="sw")
    dr7 = OptionMenu(window, cl7, "True", "False").place(x=120, y=502)

    blast_b = Button(window, text="BLAST", bg="#e5e5e5", fg="white",
                     font="bold 30", highlightbackground="#3e3e3e",
                     command=get_Para).place(x=750, y=650)

    window.mainloop()
    # Returning all the BLAST parameters
    return cl0, cl1, cl3, cl6, cl7


def get_Para():
    """
    Gets all the given parameters and puts them in seperated Lists
    :return: selection_blast, selection_orf
    """
    # List for the ORF parameter
    selection_orf = [cl0.get()]

    # List for the BLAST parameters
    selection_blast = [cl1.get(), "1e-" + entry1.get(), cl3.get(), cl5.get(),
                       cl6.get(), cl7.get()]
    messagebox.showinfo(title="Runtime update", message="Blast has started")
    main_app.maintest(filepath, selection_orf, selection_blast)
    return selection_blast, selection_orf


if __name__ == '__main__':
    gui()
    bestand = openFile
