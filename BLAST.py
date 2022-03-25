from Bio.Blast import NCBIWWW


def parameters_check_blastn(selection_BLAST):
    """
    Checks the user given parameters for invalid values.

            Parameters:
                    selection_BLAST (list): A list of all adjustable parameters

            Returns:
                    selection_BLAST (list): A list of BLAST parameters
    """
    evalue = True
    # expect: afhankelijk van hoe e-value wordt meegegeven vanuit GUI
    if selection_BLAST[1] != int:
        evalue = False
    elif 0 >= float(selection_BLAST[1]) >= 1:
        evalue = False

    # organism adjustments
    if selection_BLAST[3] == "Eukaryote":
        selection_BLAST[3] = "txid2759[ORGN]"
    elif selection_BLAST[3] == "Prokaryote":
        selection_BLAST[3] = "txid2[ORGN]"
    elif selection_BLAST[3] == "Archaea":
        selection_BLAST[3] = "txid2157[ORGN]"
    elif selection_BLAST[3] == "Yeast":
        selection_BLAST[3] = "txid4892[ORGN]"
    elif selection_BLAST[3] == "Fungi":
        selection_BLAST[3] = "txid4751[ORGN]"

    return evalue, selection_BLAST


def blastn(selection_BLAST):
    """
    BLASTs the ORFs
            Parameters:
                    selection_BLAST (list): List of BLAST parameters
            Returns:
                    ORF.xml (file): one XML file with all BLAST results
    """
    sequence_data = open("ORF.fa").read()
    result_handle = NCBIWWW.qblast("blastn", selection_BLAST[0],
                                   sequence_data,
                                   expect=selection_BLAST[1],
                                   word_size=selection_BLAST[2],
                                   # matrix_name=selection_BLAST[3],
                                   entrez_query=selection_BLAST[3],
                                   hitlist_size=selection_BLAST[4],
                                   megablast=selection_BLAST[5])

    with open("ORF_XML/ORF.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

    print("The BLAST has finished")


def main_blast(selection_BLAST):
    evalue, selection_BLAST = parameters_check_blastn(selection_BLAST)

    if evalue:
        blastn(selection_BLAST)
