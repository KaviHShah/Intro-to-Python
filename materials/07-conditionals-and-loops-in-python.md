---
title: Conditionals and Loops in Python
---

::: {.callout-tip}
#### Learning Objectives

- Be able to code conditional statements and loops in Python 
- Understand how to handle errors (exceptions) and edge cases in programs
- Compare different Python methods and their pros and cons

:::

## Conditionals

Conditionals in Python allow you to execute different blocks of code based on conditions with boolean outputs. This is mainly done using `if`, `elif`, and `else` statements.


**`if` Statement:**

The `if` statement evaluates a condition which has returned a boolean (`True` or `False`). If the condition is `True`, the block of code inside the `if` statement is executed.

**`elif` Statement:**

The `elif` (short for "else if") statement allows you to check multiple conditions.
It follows an `if` statement and is executed if the previous conditions were `False` and its own condition is `True`.

**`else` Statement:**

The `else` statement is used to execute a block of code if none of the preceding `if` or `elif` conditions were `True`.

**Syntax**

```
if condition:
    print(x) # Code to execute if condition is True
elif another_condition:
    print(y) # Code to execute if first condition is False and another_condition is True
else:
    print(z) # Code to execute if all conditions are False

```
Note the colon and indentation used in the above example

- Indentation is also used to nest conditionals and loops in python, and incorrect indentation is a common cause for errors.

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

With very simple conditions, python has a shorthand that is useful. You can do things like:

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
#### examining conditional statements
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

The code that might raise an exception is placed inside the `try` block.
If an exception occurs during execution of this block, the rest of the block is skipped, and control is passed to the `except` block.

**`except` Block:**

This block contains code that handles the exception. You can specify which exception to catch, or leave it blank to catch any exception.
If the exception type matches the one specified in the `except` block, the code inside it is executed.

**Multiple `except` Blocks:**

You can have multiple `except` blocks to handle different types of exceptions.

**`else` Block:**

You can add an `else` block after the `except` block. This block runs if the `try` block executes without raising an exception.

**`finally` Block:**

The `finally` block runs regardless of whether an exception was raised or not. It is often used for cleanup actions, like closing files or releasing resources.

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

**Benefits of Using `try` and `except`:**

- **Prevents Crashes:** By handling exceptions, you can prevent your program from crashing due to unforeseen errors.
- **Cleaner Code:** It allows for clearer separation of normal code and error handling.
- **More Robust Programs:** By anticipating and handling potential errors, your programs can handle unexpected situations better.

## `for` Loops in Python

`for` loops iterate over a sequence (list, tuple, string, dictionary, set, or range) and perform processes. The syntax of a `for` loop is simple but must be carefully followed, especially with respect to the colon (`:`) and indentation.

**Syntax**

- The `for` keyword is followed by a variable name (e.g., `item`) that will take on the value of each element in the sequence.  
- The sequence can be a list, tuple, string, or any iterable object.  
- The colon (`:`) indicates the start of the loop block.  
- The indented lines that follow the colon are the code that will be executed.


```
for item in sequence:
    print(x) # Code block to execute
```
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

## Using `enumerate()` in `for` Loops

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

::: {.callout-exercise}
#### Make your own `for` loop
{{< level 2 >}}

Exercise: Create your own `for` loop example with a dictionary, using the `enumerate()` function, `try` and `except`, and `if` statements. Explain what your code does?
Discuss in groups how you might improve each other's code?

::: {.callout-answer}
Example answer:

```
# Define a dictionary of animals and their respective speeds in km/h
animal_speeds = {
    "Cheetah": 120,
    "Tortoise": 0.3,
    "Falcon": "fast",  # Intentional error: speed should be a number
    "Horse": 88,
    "Elephant": 40
}

# Loop through the dictionary using enumerate
for index, (animal, speed) in enumerate(animal_speeds.items()):
    try:
        # Check if speed is numeric, and if the animal is faster than 50 km/h
        if speed > 50:
            print(f"{index + 1}. {animal} is fast with a maximum speed of {speed} km/h!")
        else:
            print(f"{index + 1}. {animal} is slow with a maximum speed of {speed} km/h.")
    except TypeError:
        # Handle the case where speed is not a numeric value
        print(f"{index + 1}. {animal} has an invalid speed value: {speed}")
```
For this code, some improvements are:

```
animal_speeds = {
    "Cheetah": 120,
    "Tortoise": 0.3,
    "Falcon": "fast",  # Intentional error: speed should be a number
    "Horse": 88,
    "Elephant": 40,
}

for index, (animal, speed) in enumerate(animal_speeds.items(), start=1):
    try:
        # Check if speed is numeric, and if the animal is faster than 50 km/h
        if speed > 50:
            print(f"{index}. {animal} is fast with a maximum speed of {speed} km/h!")
        else:
            print(f"{index}. {animal} is slow with a maximum speed of {speed} km/h.")
    except TypeError:
        # Handle the case where speed is not a numeric value
        print(f"{index}. {animal} has an invalid speed value: {speed}")

    except Exception as e:
        print(f"An error occurred: {e}")
```
output:
```

1. Cheetah is fast with a maximum speed of 120 km/h!
2. Tortoise is slow with a maximum speed of 0.3 km/h.
3. Falcon has an invalid speed value: fast
4. Horse is fast with a maximum speed of 88 km/h!
5. Elephant is slow with a maximum speed of 40 km/h.

```

:::
:::

::: {.callout-exercise}
#### Edge Cases
{{< level 2 >}}

How would you deal with the following edge case?

```
animal_speeds = {
    "Cheetah": 120,
    "Tortoise": 0.3,
    "Falcon": "fast",  # Intentional error: speed should be a number
    "Horse": 88,
    "Elephant": 40,
    (20,3): 0.5
}
```

This would run as if there is no problem in the code.


::: {.callout-answer}

maybe add a if Statement?

:::
:::

## `match` Statements

### A newer way of working with conditionals!

`match` statements (Python 3.10 onwards) allow for structural pattern matching, which is a more powerful and flexible version of if-elif chains. With `match`, you can compare variables to patterns and handle complex matching scenarios in a clear, concise way, and also directly deconstruct variables!

| Feature                      | if Statements                          | match Statements                                      |
|------------------------------|-----------------------------------------|-------------------------------------------------------|
| Simplicity for Basic Cases    | Easy for simple comparisons             | Similar simplicity for simple matches                 |
| Handling Complex Structures   | Requires manual decomposition           | Can match directly on structures                      |
| Deconstruction                | Requires explicit unpacking             | Automatically deconstructs data structures            |
| Type Matching                 | Needs `isinstance()` checks             | Can match types directly                              |
| Readability                   | Becomes verbose with complex logic      | More concise for complex scenarios                    |
| Flexibility                   | Can use `if`-`elif`-`else` chains for conditions | Can handle advanced pattern matching with custom conditions |


Example:
```
filtered_sequences = []
dna_sequences = [
    "ATCGTAGCTAGCTAGCTAGCTA",
    "ATCG",
    "ATGCGTAGCTAGCTAGCTAGCTAGCTAG",
    12345,
    "ATCGTAGCTAGCTAGCTAGCTAGC"
]

for sequence in dna_sequences:
    match sequence:
        case str():
          print(f' reported DNA is {sequence}')
          filtered_sequences.append(sequence)
        case int():
          print(f'{sequence} is not DNA')
        case _:
          print(f'{sequence} is not DNA')

print(filtered_sequences)

```
Output:

```
 reported DNA is ATCGTAGCTAGCTAGCTAGCTA
 reported DNA is ATCG
 reported DNA is ATGCGTAGCTAGCTAGCTAGCTAGCTAG
12345 is not DNA
 reported DNA is ATCGTAGCTAGCTAGCTAGCTAGC
['ATCGTAGCTAGCTAGCTAGCTA', 'ATCG', 'ATGCGTAGCTAGCTAGCTAGCTAGCTAG', 'ATCGTAGCTAGCTAGCTAGCTAGC']

```
::: {.callout-exercise}
#### Short Description
{{< level 1 >}}

How would you do the above if you had to use `if` statements?

:::

::: {.callout-exercise}
#### Short Description
{{< level 2 >}}

Use the animal_speeds dictionary in the previous exercise and write a match statement which would give the desired output

::: {.callout-answer}

```
animal_speeds = {
    "Cheetah": 120,
    "Tortoise": 0.3,
    "Falcon": "fast",  # Intentional error: speed should be a number
    "Horse": 88,
    "Elephant": 40,
}

for index, (animal, speed) in enumerate(animal_speeds.items(), start=1):
    match (animal, speed):
        case (str(), int()|float()):
            if s > 50:
                print(f"{index}. {animal} is fast with a maximum speed of {speed} km/h!")
            else:
                print(f"{index}. {animal} is slow with a maximum speed of {speed} km/h.")
        case (animal,int()|float()):
            print(f"{index}. Invalid animal name: {animal}")
        case (str(),speed):
            print(f"{index}. {animal} has an invalid speed value: {speed}")
        case _:
            print("Unknown error")

```

:::
:::

::: {.callout-exercise}
#### Short Description
{{< level 2 >}}

Discussion: Can match statements replace try except?

::: {.callout-answer}

NO! - match statements can reduce the errors and deal with edge casees, but errors can arise within the cases that cannot be handled.

- Edge cases can be different to errors - the code runs without throwing errors but the output does not behave as expected

- You should always inspect data first and check things make sense.

:::
:::

**Automatic Unpacking with `match` statements:**

```
dna_data = {
    "sequence": "AGCTAGCCTAAGT",
    "length": 12,
    "type": "coding"
}

# match statement to unpack DNA information
match dna_data:
    case {"sequence": sequence, "length": length, "type": type}:
        print(f"The DNA sequence is {sequence}, it has a length of {length} bases, and it is of type '{type}'.")
    case {"sequence": sequence, "length": length}:
        print(f"The DNA sequence is {sequence} and has a length of {length} bases, but type information is missing.")
    case {"sequence": sequence}:
        print(f"The DNA sequence is {sequence}, but length and type information are missing.")
    case _:
        print("Unknown DNA data.")
```
Output:
```
The DNA sequence is AGCTAGCCTAAGT, it has a length of 12 bases, and it is of type 'coding'.
```

**This can be incredibly useful when writing functions which we will get on to shortly**

## List Comprehensions

List comprehensions in python enable you to write shorter and sometimes faster code than standard loops. The syntax is:

[expression for item in iterable if condition]

Similar tools occur for dictionaries (Dictionary comprehension)

::: {.callout-exercise}
#### Use list Comprehensions
{{< level 1 >}}

print the animals list in upper case using list comprehensions


::: {.callout-answer}

Answer:
```
animals = ["dog", "cat", "rabbit", "elephant"]
print([animal.upper() for animal in animals])
```
output:
```
['DOG', 'CAT', 'RABBIT', 'ELEPHANT']
```

:::
:::

## `while` Loops in Python

A `while` loop in Python is a control flow statement that allows code to be executed repeatedly based on a boolean condition. The loop continues to execute as long as the condition remains `True`. Here's a breakdown of how `while` loops work:

**Key Components**

1. **Condition:** The loop starts with a condition that is evaluated before each iteration. If the condition is `True`, the code block within the loop is executed.

2. **Code Block:** The statements inside the loop are indented, and these will run repeatedly as long as the condition remains `True`.

3. **Increment/Decrement:** It's crucial to modify the variable used in the condition within the loop; otherwise, you may create an infinite loop.

4. **Exit:** Once the condition evaluates to `False`, the loop stops, and the program continues with the next line of code following the loop.

**Syntax**

```
while condition:
    # Code block to execute
    # Update condition variable
```
**Example**

Here's a simple example to illustrate how a while loop works:

```
count = 0

while count < 5:
    print("Count is:", count)
    count += 1  # Increment count
```
**Explanation of the Example**

- **Initialization:** The variable `count` is initialized to `0`.
  
- **Condition:** The `while` loop checks if `count` is less than `5`.
  
- **Code Execution:** If the condition is `True`, it prints the current value of `count`.
  
- **Increment:** The line `count += 1` increments the value of `count` by `1` after each iteration.
  
- **Termination:** Once `count` reaches `5`, the condition becomes `False`, and the loop exits.

This can be incredibly useful in simulations. Or when interacting in the environment. Here the number of iterations is not known beforehand and depend on a certain condition being met. They provide a way to repeat actions and process data dynamically within a program.

**However**

- **Infinite Loops:** Ensure the condition will eventually evaluate to `False` to avoid infinite loops.
  
- **Break Statement:** You can use the `break` statement to exit a loop prematurely if needed.
  
- **Continue Statement:** The `continue` statement can skip the current iteration and proceed to the next one based on a condition.

An example is:

```
import random

population = 1000
infected = 1
days = 0
infection_rate = 1.5
max_days = 30

while infected < population:
    days += 1

    if random.random() > 0.9:
        print(f"Day {days}: Lockdown in effect, no new infections today.")
        continue
    
    new_infections = int(infected * infection_rate)

    if new_infections + infected > population:
        new_infections = population - infected
    
    infected += new_infections

    print(f"Day {days}: {infected} infected.")

    if infected >= population:
        print(f"Day {days}: The entire population is infected.")
        break

    if random.random() > 0.8:
        print(f"Day {days}: Health measures implemented, slowing infection.")
        infection_rate -= 0.3
    
    if infection_rate <= 0.1:
        print(f"Day {days}: The infection has nearly stopped spreading.")
        break
    
    if days >= max_days:
        print("The simulation has reached its time limit.")
        break

```

::: {.callout-exercise}
#### Code Legibility
{{< level 2 >}}

Discussion:
What does the above code do?
Is it legibly written?
What can be done to improve this?

::: {.callout-answer}

```

# Commenting the code appropriately is important!
import random

# Parameters of the simulation
population = 1000       # Total population
infected = 1            # Initially 1 person is infected
days = 0                # Start at day 0
infection_rate = 1.5    # Rate of infection: how many people one infected person can infect per day
max_days = 30           # Maximum number of days to simulate

while infected < population:
    days += 1

    # Simulate random events like lockdown or vaccines
    if random.random() > 0.9:  # 10% chance of stopping the spread for the day
        print(f"Day {days}: Lockdown in effect, no new infections today.")
        continue  # Skip the infection calculation for this day and move to the next

    # Simulate daily infections
    new_infections = int(infected * infection_rate)

    # If new infections exceed the remaining healthy population, adjust them
    if new_infections + infected > population:
        new_infections = population - infected

    infected += new_infections

    # Display day-by-day status
    print(f"Day {days}: {infected} infected.")

    # Continue if there are still people to infect
    if infected >= population:
        print(f"Day {days}: The entire population is infected.")
        break

    # Random chance to reduce the infection rate due to interventions
    if random.random() > 0.8:  # 20% chance to reduce infection rate
        print(f"Day {days}: Health measures implemented, slowing infection.")
        infection_rate -= 0.3  # Decrease the infection rate

    # If the infection rate gets too low, break out of the loop (end of epidemic)
    if infection_rate <= 0.1:
        print(f"Day {days}: The infection has nearly stopped spreading.")
        break

    # Stop the simulation after a max number of days to avoid infinite loops
    if days >= max_days:
        print("The simulation has reached its time limit.")
        break
```

:::

:::

## Summary

Python has many ways to work with conditions and loops.
It is key for these statements to be written concisely, while catching edge cases and dealing with errors.

::: {.callout-tip}
#### Key Points

By this point you should be comfortable with:

- `if`, `elif`, `else` statements
- `match` , `case` statements
- `for` loops with `range()`, `len()`, and `enumerate()`
- Working with different composite data types
- `try` and `except` for error handling
- `while` loops

:::
