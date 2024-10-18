---
title: Escape Room - You are locked in!
---

::: {.callout-warning}
I am a rich billionaire. I have kidnapped you budding bioinformatitions on the systems biology Part III course (with the help of your course organisers) because my mad doctor has run away before telling me my diagnosis.  

I have locked this room! Until you can figure out what it is using the clues my mad doctor has left behind, and can tell me how to treat it, I will not let you out!

**If I die before you can figure it out unfortunately you will be trapped in this room forever....**

The mad doctor told me in an email left to me after he escaped, that the expertise you all have from the introduction to python course, should allow you to follow the clues he has provided in the instructions below and in the encrypted files.

I was advised to get you to compete in three to four teams. A different person must type in each of the tasks with others only being allowed to talk - not type. There will be extra reward clues on offer for the most elegant solutions.

:::

::: {.callout-exercise}
#### Mad Doctor's Instructions

First install the `cryptography` module.

Then import the `decryptor` module provided in `decryptor.py` to your python script.

Only then will you be able to investigate the secret files.

1. The clue to generate the password to open the first secret file is a message encoded:
```
[84, 104, 101, 32, 121, 101, 97, 114, 32, 116, 104, 97, 116, 32, 68, 78, 65, 32, 119, 97, 115, 32, 100, 105, 115, 99, 111, 118, 101, 114, 101, 100, 32, 105, 110]
```

Use the password and the `decrypt()` function to open the file `secret_file_1.txt.enc`. This will decrypt the secret file and return a decrpted copy in your working directory. Use the `help()` function to investigate use of the module and function.

<!--
:::{.callout-hint}
Hint(s) here.
:::
Extra clue is that the list can also be represented as the following:
\x54\x68\x65\x20\x79\x65\x61\x72\x20\x74\x68\x61\x74\x20\x44\x4e\x41\x20\x77\x61\x73\x20\x64\x69\x73\x63\x6f\x76\x65\x72\x65\x64\x20\x69\x6e

:::
-->

<!--
:::{.callout-hint}
Discovered nuclein
:::

-->

<!--
Password: "1869"
-->

2. To find the clue in the `secret_file_1.txt`, load this sequence and pull the characters at the fibonacci numbers. 

The password to decrypt `secret_file_2.tsv.enc` is all lowercase:
(third-word-in-clue) + (first word in the clue) + (6th letter in the 5th word) + (the last word backwards)

<!--
Password = "fatalillnessoraeppa"
-->


3. To find the clue in the second file, read the `secret_file_2.csv`. Multiply the animal_weight by 4, and log transform the madness_index using the natural log. Plot the output as a scatter plot.

The password to decrypt `secret_file_3.txt.enc` is the first 5 letters of the cell type represented - all in Upper case

<!--
:::{.callout-hint}

begins in N
(extra hint at this step to the best team so far - this disease is not cancer/normally curable)
:::

-->

<!--
Password = "NEURO"
-->

4. Plot the equations in `secret_file_3.txt`. This will show you the clue. 

The password to decrypt `secret_file_4.tsv.enc` is an animal all upper case.

<!--
Password = "BAT"
-->

5. Write code to pull out and print the unexpected values in the data to find the clue in secret_file_4.tsv

The password for `secret_file_5.txt.enc` is in the clue. The password is all lower case.

<!--
Password = "virus"
-->

6. Open `secret_file_5.txt`. Put the amino acid sequence contents into a numpy array. Each letter should be in a new element in the array and each line forms a new row. Order the amino acids in alphabetical order. Convert the array to numeric encoding, with A being represented by '0' and the last amino acid by '19'. Plot a heatmap of your matrix.


The family name of the animal species in the heatmap (all lower case) is the clue to decrypt the next file, `secret_file_6.txt.enc`. 

<!--
Password = "canidae"
-->

7. The message clue in `secret_file_6.txt` is encoded as triangular numbers where 'a' = 1 and therefore the first triangular number and 'z' = 26, and therefore the 26th triangular number. Write code to retrieve the message.

The last two words without gaps (all lower case) is the password for the final clue in `secret_file_7.txt.enc`. 

<!--
"throughbites"
-->

For the last clue, load the dictionary in `secret_file_7.txt`. The next word in the clue can be retrieved by using the "key" which equals the current word's "value". The first word in the clue is "If"

:::


<!--

## Section



## Summary

::: {.callout-tip}
#### Key Points

- Last section of the page is a bulleted summary of the key points
:::


-->