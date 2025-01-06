# Strings
Strings in Python are a sequence of characters and are one of the most commonly used data types. They can be used to handle textual data in various applications. Here’s a comprehensive overview of strings in Python, from the basics to more advanced operations:

### Creation of Strings

Strings can be created by enclosing characters in single, double, or triple quotes:

```python
s1 = 'hello'
s2 = "world"
s3 = """hello world"""
```
#### Immutability
Strings are immutable, meaning once created, their elements cannot be changed.
```
greeting = "Hello"
new_greeting = 'J' + greeting[1:]  # Correct way to modify a string
```

#### Indexing and Slicing
Access individual characters or a range of characters in a string.
```
alpha = "abcdef"
print(alpha[0])  # Outputs 'a'
print(alpha[1:4])  # Outputs 'bcd'
```
