
gene1 = "gtgggagacatagtggtcaaggtccccccgagtgtggacgaaaagctggccgatttgatagcaaagactatcgcggagagactgaaaaccctcgcaaggctcaatgagatgctcaagaactccgaactctcagaagaggatgcaatagaactcggacggaaggcgaaaatgggaaggggcgagtaccttgagagaagatattcttctcgtagttaa"
gene2 = "atgagagaagatattcttctcgtagttaacacaaacgtgctattctctttcttcgggaaatcaacagtaaccagagagctcgtgttcttggtatcagggagacttataagtcccgagtttgcactggaagagcttcacgagcacagggacgaagtcctgaaaaaagcaaagatcggagagaaagagttcgaggaaatactgtccgttcttaaagagcatgtcatattcgtaaacgaggggttctacgccgagttcatacctctagcactcgaataa"
gene3 = "atggaagttatccgtctgctgaagagaaagtcccaagacaaggttgagttcgtgcgcgatctggtagttttcatggcttctcccgacgttgatttttccaacgaggttctgtttaaggacgccgttgatgagatatactcaatcctgagggaggaagtcattgaaaatgggaacaaagagctagccagcgcgtatgaaaaagccgttctccttagagctgcggtttttggagaggaaatggatccgaaaaagctccttaagggtattctcgaggagctgaggtga"

## Here is a function to reverse compliment a sequence. The function is called rev_comp() and takes a string as an argument.
def rev_comp(sequence):
    complement_dictionary = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
    rev_complement = "".join(complement_dictionary.get(base, base) for base in reversed(sequence))
    return rev_complement


### Gene names for FASTA output
genes = ("gene1", "gene2", "gene3")

### Convert sequence to uppercase
gene_ls = [gene1.upper(), gene2.upper(), gene3.upper()]

### Function for forward primer
def primer_for_output(i):
    gene_for = i
    for n in [18, 19, 20, 21]:
        if gene_for[n-1] == "C":
            primer_for = gene_for[:(n)]
            break
        elif gene_for[n-1] == "G":
            primer_for = gene_for[:(n)]
            break
        else:
            continue
    return primer_for

### function for forward primer melting temperature
def primer_for_tm_output(l):
    primer_for_tm = 2 * len(primer_for_output(l))
    return primer_for_tm

### function for reverse primer
def primer_rev_output(i):
    gene_rev = rev_comp(i)
    for n in [18, 19, 20, 21]:
        if gene_rev[n-1] == "C":
            primer_rev = gene_rev[:(n)]
            break
        elif gene_rev[n-1] == "G":
            primer_rev = gene_rev[:(n)]
            break
        else:
            continue
    return primer_rev

### function for reverse primer melting temperature
def primer_rev_tm_output(l):
    primer_rev_tm = 2 * len(primer_rev_output(l))
    return primer_rev_tm

### FASTA output

for FASTA in (0, 1, 2):
    print(">", genes[FASTA], " | forward primer | approximate melting temperature:", primer_for_tm_output(gene_ls[FASTA]), "degrees Celsius")
    print(primer_for_output(gene_ls[FASTA]), "\n")
    print(">", genes[FASTA], " | reverse primer | approximate melting temperature:", primer_rev_tm_output(gene_ls[FASTA]), "degrees Celsius")
    print(primer_rev_output(gene_ls[FASTA]), "\n")
