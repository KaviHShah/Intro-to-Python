---
title: Python Operators
---

::: {.callout-tip}
#### Learning Objectives

- to get aquick overview of the python operators 
- To know the different classes of operators
- To understand that operators can be used beyond numerical data
:::


## What are Operators?

In computer science, **operators** are symbols or keywords used to perform operations on data and variables (operands), like calculations or comparisons. They are essential for building expressions in programming.

Operators are classified by the type of operation:

- **Arithmetic Operators**: Basic math operations (`+`, `-`, `*`, `/`).
- **Logical Operators**: Return `True` or `False` (`AND`, `OR`, `NOT`).
- **Relational Operators**: Compare values, returning boolean results (`>`, `<`, `==`).
- **Assignment Operators**: Assign values to variables (`=`, `+=`).
- **Bitwise Operators**: Operate on bits (`&`, `|`, `^`).
- **Unary/Binary Operators**: Work with one or two operands respectively.

Python has a rich set of operators that are classified into multiple categories

Good resources for python operators can be found at the following: 

https://www.w3schools.com/python/python_operators.asp
https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not

## 1. Arithmetic Operators

These operators perform basic arithmetic operations.

| Operator | Description            | Example  | Applicable Data Types                                       |
|----------|------------------------|----------|-------------------------------------------------------------|
| +        | Addition                | a + b    | int, float, complex, str, list, tuple, byte, bytearray       |
| -        | Subtraction             | a - b    | int, float, complex                                         |
| *        | Multiplication          | a * b    | int, float, complex, str, list, tuple, bytearray            |
| /        | Division                | a / b    | int, float, complex                                         |
| %        | Modulus (remainder)     | a % b    | int, float                                                  |
| **       | Exponentiation          | a ** b   | int, float                                                  |
| //       | Floor Division          | a // b   | int, float                                                  |

## 2. Comparison (Relational) Operators

These operators compare two values and return a boolean (True or False).

| Operator | Description                 | Example  | Applicable Data Types                                      |
|----------|-----------------------------|----------|------------------------------------------------------------|
| ==       | Equal to                    | a == b   | int, float, str, list, tuple, set, frozenset, dict, range   |
| !=       | Not equal to                | a != b   | int, float, str, list, tuple, set, frozenset, dict, range   |
| >        | Greater than                | a > b    | int, float, str, range                                     |
| <        | Less than                   | a < b    | int, float, str, range                                     |
| >=       | Greater than or equal to    | a >= b   | int, float, str, range                                     |
| <=       | Less than or equal to       | a <= b   | int, float, str, range                                     |

## 3. Logical Operators

Used to combine conditional statements.

| Operator | Description                       | Example      | Applicable Data Types                    |
|----------|-----------------------------------|--------------|------------------------------------------|
| and      | Logical AND (both must be true)   | a and b      | bool, int                                |
| or       | Logical OR (either can be true)   | a or b       | bool, int                                |
| not      | Logical NOT (negates boolean)     | not a        | bool, int                                |

## 4. Assignment Operators

Used to assign values to variables, sometimes with an operation included.

| Operator | Description            | Example  | Applicable Data Types                       |
|----------|------------------------|----------|---------------------------------------------|
| =        | Assign                  | a = 5    | All types                                  |
| +=       | Add and assign          | a += 5   | int, float, str, list, tuple, bytearray     |
| -=       | Subtract and assign     | a -= 5   | int, float                                  |
| *=       | Multiply and assign     | a *= 5   | int, float, str, list, tuple, bytearray     |
| /=       | Divide and assign       | a /= 5   | int, float                                  |
| %=       | Modulus and assign      | a %= 5   | int, float                                  |
| **=      | Exponentiate and assign | a **= 5  | int, float                                  |
| //=      | Floor-divide and assign | a //= 5  | int, float                                  |

## 5. Bitwise Operators

Perform operations at the bit level.

| Operator | Description     | Example  | Applicable Data Types      |
|----------|-----------------|----------|----------------------------|
| &        | Bitwise AND      | a & b    | int, byte, bytearray        |
| \|       | Bitwise OR       | a \| b   | int, byte, bytearray        |
| ^        | Bitwise XOR      | a ^ b    | int, byte, bytearray        |
| ~        | Bitwise NOT      | ~a       | int, byte, bytearray        |
| <<       | Left shift       | a << 2   | int, byte, bytearray        |
| >>       | Right shift      | a >> 2   | int, byte, bytearray        |

## 6. Membership Operators

Used to check membership within sequences (like strings, lists, tuples).

| Operator | Description                 | Example         | Applicable Data Types                           |
|----------|-----------------------------|-----------------|------------------------------------------------|
| in       | True if value is present     | 'a' in 'apple'  | str, list, tuple, set, frozenset, dict, range   |
| not in   | True if value is not present | 'b' not in 'apple' | str, list, tuple, set, frozenset, dict, range   |

## 7. Identity Operators

Used to compare memory locations of two objects.

| Operator | Description                          | Example    | Applicable Data Types           |
|----------|--------------------------------------|------------|---------------------------------|
| is       | True if both refer to same object    | a is b     | All types                       |
| is not   | True if not same object              | a is not b | All types                       |

## 8. Unary Operators

Operate on a single operand.

| Operator | Description               | Example  | Applicable Data Types         |
|----------|---------------------------|----------|--------------------------------|
| -        | Negation (unary minus)     | -a       | int, float, complex            |
| +        | Unary plus                 | +a       | int, float, complex            |
| not      | Logical NOT                | not a    | bool, int                      |

## 9. Set Operators

Set-specific operators.

| Operator | Description               | Example     | Applicable Data Types         |
|----------|---------------------------|-------------|--------------------------------|
| \|       | Union (combine sets)       | a \| b      | set, frozenset                 |
| &        | Intersection (common)      | a & b       | set, frozenset                 |
| -        | Difference (in a not in b) | a - b       | set, frozenset                 |
| ^        | Symmetric difference       | a ^ b       | set, frozenset                 |

## Order of Precedence for operators
Operators are ordered in precedence in code (think BODMAS)

Use the table below to see the order: 

# Operator Precedence in Python

| Precedence Level | Operator(s)             | Description                                       | Example                   |
|------------------|-------------------------|---------------------------------------------------|---------------------------|
| 1 (Highest)      | `()`                     | Parentheses (brackets) for grouping expressions    | `(a + b) * c`             |
| 2                | `**`                     | Exponentiation                                    | `a ** b`                  |
| 3                | `+x, -x, ~x`             | Unary plus, unary minus, bitwise NOT              | `+a, -a, ~a`              |
| 4                | `*, /, //, %`            | Multiplication, division, floor division, modulus | `a * b, a / b`            |
| 5                | `+, -`                   | Addition, subtraction                             | `a + b, a - b`            |
| 6                | `<<, >>`                 | Bitwise left shift, right shift                   | `a << b, a >> b`          |
| 7                | `&`                      | Bitwise AND                                       | `a & b`                   |
| 8                | `^`                      | Bitwise XOR                                       | `a ^ b`                   |
| 9                | `|`                      | Bitwise OR                                        | `a | b`                   |
| 10               | `in, not in`             | Membership operators                              | `'a' in 'apple'`          |
| 11               | `<, >, <=, >=, ==, !=`   | Comparison operators                              | `a < b, a == b`           |
| 12               | `is, is not`             | Identity operators                                | `a is b`                  |
| 13               | `not`                    | Logical NOT                                       | `not a`                   |
| 14               | `and`                    | Logical AND                                       | `a and b`                 |
| 15               | `or`                     | Logical OR                                        | `a or b`                  |
| 16 (Lowest)      | `=, +=, -=, *=, /=,      | Assignment operators                              | `a = 5,                   |
|                  | //=, %=, **=, &=, ^=,    |                                                   | a += 5`                   |
|                  | \|=, <<=, >>=`           |                                                   |                           |



## Summary
Use the above tables to find operators you can use in python - they can make code more concise and readable, and can be intuitive to those not familiar with python functions.
However operators can make the code less readable and understandable in some situations, can be less precise and cannot generally be passed as arguments into higher order functions.

::: {.callout-tip}
#### Key Points

- There are many operators that can be used in python
- Operators can behave differently when used with different data types and structures as we will see in the next sections

:::
