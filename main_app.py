import BLAST
import test_ORF


def maintest(bestand, ORF_par, BLAST_par):
   test_ORF.main_ORF(bestand, ORF_par)
   print(ORF_par)
   print(BLAST_par)
   #BLAST.main_blast()
   #print("doie")


if __name__ == '__main__':
    main()