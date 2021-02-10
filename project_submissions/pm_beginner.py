gene1 = "gtgggagacatagtggtcaaggtccccccgagtgtggacgaaaagctggccgatttgatagcaaagactatcgcggagagactgaaaaccctcgcaaggctcaatgagatgctcaagaactccgaactctcagaagaggatgcaatagaactcggacggaaggcgaaaatgggaaggggcgagtaccttgagagaagatattcttctcgtagttaa"
gene2 = "atgagagaagatattcttctcgtagttaacacaaacgtgctattctctttcttcgggaaatcaacagtaaccagagagctcgtgttcttggtatcagggagacttataagtcccgagtttgcactggaagagcttcacgagcacagggacgaagtcctgaaaaaagcaaagatcggagagaaagagttcgaggaaatactgtccgttcttaaagagcatgtcatattcgtaaacgaggggttctacgccgagttcatacctctagcactcgaataa"
gene3 = "atggaagttatccgtctgctgaagagaaagtcccaagacaaggttgagttcgtgcgcgatctggtagttttcatggcttctcccgacgttgatttttccaacgaggttctgtttaaggacgccgttgatgagatatactcaatcctgagggaggaagtcattgaaaatgggaacaaagagctagccagcgcgtatgaaaaagccgttctccttagagctgcggtttttggagaggaaatggatccgaaaaagctccttaagggtattctcgaggagctgaggtga"

def rev_comp(sequence):
    complement_dictionary = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
    rev_complement = "".join(complement_dictionary.get(base, base) for base in reversed(sequence))
    return rev_complement

## write a script to print the sequence of the forward and reverse primers in fasta format.
    ## '\n' will print a new line. You could also stack two print statements on separate lines to separate the fasta header from the sequence.


#gene1
sequence = gene1[0:20]
rev_sequence = gene1[-20:len(gene1)]
final = rev_comp(rev_sequence)
print(">gene1 reverse\n",final)

fwd_sequence = gene1[0:20]
print(">gene1 forward\n",fwd_sequence)

#gene2
fwd_sequence2 = gene2[0:20]
print(">gene2 forward\n",fwd_sequence)

rev_sequence2 = gene2[-20:len(gene2)]
final2 = rev_comp(rev_sequence2)
print(">gene2 reverse\n",final2)

#gene3
fwd_sequence3 = gene3[0:20]
print(">gene3 forward\n",fwd_sequence)

rev_sequence3 = gene3[-20:len(gene3)]
final3 = rev_comp(rev_sequence3)
print(">gene3 reverse\n",final3)
