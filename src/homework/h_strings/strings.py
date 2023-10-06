def get_hamming_distance(dna1, dna2):
    distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            distance +=1
    return distance

def get_dna_complement(dna):
    complemented_dna = ""

    for base in dna[::-1]:
   
        if base == 'A':
            complemented_dna += 'T'

        elif base == 'T':
            complemented_dna += 'A'

        elif base == 'C':
            complemented_dna += 'G'

        else:
            base == 'G'
            complemented_dna += 'C'

    return complemented_dna





#def get_dna_complement(dna):



