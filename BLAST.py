from Bio.Blast import NCBIWWW
from time import sleep


# def read_orf(file):
#     """
#     Reads and places the ORFs from the ORF-finder generated file in a list.
#
#             Parameters:
#                     file (file): File containing ORFs generated with the ORF-finder class
#
#             Returns:
#                     orf_list (list): A list containing all the ORFs from the ORF-file
#     """
#     seq = ""
#     orf_headers, orf_seqs = [], []
#
#     with open(file) as file:
#         for line in file:
#             if line.startswith(">"):
#                 if seq == "":
#                     header = line.strip()
#                 else:
#                     headers.append(header)
#                     seqs.append(seq)
#                     header = line.strip()
#                     seq = ""
#             else:
#                 seq += line.strip()
#         seqs.append(seq)
#
#     return orf_headers, orf_seqs
#
#
# def parameters_check_blastn(parameters):
#     """
#     Checks the user given parameters for invalid values.
#
#             Parameters:
#                     parameters (list): A list of all adjustable parameters,
#
#             Returns:
#     """
#     # afhankelijk van hoe parameters doorgegeven worden.


def blastn():
    """
    BLASTs the ORFs

            Parameters:
                    seqs (list): List of ORF sequences

            Returns:

    """
    sequence_data = open("orf__all.fa").read()
    result_handle = NCBIWWW.qblast("blastp", "refseq_protein", sequence_data, entrez_query="txid4892[ORGN]", hitlist_size=10)

    #with open("ORF_XML/ORF%s.xml" % i, "w") as out_handle:
    with open("ORF_XML/ORF.xml", "w") as out_handle:
        out_handle.write(result_handle.read())
    result_handle.close()

    print("klaar")


if __name__ == "__main__":
    #orf_file = "ORF__all.fa"

    #headers, seqs = read_orf(orf_file)
    #parameters_check_blastn(parameters)
    blastn()
