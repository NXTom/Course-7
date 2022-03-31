import BLAST
import test_ORF


def maintest(bestand, ORF_par, BLAST_par):
    """
    Haalt alle benodigde parameters en variabelen op uit de GUI
    Deze worden daarna verwerkt in ORF finder
    De resultaten hieruit zijn voor de blast functie.
    De blast functie slaat uiteindelijk alle resultaten op.
    """
    test_ORF.main_ORF(bestand, ORF_par)
    BLAST.main_blast(BLAST_par)