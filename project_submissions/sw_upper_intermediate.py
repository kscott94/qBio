#######################################################################################################################
# Project: design primers for gene1, gene2, and gene3.
    # There are a lot of different ways to do this!
    # If you want a challenge, consider writing a function (def) to design primers
    # If you want even more of a challenge, use a for-loop to iterate over each gene.

gene1 = "gtgggagacatagtggtcaaggtccccccgagtgtggacgaaaagctggccgatttgatagcaaagactatcgcggagagactgaaaaccctcgcaaggctcaatgagatgctcaagaactccgaactctcagaagaggatgcaatagaactcggacggaaggcgaaaatgggaaggggcgagtaccttgagagaagatattcttctcgtagttaa"
gene2 = "atgagagaagatattcttctcgtagttaacacaaacgtgctattctctttcttcgggaaatcaacagtaaccagagagctcgtgttcttggtatcagggagacttataagtcccgagtttgcactggaagagcttcacgagcacagggacgaagtcctgaaaaaagcaaagatcggagagaaagagttcgaggaaatactgtccgttcttaaagagcatgtcatattcgtaaacgaggggttctacgccgagttcatacctctagcactcgaataa"
gene3 = "atggaagttatccgtctgctgaagagaaagtcccaagacaaggttgagttcgtgcgcgatctggtagttttcatggcttctcccgacgttgatttttccaacgaggttctgtttaaggacgccgttgatgagatatactcaatcctgagggaggaagtcattgaaaatgggaacaaagagctagccagcgcgtatgaaaaagccgttctccttagagctgcggtttttggagaggaaatggatccgaaaaagctccttaagggtattctcgaggagctgaggtga"

## Other considerations:
    # Generally, it is good practice for your primers to have a 3' end that ends with "c" or "g", but this is not necessary and might require more advanced skills (if-else statements).
    # Primer sequences are usually between 18 and 21 bp long.
    # If you want to be fancy, consider calculating the melting temperature of each primer. (crudly, the Tm increases ~2 C for each base.)

## Here is a function to reverse complement a sequence. The function is called rev_comp() and takes a string as an argument.
def rev_comp(sequence):
    complement_dictionary = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
    rev_complement = "".join(complement_dictionary.get(base, base) for base in reversed(sequence))
    return rev_complement

## write a script to print the sequence of the forward and reverse primers in fasta format.
    ## '\n' will print a new line. You could also stack two print statements on separate lines to separate the fasta header from the sequence.

def primers(gene):
    fwd = gene[0:20]
    rev = rev_comp(gene)[0:20]
    fwd_Tm = len(fwd)*2
    rev_Tm = len(rev)*2
    F = ">fwd, Tm " + str(fwd_Tm) + "˚C\n" + fwd + '\n' + ">rev, Tm" + str(rev_Tm) + "˚C\n" + rev
    return F

print("Gene1\n", primers(gene1))
print("Gene2\n", primers(gene2))
print("Gene3\n", primers(gene3))
