genomic_dna = open("genomic_dna.txt").read()

exons = open("exons.txt")

coding_sequence = ""

for line in exons:

    pos = line.split(',')

    start = int(pos[0])
    stop = int(pos[1])

    exon = genomic_dna[start:stop]

    coding_sequence = coding_sequence + exon

output = open("coding_sequence.txt", "w")
output.write(coding_sequence)
output.close()
