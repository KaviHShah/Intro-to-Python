---
title: NumPy Arrays and pandas Dataframes
---

::: {.callout-tip}
#### Learning Objectives

- Be able to work with 'pandas' dataframes and 'NumPy' arrays
- Start to be independent learners
:::


'pandas' dataframes and 'NumPy' arrays are widely used in data science in Python. The documentation for both modules and online resources available are very good. Rather than explaining every single feature, I will instead compare the two modules and when to use them. You will then explore the documentation and find out how to do some common operations in 'pandas' and 'NumPy', with some test data.

## Comparison of 'NumPy' and 'pandas'


| Feature                       | **pandas**                               | **NumPy**                                 |
|-------------------------------|------------------------------------------|-------------------------------------------|
| **Data Structure**            | DataFrame (2D, labelled) and Series (1D) | ndarray (N-dimensional array)             |
| **Data Types**                | Supports mixed data types in columns     | Homogeneous data types in columns                |
| **Indexing**                  | Labelled indexing (row/column labels)     | Integer-based indexing                     |
| **Memory Usage**              | Generally more memory overhead; can be managed by chunking and changing column dtypes | More memory efficient due to contiguous memory; optimized over time |
| **Speed**                     | Slower for numerical operations due to overhead; performance has improved with updates | Faster for numerical operations; optimized for speed in core calculations |
| **Data Manipulation**         | Rich functionality for data manipulation; has expanded over time | Primarily for numerical computation; core functionality remains stable |
| **Handling Missing Data**     | Built-in support for NaN values          | Limited support; must handle manually     |
| **Aggregation**               | Built-in functions for grouping and aggregating | Requires custom functions                  |
| **Data Visualization**        | Built-in integration with visualization libraries | Not designed for direct visualization     |
| **Use Case**                  | Ideal for data analysis with mixed types | Ideal for numerical and scientific computing |
| **Overhead Changes**          | Increased overhead with more features (e.g., complex indexing and grouping operations) | Focus on minimizing overhead while maintaining performance |
| **Chunking Data**            | Supports chunking with functions like `pd.read_csv()` for large datasets | Requires manual implementation; typically works with whole arrays |

Generally speaking 'NumPy' arrays and 'pandas' dataframes are used for very different things, but there is cross functionality. Ultimately it depends on the data and what kinds of operations you want to use it for. 

## The Same Data in 'pandas' and 'NumPy'

**Gene Sequence Length Data (Different Data Types)**

**Using 'pandas'**

```
import pandas as pd

# Example data
data = {
    'Gene Name': ['Gene1', 'Gene2', 'Gene3'],  # Strings
    'Sequence Length': [1200, 1500, 2000],      # Integers
    'Description': ['Long gene', 'Medium gene', 'Short gene']  # Strings
}

df_genes = pd.DataFrame(data)
print("Pandas DataFrame:")
print(df_genes)
```

**Using 'NumPy' Structured Array**

```

import numpy as np

# Define a structured data type
dtype = [('Gene Name', 'U10'), ('Sequence Length', 'i4'), ('Description', 'U15')]

# Create an array with mixed data types
np_genes = np.array([
    ('Gene1', 1200, 'Long gene'),
    ('Gene2', 1500, 'Medium gene'),
    ('Gene3', 2000, 'Short gene')
], dtype=dtype)

print("\nNumPy Structured Array:")
print(np_genes)

```

**converting data to a single type**

::: {.callout-exercise}
#### Encoding
{{< level 2 >}}

Why might you want to convert all the data to the same data type?

How would you encode all the above in a single data type so that it can be held as a standard 'NumPy' array?

:::


**e.g. machine learning**:

Preparing data is crucial for building effective machine learning models. Encoding is when you convert categorical and other data into numerical formats, which algorithms can easily interpret. Common encoding techniques include:

**One-Hot Encoding:** Converts categorical variables into a binary matrix representation, where each category is represented by a unique binary vector.

**Label Encoding:** Assigns each unique category an integer label, which is suitable for ordinal data but can introduce unintended ordinal relationships in nominal data.

**Changing Data Types** involves converting data into formats that are more suitable for analysis.


## 'NumPy' and 'pandas' Documentation

The 'NumPy' and 'pandas' documentation is very good and both modules are very widely used!
For this reason I have not given any more examples here. When you start coding more, you must use the resources and documentation to solve your own challenges.

**Numpy Documentation:**

https://numpy.org/doc/


**Pandas Documentation:**

https://pandas.pydata.org/docs/

https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

::: {.callout-exercise}
#### Uses of pandas and numpy

Look through the docs and discuss the functions of 'pandas' and 'NumPy'.

Give two biological examples of types of data analysis when you would use 'NumPy' arrays and two when you would use 'pandas' dataframes.

For your use cases, what would the most important functions be?

:::

::: {.callout-exercise}
#### Encoding and memory usage

Create the 'pandas' dataframe and 'NumPy' array shown in the above example.

Implement encoding for the 'NumPy' array and 'pandas' dataframe.

Compare the deep size of the arrays and dataframes using functions found in the documentation.

::: {.callout-answer}

```
# Find the size (memory usage) of the DataFrame
df_memory = df.memory_usage(deep=True).sum()  # deep=True gives a more accurate estimate
print(f"Size of Pandas DataFrame: {df_memory} bytes")

# Find the size (memory usage) of the NumPy array
numpy_memory = numpy_array.nbytes
```

:::
:::

::: {.callout-exercise}
#### Numpy Array Task

Load the two DNA sequences in the dataset named DNA-seq.txt into python.

Implement the dot plot in a 'NumPy' array. i.e. place one sequence along the top of a grid and the other along the side and put a 1 in the grid wherever the characters match.

Find the number of non-overlapping matching sequences on sequence1 where there are more than 5 bases matching sequence2 in a row.

Find the number of independent matching sequences where there are more than 10 bases matching in a row. What about more than 20?
i.e. if seq1(i) = seq2(j) and seq1(i+1) = seq2(j+1) then it is part of the same matching sequence. Please ask if this is unclear.

::: {.callout-answer}

Answer code:
```
import numpy as np
import matplotlib.pyplot as plt

with open('DNA-seq.txt', 'r') as file:
    sequences = file.readlines()
    # Assuming the first two lines are the sequences
seq1 = sequences[0]
seq2 = sequences[1]

print(seq1)
print(seq2)
print(len(seq1))
print(len(seq2))

#seq1 = "TAGCTAGCTTGACGCTGATCGGACGCGTTGGTTCGAAG"
#seq2 = "AGTCGGACTTCGCTAGGACTTCGGTCGACCGGACGTGCC"

def create_dot_plot(seq1, seq2):
    try:
        rows = len(seq1)
        cols = len(seq2)
        dot_plot = np.zeros((rows, cols), dtype=int)

        for i in range(rows):
            for j in range(cols):
                if seq1[i] == seq2[j]:
                    dot_plot[i][j] = 1

        return dot_plot

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

dot_plot = create_dot_plot(seq1, seq2)
print(dot_plot)
#plt.imshow(dot_plot)
#plt.show()


def count_matching_regions(seq1, seq2, min_length):
    count = 0
    match_length = 0
    dot_plot = create_dot_plot(seq1, seq2)

# I have purposely not commented this code very well - try to figure out what I am doing - the prints commented out may help you
    try:

      for i in range(len(seq1)):
        j = 0
        #print(i)
        while j <= (len(seq2)-1) and i <= (len(seq1)-1):
                #print(i,j)
                if dot_plot[i,j] == 1:
                  match_length += 1
                  i += 1
                  j += 1
                else:
                  i += 1
                  j += 1

                # Check if we are at the end of the sequences or next characters don't match
                  if (match_length > 0) or i == len(seq1) or j == len(seq2):
                      if match_length >= min_length:
                          count += 1
                          #print(count)
                          match_length = 0  # Reset match length after counting
                      else:
                          match_length = 0  # Reset if there is no match

      for j in range(1,len(seq2)):
        i = 0
        while j <= (len(seq2)-1) and i <= (len(seq1)-1):
                #print(i,j)
                if dot_plot[i,j] == 1:
                  match_length += 1
                  i += 1
                  j += 1
                else:
                  i += 1
                  j += 1

                # Check if we are at the end of the sequences or next characters don't match
                  if (match_length > 0) or i == len(seq1) or j == len(seq2):
                      if match_length >= min_length:
                          count += 1
                          #print(count)
                          match_length = 0  # Reset match length after counting
                      else:
                          match_length = 0  # Reset if there is no match

      return count


    except Exception as e:
        print(f"An error occurred: {e}")

        return None

matching_20 = count_matching_regions(seq1, seq2, 20)
matching_10 = count_matching_regions(seq1, seq2, 10)
print(f"Number of matching regions with length >= 20: {matching_20}")
print(f"Number of matching regions with length >= 10: {matching_10}")


```

Answer output:

```

TAGCTAGCTTGACGCTGATCGGACGCGTTGGTTCGAAGCTTGAGATTCATAGCTGGGCGTACCTTACCCGTTGAAGACGACTTCCGAAAGGTTTAGGAACGTGCTACGAGTGTATCGGGACGTAACGGGATGACTGTAGACTATGGTTTCGGGGTGTAGGCGGCTTTGAACTCCGAGAAACCTGAGTGGCGACTTAGCCCGCCGTGTCGAATAGGAGCTCAGTTCATTCAGGATCGTCTTGGCGTTGGCAGTACGGCTCCCGGGGTCCGTCGAGGGTCACGTCGGTCCGAGCTGCTTTCCCGATATGCTACTTCGCCCGTCACTAGGTGTTTCGACCGATCGCTGGTACGCTCAGTGAGGTTGCCAGGCGTGAAACTACGCTTAGGCTTGCCGAGTGCTCCTTAGAGGTGCACCAGTAGGCGCGCGTATTGACTTACGACTTCTGTGTGACGCGAGCGACATAGCGCGCGTGGACTACAGCCTGGATCGGGCTGCGACTTGGTTGTGCAGTCGACGTGGCAGGATTGTGATCGACGATTCTTACCCGGGGTTCGACTAGGACTTTGACTGCGGTAGCCCTTGGGGAGGTTGCGGAGAGGACGACTTGGTGAGCCCGATTGATGCTGAGTCGCCAGGCTTGGGGACTTGATCGGACTTCGTAGCCGACTTGCGAGCTCGGTGCTGAGGCGGATGCTCGACTCGAGTAGGGGGTCGATCCGAGCGGTTAGGCGACCGACGTACGTGTTGGGTCGCGATGGCAGAGTGGGGCGACAGTACCGCTGTTGGCACGGACGTTAGTCGATGGGTGACCCGGCTCAGTCTTGTGATCGACTGATGCGGGTAGTACCTTGGACTACGATCGCGGGTGCGTGACTTCCGACGACCGCTTAGGCCGAGTACGTTGTGCTTCACGTCAGCGGTGCTGGGGACCGTCAGCGGACTTACGTTGAGTTGCGGTAGTTTGCACGGTGCTGAGTCCGGACTTCGACTGAGTAGGTTGGTCAGCGACTCGATGACGTCGGTTGCGGTTCGAGGTCGCGTGGGACTGCGCTGTAGCCGACTTGCTTGCTGCGTGTGGTGAGTAGCCGATTCGGTGACGTCGTACGAGTTCAGCGTCTTGCGCGTAGGTTGGACTGAGTGCACCGGAGGTTCGGCTAGCGTTGCGTTGCCGTAGGTTCGAGGACTTGGACCGCGCTGAGGTTACGGACGTTGACTTACGGACCGGTGACTGACGAGGACCGGTTCGCTGGAGTCGAGTACCGACGCTGAGTGCAGCGGCTGCGTACGGACTTGCGCGGCGACTGTGGACGTGACTAGCTAGCGTCAGCTTGAGTAGCGGTGCAGCTAGCGGCGACGACTTGCGTAGGTCGTTGGGTGCTGCTGCGCTTACGGACCGGTTGTAGGACTTGCGGTACGACTGCGCGTGAGTTGGACTTCGGTCGTGCGTGACTTGCGGGACTTGGGCTTGCCGTAGTTCGACTGCTGACTGGACGTAGGTCTTGACTGAGCGGACTTGACCGGCGTAGGCGGCTTGCGACTAGCTTGAGGCTTGACTGGACTTAGCGCGGACTTGCGTCAGTCGGACTTGGTTGCGACCTGACCTGGACGTAGGTCGACGTTGACCGCGTGGACTTCGATAGCGAAGCTTGACTCGAGCGGACTTGGCAGGACTGCGTAGGTTGAGTGGACTTGGGCGTGTGGCGTGGACTTGGGTGGACTTGGGCTCGACTTGGCAGGTTCGACGTCAGGTCGCGGTCGATCAGCGGACTGTTGAGCTGACTTGCTGACGTGAGTGGACTTGGTCGACTCGCGTGACTGCGGTAGGCTTCGACTGCGCGTAGTCGTAGGCGTGGTTACGGGTTCGCTGCGTGTTGGTCGACGTGCTGGACTTCGCGGACTCGCTCGATGCGTGGTCGTGGCGTCGGTCGAGTGGACTCGTCGGTAGGTGTGGTGGCTGCGTAGCGGACTTGCGTGTAGTTGACTGCGGTAGGTGACCGTAGCTGTAGTGGGTCTGAGCTTGAGGTTCGCGAGTTCGTGTGGTTGGCTAGGACTTGGCTTAGGTGCGACTGCGTCGATCGACTGGGTTCGCTGCGTAGTTGGGTTGACGTGTACGACGCGACTAGCTTGGGACTTGTGACGAGCGGTAGCGTCAGACTCGGAGTTCGACGCTGAGCTGAGCGGACTTTGACTGCGCGTGGCTCGGCTCGACCGTGCGGGACTTACGTACAGTTGTAGCTGGTTGGGACTTGGACTCGGTTTCGCGACTTACGTCGGACTTTGACTTGCGACTCGCTTAGTGGTCGACTGCGTCGGCTTGGAGCGGACTTAGCTCGGACTTTGGTGCGGCTTGCGTAGTTGGTCGTAGCGGATGTCGGACTCGTGGTTTGGGACTTTAGCGGACTTTAGCGGACTCGTGTGGTTTACGCTCGTGTGGTGTCGGTGGACTGTCGGTGCGGTCTGACTCGGCTTGCTCGGCTTGGTGACGTAGCGTCGTGTTCGTGACGTCGGTAGTAGCTGCTGAGTACGTTCGGGACGATGACGTTGGCTAGTTGACGTGGACTTGGAGGTTCGGTAGCGTGGGCGACTTGAGGTCGAGGCTCGTACGGGTTAGCGCTCGATTCGGTGTACGGGCTCGACTTGACTTACCGTGGGTGTGCGCTGTTGTGTGGCTTGTGACGGTTGTGGAGTTGCTGCTTGAGTGCGCGACGTGGCGTTGACTCGGACGTGGACGTGGCTCGAGTGGCGTAGTGTGGACTGGGCTTGACTCGCGCGTGGACTTGGTGCGTCGTAGTCTGACTGCGCGACTGAGCGACTTGAGTTGGTCGTAGCTTGGTGGCTTGAGCGGTGGACTTGACGTGGCTTGAGTGCGACTTGGTGGCTTGCT

AGCTGCGTAGCTGACGGACGTCGCTTAGGGTGCGACGTAGTCGGACTTCGCTAGGACTTCGGTCGACCGGACGTGCTGACTGCGACCGACTCGGACGTAGCTCGCTAGTCGCTAGTCGGGACGACTGCGGACTAGTCGTGACTTGCGCGACTTGACTGCTCGGACCGACTTAGCTGTCGTAGCTGCGTAGGACCGTCGCGACTTCGGACTTCGTCGACGGACTCGACTGGGCTCGACTCGGTCGACCTGGTGGCGGACTGCGCGTAGGACTGCGCGTGGACTTGGACTGCGCTCGACGTACGACCGTTGAGGTCGCGACTGCGCGTGGTTGACCGGTTGTAGGACCGTTTGCGACCGTACGGTGCTAGCTTGGCTCGGCTAGGACTTGCGACTCGTCGTGCTGCGCTGGTCGACCGTAGCTGACCGACTCGTAGTTCGACGACTTGAGGTCGACTCGCGCGGACGTTCGACCGGCGACTGGACTTGGACTCGGCTCGACTGACGTGGCGGACTTGACTTCGCTGGTAGCGTGACTGCGCGACTCGGACTTAGCTCGTAGTACGTACGGTAGTCGCTGGTGGTCGACGGCGTAGTTCGACTGCGCTGGTCGGTTCGACCGTACGCTGCTCGTAGACTTCGACGGGTTACGTAGTGGTCGACTTGCGCGCTGCGTAGTCGCGTAGCTCGACGTACGAC

2885
697
[[0 0 0 ... 0 0 0]
 [1 0 0 ... 1 0 0]
 [0 1 0 ... 0 0 0]
 ...
 [0 0 1 ... 0 1 0]
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 1]]
Number of matching regions with length >= 20: 0
Number of matching regions with length >= 10: 62

```

alternatively another possibly better approach is:
```
import numpy as np
import matplotlib.pyplot as plt
with open('DNA-seq.txt', 'r') as file:
    sequences = file.readlines()
    # The first two lines are the sequences
seq1 = sequences[0].strip()
seq2 = sequences[1].strip()

def count_matching_regions_2(seq1, seq2, min_length):
  try: 
    rows = len(seq1)
    cols = len(seq2)
    dot_plot = np.zeros((rows, cols), dtype=int)

    #Make the dot plot
    for i in range(rows):
        for j in range(cols):
            if seq1[i] == seq2[j]:
                dot_plot[i][j] = 1

    unique_strings_plot = dot_plot.copy()
    #print(unique_strings_plot)

    for i in range(1,rows):
        for j in range(1,cols):
          if unique_strings_plot[i][j] == 1:
            unique_strings_plot[i][j] = 1 + unique_strings_plot[i-1][j-1]
          else:
            continue

    count = np.sum(unique_strings_plot == min_length)

    return dot_plot, count

  except Exception as e:
        print(f"An error occurred: {e}")
        return None, None

dot_plot, count_20 = count_matching_regions_2(seq1, seq2, 20)
dot_plot, count_10 = count_matching_regions_2(seq1, seq2, 10)
dot_plot, count_5 = count_matching_regions_2(seq1, seq2, 5)

print(f"Number of matching regions with length >= 20: {count_20}")
print(f"Number of matching regions with length >= 10: {count_10}")
```

This should output the same answer


:::
:::

::: {.callout-exercise}
#### Working with data in 'pandas'

Find the dataset of human genes I generated from the 'humanmine' database `humanmine_results_2024.tsv` . 

In reality you should almost ALWAYS plot your dataset to see what it looks like before doing any analysis. In the next section we will explore plotting, however for this exercise:

* Load in the data in the CSV into a 'pandas' dataframe

* What does the dataset show?

* Inspect the data - what might you need to do to clean up the data?

* Clean up the data

* What is the average gene length?

* What is the standard deviation around the mean?

* What is the most common ontology term name?

* How many unique genes are there?

* Make a list ordered by gene size

* How many cytoplasmic genes are there?

* How many nuclear genes are there?

* How many genes are both nuclear and cytoplasmic?

* How many membrane proteins are there?

Extra task: 
Mess up this dataset to make it a bit closer to what you might see in real life. Now try to work with it in python.

::: {.callout-answer}

```
import pandas as pd

# Step 1: Load the data (TSV file)
file_path = 'humanmine_results_2024.tsv'  # replace with the actual file path
df = pd.read_csv(file_path, sep='\t')  # Read as a TSV (tab-separated values)

# Step 2: Inspect the data
print("First 5 rows of the dataframe:\n", df.head())
print("\nDataFrame Info:\n", df.info())
print("len df",len(df))

# Step 3: Clean the data
# 1. Drop any columns with entirely irrelevant data (e.g., "NO VALUE")
print("cleaning data")
df = df.drop_duplicates()
print(len(df)) # no rows are dropped


# Drop columns with only NaN values
df = df.dropna(axis=1, how='all')

#also drop unwanted columns

df = df.drop(columns=['Gene.secondaryIdentifier'])

df.style.set_table_attributes('style="width:100%; border: 1px solid black;"')

# you could process this more but for now I'll move onto the second step which is to find the average gene length
# I will make a deepcopy
df_meanlen = df.copy(deep=True)
#we can remove the unnecessary columns 
df_meanlen = df_meanlen.drop(columns=['Gene.goAnnotation.ontologyTerm.identifier', 'Gene.goAnnotation.ontologyTerm.name'])
# we can drop all the duplicates where the primary identifier is the same
df_meanlen = df_meanlen.drop_duplicates(subset=['Gene.primaryIdentifier'])
# we can drop all the rows where there is a NaN in the Gene.length column
df_meanlen = df_meanlen.dropna(subset=['Gene.length'])
# drop any rows with zero values in genelength
df_meanlen = df_meanlen[df_meanlen['Gene.length'] != 0]
# we might now check to see how many NaN values there are in gene description
print('empty brief description rows',df_meanlen['Gene.briefDescription'].isna().sum())
# we can calculate mean now. 
#As a biologist - I know that some of these are possibly alternate isoforms of the same protein.
#make sure all the types in the gene.length column are the same:
print('unique types in length column',df['Gene.length'].apply(type).unique())
#all floats


# What is the average gene length?
average_gene_length = df_meanlen['Gene.length'].mean()
print(f"Average gene length: {average_gene_length}")

# What is the standard deviation around the mean gene length?
std_dev_gene_length = df_meanlen['Gene.length'].std()
print(f"Standard deviation of gene length: {std_dev_gene_length}")
# If you had plotted the dataset you might use these to figure out the bounds to exclude outliers

#What is the most common ontology term name?
most_common_ontology = df['Gene.goAnnotation.ontologyTerm.name'].mode()[0]
print(f"Most common ontology term name: {most_common_ontology}")

#How many unique genes are there?
#for this one I am going to enforce that both the primary identifier and cytolocation must be unique. (just because I can) 
#We will therefore also drop the ones with no cytolocation 
df_unique = df.copy(deep=True)
df_unique_id = df_unique.drop_duplicates(subset=['Gene.primaryIdentifier'])
print('unique-genes by primary identifier =', len(df_unique_id))
df_unique_cyt = df_unique_id.drop_duplicates(subset=['Gene.cytoLocation'])
print('unique-genes by dropping those with the same cytolocation by keeping those with none =', len(df_unique_cyt))
df_unique_cyt = df_unique_cyt.dropna(subset=['Gene.cytoLocation'])
unique_genes = len(df_unique_cyt)
print(f"Number of unique genes: {unique_genes}")

#Make a list ordered by gene size
sorted_by_size = df_unique.sort_values(by='Gene.length', ascending=False)
print("List of genes ordered by size:\n", sorted_by_size[['Gene.primaryIdentifier', 'Gene.length']])


#How many cytoplasmic genes are there? 
cytoplasmic_genes = df[df['Gene.goAnnotation.ontologyTerm.name'].str.contains('cyto', case=False, na=False)] #note the difference when cytoplasm is used
cytoplasmic_count = cytoplasmic_genes['Gene.primaryIdentifier'].nunique()
print(f"Number of cytoplasmic genes: {cytoplasmic_count}")

#How many cytoplasmic genes are there? 
nuclear_genes = df[df['Gene.goAnnotation.ontologyTerm.name'].str.contains('nucle', case=False, na=False)] #note the difference when nucleus is used
nuclear_count = nuclear_genes['Gene.primaryIdentifier'].nunique()
print(f"Number of nuclear genes: {nuclear_count}")

#How many genes are both nuclear and cytoplasmic?
cyto_nuclear_genes = pd.merge(cytoplasmic_genes, nuclear_genes, on='Gene.primaryIdentifier')
cyto_nuclear_count = cyto_nuclear_genes['Gene.primaryIdentifier'].nunique()
print(f"Number of genes that are both nuclear and cytoplasmic: {cyto_nuclear_count}")

#How many membrane proteins are there?
membrane_proteins = df[df['Gene.goAnnotation.ontologyTerm.name'].str.contains('membrane', case=False, na=False)]
membrane_protein_count = membrane_proteins['Gene.primaryIdentifier'].nunique()
print(f"Number of membrane proteins: {membrane_protein_count}")
```
output

```
First 5 rows of the dataframe:
                  Gene.briefDescription Gene.cytoLocation  Gene.description  \
0  1,4-alpha-glucan branching enzyme 1            3p12.2               NaN   
1  1,4-alpha-glucan branching enzyme 1            3p12.2               NaN   
2  1,4-alpha-glucan branching enzyme 1            3p12.2               NaN   
3  1,4-alpha-glucan branching enzyme 1            3p12.2               NaN   
4  1,4-alpha-glucan branching enzyme 1            3p12.2               NaN   

   Gene.length  Gene.primaryIdentifier  Gene.score Gene.secondaryIdentifier  \
0     271943.0                    2632         NaN          ENSG00000114480   
1     271943.0                    2632         NaN          ENSG00000114480   
2     271943.0                    2632         NaN          ENSG00000114480   
3     271943.0                    2632         NaN          ENSG00000114480   
4     271943.0                    2632         NaN          ENSG00000114480   

  Gene.symbol Gene.goAnnotation.ontologyTerm.identifier  \
0        GBE1                                GO:0003844   
1        GBE1                                GO:0004553   
2        GBE1                                GO:0005515   
3        GBE1                                GO:0005737   
4        GBE1                                GO:0005829   

                 Gene.goAnnotation.ontologyTerm.name  
0         1,4-alpha-glucan branching enzyme activity  
1  hydrolase activity, hydrolyzing O-glycosyl com...  
2                                    protein binding  
3                                          cytoplasm  
4                                            cytosol  
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 277531 entries, 0 to 277530
Data columns (total 10 columns):
 #   Column                                     Non-Null Count   Dtype  
---  ------                                     --------------   -----  
 0   Gene.briefDescription                      276807 non-null  object 
 1   Gene.cytoLocation                          277301 non-null  object 
 2   Gene.description                           0 non-null       float64
 3   Gene.length                                276835 non-null  float64
 4   Gene.primaryIdentifier                     277531 non-null  int64  
 5   Gene.score                                 0 non-null       float64
 6   Gene.secondaryIdentifier                   277334 non-null  object 
 7   Gene.symbol                                277531 non-null  object 
 8   Gene.goAnnotation.ontologyTerm.identifier  277531 non-null  object 
 9   Gene.goAnnotation.ontologyTerm.name        277525 non-null  object 
dtypes: float64(3), int64(1), object(6)
memory usage: 21.2+ MB

DataFrame Info:
 None
len df 277531
cleaning data
277531
empty brief description rows 5
unique types in length column [<class 'float'>]
Average gene length: 67511.68010812004
Standard deviation of gene length: 132916.7867771459
Most common ontology term name: protein binding
unique-genes by primary identifier = 18221
unique-genes by dropping those with the same cytolocation by keeping those with none = 1221
Number of unique genes: 1220
List of genes ordered by size:
         Gene.primaryIdentifier  Gene.length
55205                    54715    2473592.0
55207                    54715    2473592.0
55216                    54715    2473592.0
55215                    54715    2473592.0
55214                    54715    2473592.0
...                        ...          ...
277526                    4541          NaN
277527                    4541          NaN
277528                    4541          NaN
277529                    4541          NaN
277530                    4541          NaN

[277531 rows x 2 columns]
Number of cytoplasmic genes: 9283
Number of nuclear genes: 8343
Number of genes that are both nuclear and cytoplasmic: 5249
Number of membrane proteins: 9445

``` 


:::
:::


## Summary

'NumPy' and 'pandas' are both useful packages for working with different types of biological data.
Now you should be able to choose which to use and be comfortable attempting to manipulate data with them

::: {.callout-tip}
#### Key Points

- 'pandasp is better for data manipulation and analysis where data is in multiple types. 
- 'NumPy' is better for numerical and array operations and is generally quicker.
- The documentation is a good tool to use to learn 'pandas' and 'NumPy'

:::
