---
title: Working with Numerical Data Types and Strings
---

::: {.callout-tip}
#### Learning Objectives

- Be able to manipulate numerical data types and strings
- Be able to look at the size of objects in memory, and effects of changes in data type on memory usage
:::


## Working with Numerical Data Types

Use the exercises below to test your familiarity with operators and working with numerical data types. 
Here we will use the sys module that ships with python. All we need to do is add the following at the start of our Jupyter notebook:
```
import sys
```
We will be using the sys.getsizeof() function:
```
variable = 3
sys.getsizeof(variable)
````

::: {.callout-exercise}
#### Assigning variables
{{< level 2 >}}

a = 10 

b  = 200.5

c = 5 + 8j

d = 3

e = 4.0

f = 0

g = 100

What are the data types of each variable and what is the size of each variable in memory. What are your observations?

::: {.callout-answer}

```
import sys
print("a:")
a = 10
print(type(a))
print(sys.getsizeof(a))

print("b:") 
b  = 200.5
print(type(b))
print(sys.getsizeof(b))

print("c:")
c = 5 + 8j
print(type(c))
print(sys.getsizeof(c))

print("d:")
d = 3
print(type(d))
print(sys.getsizeof(d))

print("e:")
e = 4.0
print(type(e))
print(sys.getsizeof(e))

print("f:")
f = 0
print(type(f))
print(sys.getsizeof(f))

print("g:")
g = 10000000000
print(type(g))
print(sys.getsizeof(g))
```

Output:
```
a:
<class 'int'>
28
b:
<class 'float'>
24
c:
<class 'complex'>
32
d:
<class 'int'>
28
e:
<class 'float'>
24
f:
<class 'int'>
24
g:
<class 'int'>
32
```

A key point is that integers vary in size, and can be larger than floats which are always 24 bytes. (Try finding the size of a very very large integer and the corresponding float). You can look up how integers and floats in python are stored in memory. Complex numbers are not used commonly, but in this case it is 32 bytes. You can look up more information about this if you are interested. 

:::
:::

::: {.callout-exercise}
#### Arithmetic Operations on Given Variables
{{< level 2 >}}

### Arithmetic Operations on Given Variables

Given the variables, what will be the results of the following arithmetic operations?

1. **What is the result of adding the integer values a and d?**
2. **What is the product of `b` and `e`?**
3. **What is the combined result of adding `a`, `b`, and `e`?**
4. **What is the difference when subtracting `c` from `b`?**
5. **What is the exponentiation of `d` raised to the power of `e`?**

In each case print the type and size

::: {.callout-answer}

```
ans_1 = a + d
type_ans_1 = type(ans_1)
size_ans_1 = sys.getsizeof(ans_1)
ans_2 = b * e
type_ans_2 = type(ans_2)
size_ans_2 = sys.getsizeof(ans_2)
ans_3 = a + b + e
type_ans_3 = type(ans_3)
size_ans_3 = sys.getsizeof(ans_3)
ans_4 = b - c
type_ans_4 = type(ans_4)
size_ans_4 = sys.getsizeof(ans_4)
ans_5 = d ** e
type_ans_5 = type(ans_5)
size_ans_5 = sys.getsizeof(ans_5)

print('ans_1:', ans_1, type_ans_1, size_ans_1)
print('ans_2:', ans_2, type_ans_2, size_ans_2)
print('ans_3:', ans_3, type_ans_3, size_ans_3)
print('ans_4:', ans_4, type_ans_4, size_ans_4)
print('ans_5:', ans_5, type_ans_5, size_ans_5)
```

output:
```
ans_1: 13 <class 'int'> 28
ans_2: 802.0 <class 'float'> 24
ans_3: 214.5 <class 'float'> 24
ans_4: (195.5-8j) <class 'complex'> 32
ans_5: 81.0 <class 'float'> 24
```

:::
:::

::: {.callout-exercise}
#### Relational Operations on Given Variables
{{< level 2 >}}

Using relational operators, determine the following comparisons:

1. **Is `a` equal to the sum of `d` and `e`?**
2. **Is `b` greater than `a` multiplied by `d`?**
3. **Is `e` less than `b` but greater than `d`?**
4. **Does the absolute value of `c` equal 10?**
5. **Is `d` less than or equal to the average of `a` and `b`?**


::: {.callout-answer}
```
ans_1 = a == d + e
ans_2 = b > a * d
ans_3 = e < b and e > d
ans_4 = abs(c) == 10
ans_5 = d <= ((a + b) / 2)
print('ans_1:', ans_1)
print('ans_2:', ans_2)
print('ans_3:', ans_3)
print('ans_4:', ans_4)
print('ans_5:', ans_5)
```

output:
```
ans_1: False
ans_2: True
ans_3: True
ans_4: False
ans_5: True
```

:::
:::

::: {.callout-exercise}
#### Logical Operations on Given Variables
{{< level 2 >}}

Use logical operators to evaluate the following conditions:

1. **Is `a` less than `b` and `d` less than `e`?**
2. **Is it false that `b` is equal to `20.5`?**
3. **Is either `a` less than `d` or `c` equal to `5 + 7j`?**
4. **Is `b` greater than `a`, and is `d` equal to `3`?**
5. **Is it true that either `e` is equal to `4`, or `c` is equal to `5 + 7j`?**

::: {.callout-answer}
```
ans_1 = a < b and d < e
ans_2 = not (b == 20.5)
ans_3 = a < d or c == 5 + 7j
ans_4 = b > a and d == 3
ans_5 = (e == 4) or (c == 5 + 7j)

print('ans_1:', ans_1)
print('ans_2:', ans_2)
print('ans_3:', ans_3)
print('ans_4:', ans_4)
print('ans_5:', ans_5)
```

Output:
```
ans_1: True
ans_2: True
ans_3: False
ans_4: True
ans_5: True
```

:::
:::

::: {.callout-exercise}
#### Assignment Operations on Variable a
{{< level 1 >}}

Use assignment operators to modify the value of `a`, and then find the new results:

1. **Increment `a` by `d`.**
2. **Subtract `e` from the new `a`.**
3. **Multiply the new `a` by `b`.**
4. **Divide the new `a` by `d`.**
5. **Raise the new `a` to the power of `e`.**

::: {.callout-answer}
```
a += d
print('ans_1:', a)
a -= e
print('ans_2:', a)
a *= b
print('ans_3:', a)
a /= d
print('ans_4:', a)
a **= e
print('ans_5:', a)

size_a = sys.getsizeof(a)
type_a = type(a)
print(size_a)
print(type_a)
```
Output:
```
ans_1: 13
ans_2: 9.0
ans_3: 1804.5
ans_4: 601.5
ans_5: 130900868105.0625
24
<class 'float'>
```

:::
:::

## String Exercises

- Strings are immutable, meaning once created they cannot be changed.
- Strings are also indexed, allowing access to individual characters and sections (slicing). Indexing with python starts with `0`.
- Strings can be concatenated and repeated using operators
- Escape character `\` can be used to include characters like quotation marks
- Python has functions known as string methods inbuilt for string manipulation
- f-strings allow you to embed expressions inside string literals using {} brackets.

Find Examples below:
**Using indexing to extract Characters**
```
dna_sequence = "ACGTAG"
print(dna_sequence[1])
```
Output:
```
C
```

**Slicing Sections**
```
dna_sequence = "ACGTAG"
print(dna_sequence[0:4])
```
Output:
```
ACGT
```

**Concatenation**
```
fragment1 = "AGCT"
fragment2 = "TGCA"
combined_sequence = fragment1 + fragment2
print(combined_sequence)
```
Output:
```
AGCTTGCA
```

**Repetition**
```
repeated_sequence = "A" * 5
print(repeated_sequence)
```
Output:
```
AAAAA
```

**Escape Characters**
```
dna_info = "The sequence is: \"ACGTAG\""
print(dna_info)
```
Output:
```
The sequence is: "ACGTAG"
```

**String Methods**
```
dna_sequence = "atcggta"
print(dna_sequence.upper())
```
Output:
```
ATCGGTA
```
Other mathods can be found at: https://www.w3schools.com/python/python_ref_string.asp

**f-strings**
```
rganism = "E. coli"
gene_count = 4000
info = f"The organism {organism} has approximately {gene_count} genes."
print(info)
```
Output:
```
The organism E. coli had approximately 4000 genes
```
Other mathods can be found at: https://www.w3schools.com/python/python_ref_string.asp

::: {.callout-exercise}
#### String Exercise: DNA Sequence Manipulation
{{< level 1 >}}

1. **Create a DNA Sequence**: Start by creating a string that represents a DNA sequence. For this exercise, use the sequence `atcgtagc`.

2. **Access Specific Bases**: Retrieve the first and third bases of the DNA sequence using indexing.

3. **Slice the Sequence**: Slice the DNA sequence to get the first five bases.

4. **Concatenate a New Fragment**: Create a new fragment `ggcta` and concatenate it to the original DNA sequence.

5. **Repeat a Base**: Create a string that consists of the base `a` repeated 10 times.

6. **Combine with Repeated Base**: Add the repeated base to the combined sequence to produce a `final_sequence`.

7. **Convert to Uppercase**: Ensure the `final_sequence` is in uppercase.

8. **Format the Output**: Use an f-string to create a descriptive output that includes the original sequence, the sliced part, the combined sequence, the repeated base, and the final sequence.

::: {.callout-answer}

```
# Step 1: Create a DNA sequence
dna_sequence = "atcgtagc"

# Step 2: Access specific bases
first_base = dna_sequence[0]   # a
third_base = dna_sequence[2]    # c

# Step 3: Slice the sequence
sliced_sequence = dna_sequence[0:5]  # atcgt

# Step 4: Concatenate a new fragment
new_fragment = "ggcta"
combined_sequence = dna_sequence + new_fragment  # atcgtagcggcta

# Step 5: Repeat a base
repeated_base = "a" * 10  # aaaaaaaaaa

# Step 6: Combine with repeated base
final_sequence = combined_sequence + repeated_base  # atcgtagcggctaaaaaaaaaa

# Step 7: Convert to uppercase
upper_final_sequence = final_sequence.upper()  # ATCGTAGCGGCTAAAAAAAAAA

# Step 8: Format the output
output = (f"Original DNA Sequence: {dna_sequence}\n"
          f"First Base: {first_base}\n"
          f"Third Base: {third_base}\n"
          f"Sliced Sequence (first 5 bases): {sliced_sequence}\n"
          f"Combined Sequence: {combined_sequence}\n"
          f"Repeated Base (a): {repeated_base}\n"
          f"Final Sequence (in uppercase): {upper_final_sequence}")

# Print the output
print(output)
```
Output:
```
Original DNA Sequence: atcgtagc
First Base: a
Third Base: c
Sliced Sequence (first 5 bases): atcgt
Combined Sequence: atcgtagcggcta
Repeated Base (a): aaaaaaaaaa
Final Sequence (in uppercase): ATCGTAGCGGCTAAAAAAAAAAA
```

:::
:::

## Summary

After these exercises you should be able to work with numerical data and strings in Python! 

::: {.callout-tip}
#### Key Points

- It is easy to use operators and functions to work both with strings and numbers in python
- Tracking memory usage and data type can be important

:::
