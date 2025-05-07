# Python - Import & Modules

## Read or Watch:
- [Modules](https://docs.python.org/3/tutorial/modules.html)
- [Command line arguments](https://docs.python.org/3/library/sys.html#sys.argv)
- [Pycodestyle – Style Guide for Python Code](https://pypi.org/project/pycodestyle/)

## Man or Help:
- `python3`

---

## Learning Objectives
By the end of this project, you should be able to explain the following concepts to anyone, **without the help of Google**:

### General
- Why Python programming is awesome.
- How to import functions from another file.
- How to use imported functions.
- How to create a module.
- How to use the built-in function `dir()`.
- How to prevent code in your script from being executed when imported.
- How to use command line arguments with your Python programs.

---

## Requirements

### General
- **Allowed editors:** `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on **Ubuntu 22.04 LTS** using `python3` (version 3.10.*).
- All your files should end with a **new line**.
- The first line of all your files should be exactly:
  ```python
  #!/usr/bin/python3

  # Python Modules & Command-Line Arguments Project

A **README.md** file at the root of the project folder is mandatory.

Your code should follow the **pycodestyle** (version 2.7.\*) style guide.  
All files must be executable.  
The length of your files will be tested using the `wc` command.

---

## Project Structure

This project contains Python scripts that demonstrate the use of modules, importing, and command-line arguments.

| File                  | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| `0-add.py`            | Demonstrates importing a function from another file and using it.           |
| `1-args.py`           | Explains how to use command-line arguments in Python.                       |
| `2-variable_load.py`  | Shows how to import variables from another file.                            |
| `3-safe_print_div.py` | Demonstrates safe division using exception handling.                        |
| `4-hidden_discovery.py` | Uses the `dir()` function to list all names defined in a module.          |
| `5-imported_module.py` | Explains how to prevent code from being executed when a script is imported. |

---

## Usage

To run any of the Python scripts in this project, use the following command format in your terminal:

```bash
./<script_name>.py
