```
# maidcleanup: Exception Handling and Static Analysis Project

---

## 📚 Resources

Read or watch:

- **Errors and Exceptions**
- **Learn to Program 11: Static & Exception Handling** (start at minute 7)

---

## 🎯 Learning Objectives

By the end of this project, you should be able to explain — without the help of Google:

### General

- Why Python programming is awesome
- What’s the difference between errors and exceptions
- What are exceptions and how to use them
- When to use exceptions appropriately
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a built-in exception
- When and how to implement clean-up actions after an exception

---

## ✅ Project Requirements

### General

```
- Allowed editors: vi, vim, emacs
- Files must be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- All files must end with a new line
- The first line of each file must be: #!/usr/bin/python3
- A README.md file is required at the root of the project
- Code must follow pycodestyle (version 2.7.*)
- All files must be executable
- File length will be checked using wc
```

---

## 💡 Example Exception Handling

```python
#!/usr/bin/python3

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("You can't divide by zero!")
        return None
    finally:
        print("Cleaning up...")

safe_divide(10, 0)
```

---

## 🧼 Clean-Up Patterns

This project may include utility scripts like `maidcleanup` to remove artifacts generated during development:

- `__pycache__/`
- `*.pyc`
- `*.log`
- `*.tmp`

Use the `maidcleanup` tool or custom scripts to keep your workspace clean and compliant with submission rules.

---

## 🧪 Testing Tips

- Run `pycodestyle your_script.py` to validate style
- Make files executable: `chmod +x your_script.py`
- Ensure all scripts start with: `#!/usr/bin/python3`
- Confirm line endings and length with: `cat -e your_script.py` and `wc your_script.py`

---

## 📄 License

```
This project is part of the Python Exceptions & Clean Code module.
MIT License applies.
```
```
