---
title: Working with Files in Python
---

::: {.callout-tip}
#### Learning Objectives

- Be able to read and write files in Python
- Understand how to use the `with` method and a context manager to work with files
- Introduce 'garbage collection' in python

:::

Working with files is simple in python. Many packages have their own built-in file reading and writing functions including for example 'pandas' which we will look at next.
Here we use the built-in `open` function.   

## Working Directory

A **working directory** is the directory within the file system where your program will use as a default to look for and read files or output files. It easier than always defining absolute file paths and can allow code to be transferred.

When running python scripts from the console, the working directory is the one where you launched the script from. 

The **`os`** module can be used in Jupyter Notebooks to check the working directory and change it.

Get working Directory:

```
import os
print(os.getcwd())  #current working directory
```

Change working Directory:

```
os.chdir('/path/to/directory')
```

You can also use the magic command:

```
%cd /path/to/directory
```

Magic commands in Jupyter Notebooks can be super useful. We will not look at them further here, but also note that they cannot be used ouside the iPython Kernel


You can also set default working directory in the config file. We will not go over this here (and I myself tend not to work this way - although I also don't often use Jupyter Notebooks).

I recommend having scripts and data in the same directory, or a subdirectory of the project directory. My common setup might be:

```
/home/user/project/
    ├── data/
    │   └── dataset.csv
    ├── scripts/
    |   └── analysis.py
    ├── logs/
    │   └── error-log.log
    │   └── output-log.log
    └── output/
        └── output.csv
```

## Opening and closing files in python

You can open files in different modes using the `open()` function. The common modes include:

- `'r'`: Read (default)
- `'w'`: Write (overwrites the file if it exists)
- `'a'`: Append (adds content to the end of the file)
- `'b'`: Binary mode (for non-text files)
- `'x'`: Exclusive creation (fails if the file already exists)

Example:

```
# Open the file in read mode
file = open('dna_sequence.txt', 'r')

# Read the contents of the file into a string
dna_sequence = file.read()

# Close the file
file.close()

# The dna_sequence variable now holds the content of dna_sequence.txt
print(dna_sequence)  # This will display the content of the file

```

`file.readlines()` will return a list with each line:

```
file = open('dna_sequences.txt', 'r')
dna_sequences = file.readlines()
file.close()
```

**Using `for` loops to iterate line by line:**

```
file = open('dna_sequences.txt', 'r')
for line in file:
    # Strip trailing whitespace or newline characters from the end of each line
    dna_sequence = line.strip()
    print(dna_sequence)  # Process or print the current line
file.close()
```
This method is memory-efficient, especially for large files, since it doesn't load the entire file into memory at once.

Consider the problems with working with files this way:

::: {.callout-exercise}
#### Discussion: Exceptions after `open()`
{{< level 2 >}}

If an exception occurs after `open()` what will happen? What have you already learnt as a method to stop this?

::: {.callout-answer}

The file will never close properly - you could use `try` ,`except` , `finally`. The `with` statement presented in the next section is a better way to deal with this.

:::
:::


## Using `with` when working with files:

Using the `with` statement is a better way to work with files in Python as it ensures that files are properly opened and closed. 

Example:

```
with open('dna_sequence.txt', 'r') as file:
    for line in file:
        # Strip the newline character from each line and print it
        dna_sequence = line.strip()
        print(dna_sequence)

```

Note it uses the same kind of syntax as for loops and conditionals


`with` does this by working with a context manager. The open() function returns a fileobject which has the `.__enter___()` and `.__exit__()` methods. You can read more about this in your own time.  

## Aside: Garbage collection

Garbage collection frees memory by cleaning up objects and variables that are no longer needed.

Python does this automatically through reference counting and generational garbage collection. 

You can interact with this using the `gc` module.

## Writing to a file

The same methods are used to write to a file:

**Write to a new file or replace an existing file**

Writing to a new file or overwriting an existing file is simple:
```
with open('sequences.txt', 'w') as file:
    file.write("ACGTGCTTCCAAACGTA\n")
    file.write("ACGTGCTTCCAAACGTA\n")

```
`file.writelines():` Takes an iterable (like a list) and writes each item to the file. You can also use `for` loops.

- the `\n` is needed when manually adding lines.

**Appending to an existing file**

This is exactly the same however you need to replace `'w'` with `'a'` for append mode. 

**binary files** 
Use the `'wb'` for writing binaries for example.


::: {.callout-exercise}
#### Reading and writing files
{{< level 2 >}}

Use the above to first write something to a file. Then read and append to the file.

:::



## Moving files

The `shutil` module can be used to move files in python.

```
import shutil
import os

# Define paths
source_file = 'source_folder/file.txt' 
destination_file = 'destination_folder/file.txt' 

# Create the destination folder if it doesn't exist
os.makedirs(os.path.dirname(destination_file), exist_ok=True)

# Move the file
shutil.move(source_file, destination_file)


```

The same can be used to move directories

## Summary

It is important to be able to manipulate files in python. 
Many packages like pandas come with functions to read and write specific file types.
See the following file types and modules to work with them:

| **File Type**      | **Extension(s)**       | **Description**                                                      | **Modules**                         |
|---------------------|-----------------------|----------------------------------------------------------------------|-------------------------------------|
| **Text File**       | `.txt`                | Plain text files that contain unformatted text.                     | Built-in `open()`, `io`            |
| **CSV File**        | `.csv`                | Comma-separated values, files used to store tabular data.            | `csv`, `pandas`                    |
| **TSV File**        | `.tsv`                | Tab-separated values, files used to store tabular data, similar to CSV. | `csv`, `pandas`                    |
| **JSON File**       | `.json`               | JavaScript Object Notation, a lightweight data interchange format.  | `json`, `pandas`                   |
| **XML File**        | `.xml`                | Extensible Markup Language, used to store structured data.           | `xml.etree.ElementTree`, `lxml`    |
| **Excel File**      | `.xls`, `.xlsx`       | Microsoft Excel files for storing spreadsheet data.                  | `pandas`, `openpyxl`, `xlrd`       |
| **Pickle File**     | `.pkl`, `.pickle`     | Serialized Python objects for saving and loading Python data types.  | `pickle`                           |
| **SQLite Database** | `.sqlite`, `.db`      | Lightweight database files used with SQLite, a C-based database engine. | `sqlite3`, `pandas`               |
| **HDF5 File**       | `.h5`, `.hdf5`        | Hierarchical Data Format for storing large amounts of data efficiently. | `h5py`, `pandas`                   |
| **Parquet File**    | `.parquet`            | Columnar storage file format optimized for use with big data processing. | `pyarrow`, `pandas`                |
| **Zarr File**       | `.zarr`               | Chunked, compressed N-dimensional arrays for large datasets, designed for cloud storage. | `zarr`, `xarray`                   |
| **HTML File**       | `.html`, `.htm`       | HyperText Markup Language files used for web pages.                  | `html.parser`, `BeautifulSoup`     |
| **Markdown File**   | `.md`                 | Plain text files formatted using Markdown for easy reading and writing. | `markdown`, `Mistune`              |
| **Log File**        | `.log`                | Text files that record events or messages from applications.         | Built-in `open()`, `logging`       |
| **Image Files**     | `.jpg`, `.jpeg`, `.png`, `.gif` | Common image formats for graphics.                    | `PIL`, `OpenCV`, `imageio`         |
| **Audio Files**     | `.mp3`, `.wav`, `.ogg` | Common audio formats for music and sound.                           | `pydub`, `wave`, `soundfile`       |
| **Video Files**     | `.mp4`, `.avi`, `.mov` | Common video formats for visual media.                              | `moviepy`, `opencv`, `imageio`     |
| **Archive Files**   | `.zip`, `.tar`, `.gz` | Compressed files for reducing file size and bundling multiple files. | `zipfile`, `tarfile`, `shutil`     |
| **PDF File**        | `.pdf`                | Portable Document Format, used for presenting documents.            | `PyPDF2`, `pdfplumber`, `reportlab` |
| **FASTA File**      | `.fasta`, `.fa`       | Text-based format for representing nucleotide or peptide sequences.   | `BioPython`                        |
| **GenBank File**    | `.gb`, `.gbk`         | Format for storing genomic data, including sequence and annotation.   | `BioPython`                        |
| **Alignment File**  |`.maf         `        | Files that store multiple sequences aligned against each other.       | `BioPython`                       |


::: {.callout-tip}
#### Key Points

- It is essential to be able to work with different file types
- It is better to use the `with` method when working with files to handle opening and closing files
- Many modules can be used to work with different file types
 
:::
