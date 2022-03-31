def read_scaffold(file_scaffold):
    """
    Reads in a FASTA-file containing a scaffold.
    :param file_scaffold: String - file name
    :return: scaf_header - String - header of scaffold
             scaf_seq - String - sequence of scaffold
    """
    scaf_header = ""  # instantiates String scaf_header
    scaf_seq = ""  # instantiates String scaf_seq
    with open(file_scaffold, "r") as scaf_file:
        for line in scaf_file:
            if line.startswith(">"):
                scaf_header = line.strip()
            else:
                scaf_seq = scaf_seq.upper()  # Sets sequence in uppercase
                scaf_seq += line.strip()

    return scaf_header, scaf_seq


def frame_finder(scaf_header, scaf_seq):
    """
    Storing the six frame translation that it should be
    extacted from the fragments.
    :param scaf_header: String - header of scaffold
    :param scaf_seq:  String - sequence of scaffold
    :return: frames: list - storing the six frame translation
             header -  String header of scaffold
    """
    rf = []  # storing the six frame translation that it should be
    # extacted from the fragments
    dna = scaf_seq  # extract the fragment
    header = scaf_header  # extact the desciption
    r_cdna = []  # storing the reverse compliments
    # create the positive frames
    # split the frames into codons for better performance
    rf.append([dna[i:i + 3] for i in range(0, len(dna), 3)])
    rf.append([dna[i:i + 3] for i in range(1, len(dna), 3)])
    rf.append([dna[i:i + 3] for i in range(2, len(dna), 3)])
    # reverse compliment of the fragment
    reverse = {"A": "T", "C": "G", "T": "A", "G": "C"}
    for i in range(len(dna)):
        r_cdna.append(reverse[dna[-i - 1]]) if dna[-i - 1] in reverse.keys()\
            else r_cdna.append(dna[-i - 1])
        # if any contamination found we keep it for further checks
    r_cdna = ''.join(r_cdna)  # joining
    # create the negative frames
    rf.append([r_cdna[i:i + 3] for i in range(0, len(r_cdna), 3)])
    rf.append([r_cdna[i:i + 3] for i in range(1, len(r_cdna), 3)])
    rf.append([r_cdna[i:i + 3] for i in range(2, len(r_cdna), 3)])

    return rf, header


def get_par_orf(orf_par):
    for i in orf_par:
        min_length = i
        if min_length != 75:
            break
        else:
            min_length = 75
    return min_length


def orf_finder(frames, min_length):
    """
    Looping over all frames and looking for ORFs from stop to stop codons. The
    ORFs found were stored into the list list_of_orf.
    :param frames: list - storing the six frame translation.
    :return: list_of_orf - list - storing the ORFs found.
             list_of_frame - list - storing the used reading frames for each
             ORF.
    """
    list_of_orf = list()
    list_of_frame = []  # list of frames
    for i in range(0, len(frames), 1):  # looping all the frames
        start = 0
        while start < len(frames[i]):  # looping each frame for stop and stop
            # codons
            if frames[i][start] == "TAA" or frames[i][start] == "TAG" \
                    or frames[i][start] == "TGA":
                for stop in range(start + 1, len(frames[i]), 1):
                    if frames[i][stop] == "TAA" or frames[i][stop] == \
                            "TAG" or \
                            frames[i][stop] == "TGA":
                        if (len(frames[i][start:stop]) * 3) >= min_length:
                            # filters on minimal length
                            list_of_orf.append(frames[i][start:stop])
                            # retrieve the orf
                            list_of_frame.append(i)  # retrieve reading frame
                        start = stop + 1  # avoiding multiple start codons
                        break
            start += 1
    return list_of_orf, list_of_frame


def Write_Orf_Fasta(list_of_orf, list_of_frame, description):
    """
    Writes all found ORF to a file.
    :param list_of_orf: list - storing the ORFs found.
    :param list_of_frame: list - storing the used reading frames for each ORF.
    :param description: String header of scaffold
    :return:
    """
    counter = 0
    with open("ORF.fa", "w") as file:
        for orf, frame in zip(list_of_orf, list_of_frame):
            counter += 1
            seq = ""
            for i in orf:
                seq += i

            file.write(description + "+" + str(counter) + " / " + str(frame))
            file.write("\n")
            file.write(seq)
            file.write("\n")
    file.close()


def main_orf(bestand, orf_par):
    scaf_header, scaf_seq = read_scaffold(file_scaffold=bestand)
    frames, description = frame_finder(scaf_header, scaf_seq)
    min_length = get_par_orf(orf_par)
    list_of_orf, list_of_frame = orf_finder(frames, min_length)
    Write_Orf_Fasta(list_of_orf, list_of_frame, description)
