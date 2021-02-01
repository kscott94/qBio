#######################################################################################################################
## Project: design primers for gene1, gene2, and gene3.
    ## There are a lot of different ways to do this!
    ## If you want a challenge, consider writing a function (def) to design primers
    ## If you want even more of a challenge, use a for-loop to iterate over each gene.

gene1 = "gtgggagacatagtggtcaaggtccccccgagtgtggacgaaaagctggccgatttgatagcaaagactatcgcggagagactgaaaaccctcgcaaggctcaatgagatgctcaagaactccgaactctcagaagaggatgcaatagaactcggacggaaggcgaaaatgggaaggggcgagtaccttgagagaagatattcttctcgtagttaa"
gene2 = "atgagagaagatattcttctcgtagttaacacaaacgtgctattctctttcttcgggaaatcaacagtaaccagagagctcgtgttcttggtatcagggagacttataagtcccgagtttgcactggaagagcttcacgagcacagggacgaagtcctgaaaaaagcaaagatcggagagaaagagttcgaggaaatactgtccgttcttaaagagcatgtcatattcgtaaacgaggggttctacgccgagttcatacctctagcactcgaataa"
gene3 = "atggaagttatccgtctgctgaagagaaagtcccaagacaaggttgagttcgtgcgcgatctggtagttttcatggcttctcccgacgttgatttttccaacgaggttctgtttaaggacgccgttgatgagatatactcaatcctgagggaggaagtcattgaaaatgggaacaaagagctagccagcgcgtatgaaaaagccgttctccttagagctgcggtttttggagaggaaatggatccgaaaaagctccttaagggtattctcgaggagctgaggtga"

## Other considerations:
    ## Generally, it is good practice for your primers to have a 3' end that ends with "c" or "g", but this is not necessary and might require more advanced skills (if-else statements).
    ## Primer sequences are usually between 18 and 21 bp long.
    ## If you want to be fancy, consider calculating the melting temperature of each primer. (crudly, the Tm increases ~2 C for each base.)

## Here is a function to reverse compliment a sequence. The function is called rev_comp() and takes a string as an argument.
def rev_comp(sequenec):
    complement_dictionary = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
    rev_complement = "".join(complement_dictionary.get(base, base) for base in reversed(sequenec))
    return rev_complement

## write a script to print the sequence of the forward and reverse primers in fasta format.
    ## '\n' will print a new line. You could also stack two print statements on separate lines to separate the fasta header from the sequence.

gene1_F = gene1[0:20]
gene1_R = rev_comp(gene1[-20:len(gene1)])
print(">gene1_F\n", gene1_F)
print(">gene1_R\n", gene1_R)


gene2_F = gene2[0:20]
gene2_R = rev_comp(gene2[-20:len(gene2)])
print(">gene2_F\n", gene2_F)
print(">gene2_R\n", gene2_R)

gene3_F = gene3[0:20]
gene3_R = rev_comp(gene3[-20:len(gene2)])
print(">gene3_F\n", gene3_F)
print(">gene3_R\n", gene3_R)
