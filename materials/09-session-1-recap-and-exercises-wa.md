---
title: Recap Exercise
---

::: {.callout-tip}
#### Aims

Refresh the topics covered yesterday including:
- Data types
- Conditionals and loops
- Errors and edge cases
- Defining functions and classes
:::


## Overview

Today we have a range of exciting topics to cover, however the style of teaching will be a little different from the first day. 
There will be fewer notes, and you will use the documentation pages and other resources to help you. There will be much more self-learning involved.
This is a little closer to how things will be when you are undertaking projects on your own. 

Before we go on to the new parts, have a try at this exercise to test how familiar you are with the content from the last session:

Answers will be uploaded after the session

::: {.callout-exercise}
#### Phenotypes and Genes
{{< level 2 >}}

Write a global variable which has the DNA to RNA transitions as a dictionary, and a global variable that has the DNA to amino acid transitions as a dictionary. 

**1.** Initiaise a class gene which 

has the class variables:

- tpye = protein_coding

Has the attributes:

- name
- id
- length 
- coding sequence
- rna sequence
- protein sequence

And has functions:

- add_length: to add length based on the coding sequence (deal with invalid characters)
- add_RNA to turn it into an RNA sequence (deal with invalid characters)
- add_protein_seq: to turn it into a protein sequence if it has a dna sequence
- modify_sequence: to alter a base of the DNA sequence at 'x' position and update the length, RNA and protein sequence
- print the attributes

**2.** Write a list of 10 made-up gene names

**3.** Using a 'for loop'/'list comprehension', and a random number generator, generate a dictionary of the 10 DNA sequences of 100 bases associated with the gene_names.
note:
```
import random
random.choices(options_list) #will make random choices on an options list
random.choices(options_list, k=100) # can be used to generate 100 outputs in one go
```
**4.** Use the dictionary to initialise 10 gene objects.


**5.** Initialise a class phenotype which is made up of:

attributes:

- name
- description (a string description")
- contributing genes (a list of gene objects)

functions:

- add multiple genes to the list
- remove genes from list
- append extra lines to the description
- replace the description. 
- print the attributes , and the attributes of the genes held. 

Use 'try', 'except', and 'match' to deal with errors.

**6.** Use a 'for loop' to initialise three phenotypes.

**7.** What is the size of the gene objects and phenotype objects using `sys.getsizeof()`?

**8.** What does this tell you about the sys.getsizeof() function?


**9.** Modify the sequence of one of the geneobjects - does the phenotype object change as seen when you print all the attributes.

**10.** Make a deep copy of a gene object and show that it is a deep copy. 

::: {.callout-answer}

```
# Global variable for DNA to RNA transitions
DNA_TO_RNA_TRANSITIONS = {
    'A': 'U',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

# Global variable for DNA to Amino Acid transitions
DNA_TO_AMINO_ACID_TRANSITIONS = {
    # DNA codon to single-letter amino acid code dictionary (sorted)
    "TTT":"F",
    "TTC":"F",
    "TTA":"L",
    "TTG":"L",
    "TCT":"S",
    "TCC":"S",
    "TCA":"S",
    "TCG":"S",
    "TAT":"Y",
    "TAC":"Y",
    "TAA":"X",
    "TAG":"X",
    "TGT":"C",
    "TGC":"C",
    "TGA":"X",
    "TGG":"W",
    "CTT":"L",
    "CTC":"L",
    "CTA":"L",
    "CTG":"L",
    "CCT":"P",
    "CCC":"P",
    "CCA":"P",
    "CCG":"P",
    "CAT":"H",
    "CAC":"H",
    "CAA":"Q",
    "CAG":"Q",
    "CGT":"R",
    "CGC":"R",
    "CGA":"R",
    "CGG":"R",
    "ATT":"I",
    "ATC":"I",
    "ATA":"I",
    "ATG":"M",
    "ACT":"T",
    "ACC":"T",
    "ACA":"T",
    "ACG":"T",
    "AAT":"N",
    "AAC":"N",
    "AAA":"K",
    "AAG":"K",
    "AGT":"S",
    "AGC":"S",
    "AGA":"R",
    "AGG":"R",
    "GTT":"V",
    "GTC":"V",
    "GTA":"V",
    "GTG":"V",
    "GCT":"A",
    "GCC":"A",
    "GCA":"A",
    "GCG":"A",
    "GAT":"D",
    "GAC":"D",
    "GAA":"E",
    "GAG":"E",
    "GGT":"G",
    "GGC":"G",
    "GGA":"G",
    "GGG":"G",
}

class Gene:
    # Class variable
    type = "protein_coding"
    
    def __init__(self, name, gene_id, coding_sequence):
        self.name = name
        self.gene_id = gene_id
        self.length = None  # Initialize length to None
        self.coding_sequence = coding_sequence.upper()  # Ensure sequence is uppercase
        self.rna_sequence = ""
        self.protein_sequence = ""

    def add_length(self):
        """
        Calculate the length of the coding sequence, ignoring invalid characters.
        """
        valid_bases = {'A', 'T', 'C', 'G'}
        self.length = sum(1 for base in self.coding_sequence if base in valid_bases)
        print(f"Length updated: {self.length}")

    def add_RNA(self):
        """
        Convert the DNA sequence to an RNA sequence.
        """
        try:
            rna_sequence = []
            for base in self.coding_sequence:
                if base in DNA_TO_RNA_TRANSITIONS:
                    rna_sequence.append(DNA_TO_RNA_TRANSITIONS[base])
                else:
                    raise ValueError(f"Invalid base '{base}' in DNA sequence.")
            self.rna_sequence = ''.join(rna_sequence)
            print(f"RNA sequence added: {self.rna_sequence}")
        except ValueError as e:
            print(f"Error: {e}")

    def add_protein_seq(self):
        """
        Convert DNA sequence to a protein sequence if exists.
        """
        if self.coding_sequence:
            protein_sequence = []
            for i in range(0, len(self.coding_sequence) - 2, 3):  # Iterate in steps of 3
                codon = self.coding_sequence[i:i + 3]
                if codon in DNA_TO_AMINO_ACID_TRANSITIONS:
                    amino_acid = DNA_TO_AMINO_ACID_TRANSITIONS[codon]
                    if amino_acid == 'STOP':
                        break
                    protein_sequence.append(amino_acid)
                else:
                    print(f"Warning: Codon '{codon}' not recognized.")
            self.protein_sequence = ''.join(protein_sequence)
            print(f"Protein sequence added: {self.protein_sequence}")
        else:
            print("DNA sequence not available. Cannot generate protein sequence.")

    def modify_sequence(self, position, new_base):
        """
        Modify a base of the DNA sequence at position and update length, RNA, and protein sequences.
        """
        try:
            if position < 0 or position >= len(self.coding_sequence):
                raise IndexError("Position out of range.")
            valid_bases = {'A', 'T', 'C', 'G'}
            if new_base not in valid_bases:
                raise ValueError("Invalid base. Must be A, T, C, or G.")
            
            # Modify the base
            self.coding_sequence = self.coding_sequence[:position] + new_base + self.coding_sequence[position + 1:]
            print(f"Modified DNA sequence: {self.coding_sequence}")

            # Update length, RNA, and protein sequences
            self.add_length()
            self.add_RNA()
            self.add_protein_seq()
        except (IndexError, ValueError) as e:
            print(f"Error: {e}")

    def print_attributes(self):
        """
        Print the attributes of the gene.
        """
        print(f"Gene Name: {self.name}")
        print(f"Gene ID: {self.id}")
        print(f"Length: {self.length}")
        print(f"Coding Sequence: {self.coding_sequence}")
        print(f"RNA Sequence: {self.rna_sequence}")
        print(f"Protein Sequence: {self.protein_sequence}")

# Example usage:
#gene1 = Gene(name="Gene1", id="G001", coding_sequence="ATGCTGAAATAG")
#gene1.add_length()  # Calculate and set the length
#gene1.add_RNA()     # Convert to RNA
#gene1.add_protein_seq()  # Convert to protein sequence
#gene1.modify_sequence(3, 'A')  # Modify a base
#gene1.print_attributes()  # Print the attributes of the gene

```

now generate the dictionary of gene_name gene_sequence pairs

```

import random

# Step 1: List of 10 made-up gene names
gene_names = [
    "GeneA1",
    "GeneB2",
    "GeneC3",
    "GeneD4",
    "GeneE5",
    "GeneF6",
    "GeneG7",
    "GeneH8",
    "GeneI9",
    "GeneJ0"
]

# Step 2: Generate a dictionary of 10 DNA sequences of 100 bases each
bases = ['A', 'T', 'C', 'G']  # Possible DNA bases
#using dictionary comprehension, string methods 
gene_sequences = {gene: ''.join(random.choices(bases, k=100)) for gene in gene_names}

# Output the dictionary of gene sequences
print(gene_sequences)

```

Output:

```

{'GeneA1': 'GTTGAGATCCTCTAACTATGGCTGTACGGACTTCAATTAGTCGCGACTTCGGCAAGCTCCCCCATCTTTACCCAGACATCTATCCAATTGCATCACATCC', 'GeneB2': 'GTTCGGACCCGTCTGTGCCGCTGAACGTCTACTGCCCGATAAGTCTTAGCCTCAAATATATACAGAAGAAAACATCATACTGCTGTTCGTGAAGTTCTGG', 'GeneC3': 'TTCTACACTTATACTAGAACATGATTTCATTTCACCCAATAGATATACCGGGTGACTCATTTGGTAGGGTGGGATTGTAGAACGGTTACAACGGGTATGA', 'GeneD4': 'GACGGTGGCACATGACTCTGGGCTGTGCCATATAAAGGGGATAGCTCGCTGCCTTTGTTGCCGATTTGTCGTGGCGCTGCAGCTTGTCGGTGTTGTAATC', 'GeneE5': 'TAGTTGCAAGCGAGCGGGGTGGGTGCAGCTGTGTTAGCGATTCCGTTTCTGCCCACAACACTCCATGTCGAGCCATTATAAGATGAACGAGAAAAGCGGA', 'GeneF6': 'TCCCATTGTTGCACTCCGGACCTCAGATGCGGGGACCCCTAAAACGCTGTCCTTGTCACCCGTTTACAATGATGCTAACGTTGCGCAAATCTTTCACCTG', 'GeneG7': 'AGGTGAACTAATCAGTTACCTTTCTTCTAACTGTTACCCCAAGTAGCAGACAAACAGTCGTGGAATCCGCAGCGATCCGTTGTCCGTCCATCTTACCCTG', 'GeneH8': 'ACGGATTCAACAGGGCACACGTAACTACCTGATCGTGGTTAGGATCTTATTGGACGGGGTAATCGAGATGCTCTTATGTAGGCTCGAGTGTTGTCCATGG', 'GeneI9': 'TTTGTCACGCAGCGGCAACTCCACCGCCGGCTCTAGGCATGCCACGTTTCTGAACCATCTGACCACAGCTCGGACTGGATAAGGTCAGGTACGGATTCCC', 'GeneJ0': 'ATGTTCGGACACGGTGGCAATTACAACTCAAAGCCTCCAGACTGCTAGCTTGACAATTGGATCTTCCAGGCCACTAGACATGTACGTGATCCGCTTCAAC'}

```

Now generate the gene_objects:

```
gene_objects = []
for gene_name, dna_sequence in gene_sequences.items():
    gene_id = f"G{gene_names.index(gene_name) + 1:03}"  # Generate a unique gene ID
    gene = Gene(name=gene_name, id=gene_id, coding_sequence=dna_sequence)
    gene.add_length()  # Calculate length
    gene.add_RNA()     # Convert to RNA
    gene.add_protein_seq()  # Convert to protein sequence
    gene_objects.append(gene)

# Display the attributes of each gene object
for gene in gene_objects:
    gene.print_attributes()

```

output:

```

Length: 100
Coding Sequence: GTTGAGATCCTCTAACTATGGCTGTACGGACTTCAATTAGTCGCGACTTCGGCAAGCTCCCCCATCTTTACCCAGACATCTATCCAATTGCATCACATCC
RNA Sequence: CAACUCUAGGAGAUUGAUACCGACAUGCCUGAAGUUAAUCAGCGCUGAAGCCGUUCGAGGGGGUAGAAAUGGGUCUGUAGAUAGGUUAACGUAGUGUAGG
Protein Sequence: VEILXLWLYGLQLVATSASSPIFTQTSIQLHHI
Gene Name: GeneB2
Gene ID: G002
Length: 100
Coding Sequence: GTTCGGACCCGTCTGTGCCGCTGAACGTCTACTGCCCGATAAGTCTTAGCCTCAAATATATACAGAAGAAAACATCATACTGCTGTTCGTGAAGTTCTGG
RNA Sequence: CAAGCCUGGGCAGACACGGCGACUUGCAGAUGACGGGCUAUUCAGAAUCGGAGUUUAUAUAUGUCUUCUUUUGUAGUAUGACGACAAGCACUUCAAGACC
Protein Sequence: VRTRLCRXTSTARXVLASNIYRRKHHTAVREVL
Gene Name: GeneC3
Gene ID: G003
Length: 100
Coding Sequence: TTCTACACTTATACTAGAACATGATTTCATTTCACCCAATAGATATACCGGGTGACTCATTTGGTAGGGTGGGATTGTAGAACGGTTACAACGGGTATGA
RNA Sequence: AAGAUGUGAAUAUGAUCUUGUACUAAAGUAAAGUGGGUUAUCUAUAUGGCCCACUGAGUAAACCAUCCCACCCUAACAUCUUGCCAAUGUUGCCCAUACU
Protein Sequence: FYTYTRTXFHFTQXIYRVTHLVGWDCRTVTTGM
Gene Name: GeneD4
Gene ID: G004
Length: 100
Coding Sequence: GACGGTGGCACATGACTCTGGGCTGTGCCATATAAAGGGGATAGCTCGCTGCCTTTGTTGCCGATTTGTCGTGGCGCTGCAGCTTGTCGGTGTTGTAATC
RNA Sequence: CUGCCACCGUGUACUGAGACCCGACACGGUAUAUUUCCCCUAUCGAGCGACGGAAACAACGGCUAAACAGCACCGCGACGUCGAACAGCCACAACAUUAG
Protein Sequence: DGGTXLWAVPYKGDSSLPLLPICRGAAACRCCN
Gene Name: GeneE5
Gene ID: G005
Length: 100
Coding Sequence: TAGTTGCAAGCGAGCGGGGTGGGTGCAGCTGTGTTAGCGATTCCGTTTCTGCCCACAACACTCCATGTCGAGCCATTATAAGATGAACGAGAAAAGCGGA
RNA Sequence: AUCAACGUUCGCUCGCCCCACCCACGUCGACACAAUCGCUAAGGCAAAGACGGGUGUUGUGAGGUACAGCUCGGUAAUAUUCUACUUGCUCUUUUCGCCU
Protein Sequence: XLQASGVGAAVLAIPFLPTTLHVEPLXDEREKR
Gene Name: GeneF6
Gene ID: G006
Length: 100
Coding Sequence: TCCCATTGTTGCACTCCGGACCTCAGATGCGGGGACCCCTAAAACGCTGTCCTTGTCACCCGTTTACAATGATGCTAACGTTGCGCAAATCTTTCACCTG
RNA Sequence: AGGGUAACAACGUGAGGCCUGGAGUCUACGCCCCUGGGGAUUUUGCGACAGGAACAGUGGGCAAAUGUUACUACGAUUGCAACGCGUUUAGAAAGUGGAC
Protein Sequence: SHCCTPDLRCGDPXNAVLVTRLQXCXRCANLSP
Gene Name: GeneG7
Gene ID: G007
Length: 100
Coding Sequence: AGGTGAACTAATCAGTTACCTTTCTTCTAACTGTTACCCCAAGTAGCAGACAAACAGTCGTGGAATCCGCAGCGATCCGTTGTCCGTCCATCTTACCCTG
RNA Sequence: UCCACUUGAUUAGUCAAUGGAAAGAAGAUUGACAAUGGGGUUCAUCGUCUGUUUGUCAGCACCUUAGGCGUCGCUAGGCAACAGGCAGGUAGAAUGGGAC
Protein Sequence: RXTNQLPFFXLLPQVADKQSWNPQRSVVRPSYP
Gene Name: GeneH8
Gene ID: G008
Length: 100
Coding Sequence: ACGGATTCAACAGGGCACACGTAACTACCTGATCGTGGTTAGGATCTTATTGGACGGGGTAATCGAGATGCTCTTATGTAGGCTCGAGTGTTGTCCATGG
RNA Sequence: UGCCUAAGUUGUCCCGUGUGCAUUGAUGGACUAGCACCAAUCCUAGAAUAACCUGCCCCAUUAGCUCUACGAGAAUACAUCCGAGCUCACAACAGGUACC
Protein Sequence: TDSTGHTXLPDRGXDLIGRGNRDALMXARVLSM
Gene Name: GeneI9
Gene ID: G009
Length: 100
Coding Sequence: TTTGTCACGCAGCGGCAACTCCACCGCCGGCTCTAGGCATGCCACGTTTCTGAACCATCTGACCACAGCTCGGACTGGATAAGGTCAGGTACGGATTCCC
RNA Sequence: AAACAGUGCGUCGCCGUUGAGGUGGCGGCCGAGAUCCGUACGGUGCAAAGACUUGGUAGACUGGUGUCGAGCCUGACCUAUUCCAGUCCAUGCCUAAGGG
Protein Sequence: FVTQRQLHRRLXACHVSEPSDHSSDWIRSGTDS
Gene Name: GeneJ0
Gene ID: G010
Length: 100
Coding Sequence: ATGTTCGGACACGGTGGCAATTACAACTCAAAGCCTCCAGACTGCTAGCTTGACAATTGGATCTTCCAGGCCACTAGACATGTACGTGATCCGCTTCAAC
RNA Sequence: UACAAGCCUGUGCCACCGUUAAUGUUGAGUUUCGGAGGUCUGACGAUCGAACUGUUAACCUAGAAGGUCCGGUGAUCUGUACAUGCACUAGGCGAAGUUG
Protein Sequence: MFGHGGNYNSKPPDCXLDNWIFQATRHVRDPLQ

```

defining the class phenotype:

```

class Phenotype:
    def __init__(self, name, description):
        self.name = name
        self.description = description  # A string description
        self.contributing_genes = []     # A list to hold gene objects

    def add_genes(self, genes):
        """Add multiple gene objects to the contributing genes list."""
        try:
            match genes:
                case list():
                    self.contributing_genes.extend(genes)
                case _:
                    raise ValueError("Input must be a list of gene objects.")
        except Exception as e:
            print(f"Error: {e}")

    def remove_genes(self, genes):
        """Remove gene objects from the contributing genes list."""
        try:
            match genes:
                case list():
                    for gene in genes:
                        if gene in self.contributing_genes:
                            self.contributing_genes.remove(gene)
                        else:
                            print(f"Gene {gene} not found in the contributing genes list.")
                case _:
                    raise ValueError("Input must be a list of gene objects.")
        except Exception as e:
            print(f"Error: {e}")

    def append_description(self, extra_description):
        """Append extra lines to the description."""
        try:
            match extra_description:
                case str():
                    self.description += "\n" + extra_description
                case _:
                    raise ValueError("Extra description must be a string.")
        except Exception as e:
            print(f"Error: {e}")

    def replace_description(self, new_description):
        """Replace the current description with a new one."""
        try:
            match new_description:
                case str():
                    self.description = new_description
                case _:
                    raise ValueError("New description must be a string.")
        except Exception as e:
            print(f"Error: {e}")

    def print_attributes(self):
        """Print the attributes of the phenotype and the genes."""
        print(f"Phenotype Name: {self.name}")
        print(f"Description: {self.description}")
        print("Contributing Genes:")
        if self.contributing_genes:
            for gene in self.contributing_genes:
                gene.print_attributes()
        else:
            print("  No contributing genes.")

```

make the phenotype objects:

```
phenotypes = []
for i in range(3):
    # Randomly select 3 genes for each phenotype
    selected_genes = random.sample(gene_objects, 3)
    # Create the phenotype object with a name and description
    phenotype = Phenotype(f"phenotype_{i+1}", f"bad_phenotype_{i+1}")
    # Add the selected genes to the phenotype
    phenotype.add_genes(selected_genes)
    # Add the phenotype to the list of phenotypes
    phenotypes.append(phenotype)

# Print the attributes of the three phenotypes
for phenotype in phenotypes:
    phenotype.print_attributes()
    print("---")

```

output:

```

Protein Sequence: DGGTXLWAVPYKGDSSLPLLPICRGAAACRCCN
Gene Name: GeneI9
Gene ID: G009
Length: 100
Coding Sequence: TTTGTCACGCAGCGGCAACTCCACCGCCGGCTCTAGGCATGCCACGTTTCTGAACCATCTGACCACAGCTCGGACTGGATAAGGTCAGGTACGGATTCCC
RNA Sequence: AAACAGUGCGUCGCCGUUGAGGUGGCGGCCGAGAUCCGUACGGUGCAAAGACUUGGUAGACUGGUGUCGAGCCUGACCUAUUCCAGUCCAUGCCUAAGGG
Protein Sequence: FVTQRQLHRRLXACHVSEPSDHSSDWIRSGTDS
Gene Name: GeneG7
Gene ID: G007
Length: 100
Coding Sequence: AGGTGAACTAATCAGTTACCTTTCTTCTAACTGTTACCCCAAGTAGCAGACAAACAGTCGTGGAATCCGCAGCGATCCGTTGTCCGTCCATCTTACCCTG
RNA Sequence: UCCACUUGAUUAGUCAAUGGAAAGAAGAUUGACAAUGGGGUUCAUCGUCUGUUUGUCAGCACCUUAGGCGUCGCUAGGCAACAGGCAGGUAGAAUGGGAC
Protein Sequence: RXTNQLPFFXLLPQVADKQSWNPQRSVVRPSYP
---
Phenotype Name: phenotype_2
Description: bad_phenotype_2
Contributing Genes:
Gene Name: GeneG7
Gene ID: G007
Length: 100
Coding Sequence: AGGTGAACTAATCAGTTACCTTTCTTCTAACTGTTACCCCAAGTAGCAGACAAACAGTCGTGGAATCCGCAGCGATCCGTTGTCCGTCCATCTTACCCTG
RNA Sequence: UCCACUUGAUUAGUCAAUGGAAAGAAGAUUGACAAUGGGGUUCAUCGUCUGUUUGUCAGCACCUUAGGCGUCGCUAGGCAACAGGCAGGUAGAAUGGGAC
Protein Sequence: RXTNQLPFFXLLPQVADKQSWNPQRSVVRPSYP
Gene Name: GeneA1
Gene ID: G001
Length: 100
Coding Sequence: GTTGAGATCCTCTAACTATGGCTGTACGGACTTCAATTAGTCGCGACTTCGGCAAGCTCCCCCATCTTTACCCAGACATCTATCCAATTGCATCACATCC
RNA Sequence: CAACUCUAGGAGAUUGAUACCGACAUGCCUGAAGUUAAUCAGCGCUGAAGCCGUUCGAGGGGGUAGAAAUGGGUCUGUAGAUAGGUUAACGUAGUGUAGG
Protein Sequence: VEILXLWLYGLQLVATSASSPIFTQTSIQLHHI
Gene Name: GeneJ0
Gene ID: G010
Length: 100
Coding Sequence: ATGTTCGGACACGGTGGCAATTACAACTCAAAGCCTCCAGACTGCTAGCTTGACAATTGGATCTTCCAGGCCACTAGACATGTACGTGATCCGCTTCAAC
RNA Sequence: UACAAGCCUGUGCCACCGUUAAUGUUGAGUUUCGGAGGUCUGACGAUCGAACUGUUAACCUAGAAGGUCCGGUGAUCUGUACAUGCACUAGGCGAAGUUG
Protein Sequence: MFGHGGNYNSKPPDCXLDNWIFQATRHVRDPLQ
---
Phenotype Name: phenotype_3
Description: bad_phenotype_3
Contributing Genes:
Gene Name: GeneE5
Gene ID: G005
Length: 100
Coding Sequence: TAGTTGCAAGCGAGCGGGGTGGGTGCAGCTGTGTTAGCGATTCCGTTTCTGCCCACAACACTCCATGTCGAGCCATTATAAGATGAACGAGAAAAGCGGA
RNA Sequence: AUCAACGUUCGCUCGCCCCACCCACGUCGACACAAUCGCUAAGGCAAAGACGGGUGUUGUGAGGUACAGCUCGGUAAUAUUCUACUUGCUCUUUUCGCCU
Protein Sequence: XLQASGVGAAVLAIPFLPTTLHVEPLXDEREKR
Gene Name: GeneA1
Gene ID: G001
Length: 100
Coding Sequence: GTTGAGATCCTCTAACTATGGCTGTACGGACTTCAATTAGTCGCGACTTCGGCAAGCTCCCCCATCTTTACCCAGACATCTATCCAATTGCATCACATCC
RNA Sequence: CAACUCUAGGAGAUUGAUACCGACAUGCCUGAAGUUAAUCAGCGCUGAAGCCGUUCGAGGGGGUAGAAAUGGGUCUGUAGAUAGGUUAACGUAGUGUAGG
Protein Sequence: VEILXLWLYGLQLVATSASSPIFTQTSIQLHHI
Gene Name: GeneB2
Gene ID: G002
Length: 100
Coding Sequence: GTTCGGACCCGTCTGTGCCGCTGAACGTCTACTGCCCGATAAGTCTTAGCCTCAAATATATACAGAAGAAAACATCATACTGCTGTTCGTGAAGTTCTGG
RNA Sequence: CAAGCCUGGGCAGACACGGCGACUUGCAGAUGACGGGCUAUUCAGAAUCGGAGUUUAUAUAUGUCUUCUUUUGUAGUAUGACGACAAGCACUUCAAGACC
Protein Sequence: VRTRLCRXTSTARXVLASNIYRRKHHTAVREVL

```

check sizes:

```

import sys
print(sys.getsizeof(gene_objects[0]))

print(sys.getsizeof(phenotypes[0]))

```

output:
```
48
48
```

`sys.getsizeof()` outputs the shallow size of objects


In Python, when objects are passed as arguments to functions or assigned to other objects, they are passed by reference. 
This means that if you modify an object (e.g., a Gene object) that is part of a Phenotype object, the changes will be reflected in the Phenotype object as well, since they both refer to the same object in memory.

```

import copy

phenotype_1_deepcopy = copy.deepcopy(phenotypes[0])
phenotype_1_deepcopy.print_attributes()

print('the id of the genes of the deep copy should be different to the original:')
print(id(phenotypes[0].contributing_genes[0]))
print(id(phenotype_1_deepcopy.contributing_genes[0]))

```

output:
```
Phenotype Name: phenotype_1
Description: bad_phenotype_1
Contributing Genes:
Gene Name: GeneD4
Gene ID: G004
Length: 100
Coding Sequence: GACGGTGGCACATGACTCTGGGCTGTGCCATATAAAGGGGATAGCTCGCTGCCTTTGTTGCCGATTTGTCGTGGCGCTGCAGCTTGTCGGTGTTGTAATC
RNA Sequence: CUGCCACCGUGUACUGAGACCCGACACGGUAUAUUUCCCCUAUCGAGCGACGGAAACAACGGCUAAACAGCACCGCGACGUCGAACAGCCACAACAUUAG
Protein Sequence: DGGTXLWAVPYKGDSSLPLLPICRGAAACRCCN
Gene Name: GeneI9
Gene ID: G009
Length: 100
Coding Sequence: TTTGTCACGCAGCGGCAACTCCACCGCCGGCTCTAGGCATGCCACGTTTCTGAACCATCTGACCACAGCTCGGACTGGATAAGGTCAGGTACGGATTCCC
RNA Sequence: AAACAGUGCGUCGCCGUUGAGGUGGCGGCCGAGAUCCGUACGGUGCAAAGACUUGGUAGACUGGUGUCGAGCCUGACCUAUUCCAGUCCAUGCCUAAGGG
Protein Sequence: FVTQRQLHRRLXACHVSEPSDHSSDWIRSGTDS
Gene Name: GeneG7
Gene ID: G007
Length: 100
Coding Sequence: AGGTGAACTAATCAGTTACCTTTCTTCTAACTGTTACCCCAAGTAGCAGACAAACAGTCGTGGAATCCGCAGCGATCCGTTGTCCGTCCATCTTACCCTG
RNA Sequence: UCCACUUGAUUAGUCAAUGGAAAGAAGAUUGACAAUGGGGUUCAUCGUCUGUUUGUCAGCACCUUAGGCGUCGCUAGGCAACAGGCAGGUAGAAUGGGAC
Protein Sequence: RXTNQLPFFXLLPQVADKQSWNPQRSVVRPSYP
the id of the genes of the deep copy should be different to the original:
135961870136992
135961869732160
```

:::
:::

## Conclusion

Hopefully that was a fun exercise to go over everything we have done so far! Let's now move on to today's topics.

::: {.callout-tip}
#### Key Points

- By completing the above exercise, you should be able to independently apply the concepts covered yesterday
- If there is anything you found difficult, go back to the relevant sections and recap the material

:::
