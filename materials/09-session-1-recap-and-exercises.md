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

Today we have a range of exciting topics to cover however the style of teaching will be a little different from the first day. 
There will be fewer notes and you will use the documentation pages and other resources more to help you. There will be much more self-learning involved.
This is a little closer to how things will be when you are undertaking projects on your own. 

Before we go on to the new parts have a try at this exercise to test how familiar you are with the content from the last session:

Answers will be uploaded after the session

::: {.callout-exercise}
#### Phenotypes and Genes

Write a global variable which has the DNA to RNA transitions as a dictionary, and a global variable that has the DNA to amino acid transitions as a dictionary. 

1. Initiaise a class gene which 

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
- modify_sequence: to alter a base of the DNA sequence at 'x' position and update the length, RNA, and protein sequence
- print the attributes

2. Write a list of 10 made-up gene names

3. Using a 'for loop'/'list comprehension', and a random number generator, generate a dictionary of the 10 DNA sequences of 100 bases associated with the gene_names.
note:
```
import random
random.choices(options_list) #will make random choices on an options list
random.choices(options_list, k=100) # can be used to generate 100 outputs in one go
```
4. Use the dictionary to initialise 10 gene objects.


5. Initialise a class phenotype which is made up of:

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

6. Use a 'for loop' to initialise three phenotypes.

7. What is the size of the gene objects and phenotype objects using `sys.getsizeof()`?

8. What does this tell you about the sys.getsizeof() function?


9. Modify the sequence of one of the geneobjects - does the phenotype object change as seen when you print all the attributes.

10. Make a deep copy of a gene object and show that it is a deep copy. 

::: {.callout-answer}

Answers to be added here shortly

:::
:::

## Conclusion

Hopefully that was a fun exercise to go over everything we have done so far! Let's now move on to today's topics.

::: {.callout-tip}
#### Key Points

- By completing the above exercise, you should be able to independently apply the concepts covered yesterday
- If there is anything you found difficult, go back to the relevant sections and recap the material

:::
