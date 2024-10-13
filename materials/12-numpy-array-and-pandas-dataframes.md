---
title: Numpy Arrays and Pandas Dataframes
---

::: {.callout-tip}
#### Learning Objectives

- Work with pandas dataframes and numpy arrays
- Start to be independent learners
:::


Pandas dataframes and numpy arrays are widely used in data science in python. The documentation for both and reseources available are very good. Rather than explaining every single feature, what I will do is compare the two modules and whhen to use them. Then I will ask you to explore the docs and find out how to do some common operations in pandas and numpy, with some test data.

## Comparison of NumPy and Pandas


| Feature                       | **Pandas**                               | **NumPy**                                 |
|-------------------------------|------------------------------------------|-------------------------------------------|
| **Data Structure**            | DataFrame (2D, labeled) and Series (1D) | ndarray (N-dimensional array)             |
| **Data Types**                | Supports mixed data types in columns     | Homogeneous data types in columns                |
| **Indexing**                  | Labeled indexing (row/column labels)     | Integer-based indexing                     |
| **Memory Usage**              | Generally more memory overhead; can be managed by chunking and changing column dtypes | More memory efficient due to contiguous memory; optimized over time |
| **Speed**                     | Slower for numerical operations due to overhead; performance has improved with updates | Faster for numerical operations; optimized for speed in core calculations |
| **Data Manipulation**         | Rich functionality for data manipulation; has expanded over time | Primarily for numerical computation; core functionality remains stable |
| **Handling Missing Data**     | Built-in support for NaN values          | Limited support; must handle manually     |
| **Aggregation**               | Built-in functions for grouping and aggregating | Requires custom functions                  |
| **Data Visualization**        | Built-in integration with visualization libraries | Not designed for direct visualization     |
| **Use Case**                  | Ideal for data analysis with mixed types | Ideal for numerical and scientific computing |
| **Overhead Changes**          | Increased overhead with more features (e.g., complex indexing and groupby operations) | Focus on minimizing overhead while maintaining performance |
| **Chunking Data**            | Supports chunking with functions like `pd.read_csv()` for large datasets | Requires manual implementation; typically works with whole arrays |

Generally speaking numpy arrays and pandas datframes are used for very different things, but there is cross functionality. Ultimately it depends on the data and what kinds of operations you wantto use it for. 

## The Same Data in Pandas and Numpy

**Gene Sequence Length Data (Different Data Types)**

**Using Pandas**

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

**Using Numpy Structured array**

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

How would you encode all the above in a single data type so that it can be held as a standard numpy array?

:::


**e.g. machine learning**:

Preparing data for is crucial for building effective machine leaarning models. Encoding is when you convert categorical and other data into numerical formats, which algorithms can easily interpret. Common encoding techniques include:

**One-Hot Encoding:** Converts categorical variables into a binary matrix representation, where each category is represented by a unique binary vector.

**Label Encoding:** Assigns each unique category an integer label, which is suitable for ordinal data but can introduce unintended ordinal relationships in nominal data.

**Changing Data Types** involves converting data into formats that are more suitable for analysis.


## Numpy and Pandas Documentation

The numpy and pandas documentation is very good and they are very widely used!
For this reason it is somewhat pointless for me to take examples and write them here. When you start coding more, you must use the resources and documentation to solve your own challenges.

**Numpy Documentation:**

https://numpy.org/doc/


**Pandas Documentation:**

https://pandas.pydata.org/docs/

https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf

::: {.callout-exercise}
#### Uses of pandas and numpy

Look through the docs and discuss the functions of pandas and numpy.

Give two biological examples of types of data analysis when you would use numpy arrays and two when you would use pandas dataframes.

For your use cases what would the most important functions be?

:::

::: {.callout-exercise}
#### Encoding and memory usage

Create the same pandas dataframe and numpy array shown in the above example

Implement encoding for the numpy array and pandas dataframe.

Compare the deep size of the arrays and dataframes using functions found in the docs.

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

Load the two DNA sequences in the dataset named numpy_dnaseq.txt into python.

Implement the dot plot in a numpy array. i.e. place one sequence along the top of a grid and the other along the side and put a 1 in the grid wherever the characters match.

Find the number of non-overlapping matching sequences on sequence1 where there are more than 5 bases matching sequence2 in a row. 

Write a function that has two sequences and the minimum matching length (e.g. 5 in the last example) as inputs. It should output the number of matching regions that meet this criteria in the two sequences. 

::: {.callout-answer}

Answers will be provided after you complete the exercise

:::
:::

::: {.callout-exercise}
#### Working with data in Pandas

Find the dataset of human genes I generated from the humanmine database `humanmine_results_2024.tsv` . 

In reality you should almost ALWAYS plot your dataset to see what it looks like before doing any analysis. In the next section we will explore plotting, however for this exercise:

* Load in the data in the CSV into a pandas dataframe

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
I have made this dataset a bit closer to what you might see in real life. Now try to work with it.

::: {.callout-answer}

Answers will be provided after the session

:::
:::


## Summary

Numpy and pandas are both useful packages for working with different types of biological data.
Now you should be able to choose which to use and be comfortable attempting to manipulate data with them

::: {.callout-tip}
#### Key Points

- Pandas is better for data manipulation and analysis where data is in multiple types. 
- Numpy is better for numerical and array operations and is generally quicker.
- The documentation is a good tool to use to learn Pandas and Numpy

:::
