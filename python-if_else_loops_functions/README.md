# Python - If/Else, Loops, and Functions

This project focuses on understanding and implementing control flow tools, loops, and functions in Python. Below is a simplified explanation of the key concepts and requirements to help you navigate the project.

---

## Learning Objectives

By the end of this project, you should be able to:

### General Concepts
1. **Indentation in Python**:
   - Python uses indentation to define blocks of code. Proper indentation is critical to avoid `IndentationError`.

2. **Control Flow Statements**:
   - **`if` and `if...else`**: Used to execute code conditionally.
   - **`while` and `for` loops**: Used to iterate over sequences or execute code repeatedly.

3. **Special Statements**:
   - **`break`**: Exits a loop prematurely.
   - **`continue`**: Skips the current iteration and moves to the next.
   - **`else` in loops**: Executes after the loop finishes, unless the loop is terminated by `break`.
   - **`pass`**: A placeholder statement that does nothing.

4. **Functions**:
   - Functions are reusable blocks of code defined using the `def` keyword.
   - A function without a `return` statement implicitly returns `None`.

5. **Variables and Scope**:
   - Variables defined inside a function are local to that function.
   - Variables defined outside functions are global.

6. **Tracebacks**:
   - Tracebacks help debug errors by showing the sequence of function calls leading to the error.

7. **Arithmetic Operators**:
   - Operators like `+`, `-`, `*`, `/`, `%`, `**`, and `//` are used for mathematical operations.

---

## Requirements

### Python Scripts
- Use **Ubuntu 20.04 LTS** with Python 3.8.\*.
- All files must:
  - Start with `#!/usr/bin/python3`.
  - End with a new line.
  - Follow **pycodestyle** (version 2.7.\*).
  - Be executable.

### Tools and Resources
- **Editors**: Use `vi`, `vim`, or `emacs`.
- **Documentation**:
  - [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html)
  - [How To Use String Formatters in Python 3](https://realpython.com/python-string-formatting/)
  - [Learn to Program 2: Looping](https://www.youtube.com/watch?v=6iF8Xb7Z3wQ)
  - [Pycodestyle – Style Guide for Python Code](https://pycodestyle.pycqa.org/en/latest/)

---

## Example Code

### If/Else Example
```python
#!/usr/bin/python3
x = 10
if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")