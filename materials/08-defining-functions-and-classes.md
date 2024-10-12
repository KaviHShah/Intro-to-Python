---
title: Defining Functions and Classes
---

::: {.callout-tip}
#### Learning Objectives

- Be able to define your own functions and classes
- Briefly introduce the object oriented programming paradigm
- Understand local and global variables
:::

## Defining Functions in Python

Functions in Python are blocks of reusable code designed to perform a specific task. They help organize code, promote reusability, and make programs more readable.

**Syntax of a Function**

The basic syntax for defining a function in Python is:

```python
def function_name(parameters):
    """Docstring explaining the function"""
    # Function body
    return value
```
- **`def`**: This keyword is used to define a function.
- **`function_name`**: The name you choose for the function.
- **`parameters`**: Optional. Values that the function accepts as inputs. If there are multiple, they are separated by commas.
- **`return`**: Optional. The function can return a value using the `return` statement.

<br>

**Example 1: Function with No Parameters**

```
def welcome():
    print("Hello, World!")
```
<br>

**Example 2: Function with Parameters**

```
def welcome_person(name):
    print(f"Hello, {name}!")
This function accepts a single parameter, name.
```
It uses that parameter to personalize the greeting.
Calling the function:

```
welcome_person("Kavi")
```
Output:

```
Hello, Kavi!
```
<br>

**Example 3: Function with Multiple Parameters and a Return Value**

```
def add_numbers(a, b):
    return a + b
```
This function takes two parameters, a and b.
It returns the sum of the two numbers.
Calling the function:

```
result = add_numbers(5, 10)
print(result)
```
Output:

```
15
```
<br>

**Example 4: Function with Default Parameters**

You can set default values for parameters so that a function can be called with fewer arguments than defined.

```
def greet_person(name="Guest"):
    print(f"Hello, {name}!")

```
Calling the function with and without the parameter:
```

greet_person("Tom")  # Uses the provided argument
greet_person()         # Uses the default value

```
output
```
Hello, Tom!
Hello, Guest!
```
<br>

**Example 5: Function with Multiple Outputs**

A function can return more than one value using tuples or other data structures.

```
def calculate(a, b):
    sum_val = a + b
    product_val = a * b
    return sum_val, product_val
```

Calling the function and unpacking the values:

```
sum_result, product_result = calculate(3, 4)
print(sum_result, product_result)
```
Output:
```
7 12
```
<br>

**Functions Summary**

Functions in Python are defined using the def keyword.
Inputs (parameters) can be passed into functions, and outputs can be returned using the return statement.
Functions can have default parameters, accept multiple arguments, and return multiple values.


## Classes in Python

In Python, a class is a standard way of creating objects (instances). It allows you to bundle data (attributes) and functions (methods) into a single unit. Classes define the structure and behavior of objects in an object-oriented programming style.

::: {.callout-exercise}
#### Discussion
{{< level 2 >}}

Where have we seen this already in this course?

:::

**Basic Syntax of a Python Class:**

```
class MyClass:
    # Constructor to initialize the object
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1  # Instance variable
        self.attribute2 = attribute2  # Instance variable

    # Method (function) within the class
    def my_method(self):
        print(f"Attribute 1: {self.attribute1}")
        print(f"Attribute 2: {self.attribute2}")
```

**Key Concepts:**

- `__init__()` Method: This is the constructor method that gets called when a new object of the class is created. It initializes the object's attributes.
- **Attributes**: Variables that belong to an object, defined by `self.attribute_name`.
- **Methods**: Functions defined inside a class that operate on the object’s attributes.
- **Instance**: An individual object created from the class.


**Example for biologists:**

```
class BioComponent:
    def __init__(self, name, id, sequence, function):
        self.name = name
        self.id = id
        self.sequence = sequence
        self.length = len(sequence)
        self.function = function

    # Method to pad the sequence with user input on either side
    def pad(self, left_pad, right_pad):
        self.sequence = left_pad + self.sequence + right_pad
        self.length = len(self.sequence)  # Update the length
        print(f"Padded sequence: {self.sequence}, New length: {self.length}")

    # Method to perform a point mutation (replace a character at a specified position)
    def point_mutate(self, position, new_char):
        if position < 0 or position >= self.length:
            print("Position out of bounds.")
            return
        self.sequence = self.sequence[:position] + new_char + self.sequence[position + 1:]
        print(f"Mutated sequence: {self.sequence}")

# Inherited class Gene that restricts mutations to A, T, C, G only
class Gene(BioComponent):
    def point_mutate(self, position, new_char):
        if new_char not in "ATCG":
            print("Error: Invalid base. Must be one of A, T, C, G.")
            return
        super().point_mutate(position, new_char)  # Call parent class method

# Example Usage
# Create an instance of BioComponent
component = BioComponent(name="ProteinX", id=101, sequence="MKTFFY", function="Signaling")
print(f"Initial sequence: {component.sequence}, Length: {component.length}")

# Use the pad method
component.pad("AAA", "BBB")

# Perform a point mutation at position 2 (index starts at 0)
component.point_mutate(2, "Q")

# Create an instance of Gene (inherits from BioComponent)
gene = Gene(name="GeneX", id=202, sequence="ATGCGT", function="Coding for protein")
print(f"Initial gene sequence: {gene.sequence}, Length: {gene.length}")

# Perform a valid point mutation with a valid base (A, T, C, G)
gene.point_mutate(3, "A")

# Attempt an invalid point mutation with an invalid base (not A, T, C, G)
gene.point_mutate(2, "X")

```
**Explanation:**

BioComponent Class:
- The `__init__` method initializes the `name`, `id`, `sequence`, `length` (calculated automatically), and `function` of the component.
- The `pad` method adds user-inputted strings (`left_pad`, `right_pad`) on either side of the sequence and updates the sequence's length accordingly.
- The `point_mutate` method allows any character to replace one at a specific position in the sequence, updating the sequence accordingly.

Gene Class:
- Inherits from `BioComponent` and overrides the `point_mutate` method to ensure that only valid DNA bases (A, T, C, G) can be used for mutation.
- Calls the parent class's `point_mutate` method if the mutation is valid.

Example Usage:
- A **BioComponent** (e.g., a protein) can be padded and mutated freely with any character.
- A **Gene** restricts mutations to valid DNA bases and throws an error if any invalid base is provided.
- The `super().point_mutate(position, new_char)` call in the **Gene** class refers to invoking the `point_mutate` method from its parent class (**BioComponent**). The `super()` function is used to give access to methods of the parent class from within a child class.
- When the **Gene** class overrides the `point_mutate` method, it restricts the mutations to DNA bases (A, T, C, G). After checking that the new character (`new_char`) is valid, the `super().point_mutate(position, new_char)` call allows the **Gene** class to reuse the logic of `point_mutate` from **BioComponent** to actually mutate the sequence.

How `super()` Works in This Case:

- `super()` looks up the parent class of **Gene** (which is **BioComponent**).
- `super().point_mutate(position, new_char)` calls the `point_mutate` method of **BioComponent** with the `position` and `new_char` arguments.
- This lets **Gene** use the existing logic of `point_mutate` defined in **BioComponent** for sequence mutation, without having to reimplement it.

::: {.callout-exercise}
#### Short Description
{{< level 2 >}}

Exercise add your own function to the biocomponent class. Add protein to the biocomponent class and decide if you want to overide the functions

:::

::: {.callout-exercise}
#### Short Description
{{< level 2 >}}

What have I not added in many of these examples including the syntax note that I should have?

:::{.callout-hint}

try run the `help()` function on MyClass and function_name()

:::

::: {.callout-answer}

Docstring comments

```

class BioComponent:
    """
    A class to represent a biological component (like a protein or gene).
    
    Attributes:
    -----------
    name : str
        Name of the component.
    id : str
        Unique identifier for the component.
    sequence : str
        The biological sequence (e.g., amino acids or nucleotides).
    length : int
        Length of the sequence (calculated automatically).
    function : str
        Description of the component's biological function.
    """
    
    def __init__(self, name, id, sequence, function):
        """
        Initialize a BioComponent with name, id, sequence, and function.
        
        Parameters:
        -----------
        name : str
            The name of the component.
        id : str
            The unique identifier for the component.
        sequence : str
            The biological sequence of the component.
        function : str
            The biological function of the component.
        """
        self.name = name
        self.id = id
        self.sequence = sequence
        self.length = len(sequence)
        self.function = function
    
    def pad(self, left_pad, right_pad):
        """
        Pads the sequence with the given left and right strings.
        
        Parameters:
        -----------
        left_pad : str
            The string to add to the left of the sequence.
        right_pad : str
            The string to add to the right of the sequence.
        """
        self.sequence = left_pad + self.sequence + right_pad
        self.length = len(self.sequence)  # Update the length
        
    def point_mutate(self, position, new_char):
        """
        Mutates the sequence by replacing a character at the specified position.
        
        Parameters:
        -----------
        position : int
            The index at which to replace the character.
        new_char : str
            The new character to insert into the sequence.
        """
        if 0 <= position < self.length:
            self.sequence = self.sequence[:position] + new_char + self.sequence[position + 1:]


```

:::
:::    

::: {.callout-exercise}
#### Define Your own Data Type

I mentioned in python that it is easy to define your own data types.
Now you have all the tools to do it!

Define your own composite data type with unique attributes and
write some functions for it!

What is it useful for?

:::

## Local and Global Variables, instance and class attributes

In Python, variables can be classified into two main categories based on their **scope**: **local** and **global** variables.

**Local Variables**

- A **local variable** is a variable that is defined inside a function and is only accessible within that function. Once the function exits, the local variable is destroyed, and its value cannot be accessed from outside the function.

Example

```
def my_name():
    name = "Kavi"  # Local variable
    print("Inside the function my name is:", x)

my_name()
print(name)  # This would raise an error because x is not accessible outside the function.
```

**Global Variables**

- A **global variable** is a variable that is defined outside of any function and is accessible throughout the program, including within functions (unless specifically overridden within a function). Global variables maintain their values until the program terminates.

Eaxample:

```

number = 1  # Global variable

def my_number():
    print("Inside the function the number is:", number)

my_number()  # Can access the global variable
print("Outside the function:", number)  # Global variable accessible here as well

```

**Modifying Global Variables Inside a Function**

- If you want to modify a global variable within a function, you need to explicitly declare it as `global` using the `global` keyword. Without the `global` keyword, Python would treat the variable as a new local variable inside the function, and the global variable would remain unchanged.

Example:
```
age = 30  # Global variable

def my_age():
    global age
    age += 1  # Modifying the global variable
    print("Inside the function:", age)

my_age()
print("Outside the function:", age)  # Global variable now changed

```

**`__main__` in Python**

- In Python, `__main__` refers to the environment where the top-level code is being executed. When a Python script is run directly, Python assigns the special name `"__main__"` to the `__name__` variable in that script.

**`if __name__ == "__main__":`**

- This construct is used to check if a script is being run directly or being imported as a module in another script. The code under this condition will only be executed if the script is run directly.

Example:
```
# script.py
def welcome():
    print("Hello, world!")

if __name__ == "__main__":
    welcome()

```

**Purpose of `__main__`:**

- **Testing and Debugging**: It allows you to write test code in the same file without it running when the file is imported elsewhere.
- **Modular Code**: It helps keep code modular, where functions and classes are defined for reuse, but certain behaviors (like running a function) are executed only when the file is executed directly.

<br>

**Local and Global Variables in Classes**

When dealing with **classes** in Python, the concept of **local** and **global** variables applies similarly, but there are additional layers related to **instance** and **class attributes**.

**Instance and Class Attributes**
In addition to local and global variables, classes introduce two other types of variables: **instance attributes** and **class attributes**.

- **Instance Attributes**: These are specific to an instance (object) of a class. Each object has its own separate copy of these attributes.

- **Class Attributes**: These are shared among all instances of a class and are declared **outside** the `__init__()` method.

Example
```
class MyClass:
    class_variable = 5  # Class attribute, shared by all instances

    def __init__(self, value):
        self.value = value  # Instance attribute

obj1 = MyClass(10)
obj2 = MyClass(20)

print(obj1.class_variable)  # 5
print(obj2.class_variable)  # 5
print(obj1.value)           # 10
print(obj2.value)           # 20

```

#### Summary:

**Summary:**

- **Local variables** are declared inside a function and only exist within that function.

- **Global variables** are declared outside of functions and can be accessed anywhere in the script unless shadowed by a local variable.
- The `__name__ == "__main__"` construct is used to determine if a script is being run directly or imported, allowing control over code execution in different contexts.

- **Instance attributes** are tied to specific objects of a class.

- **Class attributes** are shared among all instances of a class.

- Generally speaking I think it is always a good idea to clearly add inputs and outputs to a function in any complex function. This includes if they are global variables as you may want to use those functions in other scripts that do not have the same global variables.


## Summary

Now you have had a look at building functions and classes. They are key parts of programming in python.
Imagine living in a world without being able to define and call functions in python. Just think of the amount of code you would have to write and sift through!


::: {.callout-tip}
#### Key Points

- 
- **Functions**: Reusable blocks of code that perform a specific task. They help you concisely repeat different kinds of tasks
  
- **Classes**: Blueprints for creating objects (instances) that bundle data (attributes) and behavior (methods). They are part of the Object-Oriented Programming paradigm.
Both are useful for improving code structure, making it more modular, maintainable, and easier to debug.


:::
