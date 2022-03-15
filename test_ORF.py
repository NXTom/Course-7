header = ">sdjlkfdsj33"
sequentie = "ATGATAGATAATGGATAACAGATACAAGTATAGACAATcccTTTAACCAGGA"

listOfOrf = list()
frames = []  # storing the six frame translation that it zould be extacted from the fragments
dna = sequentie  # extract the fragment
description = header  # extact the desciption even were not use it, just for learning purpose
reverseCdna = []  # storing the reverse compliments
listOfFrame = []  # list of frames
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

for i in range(0,len(frames),1): #looping all the frames
    start=0
    while start <len(frames[i]): #looping each frame for stop and stop codons
        if frames[i][start]=="TAA" or frames[i][start]=="TAG" or frames[i][start]=="TGA":
            for stop in range(start+1,len(frames[i]),1):
                         if frames[i][stop]=="TAA" or  frames[i][stop]=="TAG" or  frames[i][stop]=="TGA" :
                                listOfOrf.append(frames[i][start:stop]) # retrieve the orf
                                listOfFrame.append(i)
                                start=stop+1 # avoiding multiple start codons
                                break
        start+=1

print(listOfOrf)

with open("ORF.fa", "w") as file:
    for orf, frame in zip(listOfOrf, listOfFrame):
        seq = ""
        for i in orf:
            seq += i
        file.write(description + " / " + str(frame))
        file.write("\n")
        file.write(seq)
        file.write("\n")
file.close()





