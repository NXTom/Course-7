from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML
from tkinter import messagebox


def parameters_check_blastn(selection_blast):
    """
    Checks the user given parameters for invalid values.
    :param selection_blast: list - list containing the BLAST parameters
    :return evalue: boolean - if evalue is invalid returns false
            selection_blast: list - returns parameters list with tax id
    """
    evalue = True
    # Looks for invalid e-values and cancels the BLAST
    if selection_blast[1] == "1e-":
        evalue = False
        messagebox.showwarning(title="Error", message="Invalid E-value")
    elif selection_blast[1].split("-")[1].isalpha():
        print(selection_blast[1].isalpha())
        evalue = False
        messagebox.showwarning(title="Error", message="Invalid E-value")
    elif 0 >= float(selection_blast[1]) >= 1:
        evalue = False
        messagebox.showwarning(title="Error", message="Invalid E-value")

    # Changes organism to their corresponding taxid
    if selection_blast[3] == "Eukaryote":
        selection_blast[3] = "txid2759[ORGN]"
    elif selection_blast[3] == "Prokaryote":
        selection_blast[3] = "txid2[ORGN]"
    elif selection_blast[3] == "Archaea":
        selection_blast[3] = "txid2157[ORGN]"
    elif selection_blast[3] == "Yeast":
        selection_blast[3] = "txid4892[ORGN]"
    elif selection_blast[3] == "Fungi":
        selection_blast[3] = "txid4751[ORGN]"

    return evalue, selection_blast


def blastn(selection_blast):
    """
    Calling biopython's BLAST function to BLAST the ORFs
    :param selection_blast: list - list containing the BLAST parameters
    :return: ORF.xml: file - one XML file containing all BLAST results
    """
    sequence_data = open("ORF.fa").read()
    result_handle = NCBIWWW.qblast("blastn", selection_blast[0],
                                   sequence_data,
                                   expect=selection_blast[1],
                                   word_size=selection_blast[2],
                                   entrez_query=selection_blast[3],
                                   hitlist_size=selection_blast[4],
                                   megablast=selection_blast[5])

    # saves the XML in a new Record variable
    blast_records = NCBIXML.parse(result_handle)
    # Writes the information from blast_records to a fasta file
    xml_to_fasta(blast_records)


def xml_to_fasta(blast_records):
    """
    Writes the important information from the BLAST results to a single
    file.
    :param blast_records: Record - variable containing all results from
           the BLAST XML
    """
    with open("ORF_func_anno.fa", "w") as file:
        # Looping through all the records in the XML file
        for blast_record in blast_records:
            counter = 0
            if blast_record.alignments:
                counter = 0
                file.write(blast_record.query + "\n")
                file.write("-" * len(blast_record.query) + "\n")
            # Looping through all the hits in each record
            for alignment in blast_record.alignments:
                counter += 1
                file.write("hit number " + str(counter) + "\n")
                for hsp in alignment.hsps:
                    file.write(
                        "\thit description:" + alignment.title + "\n")
                    file.write(
                        "\tAccession:" + alignment.accession + "\n")
                    file.write(
                        "\tlength:" + str(alignment.length) + "\n")
                    file.write("\te-value:" + str(hsp.expect) + "\n")
                    file.write("\talignment length:" + str(
                        hsp.align_length) + "\n")
                    file.write(
                        "\tpositives:" + str(hsp.positives) + "\n")
                    file.write("\t" + hsp.query[0:] + "\n")
                    file.write("\t" + hsp.match[0:] + "\n")
                    file.write("\t" + hsp.sbjct[0:] + "\n")
                    file.write("\n")


def main_blast(selection_blast):
    """
    Calls the two functions from the BLAST script
    :param selection_blast: list - list containing the BLAST parameters
    """
    evalue, selection_blast = parameters_check_blastn(selection_blast)

    # If the e-value is valid, calls the BLAST function
    if evalue:
        blastn(selection_blast)
