import BLAST
import ORF


def maintest(bestand, orf_par, blast_par):
    """
    Haalt alle benodigde parameters en variabelen op uit de GUI
    Deze worden daarna verwerkt in ORF finder
    De resultaten hieruit zijn voor de blast functie.
    De blast functie slaat uiteindelijk alle resultaten op.
    """
    ORF.main_orf(bestand, orf_par)
    BLAST.main_blast(blast_par)