---
title: Starting in Python
---

::: {.callout-tip}
#### Learning Objectives

- Identify basic Python Syntax
- Understand markdown and the Jupyter notebook syntax
- Be able to define variables and call functions
- Identify the type of a variable

:::


## Basic Python Syntax

**Comments and new lines**

Commenting your code, and using lines liberally, are key to making your code easily understandable for others.

- A **```#```** (Hash) is used for single line comments 

- A **```"""```** (triple quotes) is used around multiline comments or strings

- A **```\```** (backslash) is used to explicitly break a line

- Lines can be implicitly continued in some cases, for example when in brackets. We will see this later. 

<br>

**Assigning variables**

In Python initialising variables is easy:

- Variables are assigned using the = sign

- Case sensitive

- No need to declare the type explicitly (dynamic typing)

```
# Initialising my_height in cm 
my_height = 176
my_name = "Kavi"

```
<br>

**Variable Naming Conventions in Python**

When naming variables, it's important to follow Python's guidelines for consistency and readability. Here are some key rules to remember:

* **Case-sensitive:** weight and Weight are different variables.

* **Use lowercase:** Separate words with underscores, e.g., weight_kg.

* **Don't start with numbers:** Variable names cannot begin with a digit.

* **Stick to letters:** Use only letters, underscores, and digits (when needed).

* **Be descriptive:** Choose clear, meaningful names (e.g., asdjks is not helpful).

* **Avoid overly long names:** For example 'this_is_my_height_in_cm' is too long.

* **Don't use keywords:** Avoid using Python function names, class names, or data types as variable names.

For more detailed guidelines, refer to PEP 8 or the Google Python Style Guide.

<br>

**Indentation**

In python indentation is used to define code blocks. We will see more of this later when we get to conditional statements and loops. 
- Unexpected indents will result in errors.
- indents are 4 spaces according to PEP 8 standards, however commonly also two spaces on web interfaces. Be consistent.
- Using spaces is preferable to using tabs

```
# Initialising my_height in cm 
my_height = 176
 my_name = "Kavi"
 
```
The above would produce an error

## Calling a function

Functions are chunks of code which produce an output. They can (but do not have to) take user defined inputs. 
Python ships with many in built functions. See: https://docs.python.org/3/library/functions.html

To call a function, simply use the function name followed by parentheses. If the function takes parameters, provide the arguments inside the parentheses.
- functions may take arguments in an order separated by a comma: 
```
function(a, b) 
```

- alternatively functions may use assignment for inputs:
```
function(a, type = b)
```

- variable inputs into functions can defined globally
```
b = number
function(a, type = b)
```
- Functions can have default inputs if none specified

- functions can be nested although this can make code less readable
```
function_two(function_one(a))
```
::: {.callout-exercise}
#### Print 'Hello World"
{{< level 1 >}}

Open the python console in command line. Use variable assignment and the print() function assign "Hello World!" to the **message** variable and print it in standard output

::: {.callout-answer}
```
message = "Hello World!"
print(message)
```
:::
:::

## Using the type() function

As mentioned python uses dynamic typing. The type() function can output the datatype assigned to a variable

::: {.callout-exercise}
#### Find the data type
{{< level 1 >}}

What is the data type of the **message** variable? Print it to Standard output

::: {.callout-answer}
```
print(type(message))
```
output:
```
<class 'str'>
```
It is a string
:::
:::

## Using Jupyter Notebooks


Python programs (.py files) are essential in data analysis and structured software development. In this course, we will primarily use Jupyter Notebooks for coding.
Jupyter Notebooks enable literate programming by merging natural language (like English) with source code in a single document. 
Instead of separate text documents and .py files, Jupyter Notebooks integrate both functionalities, making analyses and code reproducible. 
This is important for FAIR (Findable, Accessible, Interoperable, and Reproducible) research standards.

The name "Jupyter" derives from its core languages: Julia, Python, and R, with its logo inspired by Galileo’s discovery of Jupiter's moons.
Each coding language has its own kernel for executing code cells. For Python, the kernel is IPython. 
Jupyter Notebook files have a '.ipynb' extension, indicating their connection to IPython.

The Jupyter Notebook file, kernel, and web browser interact via the Jupyter Notebook Server, enabling a seamless user experience.

For a more in-depth look at Jupyter Notebooks, refer to the MCB course:
https://ac812.github.io/mcb-python/jupyter.html

::: {.callout-exercise}
#### Create a Jupyter Notebook 
{{< level 1 >}}

You should have already installed Jupyter Notebook. 
Launch a Jupyter Notebook from the terminal:

```
jupyter notebook
```
Create a new python file and print "Hello World!" in a code chunk.
Add a text chunk and describe what you have done. Save the file.

::: {.callout-answer}

In the Jupyter Notebook interface, you willl see a list of files and folders in the current directory.
1. Click on the New button on the right side of the interface.
2. From the dropdown menu, select Python 3 (or whichever version you have installed). This will create a new notebook.
3. You will see a new notebook open up with a cell where you can write Python code. 
Add:
```
print("Hello, World!")
```
4. Run the Code by clicking on the cell containing the code.
Press Shift + Enter on your keyboard, or click the Run button in the toolbar.
5.  Save Your Notebook by clicking on the File menu at the top left.
Select Save and Checkpoint or press Ctrl + S (Windows) or Cmd + S (Mac).

:::
:::

## Summary
You should now be able to call in-built functions in python and be set up to use Jupyter Notebooks.

::: {.callout-tip}

#### Key Points

- Python uses # for comments
- Variables are assigned with `=`
- There is no need to define the variable type explicitly
- Indentation is used in python to identify code chunks
- Jupyter Notebooks enable literate programming in python, combining code chunks and markdown text

:::
