gene1 = "gtgggagacatagtggtcaaggtccccccgagtgtggacgaaaagctggccgatttgatagcaaagactatcgcggagagactgaaaaccctcgcaaggctcaatgagatgctcaagaactccgaactctcagaagaggatgcaatagaactcggacggaaggcgaaaatgggaaggggcgagtaccttgagagaagatattcttctcgtagttaa"
gene2 = "atgagagaagatattcttctcgtagttaacacaaacgtgctattctctttcttcgggaaatcaacagtaaccagagagctcgtgttcttggtatcagggagacttataagtcccgagtttgcactggaagagcttcacgagcacagggacgaagtcctgaaaaaagcaaagatcggagagaaagagttcgaggaaatactgtccgttcttaaagagcatgtcatattcgtaaacgaggggttctacgccgagttcatacctctagcactcgaataa"
gene3 = "atggaagttatccgtctgctgaagagaaagtcccaagacaaggttgagttcgtgcgcgatctggtagttttcatggcttctcccgacgttgatttttccaacgaggttctgtttaaggacgccgttgatgagatatactcaatcctgagggaggaagtcattgaaaatgggaacaaagagctagccagcgcgtatgaaaaagccgttctccttagagctgcggtttttggagaggaaatggatccgaaaaagctccttaagggtattctcgaggagctgaggtga"


############ Project Answer ############
import pandas as pd

#reverse complement
def rev_comp(sequenec):
    complement_dictionary = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A', 'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
    rev_complement = "".join(complement_dictionary.get(base, base) for base in reversed(sequenec))
    return rev_complement

#complement
def comp(seq):
    seq = seq.lower()
    comp_dict = {'a': 't', 'c': 'g', 'g': 'c', 't': 'a'}
    comp_seq = ''.join(comp_dict.get(base, base) for base in seq)
    return comp_seq

#melting temperature
def calc_tm(seq):
    seq = seq.lower()
    at = 0
    gc = 0
    for i in seq:
        if i == "a" or i == "t":
            at += 1
        elif i == "g" or i == "c":
            gc += 1

    Tm = 64.9 + 41 * (gc - 16.4) / (gc + at)
    return round(Tm,4)

#primer df filter by melting temp
def filter_primer_df(df, tm_top, tm_bottom):
    df_out = df[df['Tm'] <= tm_top]
    return df_out[df_out['Tm'] >= tm_bottom]

#create df of primers, melting temperatures, and direction (forward/reverse)
def design_primers_df(sequence, primer_len=20, tm_top = 58, tm_bottom = 52):
    sequence = sequence.lower()
    primers_f = [comp(sequence[i : i + primer_len]) for i in range(0, len(sequence), primer_len)]
    primers_r = [rev_comp(sequence[i : i + primer_len]) for i in range(0, len(sequence), primer_len)]

    #remove primers that don't end in c or g
    primers_out_f = [p for p in primers_f if p[-1] == "c" or p[-1] == "g"]
    primers_out_r = [p for p in primers_r if p[-1] == "c" or p[-1] == "g"]

    #remove primers with less than primer_len bases
    primers_out_f = [p for p in primers_out_f if len(p) == primer_len]
    primers_out_r = [p for p in primers_out_r if len(p) == primer_len]

    #crude melting temp
    tm_f = [calc_tm(i) for i in primers_out_f]
    tm_r = [calc_tm(i) for i in primers_out_r]

    #forward / reverse list
    forward_reverse = ["forward"]*len(primers_out_f) + ["reverse"]*len(primers_out_r)
    primers_out = primers_out_f + primers_out_r
    tm_out = tm_f + tm_r

    df = pd.DataFrame(list(zip(primers_out, tm_out, forward_reverse)),
                      columns=['Primer Sequences', 'Tm', 'direction'])

    df_return = filter_primer_df(df, tm_top, tm_bottom)
    return df_return

#generate fasta files from primer df
def create_primer_fasta(df, filename):
    with open(f'{filename}.fa', 'w') as file:
        for i in range(0, df.shape[0]):
            file.write(f'>Primer{i+1}_{df.iloc[i,2]}_tm_{df.iloc[i,1]} \n')
            file.write(f'{df.iloc[i, 0]}\n')
    print(f'Created {filename}.fa')

#function calls
create_primer_fasta(design_primers_df(gene1), "gene1")
create_primer_fasta(design_primers_df(gene2), "gene2")
create_primer_fasta(design_primers_df(gene3), "gene3")
