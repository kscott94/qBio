gene1 = "gtgggagacatagtggtcaaggtccccccgagtgtggacgaaaagctggccgatttgatagcaaagactatcgcggagagactgaaaaccctcgcaaggctcaatgagatgctcaagaactccgaactctcagaagaggatgcaatagaactcggacggaaggcgaaaatgggaaggggcgagtaccttgagagaagatattcttctcgtagttaa"
gene2 = "atgagagaagatattcttctcgtagttaacacaaacgtgctattctctttcttcgggaaatcaacagtaaccagagagctcgtgttcttggtatcagggagacttataagtcccgagtttgcactggaagagcttcacgagcacagggacgaagtcctgaaaaaagcaaagatcggagagaaagagttcgaggaaatactgtccgttcttaaagagcatgtcatattcgtaaacgaggggttctacgccgagttcatacctctagcactcgaataa"
gene3 = "atggaagttatccgtctgctgaagagaaagtcccaagacaaggttgagttcgtgcgcgatctggtagttttcatggcttctcccgacgttgatttttccaacgaggttctgtttaaggacgccgttgatgagatatactcaatcctgagggaggaagtcattgaaaatgggaacaaagagctagccagcgcgtatgaaaaagccgttctccttagagctgcggtttttggagaggaaatggatccgaaaaagctccttaagggtattctcgaggagctgaggtga"

def rev_comp(sequence):
    complement_dictionary = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
    rev_complement = "".join(complement_dictionary.get(base, base) for base in reversed(sequence))
    return rev_complement

## write a script to print the sequence of the forward and reverse primers in fasta format.
    ## '\n' will print a new line. You could also stack two print statements on separate lines to separate the fasta header from the sequence.



gene_list = [gene1,gene2,gene3]

gene_number = 1

for gene in gene_list:
    print("Forward primer",number)
    print(gene[:-18:-1])
    print("Reverse primer",number)
    print(rev_comp(gene)[0:18])
    gene_number = gene_number + 1 #add a number to gene_number after each loop to keep track of which gene we are on
