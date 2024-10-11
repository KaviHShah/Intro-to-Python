---
title: Conditionals and Loops in Python
---

::: {.callout-tip}
#### Learning Objectives

- Work with conditional statments and loops in python 
- Handle errors (exceptions) and edge cases in programs
- Compare different methods 
:::

## Conditionals

Conditionals in Python allow you to execute different blocks of code based on conditions with boolean outputs. This is mainly done using `if`, `elif`, and `else` statements.


**If Statement**
- The `if` statement evaluates a condition which has returned a boolean (`True` or `False`).
- If the condition is `True`, the block of code inside the `if` statement is executed.

**Elif Statement**
- The `elif` (short for "else if") statement allows you to check multiple conditions.
- It follows an `if` statement and is executed if the previous conditions were `False` and its own condition is `True`.

**Else Statement**
- The `else` statement is used to execute a block of code if none of the preceding `if` or `elif` conditions were `True`.

**Syntax**

```
if condition:
    # Code to execute if condition is True
elif another_condition:
    # Code to execute if another_condition is True
else:
    # Code to execute if all conditions are False

```
Note the colon and indentation used in the above example

- Indentation is used to nest conditionals and loop in python, and incorrect indentation is a common cause for errors.

Here is a very simple example of using conditionals:

```
temperature = 25

if temperature > 30:
    print("It's a hot day.")
    #The program checks if the temperature is greater than 30. If it is, it prints "It's a hot day."
elif temperature < 10:
    print("It's a cold day.")
    #If the first condition is False, it checks if the temperature is less than 10. If this condition is True, it prints "It's a cold day."
else:
    print("It's a pleasant day.")
    #If both conditions are False, the else block executes and prints "It's a pleasant day."
```

With very simple conditions python has a shorthand that is useful. You can do things like:

```
print("it's a hotday") if temperature > 30 else (print("it's a cold day") if temperature < 10 else print("it's a pleasent day"))
# these are known as ternary operators - there is no elif
```

**Operators**

The operators are a key tool when using conditional statements in python. Remind yourself about them and their order of precedence.

::: {.callout-exercise}
#### Discussion: Operators
{{< level 2 >}}

Which types of operators are most useful when using conditional statements in Python?

:::

::: {.callout-exercise}
#### examining contitional statements
{{< level 2 >}}

- What do the following `if` statements do?
- How can you write complex conditions and make your code legible?

Some actual examples from my (not perfect) code:
```
if (len(x[0]) == 2) and not any(x % 10 in {0, 9} for x in x[0]):
```
```
    if (
        (coordcolumnchoice[0] == (1,1) and coordinateM[0,0] in x[0] and coordinateM[1,1] in x[0]) or
        (coordcolumnchoice[0] == (1,1) and coordinateM[1,0] in x[0] and coordinateM[0,1] in x[0]) or
        (coordcolumnchoice[0] == (1,0) and coordinateM[1,0] in x[0] and coordinateM[0,0] in x[0]) or
        (coordcolumnchoice[0] == (1,0) and coordinateM[1,1] in x[0] and coordinateM[0,1] in x[0])
      ):
```
How might the second example be clearer if I was writing it again?

:::

## `try` and `except` in Python

In Python, `try` and `except` blocks are used for handling exceptions, which are errors that can occur during program execution. This mechanism allows developers to anticipate potential errors, provide alternate code to handle them, and prevent the program from crashing. Here's how it works:

**`try` Block:**
- The code that might raise an exception is placed inside the `try` block.
- If an exception occurs during execution of this block, the rest of the block is skipped, and control is passed to the `except` block.

**`except` Block:**
- This block contains code that handles the exception. You can specify which exception to catch or leave it blank to catch any exception.
- If the exception type matches the one specified in the `except` block, the code inside it is executed.

**Multiple `except` Blocks:**
- You can have multiple `except` blocks to handle different types of exceptions.

**`else` Block:**
- You can add an `else` block after the `except` block. This block runs if the `try` block executes without raising an exception.

**`finally` Block:**
- The `finally` block runs regardless of whether an exception was raised or not. It is often used for cleanup actions, like closing files or releasing resources.

**Example**

Here’s a simple example demonstrating the use of `try` and `except`:

```python
try:
    # Code that may raise an exception
    numerator = 10
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError:
    # Handling a specific exception
    print("Error: You cannot divide by zero.")
except Exception as e:
    # Handling any other exception
    print(f"An unexpected error occurred: {e}")
else:
    # Executes if no exception occurred
    print("The result is:", result)
finally:
    # This block runs no matter what
    print("Execution completed.")
```
*Explanation of the Example:*

`try`:

- Attempts to divide `numerator` by `denominator`. Since `denominator` is zero, this raises a `ZeroDivisionError`.

`except`:

- The first `except` catches the `ZeroDivisionError` and prints an error message.
- The second `except` would catch any other unexpected exceptions, but it won't run in this case because the first `except` handles the error.

`else`:

- If there were no exceptions, the `else` block would print the result.

`finally`:

- This block runs at the end of the `try/except` structure, regardless of whether an exception occurred or not. It's useful for cleanup actions.

In this case I might not use the `else` or `finally`

**Benefits of Using `try` and `except`**
- **Prevents Crashes:** By handling exceptions, you can prevent your program from crashing due to unforeseen errors.
- **Cleaner Code:** It allows for clearer separation of normal code and error handling.
- **More Robust Programs:** By anticipating and handling potential errors, your programs can handle unexpected situations better.

## `for` Loops in Python

`for` loops iterate over a sequence (list, tuple, string, dictionary, set or range) and perform processes. The syntax of a `for` loop is simple but must be carefully followed, especially with respect to the colon (`:`) and indentation.

**Syntax**

- The `for` keyword is followed by a variable name (e.g., `item`) that will take on the value of each element in the sequence.  
- The sequence can be a list, tuple, string, or any iterable object.  
- The colon (`:`) indicates the start of the loop block.  
- The indented lines that follow the colon are the code that will be executed.


```
for item in sequence:
    # Code block to execute
`````
Example:

```
animals = ["dog", "cat", "rabbit", "elephant", "tiger"]

for animal in animals:
    print(f'I have a {animal}.')
```
Output
```
I have a dog.
I have a cat.
I have a rabbit.
I have an elephant.
I have a tiger.
```

## Using `len()` and `range()` in `for` loops

In Python, `len()` and `range()` are often used with for loops to control iterations and access elements by their index.

**Using `len()`**

The `len()` function returns the number of items in an iterable (like a list, tuple, or string). This is useful when you need to loop through each element of a sequence without manually specifying the length.

**Using `range`**

The range() function generates a sequence of numbers, which can be useful for iterating over a sequence with a specified start and end. The syntax is range(start, stop[, step])

```
# Loop through the first five integers
for num in range(5):
    print(num)

```

**Examples:**

```
animals = ["dog", "cat", "rabbit", "elephant"]

for i in range(len(animals)):            # only 1 value - stop
    print(f"Animal at index {i}: {animals[i]}")

for i in range(0,len(animals),2):        #start, stop, step
    print(f"Animal at index {i}: {animals[i]}")


```

## Using `enumerate()` in For Loops

The `enumerate()` function in Python adds a counter to an iterable and returns it as an `enumerate` object. This is particularly useful when you want to loop through a sequence and keep track of the index of each item without using `range()`.

**Syntax**

The syntax of `enumerate()` is as follows:

```python
enumerate(iterable, start=0)
```
- iterable: The sequence (like a list, tuple, or string) you want to iterate over.
- start: The starting index (default is 0).

**Example of `enumerate()`**
Here's a simple example demonstrating how to use enumerate() with a list of animals:

```
animals = ["dog", "cat", "rabbit", "elephant"]

for index, animal in enumerate(animals):
    print(f"Animal {index}: {animal}")
```
output:
```
Animal 0: dog
Animal 1: cat
Animal 2: rabbit
Animal 3: elephant
```
**Benefits of Using `enumerate()`**

- **Clarity:** It makes the code cleaner and more readable by eliminating the need to manually manage the index.
- **Convenience:** Automatically handles the index tracking for you, reducing the risk of errors.

::: {.callout-exercise}
#### Count Nucleotide Occurrences
{{< level 2 >}}

Given a DNA sequence, write a loop to count the occurrences of each nucleotide (A, T, C, G).

**DNA Sequence:**
```python
dna_sequence = "ATCGATCGATCGATCG"

```

::: {.callout-answer}

```
# Given DNA sequence
dna_sequence = "ATCGATCGATCGATCG"

```
Initial Answer
```
# Initialize counts
count_A = 0
count_T = 0
count_C = 0
count_G = 0

# Count nucleotides
for nucleotide in dna_sequence:
    if nucleotide == 'A':
        count_A += 1
    elif nucleotide == 'T':
        count_T += 1
    elif nucleotide == 'C':
        count_C += 1
    elif nucleotide == 'G':
        count_G += 1

print(f"A: {count_A}, T: {count_T}, C: {count_C}, G: {count_G}")
```

:::

What exceptions might be generated?
- Add an else statement to deal with other characters
- Use try and except - what exception cases would this allow you to handle? Remember to follow the indentation pattern

:::

## Section


Headings for material sections start at level 2. 

More guidelines for content available here: https://cambiotraining.github.io/quarto-course-template/materials/02-content_guidelines.html


## Summary

::: {.callout-tip}
#### Key Points

- Last section of the page is a bulleted summary of the key points
:::
