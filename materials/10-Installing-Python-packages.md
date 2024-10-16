---
title: Installing Python Packages
---

::: {.callout-tip}
#### Learning Objectives

- Be able to install the packages and modules needed

:::

## Installing Packages with `pip`

`pip` (Python's default package installer) is used to install packages from the **Python Package Index (PyPI)**, a repository of software for Python.

You can install packages by running the following command in your terminal or command prompt:

`pip install package_name`

For example, to install the `numpy` library:

`pip install numpy`

You can install a specific version of a package by specifying the version number:

`pip install numpy==1.21.0`

To update a package to the latest version:

`pip install --upgrade package_name`

**Pros of Using `pip`**

- **Wide range of packages**: Since `pip` installs from PyPI, it gives access to a vast collection of Python libraries.
- **Lightweight**: Pip is small and fast, suitable for installing Python-only packages.
- **Flexible**: Pip works well with virtual environments (e.g., `venv` or `virtualenv`) to isolate dependencies.

**Cons of Using `pip`**

- **Dependency management**: Pip doesn't handle package dependencies as robustly as `conda`. This can result in conflicts or missing dependencies.
- **Python-only**: Pip is designed for Python packages. If a package has non-Python dependencies (e.g., compiled libraries), you may have to install them manually.


## Installing Packages with `conda`

`conda` is a package manager included with the **Anaconda** distribution, which is widely used for data science, scientific computing, and machine learning. It manages both **Python** and **non-Python dependencies**, making it a more versatile option in certain environments. 

Rather than using the Anaconda distribution, (which though good comes with a lot unnecessary packages) install conda directly. New lightweight faster alternatives to `conda`, `mamba` and `micromamba` are now widely used. They work in the same way with the same commands.

**How to Install a Package with `conda`**

To install a package using `conda`, you would use:

`conda install package_name`

For example, to install `numpy`:

`conda install numpy`

To install a specific version of a package using `conda`:

`conda install numpy=1.21.0`

To update an installed package to the latest version:

`conda update package_name`

Generally you would create a environment specific maybe to python projects with the packages you need etc. 
```
conda create --name env_name
conda env list
conda activate env_name
conda install -c conda-forge package_name 
#conda-forge is a channel with generally more up to date packages
conda deactivate
```

**Pros of Using `conda`**

- **Cross-language package management**: `Conda` can install packages and libraries that are written in Python, C, C++, R, or other languages.
- **Handles non-Python dependencies**: Unlike `pip`, conda can install non-Python dependencies such as `libc`, `OpenBLAS`, or other compiled libraries.
- **Robust dependency resolution**: Conda provides more sophisticated dependency resolution, reducing the risk of package conflicts.
- **Environment management**: Conda simplifies creating isolated environments, allowing you to manage multiple versions of Python or other libraries on the same system easily.

**Cons of Using `conda`**

- **Limited packages**: Although conda has its own package repository, it doesn't have access to all Python packages in PyPI. Sometimes, you might need to fall back on `pip`.
- **Slower**: Conda can be slower and heavier than pip, especially when solving complex package dependencies.
- **Larger installation**: The Anaconda distribution is large, as it comes with many pre-installed libraries. This might be unnecessary if you only need specific packages.
- **Multiple environments use more space**: Having multiple different environments with different software versions can take up a lot of space (though unfortunately itis often necessary)

Overview of using conda:

| **Feature**                  | **Description**                                                                                       |
|------------------------------|-------------------------------------------------------------------------------------------------------|
| **Isolation**                | Each environment has its own packages and dependencies, avoiding conflicts between projects           |
| **Reproducibility**           | Environments can be exported to `environment.yml` files, ensuring consistent setups across systems    |
| **Package Management**        | Conda manages not just Python packages, but also dependencies for languages like R, C++, etc          |
| **Multiple Environments**     | Supports creating and switching between environments for different projects with different setups     |
| **Creating an Environment**   | `conda create --name myenv python=3.9` – Creates a new environment with a specific Python version      |
| **Activating an Environment** | `conda activate myenv` – Activates the environment for use                                            |
| **Installing Packages**       | `conda install numpy pandas` – Installs packages into the active environment                          |
| **Listing Environments**      | `conda env list` – Lists all environments                                                             |
| **Exporting an Environment**  | `conda env export > environment.yml` – Exports environment setup to a file                            |
| **Creating from yml File**    | `conda env create -f environment.yml` – Recreates environment from a `.yml` file                      |
| **Removing an Environment**   | `conda env remove --name myenv` – Deletes an environment                                              |


## Combining `pip` and `conda`

In some cases, you may need to use both `pip` and `conda` in the same environment. For example, if a package isn't available via `conda`, you can use `pip` to install it.

Example: Using `conda` and `pip` together:

1. Create a new conda environment:

`conda create -n myenv python=3.9`

2. Activate the environment:

`conda activate myenv`

3. Install a package with `conda`:

`conda install numpy`

4. Install a package with `pip`:

`pip install some_package_not_in_conda`

**Important Note:**

- **Install with `conda` first**: It's generally recommended to install packages with `conda` first. If the package is not available, then use `pip` as a fallback to minimize conflicts.

---

## Summary: When to Use `pip` or `conda`

| **Criteria**                    | **pip**                           | **conda**                          |
|----------------------------------|-----------------------------------|------------------------------------|
| **Primary Use**                  | Python packages from PyPI         | Cross-language package management |
| **Dependency Resolution**        | Basic (manual at times)           | Advanced (automatic)              |
| **Non-Python Dependencies**      | Not handled                       | Handled                           |
| **Speed and Performance**        | Lightweight and fast              | Slower, but more robust           |
| **Access to Packages**           | Vast library via PyPI             | Limited to conda channels         |
| **Environments**                 | Works with `venv` or `virtualenv` | Built-in environment management   |
| **Best For**                     | Pure Python projects              | Data science, scientific computing|


## Using Command Line in Jupyter Notebooks or Python Console

When working in Jupyter notebooks or the Python console, you can use command-line operations to install and manage Python packages. This can be done using either `pip` or `conda`, depending on your setup.


You can run shell commands directly in a Jupyter notebook by prefixing them with an exclamation mark (`!`). Here’s how to install packages using `pip`:

- with `pip`

To install a package (e.g., `numpy`), you can run the following command in a cell:

```
!pip install numpy

```
- with conda

To install a package (e.g., `numpy`), you can run:

```
!conda install numpy -y
```

::: {.callout-exercise}
#### Install `pandas` and `numpy`

try to install pandas and numpy using `mamba` , `conda` or `pip`
You should have already installed mamba using the setup instructions

:::



## Summary

Using Package managers can be very useful to enable you to easily install, update, and manage software packages (libraries or programs) on your computer. 
They automate the process, saving you time and effort. 
virtual environments are isolated environments that allow you to manage dependencies and packages for different projects separately. 
They can be used to create specific setups for each project without interference from global installations.

::: {.callout-tip}
#### Key Points

- Easy Installation: Quickly install software with simple commands instead of downloading and configuring manually.
- Dependency Management: Automatically handle and install any additional software that your main software needs to run (dependencies).
- Version Control: Manage different versions of packages to ensure compatibility and avoid conflicts.
- Updates: Easily update installed software to the latest versions with a single command.
- Environment Isolation: Create separate environments for different projects, preventing conflicts between package versions.

:::
