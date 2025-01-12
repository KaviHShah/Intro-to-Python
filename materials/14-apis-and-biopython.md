---
title: API's and Biopython
---

::: {.callout-tip}
#### Learning Objectives

- Introduce briefly API's and Biopython - both useful tools for bioinformaticians.
:::


## What is an API?

An **API** (Application Programming Interface) allows different software applications to communicate with each other.

In the context of Python and biological data, APIs enable bioinformaticians to access various functionalities and data from externally managed services, libraries, and databases, through Python code. APIs are available in python for NCBI Entrez (including Genbank and Pubmed), Uniprot, Ensembl, KEGG, and Intermine (HumanMine , FlyMine etc.) databases to name a few.

APIs allow you to automate queries to biological databases and retrieve data in a rapid and simple way. This can be particularly useful if submitting multiple queries. APIs can also enable you to access analysis software tools through code (e.g. python code). Furthermore, the code used to submit the query often gives greater clarity concerning what information was retrieved, than is sometimes reported in the web interface. This supports clearer documentation.

## Example from HumanMine

HumanMine is an integrated database of human genomics and proteomics data. The web interface query builder also outputs the equivalent python code to retrieve the same data through the API, making it very simple to start to work with the API.

An example is below: 

```
#!/usr/bin/env python

# This is an automatically generated script to run your query
# to use it you will require the intermine python client.
# To install the client, run the following command from a terminal:
#
#     sudo easy_install intermine
#
# For further documentation you can visit:
#     http://intermine.readthedocs.org/en/latest/web-services/

# The line below will be needed if you are running this script with python 2.
# Python 3 will ignore it.
from __future__ import print_function

# The following two lines will be needed in every python script:
from intermine.webservice import Service
service = Service("https://www.humanmine.org/humanmine/service")

# Get a new query on the class (table) you will be querying:
query = service.new_query("Gene")

# The view specifies the output columns
query.add_view(
    "primaryIdentifier", "symbol", "name", "pathways.name",
    "pathways.dataSets.name", "pathways.identifier", "organism.shortName"
)

# This query's custom sort order is specified below:
query.add_sort_order("Gene.primaryIdentifier", "ASC")
query.add_sort_order("Gene.primaryIdentifier", "ASC")
query.add_sort_order("Gene.primaryIdentifier", "ASC")

# You can edit the constraint values below
query.add_constraint("Gene", "LOOKUP", "BRCA1", code="A")
query.add_constraint("organism.name", "=", "Homo sapiens", code="B")

# Uncomment and edit the code below to specify your own custom logic:
# query.set_logic("B and A")

for row in query.rows():
    print(row["primaryIdentifier"], row["symbol"], row["name"], row["pathways.name"], \
        row["pathways.dataSets.name"], row["pathways.identifier"], row["organism.shortName"])

```

https://www.humanmine.org/humanmine


## Biopython

Biopython is a widely used python package for working with biological data. 
It includes functions for working with biological data files including 'fasta' files, and data structures (classes) for biological data, for example `SeqRecord`. Modules include: `Bio.Seq`, `Bio.Align`, `Bio.PDB`. It is managed by a team of Bioinformatitions. You can also query some of biological database API's using Biopython functions, for example you can query the KEGG database.
https://biopython.org/docs/latest/Tutorial/chapter_kegg.html

**Documentation**

https://biopython.org/wiki/Documentation

Example use:

```
!pip install biopython
from Bio import SeqIO
from Bio import pairwise2  # Import pairwise2 for alignments
from Bio.pairwise2 import format_alignment  # Import format_alignment to display the results

# Step 1: Parse the FASTA file and extract the first 100 sequences
fasta_file = "example.fasta"  # Path to your FASTA file
seq_records = []

# Parsing the FASTA file and collecting the first 100 SeqRecord objects
for i, record in enumerate(SeqIO.parse(fasta_file, "fasta")):
    if i < 100:
        seq_records.append(record)
    else:
        break

# Step 2: Write the 100 sequences to a temporary file
with open("subset_100.fasta", "w") as output_handle:
    SeqIO.write(seq_records, output_handle, "fasta")

# Step 3: Align the sequences using Clustal Omega (you need Clustal Omega installed)
# Clustal Omega command-line tool should be installed and accessible in your system
# Parse only the first two sequences from the FASTA file
for i, record in enumerate(SeqIO.parse(fasta_file, "fasta")):
    if i < 2:
        seq_records.append(record)
    else:
        break

# Step 2: Extract the sequences from the SeqRecord objects
seq1 = seq_records[0].seq
seq2 = seq_records[1].seq

# Step 3: Perform pairwise alignment using Biopython's pairwise2 module
alignments = pairwise2.align.globalxx(seq1, seq2)

# Step 4: Display the alignment results
# The globalxx method aligns globally, using simple match scoring (1 for match, 0 for mismatch/gap)
for alignment in alignments:
    print(pairwise2.format_alignment(*alignment))

```

**Output:**

```
Requirement already satisfied: biopython in /usr/local/lib/python3.10/dist-packages (1.84)
Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from biopython) (1.26.4)
/usr/local/lib/python3.10/dist-packages/Bio/pairwise2.py:278: BiopythonDeprecationWarning: Bio.pairwise2 has been deprecated, and we intend to remove it in a future release of Biopython. As an alternative, please consider using Bio.Align.PairwiseAligner as a replacement, and contact the Biopython developers if you still need the Bio.pairwise2 module.
  warnings.warn(
AAAAAAACCACCGCTACCAGCGGTGGTTTGTTTGCCGGATCAAGAGCTACCAACTCTTTTTCCGAGGTAACTGGCTTCAGCAGAGCGCAGATACCAAATACTGTTCTTCTAGTGTAGCCGTAGTTAGGCCACCACTTCAAGAACTCTGTAGCACCGCCTACATACCTCGCTCTGCTAATCCTGTTACCAGTGGCTGCTGCCAGTGGCGATAAGTCGTGTCTTACCGGGTTGGACTCAAGACGATAGTTACCGGATAAGGCGCAGCGGTCGGGCTGAACGGGGGGTTCGTGCACACAGCCCAGCTTGGAGCGAACGACCTACACCGAACTGAGATACCTACAGCGTGAGCTATGAGAAAGCGCCACGCTTCCCGAAGGGAGAAAGGCGGACAGGTATCCGGTAAGCGGCAGGGTCGGAACAGGAGAGCGCACGAGGGAGCTTCCAGGGGGAAACGCCTGGTATCTTTATAGTCCTGTCGGGTTTCGCCACCTCTGACTTGAGCATCGATTTTTGTGATGCTCGTCAGGGGGGCGGAGCCTATGGAAAAACGCCAGCAACGCAGAAAGGCCCACCCGAAGGTGAGCCAGGTGATTACATTTGGGCCCTCATCAGAGGTTTTCACCGTCATCACCGAAACGCGCGAGGCAGCTGCGGTAAAGCTCATCAGCGTGGTCGTGAAGCGATTCACAGATGTCTGCCTGTTCATCCGCGTCCAGCTCGTTGAGTTTCTCCAGAAGCGTTAATGTCTGGCTTCTGATAAAGCGGGCCATGTTAAGGGCGGTTTTTTCCTGTTTGGTCACTTACCAATGCTTAATCAGTGAGGCACCTATCTCAGCGATCTGTCTATTTCGTTCATCCATAGTTGCCTGACTCCCCGTCGTGTAGATAACTACGATGCGGGAGGGCTTACCATCTGGCCCCAGTGCTGCAATGATACCGCGAGACCCACGCTCACCGGCTCCAGATTTATCAGCAATAAACCAGCCAGCCGGGAGTGCCGAGCGCAGAAGTGATCCTGCAACTTTATCCGCCTCCATCCAGTCTATTAATTGTTGCCGGGAAGCTAGAGTAAGTAGTTCGCCAGTTAATAGTTTGCGCAACGTTGTTGCCATTGCTACAGGCATCGTGGTGTCACGCTCGTCGTTTGGTATGGCTTCATTCAGCTCCGGTTCCCAACGATCAAGGCGAGTTACATGATCCCCCATGTTGTGCAAAAAAGCGGTTAGCTCCTTCGGTCCTCCGATCGTTGCCAGAAGTAAGTTGGCCGCAGTGTTATCACTCATGGTTATGGCAGCACTGCATAATTCTCTTACTGTCATGCCATCCGTGAGATGCTTTTCTGTGACTGGTGAGTACTCAACCAAGTCATTCTGAGAATAGTGTATGCGGCGACCGAGTTGCTCTTGCCCGGCGTCAATACGGGATAATACCGCGCCACATAGCAGAACTTTAAAAGTGCTCATCATTGGAAAACGTTCTTCGGGGCGTAAACTCTCAAGGATCTTACCGCTGTTGAGATCCAGTTCGATGTAACCCACTCGTGCACCCAACTGATCTTCAGCATCTTTTACTTTCACCAGCGTTTCTGGGTGAGCAAAAACAGGAAGGCAAAATGCCGCAAAAAAGGGAATAAGGGCGACACGGAAATGTTGAATACTCATTTTAGCTTCCTTAGCTCCTGAAAATCTCGATAACTCAAAAAATACGCCCGGTAGTGATCTTATTTCATTATGGTGAAAGTTGGAACCTCTTACGTGCCGATCAAGTCAAAAGCCTCCGGTCGGAGGCTTTTGACTTTCTGCTATGGAGGTCAGGTATGATTTAAATGGTCAGTGATGAACGCACAGCGAAATGGGGAGCCAAAAAACCCCTCAAGACCCGTTTAGAGGCCCCAAGGGGTTATGCTAGCATAAATCATAAGAAATTCGCGCCATACCTATTAAGACTCCTTATTACGCAGTATGTTAGCAAACGTAGAAAATACATACATAAAGGTGGCAACATATAAAAGAAACGCAAAGACACCACGGAATAAGTTTATTTTGTCACAATCAATAGAAAATTCATATGGTTTACCAGCGCCAAAGACAAAAGGGCGACATTCAACCGATTGAGGGAGGGAAGGTAAATATTGACGGAAATTATTCATTAAAGGTGAATTATCACCGTCACCGACTTGAGCCATTTGGGAATTAGAGCCAGCAAAATCACCAGTAGCACCATTACCATTAGCAAGGCCGGAAACGTCACCAATGAAACCATCGATAGCAGCACCGTAATCAGTAGCGACAGAATCAAGTTTGCCTTTAGCGTCAGACTGTAGCGCGTTTTCATCGGCATTTTCGGTCATAGCCCCCTTATTAGCGTTTGCCATCTTTTCATAATCAAAATCACCGGAACCAGAGCCACCACCGGAACCGCCTCCCTCAGAGCCGCCACCCTCAGAACCGCCACCCTCAGAGCCACCACCCTCAGAGCCGCCACCAGAACCACCACCAGAGCCGCCGCCAGCATTGACAGGAGGTTGAGGCAGGTCAGACGATTGGCCTTGATATTCACAAACGAATGGATCCTCATTAAAGCCAGAATGGAAAGCGCAGTCTCTGAATTTACCGTTCCAGTAAGCGTCATACATGGCTTTTGATGATACAGGAGTGTACTGGTAATAAGTTTTAACGGGGTCAGTGCCTTGAGTAACAGTGCCCGTATAAACAGTTAATGCCCCCTGCCTATTTCGGAACCTATTATTCTGAAACATGAAAGTATTAAGAGGCTGAGACTCCTCAAGAGAAGGATTAGGATTAGCGGGGTTTTGCTCAGTACCAGGCGGATAAGTGCCGTCGAGAGGGTTGATATAAGTATAGCCCGGAATAGGTGTATCACCGTACTCAGGAGGTTTAGTACCGCCACCCTCAGAACCGCCACCCTCAGAACCGCCACCCTCAGAGCCACCACCCTCATTTTCAGGGATAGCAAGCCCAATAGGAACCCATGTACCGTAACACTGAGTTTCGTCACCAGTACAAACTACAACGCCTGTAGCATTCCACAGACAGCCCTCATAGTTAGCGTAACGATCTAAAGTTTTGTCGTCTTTCCAGACGTTAGTAAATGAATTTTCTGTATGGGGTTTTGCTAAACAACTTTCAACAGTTTCAGCGGAGTGAGAATAGAAAGGAACAACTAAAGGAATTGCGAATAATAATTTTTTCATTTAGTATTTCTCCTCTTTAATCTAGTAGCTAAGATCCATTCCCTTTAGTGAGGCTAAATACAGTGGAGAGCGTTCACCGACAAACAACAGATAAAACGAAAGCCAGTCTTTCGACTGAGCCTTTCGTTTTATTTGAAGCTTGACTCCAGCGTAACTGGACTGCAATCAACTCACTGGCTCACCTTCACGGGTGGGCCTTTCTTCGGTAGAAAATCAAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCTTGCAAAC
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
AAAAAAACCACCGCTACCAGCGGTGGTTTGTTTGCCGGATCAAGAGCTACCAACTCTTTTTCCGAGGTAACTGGCTTCAGCAGAGCGCAGATACCAAATACTGTTCTTCTAGTGTAGCCGTAGTTAGGCCACCACTTCAAGAACTCTGTAGCACCGCCTACATACCTCGCTCTGCTAATCCTGTTACCAGTGGCTGCTGCCAGTGGCGATAAGTCGTGTCTTACCGGGTTGGACTCAAGACGATAGTTACCGGATAAGGCGCAGCGGTCGGGCTGAACGGGGGGTTCGTGCACACAGCCCAGCTTGGAGCGAACGACCTACACCGAACTGAGATACCTACAGCGTGAGCTATGAGAAAGCGCCACGCTTCCCGAAGGGAGAAAGGCGGACAGGTATCCGGTAAGCGGCAGGGTCGGAACAGGAGAGCGCACGAGGGAGCTTCCAGGGGGAAACGCCTGGTATCTTTATAGTCCTGTCGGGTTTCGCCACCTCTGACTTGAGCATCGATTTTTGTGATGCTCGTCAGGGGGGCGGAGCCTATGGAAAAACGCCAGCAACGCAGAAAGGCCCACCCGAAGGTGAGCCAGGTGATTACATTTGGGCCCTCATCAGAGGTTTTCACCGTCATCACCGAAACGCGCGAGGCAGCTGCGGTAAAGCTCATCAGCGTGGTCGTGAAGCGATTCACAGATGTCTGCCTGTTCATCCGCGTCCAGCTCGTTGAGTTTCTCCAGAAGCGTTAATGTCTGGCTTCTGATAAAGCGGGCCATGTTAAGGGCGGTTTTTTCCTGTTTGGTCACTTACCAATGCTTAATCAGTGAGGCACCTATCTCAGCGATCTGTCTATTTCGTTCATCCATAGTTGCCTGACTCCCCGTCGTGTAGATAACTACGATGCGGGAGGGCTTACCATCTGGCCCCAGTGCTGCAATGATACCGCGAGACCCACGCTCACCGGCTCCAGATTTATCAGCAATAAACCAGCCAGCCGGGAGTGCCGAGCGCAGAAGTGATCCTGCAACTTTATCCGCCTCCATCCAGTCTATTAATTGTTGCCGGGAAGCTAGAGTAAGTAGTTCGCCAGTTAATAGTTTGCGCAACGTTGTTGCCATTGCTACAGGCATCGTGGTGTCACGCTCGTCGTTTGGTATGGCTTCATTCAGCTCCGGTTCCCAACGATCAAGGCGAGTTACATGATCCCCCATGTTGTGCAAAAAAGCGGTTAGCTCCTTCGGTCCTCCGATCGTTGCCAGAAGTAAGTTGGCCGCAGTGTTATCACTCATGGTTATGGCAGCACTGCATAATTCTCTTACTGTCATGCCATCCGTGAGATGCTTTTCTGTGACTGGTGAGTACTCAACCAAGTCATTCTGAGAATAGTGTATGCGGCGACCGAGTTGCTCTTGCCCGGCGTCAATACGGGATAATACCGCGCCACATAGCAGAACTTTAAAAGTGCTCATCATTGGAAAACGTTCTTCGGGGCGTAAACTCTCAAGGATCTTACCGCTGTTGAGATCCAGTTCGATGTAACCCACTCGTGCACCCAACTGATCTTCAGCATCTTTTACTTTCACCAGCGTTTCTGGGTGAGCAAAAACAGGAAGGCAAAATGCCGCAAAAAAGGGAATAAGGGCGACACGGAAATGTTGAATACTCATTTTAGCTTCCTTAGCTCCTGAAAATCTCGATAACTCAAAAAATACGCCCGGTAGTGATCTTATTTCATTATGGTGAAAGTTGGAACCTCTTACGTGCCGATCAAGTCAAAAGCCTCCGGTCGGAGGCTTTTGACTTTCTGCTATGGAGGTCAGGTATGATTTAAATGGTCAGTGATGAACGCACAGCGAAATGGGGAGCCAAAAAACCCCTCAAGACCCGTTTAGAGGCCCCAAGGGGTTATGCTAGCATAAATCATAAGAAATTCGCGCCATACCTATTAAGACTCCTTATTACGCAGTATGTTAGCAAACGTAGAAAATACATACATAAAGGTGGCAACATATAAAAGAAACGCAAAGACACCACGGAATAAGTTTATTTTGTCACAATCAATAGAAAATTCATATGGTTTACCAGCGCCAAAGACAAAAGGGCGACATTCAACCGATTGAGGGAGGGAAGGTAAATATTGACGGAAATTATTCATTAAAGGTGAATTATCACCGTCACCGACTTGAGCCATTTGGGAATTAGAGCCAGCAAAATCACCAGTAGCACCATTACCATTAGCAAGGCCGGAAACGTCACCAATGAAACCATCGATAGCAGCACCGTAATCAGTAGCGACAGAATCAAGTTTGCCTTTAGCGTCAGACTGTAGCGCGTTTTCATCGGCATTTTCGGTCATAGCCCCCTTATTAGCGTTTGCCATCTTTTCATAATCAAAATCACCGGAACCAGAGCCACCACCGGAACCGCCTCCCTCAGAGCCGCCACCCTCAGAACCGCCACCCTCAGAGCCACCACCCTCAGAGCCGCCACCAGAACCACCACCAGAGCCGCCGCCAGCATTGACAGGAGGTTGAGGCAGGTCAGACGATTGGCCTTGATATTCACAAACGAATGGATCCTCATTAAAGCCAGAATGGAAAGCGCAGTCTCTGAATTTACCGTTCCAGTAAGCGTCATACATGGCTTTTGATGATACAGGAGTGTACTGGTAATAAGTTTTAACGGGGTCAGTGCCTTGAGTAACAGTGCCCGTATAAACAGTTAATGCCCCCTGCCTATTTCGGAACCTATTATTCTGAAACATGAAAGTATTAAGAGGCTGAGACTCCTCAAGAGAAGGATTAGGATTAGCGGGGTTTTGCTCAGTACCAGGCGGATAAGTGCCGTCGAGAGGGTTGATATAAGTATAGCCCGGAATAGGTGTATCACCGTACTCAGGAGGTTTAGTACCGCCACCCTCAGAACCGCCACCCTCAGAACCGCCACCCTCAGAGCCACCACCCTCATTTTCAGGGATAGCAAGCCCAATAGGAACCCATGTACCGTAACACTGAGTTTCGTCACCAGTACAAACTACAACGCCTGTAGCATTCCACAGACAGCCCTCATAGTTAGCGTAACGATCTAAAGTTTTGTCGTCTTTCCAGACGTTAGTAAATGAATTTTCTGTATGGGGTTTTGCTAAACAACTTTCAACAGTTTCAGCGGAGTGAGAATAGAAAGGAACAACTAAAGGAATTGCGAATAATAATTTTTTCATTTAGTATTTCTCCTCTTTAATCTAGTAGCTAAGATCCATTCCCTTTAGTGAGGCTAAATACAGTGGAGAGCGTTCACCGACAAACAACAGATAAAACGAAAGCCAGTCTTTCGACTGAGCCTTTCGTTTTATTTGAAGCTTGACTCCAGCGTAACTGGACTGCAATCAACTCACTGGCTCACCTTCACGGGTGGGCCTTTCTTCGGTAGAAAATCAAAGGATCTTCTTGAGATCCTTTTTTTCTGCGCGTAATCTGCTGCTTGCAAAC
  Score=3482
```
** Note here the deprecation warning: tools are constantly changing which is why it is so important to properly manage software and software dependencies!*






## Summary

Bioinformaticians have built a range of tools to aid bioinformatics analysis in Python. This active community and support is one of the great benefits of working with python!

::: {.callout-tip}
#### Key Points

- API's can be used to interface softwares with Python, and can be used to access common biological databases.
- Biopython is a commonly used package to work with biological data

:::
