from Bio.Blast import NCBIWWW
from Bio.Blast import NCBIXML


def parameters_check_blastn(selection_BLAST):
    """
    Checks the user given parameters for invalid values.
    :param selection_BLAST: list - list containing the BLAST parameters
    :return evalue: boolean - if evalue is invalid returns false
            selection_BLAST: list - returns parameters list with tax id
    """
    evalue = True
    # expect: afhankelijk van hoe e-value wordt meegegeven vanuit GUI
    if selection_BLAST[1] == "1e-":
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
    Calling biopython's BLAST function to BLAST the ORFs
    :param selection_BLAST: list - list containing the BLAST parameters
    :return: ORF.xml: file - one XML file containing all BLAST results
    """
    sequence_data = open("ORF.fa").read()
    result_handle = NCBIWWW.qblast("blastn", selection_BLAST[0],
                                   sequence_data,
                                   expect=selection_BLAST[1],
                                   word_size=selection_BLAST[2],
                                   entrez_query=selection_BLAST[3],
                                   hitlist_size=selection_BLAST[4],
                                   megablast=selection_BLAST[5])

    blast_records = NCBIXML.parse(result_handle)
    xml_to_fasta(blast_records)

    # with open("ORF.xml", "w") as out_handle:
    #     out_handle.write(result_handle.read())
    # result_handle.close()


def xml_to_fasta(blast_records):
    with open("ORF_func_anno.fa", "w") as file:
        for blast_record in blast_records:
            counter = 0
            if blast_record.alignments:
                counter = 0
                file.write(blast_record.query + "\n")
                file.write("-" * len(blast_record.query) + "\n")
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




def main_blast(selection_BLAST):
    """
    Calls the two functions from the BLAST script
    :param selection_BLAST: list - list containing the BLAST parameters
    """
    evalue, selection_BLAST = parameters_check_blastn(selection_BLAST)

    if evalue:
        blastn(selection_BLAST)
