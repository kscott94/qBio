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


gene_ls = [gene1, gene2, gene3]   # make a list of the genes to parse through

for gene in gene_ls:        #for every gene in gene_ls, the following instructions will be executed
    gene_length = len(gene)         # get the length of each gene. This will make indexing easier
    primer_F = gene[0:20]           # use a an indexing method to query the first 20 bases of the string (gene)
    primer_R_Forward_sequence = gene[-20:gene_length] # use a an indexing method to query the last 20 bases of the string (gene)
    primer_R = rev_comp(primer_R_Forward_sequence)    # rverse compliment the forward sequence of the Reverse primer
    print(">primer_F\n", primer_F)    # print each primer. The \n creates a new line.
    print(">primer_R\n",primer_R)
