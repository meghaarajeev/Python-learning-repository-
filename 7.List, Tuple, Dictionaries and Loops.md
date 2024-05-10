# 📃LIST IN PYTHON

```
Syntax: l=[a1,a2,a3,....,an]
```
- Elements in a list are enclosed using '[]' paranthesis.
- Mutable data structure
- Duplicate values are allowed

# 🏗️List Constructer
 Instead of using '[ ]' you can also implement a list using a list constructor.
 
                                 list()
                                 
 eg: countries= list(('Nigeria',34,False))

 # 🎯List methods
   ```
     list1= [1,2,3,4,5]
     list2=['banana','apples','mango','oranges']
   ```
1) .extend() : combines elements of list1 with list2.
   ```
   Syntax: list1.extend(list2)
   ```
2) .append() :  A pre-defined method used to add a single item to certain collection types(here: list).
   ```
   syntax: list.append('element')
   ```
3) .insert() : To insert an element to a specified index
   ```
   syntax: list2.insert(1,'cherry')
   ```
4) .remove() : To remove an element from the list.
   ```
   syntax: list2.remove('banana')
   ```
5) .clear() : empties a list
   ```
   syntax: list.clear()
   ```
6) .index()
   ```
    syntax: print(list.index("mango"))
   ```
7) .count()
   ```
   print(list.count(mango))
8) .sort() : prints list in ascending order
   ```
   syntax: list.sort()
   ```
9) .reverse() : prints contents of a list in reverse order
   ```
   syntax: list.reverse()
   ```
10) .copy() : used to copy contents from list to a new list.
   ```
   syntax: list3= list2.copy()
   ```
11) .pop() : pops the last value of the list
   ```
   syntax: list.pop()
   ```
   pop(i) deletes the element in the specified index 'i'
12) del : used to delete the value with a specified index or a complete list
   ```
   syntax: del list[0]
   ```

# 🔢Tuple
```
Syntax: t=(a1,a2,a3,....,an)
```
-Tuples are similar to lists 
-but they are immutable, meaning their elements cannot be changed after they are created. 
-Tuples are denoted by parentheses ().
-It allows repetition of values.

eg: number=(1,'home','True',3,1)

# 👷🏿‍♀️Tuple Constructor
Adds 'tuple' as prefix and use 2 brackets.

    t= tuple((1,'home','True',3,1))

# 📖Dictionary
```
Syntax: t={'a':1,'b':2,'c':3}
```
-Dictionaries are collections of key-value pairs. 
-Each key-value pair maps the key to its corresponding value.
-Dictionaries are unordered, mutable, and indexed. 
-They are denoted by curly braces {}.

eg: d = {'a': 1, 'b': 2, 'c': 3}

# Loops

## While loop
it allows you to loop through a block of code , while a certain condition is true.

```
i=1
while<6
 print(i)
 i+=1
```

## for loop
it is used for iterating over a sequence.
syntax references :
 1) String
    ```
    for i in hello:
      print(i)
    ```
 2)List
 ```
 mylist=['ji','ju','jo']
 for i in mylist:
    print(i)
```
3)Dictionary
```
mydict={'name':'john','age':13,}
for i in mydict:
  print(i)

          
