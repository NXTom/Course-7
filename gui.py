from tkinter import *
from tkinter import filedialog


def openFile():
    """
    Opens a chosen file based on the filepath
    :return: filepath
    """
    filepath = filedialog.askopenfilename(
        initialdir="/Users/ozlemseyrani/desktop")
    file = open(filepath, "r")
    print(file.read())
    print(filepath)
    file.close()
    return filepath


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
    lb_orf = Label(text="Minimale ORF length (nt)", bg="#e5e5e5") \
        .place(x=30, y=150)
    dr0 = OptionMenu(window, cl0, 30, 75, 150).place(x=200, y=150)

    # DropdownMenu for the Databases
    global cl1
    cl1 = StringVar()
    lb1 = Label(text="Database:", bg="#e5e5e5").place(x=30, y=270,
                                                      anchor="sw")
    dr1 = OptionMenu(window, cl1, "NR", "refseq_select", "PDB") \
        .place(x=120, y=247)

    # RadioButtons for Expected E value
    global radio
    radio = IntVar()
    lb2 = Label(text="Expected:", bg="#e5e5e5").place(x=30, y=325,
                                                      anchor="sw")
    ch2 = Radiobutton(text="e-20", variable=radio, value=20) \
        .place(x=120, y=302)
    ch2_1 = Radiobutton(text="e-30", variable=radio, value=30) \
        .place(x=180, y=302)
    ch2_1 = Radiobutton(text="e-40", variable=radio, value=40) \
        .place(x=240, y=302)

    # DropdownMenu for the Word size.
    global cl3
    cl3 = IntVar()
    lb3 = Label(text="Word Size:", bg="#e5e5e5").place(x=30, y=375,
                                                       anchor="sw")
    dr3 = OptionMenu(window, cl3, 16, 32, 128).place(x=120, y=352)

    # DropdownMenu for the wanted Blast Matrix
    global cl4
    cl4 = StringVar()
    lb4 = Label(text="Matrix:", bg="#e5e5e5").place(x=30, y=425,
                                                    anchor="sw")
    dr4 = OptionMenu(window, cl4, "PAM30", "PAM70", "BLOSUM80",
                     "BLOSUM45").place(x=120, y=402)

    # DropdownMenu for the organism name/taxID
    global cl5
    cl5 = StringVar()
    lb5 = Label(text="Organism:", bg="#e5e5e5").place(x=30, y=475,
                                                      anchor="sw")
    e5 = OptionMenu(window, cl5, "Eukaryote", "Prokaryote", "Archaea",
                    "Yeast", "Fungi").place(x=120, y=452)

    # DropdownMenu for the hitlist length
    global cl6
    cl6 = IntVar()
    lb6 = Label(text="Hitlist length:", bg="#e5e5e5").place(x=30, y=525,
                                                            anchor="sw")
    ch6 = OptionMenu(window, cl6, 10, 50, 100).place(x=120, y=502)

    # DropdownMenu for MegaBlast options
    global cl7
    cl7 = StringVar()
    lb7 = Label(text="MegaBlast:", bg="#e5e5e5").place(x=30, y=575,
                                                       anchor="sw")
    dr7 = OptionMenu(window, cl7, "TRUE", "FALSE").place(x=120, y=552)

    blast_B = Button(window, text="BLAST", bg="#15616d", fg="white",
                     font="bold 30", command=get_Para).place(x=750,
                                                             y=650)

    window.mainloop()
    # Returning all the BLAST parameters
    return cl0, cl1, radio, cl3, cl4, cl6, cl7


def get_Para():
    """
    Gets all the given parameters and puts them in seperated Lists
    :return: selection_BLAST, selection_ORF
    """
    # List for the ORF parameter
    selection_ORF = []
    selection_ORF.append(cl0.get())

    # List for the BLAST parameters
    selection_BLAST = []
    selection_BLAST.append(cl1.get())
    selection_BLAST.append(radio.get())
    selection_BLAST.append(cl3.get())
    selection_BLAST.append(cl4.get())
    selection_BLAST.append(cl5.get())
    selection_BLAST.append(cl6.get())
    selection_BLAST.append(cl7.get())

    print(selection_ORF)
    print(selection_BLAST)
    return selection_BLAST, selection_ORF


if __name__ == '__main__':
    gui()
    bestand = openFile
    print(bestand)
