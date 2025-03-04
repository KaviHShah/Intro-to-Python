---
title: Why Learn Python
---

::: {.callout-tip}
#### Learning Objectives

- Gain a broad introduction to Python  
- Explore the advantages and disadvantages of Python as a programming language for data science  
- Examine various examples of Python's common applications and evaluate when to use python
:::


## What is Python?

**High-Level, General-Purpose Language:** 

Python is a versatile programming language created in the late 1980s by Guido van Rossum, emphasising code readability and simplicity. It is widely used for tasks like web development, machine learning, and automation.

**Named After:** “Monty Python’s Flying Circus” (not the reptile).

**Key Features:**

1. **Interpreted Language:** Executes code line-by-line, making debugging easier compared to compiled languages.
2. **Object-Oriented Programming (OOP):** Supports the OOP paradigm through classes and objects, enabling structured, reusable, and scalable code for larger projects.
3. **Very High-Level Language (VHLL):** Allows complex operations to be expressed in simple, single statements.

CPython is the most widely used implementation of Python. Jupyter Notebooks use IPython (Interactive Python), which is an enhanced interactive shell built on top of CPython. Other implementations of Python include Jython, which is written in Java, among others.

We won't go into further detail here, but for more information, see:

Qiang Zhang, Lei Xu, Baowen Xu 2023 , Python meets JIT compilers: A simple implementation and a comparative evaluation
https://doi.org/10.1002/spe.3267 
https://onlinelibrary.wiley.com/doi/full/10.1002/spe.3267

GeeksforGeeks 2023, Difference between various Implementations of Python
https://www.geeksforgeeks.org/difference-various-implementations-python/

IPython Interactive Computing
https://ipython.org/

## Why Python is Great for Data Science

**Simple Syntax and Readability:**

- Python's easy-to-understand syntax helps data scientists focus on solving problems rather than dealing with complex code, making it accessible for both beginners and experts.

**Large Ecosystem of Libraries:**

- NumPy: For numerical computations and array handling.

- Pandas: For data manipulation and analysis.

- Matplotlib & Seaborn: Data visualization tools.

- *Scikit-learn: Machine learning algorithms.

- *TensorFlow & PyTorch: For deep learning and neural networks.

*not covered in this intro course

**Active Community and Support:**

- Python has a large supportive community, offering tutorials, open-source contributions, and plenty of resources.

**Integration with Other Tools:**

- Python works seamlessly with databases, web scraping tools, and big data technologies like Hadoop and Apache Spark.

**Ideal for Prototyping and Interactive Experimentation:**

- Python's flexibility allows for quick algorithm testing and experimentation, which is essential for refining data models. It is not a compiled language making debugging and modifying code easier.

**Scalability:**

- Python can handle both small and large-scale applications, especially when combined with performance-boosting libraries or extensions written in languages like C or C++.

**Dominant in Machine Learning and AI:**

- Python’s libraries like Scikit-learn, TensorFlow, PyTorch and Keras simplify complex machine learning and AI tasks.

## What are the Disadvantages of Python

While Python is a widely used and popular programming language, it does have some disadvantages. Here are some of them:

**Performance Limitations**

- Python is an interpreted language, which generally makes it slower than compiled languages like C or C++. This can be a concern for CPU-intensive tasks or applications requiring high-performance computing.

**Memory Consumption**

- Python tends to use more memory than some other languages due to its data types, and the overhead of its dynamic typing. This can be a drawback in memory-constrained environments.


**Errors as a Result of Flexibility**

- While dynamic typing makes Python easy to use, it can lead to runtime errors that are hard to track down and debug. The flexibility in coding styles and lack of need to strictly specify data types etc., can sometimes lead to less readable and maintainable code if developers don’t adhere to best practices.

**Limited Packages for Certain Use Cases**

- While Python has many packages and modules, there are still areas, especially niche or specialized fields, where these may be limited compared to languages like R or Java.

**Package Dependency Management**

- Managing dependencies in Python can be tricky, particularly with conflicting library versions. Tools like package managers and virtual environments are helpful, but issues still arise in complex projects.

## Summary

Python's ease of use, broad library support, and strong community, make it a top choice for data science. Python is ideal for data analysis, machine learning, and visualization, allowing data scientists to work efficiently and effectively. However, there are downsides to using python as mentioned above. Overall, choosing a specific programming language for a computational task is a mixture of how good it is at addressing the task, and how familiar you are with the language. 

::: {.callout-exercise}
#### Discussion: Deciding to use Python
{{< level 1 >}}

What are some examples of when you would use Python and why?
What are examples of when you wouldn't use Python and why?

::: {.callout-answer}

At the moment you may not use Python for very much unless you are already familiar with it.

You might choose to use Python to train a neural network for image recognition, but not for programming a microcontroller where you might use C++, even though CircuitPython is available.

:::
:::

::: {.callout-tip}

#### Key Points

- Python is defined by its syntax, and is an easy to use high level language commonly used in data science
- Python has many packages and modules for data science and AI
- There are both advantages and disadvantages to programming in python, so choose a programming language suited to the task

:::
