---
title: Working with Composite Data Types
---

::: {.callout-tip}
#### Learning Objectives

- Be able to work with lists, disctionaries, sets, and tuples
- Understand shallow and deep copies 
- Understand the importance of benchmarking code

:::


## Overview of Composite data types

In Python, composite data types allow you to store multiple values in a single variable. They can hold a collection of items, which can be of different data types. The main composite data types in Python are:

**Lists**

- **Definition**: Ordered, mutable collections that allow duplicate items.

- **Syntax**: Defined using square brackets `[]`.

**Tuples**

- **Definition**: Ordered, immutable collections that can also contain duplicates.

- **Syntax**: Defined using parentheses `()`.

**Dictionaries**

- **Definition**: Unordered collections of key-value pairs, where each key is unique and must be immutable.

- **Syntax**: Defined using curly braces `{}` and use a colon `:` to separate keys from values.

**Sets**

- **Definition**: Unordered collections of unique items.

- **Syntax**: Defined using curly braces `{}` or the `set()` function.

**Example Initialization and Differences:**

Let's initialize one of each composite data type with a list of 10 animals, and then demonstrate some of the main differences.

```
# Initialize a list of animals
animal_list = ["Dog", "Cat", "Elephant", "Lion", "Tiger", "Giraffe", "Zebra", "Monkey", "Snake", "Rabbit"]

# Initialize a tuple of animals
animal_tuple = ("Dog", "Cat", "Elephant", "Lion", "Tiger", "Giraffe", "Zebra", "Monkey", "Snake", "Rabbit")

# Initialize a dictionary of animals with their classifications
animal_dict = {
    "Dog": "Mammal",
    "Cat": "Mammal",
    "Elephant": "Mammal",
    "Lion": "Mammal",
    "Tiger": "Mammal",
    "Giraffe": "Mammal",
    "Zebra": "Mammal",
    "Monkey": "Mammal",
    "Snake": "Reptile",
    "Rabbit": "Mammal"
}

# Initialize a set of animals
animal_set = {"Dog", "Cat", "Elephant", "Lion", "Tiger", "Giraffe", "Zebra", "Monkey", "Bear", "Rabbit"}

# Show differences between data types
print("Original List:", animal_list)
print("Original Tuple:", animal_tuple)
print("Original Dictionary:", animal_dict)
print("Original Set:", animal_set)

# Mutability Demonstration
# Modifying the list (mutable)
animal_list[0] = "Wolf"  # Change "Dog" to "Wolf"
print("Modified List:", animal_list)

# Attempting to modify the tuple (immutable)
animal_tuple[0] = "Wolf"  
# This will raise an error

# Adding a new key-value pair to the dictionary (mutable)
animal_dict["Fox"] = "Mammal"
print("Modified Dictionary:", animal_dict)

# Attempting to add a duplicate to the set (will be ignored)
animal_set.add("Dog")  # This will not change the set
print("Modified Set (after trying to add 'Dog'):", animal_set)
```

Remember the key differences:

**Mutability**

- **Lists**: Mutable - items can be changed or updated.

- **Tuples**: Immutable - once defined, items cannot be changed.

- **Dictionaries**: Mutable - keys and values can be added or updated.

- **Sets**: Mutable - can add or remove items, but cannot contain duplicates.

**Order**

- **Lists** and **Tuples**: Ordered collections (the order of elements matters).

- **Dictionaries**: Maintains insertion order as of Python 3.7.

- **Sets**: Unordered - no guaranteed order of elements

**Duplicates**

- **Lists** and **Tuples**: Allow duplicates.

- **Dictionaries**: Keys must be unique, but values can be duplicated.

- **Sets**: Do not allow duplicates.

## Composite Data types and Memory Management

The way memory is managed is important. 
When coding we both want to minimise memory use, by not making needless duplications. 

Understanding the behavior of objects and how they are copied is crucial for managing memory and ensuring that your programs behave as expected. This is even more crucial when working with composite data types. 

- In the next sections we will work with different composite data types and investigate deep and shallow copies.

**We will use the `id()` function and lists to demonstrate this.**

The `id()` function returns the unique identifier (memory address) of an object. This is an integer guaranteed to be unique and constant for the object during its lifetime.

::: {.callout-exercise}
#### Equal Variables
{{< level 1 >}}

When you assign the value of one variable to another, what happens? 
i.e.
```
a = 10
b = a
```
what are the unique memory identifiers returned for a and b?

::: {.callout-answer}

```
id(a)
id(b)
```
As you can see if you run the above code, the two variable names point to the same object in memory. Therefore change in a will also change the value of b.
:::
:::

**Python Object Behavior: Objects and References**

In Python, variables are references to objects. When you assign a variable to another variable, you’re copying the reference, not the actual object.

## Working with Lists in Python

Lists in Python are versatile and support various operations that allow you to manipulate and interact with the data they contain. Below are some common operations you can perform on lists.

**Accessing Elements**

You can access list elements using indexing (zero-based).

`first_element = my_list[0]  # 1`  
`last_element = my_list[-1]   # 5`

**Slicing a List**

You can retrieve a portion of a list using slicing.

`sub_list = my_list[1:4]  # [2, 3, 4]`

**Adding Elements**

Append: Add an element to the end of the list.

`my_list.append(6)  # [1, 2, 3, 4, 5, 6]`

Insert: Insert an element at a specific index.

`my_list.insert(2, 2.5)  # [1, 2, 2.5, 3, 4, 5, 6]`

**Removing Elements**

Remove: Remove the first occurrence of a specified value.

`my_list.remove(2.5)  # [1, 2, 3, 4, 5, 6]`

Pop: Remove and return an element at a specified index (default is the last element).

`last_item = my_list.pop()  # list is now [1, 2, 3, 4, 5]`

**Modifying Elements**

You can change the value of an element using its index.

`my_list[1] = 20  # [1, 20, 3, 4, 5]`

**Extending a List**

You can add multiple elements to the end of the list using `extend()`.

`my_list.extend([6, 7, 8])  # [1, 20, 3, 4, 5, 6, 7, 8]`


**Sorting a List**

Sort the list in ascending order.

`my_list.sort()  # [1, 3, 4, 5, 6, 7, 8, 20]`

**Reversing a List**

You can reverse the order of elements in a list.

`my_list.reverse()  # [20, 8, 7, 6, 5, 4, 3, 1]`

**Finding the Length**

Get the number of elements in the list.

`length = len(my_list)  # 8`

**Numeric operators e.g. Append multiple repeats**

`my_list * 2  # [20, 8, 7, 6, 5, 4, 3, 1, 20, 8, 7, 6, 5, 4, 3, 1]`



**Conclusion**

Lists are a fundamental data structure in Python that allow for a variety of operations. By understanding these operations, you can effectively manage and manipulate data in your programs.

::: {.callout-exercise}
#### List Exercise: part 1
{{< level 2 >}}

1.   Create a list with 5 letters a-e, named letters
2.   Investigate the unique identifiers of the list and the members of the list.
3.   Assign letter2 to letters (letters2 = letters)
4.   Change the 3rd letter in letters to `f` and sort the letters alphabetically 
5.   What happens to letters2?
6.   use slicing to take the middle three letters to the variable letters_subset
7.   What do you notice about the unique identifiers of letters_subset and the members of the list?
8.   Use the inbuilt list copy function to create a copy of letters named letters_copy 
`letters_copy = letters.copy()`
9.   What are the identifiers now?
10.  If I modified a variable in letters_copy would letters change?
11.  Do you think letters_copy is a shallow or deep copy and why?


::: {.callout-answer}

```

# 1. Create a list with 5 letters a-e, named letters
letters = ['a', 'b', 'c', 'd', 'e']

# 2. Investigate the unique identifiers of the list and the members of the list.
id_letters = id(letters)  # Get the ID of the list
id_member_1 = id(letters[0])  # ID of 'a'
id_member_2 = id(letters[1])  # ID of 'b'
id_member_3 = id(letters[2])  # ID of 'c'
id_member_4 = id(letters[3])  # ID of 'd'
id_member_5 = id(letters[4])  # ID of 'e'

print(f'ID of letters:{id_letters}')
print(f'IDs of members: {id_member_1}, {id_member_2}, {id_member_3}, {id_member_4}, {id_member_5}')
# each member has a unique identifier and is an object as is the list

# 3. Assign letter2 to letters (letters2 = letters)
letters2 = letters  # Assign letters to letters2

# 4. Change the 3rd letter in letters to `f` and sort the letters alphabetically
letters[2] = 'f'  # Change the 3rd letter
letters.sort()    # Sort the letters
print(letters)    # Output: ['a', 'b', 'd', 'e', 'f']

# 5. What happens to letters2?
# letters2 will reflect the changes made to letters because both reference the same list object.
print(f'letters2 after modification: {letters2}')  # Output: ['a', 'b', 'd', 'e', 'f']

# 6. Use slicing to take the middle three letters to the variable letters_subset
letters_subset = letters[1:4]  # This will take letters at index 1, 2, and 3
print(letters_subset)  # Output: ['b', 'd', 'e']

# 7. What do you notice about the unique identifiers of letters_subset and the members of the list?
# letters_subset has a different identifier than letters, but its members share identifiers with the corresponding members in letters.

# 8. Use the inbuilt list copy function to create a copy of letters named letters_copy
letters_copy = letters.copy()  # Create a copy of letters

# 9. What are the identifiers now?
id_letters_copy = id(letters_copy)  # Get the ID of the copied list
id_member_copy_1 = id(letters_copy[0])  # ID of 'a'
id_member_copy_2 = id(letters_copy[1])  # ID of 'b'
id_member_copy_3 = id(letters_copy[2])  # ID of 'd'
id_member_copy_4 = id(letters_copy[3])  # ID of 'e'
id_member_copy_5 = id(letters_copy[4])  # ID of 'f'

print(f"ID of letters_copy: {id_letters_copy}")
print(f"IDs of members in letters_copy: {id_member_copy_1}, {id_member_copy_2}, {id_member_copy_3}, {id_member_copy_4}, {id_member_copy_5}")

# 10. If I modified a variable in letters_copy would letters change?
# No, modifying letters_copy will not affect letters because letters_copy is a separate list.

# 11. Do you think letters_copy is a shallow or deep copy and why?
# letters_copy is a shallow copy because it copies the references to the objects in the original list rather than the objects themselves.
```
:::
:::

::: {.callout-exercise}
#### List Exercise: Part 2
{{< level 2 >}}

1.  Try changing the second element of the letters list to the list ['n' , 'w'] to create a nested list. Look at the identifiers

2. make a copy called newletters_copy.

3. Before doing any computing - what do you think would happen if I changed `letters_copy[1][1]` to `"s"` ?

4. Try it and see what happens. Think about what it means in terms of deep and shallow copies. How would you create a deep copy?

::: {.callout-answer}

```
# Original letters list
letters = ['a', 'b', 'c', 'd', 'e']

# 1 Change the second element of the letters list to a nested list
letters[1] = ['n', 'w']  # Now letters is ['a', ['n', 'w'], 'c', 'd', 'e']

# Check the identifiers of the modified letters list and its elements
id_letters = id(letters)  # Get the ID of the outer list
id_second_element = id(letters[1])  # ID of the nested list ['n', 'w']
print(f'id_letters{id_letters}')
print("second element id", id_second_element)
#All the other ID's stay the same

#could also see:
#id_first_nested_element = id(letters[1][0])  # ID of 'n'
#id_second_nested_element = id(letters[1][1])  # ID of 'w'
print(f'ID of the first element in the nested list: {id_first_nested_element}')
print(f'ID of the second element in the nested list: {id_second_nested_element}')

# 2. Make a copy of letters called newletters_copy
newletters_copy = letters.copy()  

```

**3. Predict what will happen if we change newletters_copy[1][1] to "s"**
Since newletters_copy[1] will be a reference to the same nested list as letters[1], changing newletters_copy[1][1] will also change letters[1][1]. You can check this is the case by looking at the identifiers
```
# 4 Perform the change
newletters_copy[1][1] = "s"

# Check the modified lists
print(f"Modified letters: {letters}")  # Expect: ['a', ['n', 's'], 'c', 'd', 'e']
print(f"Modified newletters_copy: {newletters_copy}")  # Expect: ['a', ['n', 's'], 'c', 'd', 'e']

```

**Explanation**
This shows that when you change a nested element in a shallow copy, it affects the original list because both lists reference the same nested object.
:::
:::

## Shallow Copy verses Deep Copy 

**Shallow Copy**
A shallow copy creates a new object but inserts references into it to the objects found in the original. This means that if the original object contains other mutable objects (like lists or dictionaries), those nested objects are not copied; they are shared between the original and the copied object.

**Deep Copy**
A deep copy creates a new object and recursively adds copies of nested objects found in the original. This means that all levels of the object hierarchy are duplicated, and changes made to the copied object do not affect the original.

You can create a deep copy using the `copy` module:

```
import copy

original = [1, 2, [3, 4]]
deep_copied = copy.deepcopy(original)
```

**Memory Usage**

Shallow Copy: Uses less memory as it only copies references.

Deep Copy: Uses more memory because it creates full copies of all objects.

**Performance**

Shallow Copy: Faster due to less overhead in copying.

Deep Copy: Slower because of the recursive copying of all elements.

**Overview**

Understanding shallow and deep copies is essential for effective memory management and to avoid unintended side effects when working with mutable objects in Python. Choose the appropriate type of copy based on whether you need to maintain shared references to nested objects or require complete independence between copies.

## Working with Dictionaries

Dictionaries are efficient ways to manage and access data. Keys must be immutable, but values can be anything. 

Examples are presented below:
```
gene_info = {
    "gene": "BRCA1",
    "sequence": "ATCGGCCGTAAGCTAGCTAGCTAGC",
    "function": "DNA repair",
    "organism": "Homo sapiens"
}
```

**Accessing Values**

You can access a value by referring to its key.

`print("Gene Name:", gene_info["gene"])  # Output: Gene Name: BRCA1`

**Adding a New Key-Value Pair**

You can add new key-value pairs to a dictionary.
```
gene_info["chromosome"] = "17"
print("Updated gene info dictionary:", gene_info)
```

**Modifying Existing Values**

You can change the value of an existing key.
```
gene_info["function"] = "DNA repair and regulation"
print("Updated function:", gene_info["function"])  # Output: Updated function: DNA repair and regulation
```

**Removing a Key-Value Pair**

Use the del statement to remove a key-value pair.
```
del gene_info["organism"]
print("After removing organism:", gene_info)
```

**Using get() Method**

Use the get() method to avoid KeyError if the key does not exist.
```
chromosome = gene_info.get("chromosome", "Not available")
print("Chromosome:", chromosome)  # Output: Chromosome: 17
```

## Benchmarking
As there are often different methods to implement code. It is important to test the performance of different code through Benchmarking.

Memory use and how fast your code runs are two things that can be optimised.

<br>

cprofiler and timeit are both modules that can be used. Here we will use timeit to compare the dictionaries and lists. 

```
import timeit

gene_info_list = ["BRCA1", "ATCGGCCGTAAGCTAGCTAGCTAGC", "DNA repair", "Homo sapiens", "17"]
gene_info_dictionary = {
    "gene": "BRCA1",
    "sequence": "ATCGGCCGTAAGCTAGCTAGCTAGC",
    "function": "DNA repair",
    "organism": "Homo sapiens",
    "chromosome": "17"
}

# Define functions to access list and dictionary elements - we will go over this later

def access_list_element():
    gene_info_list[1]  # Accessing element using lists

def access_dictionary_element():
    gene_info_dictionary["sequence"]  # Accessing element using dictionaries

# Measure execution time
execution_time_list = timeit.timeit(access_list_element, number=100000)
execution_time_dictionary = timeit.timeit(access_dictionary_element, number=100000)

print("execution time list", execution_time_list)
print("execution time dictionary", execution_time_dictionary)

```
Output
```
execution time list 0.013154594002116937
execution time dictionary 0.009285816002375213
```
Try it yourself!
*For extra reading you can read about optimising compilers, how they apply to python and other coding languages, and what they can and cannot do.

## Sets and tuples

Although we won't go through sets and tuples in detail, information can be found here:

- https://www.w3schools.com/python/python_sets.asp

- https://www.w3schools.com/python/python_tuples.asp

## Summary

Composite data types are data structures that group multiple elements, potentially of different types, into a single unit. Examples include arrays, lists, tuples, and records (like structs or objects). 
They allow for more complex data organization by storing and managing collections of related information.
There are multiple ways to implement things and as we have seen benchmarking can be an effective way to choose the best method.

::: {.callout-tip}

#### Key Points

- Different composite data types have different properties
- Benchmarking and understanding the different properties of the data types can be used to choose the best approach 

:::
