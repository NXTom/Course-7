from Bio.Blast import NCBIWWW


def blastN():
    fasta_string = open("ons_bestand.fasta").read()
    result_handle = NCBIWWW.qblast("blastn", "nt", fasta_string)


def wegSchrijven():
    print("hoi")
