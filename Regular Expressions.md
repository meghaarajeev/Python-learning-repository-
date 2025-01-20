# Regular Expressions in Python from Scratch

Regular expressions (regex) in Python are used for string matching and pattern recognition. They are highly versatile and allow you to specify complex search patterns. Here's a comprehensive guide to learning regex from scratch in Python.

---

## 1. Basics of Regular Expressions
A regular expression is a sequence of characters that define a search pattern.

**Common use cases:**
- Finding substrings in text.
- Replacing patterns.
- Splitting strings based on patterns.
- Validating input (e.g., email, phone numbers).

---

## 2. Importing the `re` Module
To use regex in Python, import the `re` module:

```python
import re
```

---

## 3. Simple Matching
To match a specific word or phrase:

```python
import re

text = "hello world"
pattern = "hello"

if re.search(pattern, text):
    print("Match found!")
```

---

## 4. Common Regex Functions

### 4.1 `re.search()`
Searches for the first occurrence of a pattern in a string:

```python
match = re.search(r"world", "hello world")
if match:
    print("Found:", match.group())  # Output: Found: world
```
