def read_Scaffold(file_scaffold):
    """
    Reads in a FASTA-file containing a scaffold.
    :param file_scaffold: String - file name
    :return: scaf_header - String - header of scaffold
             scaf_seq - String - sequence of scaffold
    """
    scaf_header = "" # instantiates String scaf_header
    scaf_seq = ""      # instantiates String scaf_seq
    with open(file_scaffold, "r") as scaf_file:
        for line in scaf_file:
            if line.startswith(">"):
                scaf_header = line.strip()
            else:
                scaf_seq = scaf_seq.upper() # Sets sequence in uppercase
                scaf_seq += line.strip()

    return scaf_header, scaf_seq

def Frame_finder(scaf_header, scaf_seq):
    """
    Storing the six frame translation that it should be extacted from the fragments.
    :param scaf_header: String - header of scaffold
    :param scaf_seq:  String - sequence of scaffold
    :return: frames: list - storing the six frame translation
             description -  String header of scaffold
    """
    frames = []  # storing the six frame translation that it should be extacted from the fragments
    dna = scaf_seq  # extract the fragment
    description = scaf_header # extact the desciption
    reverseCdna = []  # storing the reverse compliments
    # create the positive frames
    # split the frames into codons for better performance
    frames.append([dna[i:i + 3] for i in range(0, len(dna), 3)])
    frames.append([dna[i:i + 3] for i in range(1, len(dna), 3)])
    frames.append([dna[i:i + 3] for i in range(2, len(dna), 3)])
    # reverse compliment of the fragment
    reverse = {"A": "T", "C": "G", "T": "A", "G": "C"}
    for i in range(len(dna)):
        reverseCdna.append(reverse[dna[-i - 1]]) if dna[-i - 1] in reverse.keys() else reverseCdna.append(
            dna[-i - 1])  # if any contamination found we keep it for further more check
    reverseCdna = ''.join(reverseCdna)  # joining
    # create the negative frames
    frames.append([reverseCdna[i:i + 3] for i in range(0, len(reverseCdna), 3)])
    frames.append([reverseCdna[i:i + 3] for i in range(1, len(reverseCdna), 3)])
    frames.append([reverseCdna[i:i + 3] for i in range(2, len(reverseCdna), 3)])

    return frames, description

def get_par_ORF(ORF_par):
    for i in ORF_par:
        min_length = i
        if min_length != 75:
            min_lenth = min_length
        else:
            min_length = 75
    return min_length

def ORF_finder(frames, min_length):
    """
    Looping over all frames and looking for ORFs from stop to stop codons. The ORFs found were
    stored into the list listOfOrf.
    :param frames: list - storing the six frame translation.
    :return: listOfOrf - list - storing the ORFs found.
             listOfFrame - list - storing the used reading frames for each ORF.
    """
    listOfOrf = list()
    listOfFrame = []  # list of frames
    for i in range(0,len(frames),1): #looping all the frames
        start=0
        while start <len(frames[i]): #looping each frame for stop and stop codons
            if frames[i][start]=="TAA" or frames[i][start]=="TAG" or frames[i][start]=="TGA":
                for stop in range(start+1,len(frames[i]),1):
                             if frames[i][stop]=="TAA" or  frames[i][stop]=="TAG" or  frames[i][stop]=="TGA" :
                                 if (len(frames[i][start:stop])*3) >= min_length: # filters on minimal length
                                    listOfOrf.append(frames[i][start:stop]) # retrieve the orf
                                    listOfFrame.append(i) # retrieve reading frame
                                 start=stop+1 # avoiding multiple start codons
                                 break
            start+=1
    return listOfOrf, listOfFrame


def Write_Orf_Fasta(listOfOrf, listOfFrame, description):
    """
    Writes all found ORF to a file.
    :param listOfOrf: list - storing the ORFs found.
    :param listOfFrame: list - storing the used reading frames for each ORF.
    :param description: String header of scaffold
    :return:
    """
    counter = 0
    with open("ORF.fa", "w") as file:
        for orf, frame in zip(listOfOrf, listOfFrame):
            counter += 1
            seq = ""
            for i in orf:
                seq += i

            file.write(description + "+" + str(counter) + " / " + str(frame))
            file.write("\n")
            file.write(seq)
            file.write("\n")
            seq = ""
    file.close()

def main_ORF(bestand, ORF_par):
    scaf_header, scaf_seq = read_Scaffold(file_scaffold= bestand)
    frames, description = Frame_finder(scaf_header, scaf_seq)
    min_length = get_par_ORF(ORF_par)
    listOfOrf, listOfFrame = ORF_finder(frames, min_length)
    Write_Orf_Fasta(listOfOrf, listOfFrame, description)








