---
title: Data Types in Python
---

::: {.callout-tip}
#### Learning Objectives

- Know the different data types in python
- Understand that different data types can have advantages and disadvantages
- Be able to choose when to use different data types
- Specify and change data types
- Be aware that packages and modules can enable access to more data types and structures

:::


## Inbuilt Data Types

In programming, data type is an important concept. Variables can store data of different types, and different types can do different things.

Python has the following data types built-in without needing any other libraries:

**Simple/primitive data types:**

- None Type:    NoneType

- Boolean Type:    bool

- Text Type:    str

- Numeric Types:    int, float, complex

- Binary Types:    bytes

<br>

**Composite Datatypes / data structures**

- Sequence Types:    list, tuple, range

- Set Types:    set, frozenset

- Mapping Type:    dict

- Binary composite type: bytearray, memoryview

<br>

**We will also look at the numpy arrays and pandas dataframes, you can also use the decimal module for correctly rounded arithmetic**

<br>

In Python, each data type has specific use cases and trade-offs. Let's look at each category and examine when it might be used, along with its benefits and disadvantages:

| Category       | Type         | Common Use Case                                    | Benefits                                           | Disadvantages                                          |
|----------------|--------------|---------------------------------------------------|---------------------------------------------------|-------------------------------------------------------|
| **None Type**  | NoneType     | Represents absence of value                        | Useful for optional values and placeholders        | Can cause errors if operations expect a value         |
|                |              |                                                   |                                                   |                                                       |
| **Boolean**    | bool         | Represents True or False                           | Simple and efficient for control flow              | Limited to two states (True/False)                    |
|                |              |                                                   |                                                   |                                                       |
| **Text**       | str          | Text representation                                | Immutable, Unicode support- multilingual, rich manipulation methods | Inefficient for heavy modifications                    |
|                |              |                                                   |                                                   |                                                       |
| **Numeric**    | int          | Represents whole numbers                           | No precision issues                                | Limited to integers                                    |
|                | float        | Represents decimal numbers                         | Supports real numbers                              | Precision issues due to storage                        |
|                | complex      | Represents complex numbers                         | Direct support for complex arithmetic               | Rarely needed in general programming                   |
|                |              |                                                   |                                                   |                                                       |
| **Sequence**   | list         | Mutable sequence of items                         | Flexible, dynamic size, rich methods               | Slower resizing operations                             |
|                | tuple        | Immutable sequence of items                       | Memory-efficient, safe                             | Cannot change values once set                          |
|                | range        | Sequence of numbers                               | Memory-efficient                                   | Less flexible than lists                               |
|                |              |                                                   |                                                   |                                                       |
| **Mapping**    | dict         | Key-value pairs                                   | Fast lookups, flexible types                       | Higher memory usage due to hashing                     |
|                |              |                                                   |                                                   |                                                       |
| **Set**        | set          | Unordered collection of unique items              | Fast membership testing; generally ordered in CPython (3.7+) | Unordered in the Python specification; no indexing     |
|                | frozenset    | Immutable set                                     | Hashable, can be used as dictionary keys          | Cannot modify after creation                           |
|                |              |                                                   |                                                   |                                                       |
| **Binary**     | bytes        | Immutable binary data                             | Efficient, compact for binary data                 | Not human-readable, cumbersome for some operations     |
|                | bytearray    | Mutable binary data                               | Allows modification of binary data                 | Consumes more memory than bytes                        |
|                | memoryview   | Efficient access to binary data without copying   | No data duplication                                | More complex to use                                    |


**Custom Data types**

- In python it is possible to define custom data types with custom syntax and behaviours, many of the common desired data types have already been made for you by others.

## Initialising and converting between data types

Different data types have different syntax. You will notice that all inbuilt data types in python have inbuilt functions which can be used to convert to that data type or specify as that data type. 

It is not possible to convert between all data types, and some require more information and input to convert between

Resources about data types can be found in the python documentation: 
https://docs.python.org/3/library/functions.html
https://docs.python.org/3/library/stdtypes.html
 
Examples of converting between data types: 



**1. Converting int to float**
```
x = 5  # integer
y = float(x)  # converting to float
print(y)  
```
Output: 
```
5.0
```

**2. Converting float to int**
```
x = 3.23  # float
y = int(x)  # converting to int
print(b)
``` 
Output: 
```
3
```

**3. Converting int to str**
```
x = 10  # integer
y = str(x)  # converting to string
print(y)
```
Output: 
```
'10'
```

**4. Converting str to int**
```
x = "123"  # string
y = int(x)  # converting to int
print(y)
```
Output: 
```
123
```

**5. Converting str to float**
```
x = "45.67"  # string
y = float(x)  # converting to float
print(x)  
```
Output: 
```
45.67
```

**6. Converting list to tuple**
```
my_list = [1, 2, 3]  # list
my_tuple = tuple(my_list)  # converting to tuple
print(my_tuple)
```
Output: 
```
(1, 2, 3)
```

**7. Converting tuple to list**
```
my_tuple2 = (4, 5, 6)  # tuple
my_list2 = list(my_tuple2)  # converting to list
print(my_list2)  
```
Output: 
```
[4, 5, 6]
```

**8. Converting int to bool**
```
num_bool = 0  # integer
bool_value = bool(num_bool)  # converting to boolean
print(bool_value)  
```
Output: 
```
False
```

::: {.callout-exercise}
#### floats to integers: what could go wrong?
{{< level 1 >}}

What happens when I convert 3.5 to an integer

::: {.callout-answer}
The integer displayed is output is 3. Rounding does not occur correctly
```
print(int(3.5))
print(int(3.7))
```
The output to both is `3`. Note that the python round() function rounds the float a to the nearest integer.
However with this function, if the decimal is exactly 0.5, it rounds to the nearest even number (Python's default behavior).
The alternative is to use a library, for example the decimal library.

:::
:::

::: {.callout-exercise}
#### Dictionary syntax
{{< level 1 >}}

Use the python documentation to find the syntax of a dictionary

::: {.callout-answer}
The syntax is with curly brackets and colons. See examples from the docs:
```
dictionary = {'language': "Python", "number": 2}
```
and
```
dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
```

:::
:::

::: {.callout-exercise}
#### Dictionary syntax
{{< level 1 >}}

Fill in the blanks with the correct data type:

1. You want to store a sequence of names that may change (e.g., adding or removing names).

Best data type: __________
2. You need to check if certain items (e.g., unique user IDs) exist in a collection and don't care about the order.

Best data type: __________
3. You need to store an unchanging sequence of geographic coordinates (latitude, longitude).

Best data type: __________
4. You are counting the number of items in stock in an inventory system (whole numbers only).

Best data type: __________
5. You are dealing with financial calculations and need precise decimal values for prices and quantities.

Best data type: __________
6. You need to store data about a person (e.g., name, age, occupation) and retrieve the data by key.

Best data type: __________
7. You are processing binary data from an image file and need to modify the data.

Best data type: __________
8. You want to represent a logical condition (True or False) to check user login status.

Best data type: __________
9. You want to ensure a set of elements stays constant and cannot be modified after creation.

Best data type: __________
10. A function you are writing returns nothing (i.e., no meaningful value to return).

Best data type: __________
11. You need to handle a collection of scientific data points with floating-point precision (e.g., temperature readings).

Best data type: __________
12. You are working with a string of text that may need to be split, joined, or manipulated.

Best data type: __________

::: {.callout-answer}
1. list — Ordered and mutable collection of names.
2. set — For fast membership tests with unique elements, order is irrelevant (unordered but generally ordered in CPython since Python 3.7).
3. tuple — Immutable sequence, perfect for storing fixed data like geographic coordinates.
4. int — Used for counting and working with whole numbers.
5. float — If precision is required, consider decimal.Decimal, but float for most cases.
6. dict — For key-value pairs (e.g., storing data about a person).
7. bytearray — Mutable sequence of bytes, useful for modifying binary data.
8. bool — Represents binary conditions (True or False).
9. frozenset — Immutable version of a set.
10. None — Represents the absence of a value, useful for functions that don’t return anything.
11. float — Floating-point numbers are used for measurements and continuous values.
12. str — For handling textual data with built-in manipulation methods.

Which data type you use effects memory useage and speed of computations which may be important in larger programs.
For further reading you can investigate why sets are generally faster to find unordered elements (membership tests) than lists or tuples
:::
:::

## Summary

There are many inbuilt data types in python. We will explore them further in the next few sections.
It is inportant to use the correct data type for your use case 

::: {.callout-tip}
#### Key Points

- Use the table to remember the key information about data types
- Check the python documentation for further information on data types and inbuilt functions
- It is important to use the correct data types for your use case rather than the same data type all the time.

:::
