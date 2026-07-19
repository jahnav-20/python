                    PYTHON NOTES (ONE PAGE)

1. List
- Ordered and mutable (changeable).
- Allows duplicate values.
- Syntax: []

Example:
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
print(fruits)

2. Nested List
- A list containing one or more lists.
- Used for rows and columns (2D data).

Example:
students = [["Raju", 20], ["Anu", 21], ["Ravi", 19]]
print(students)
print(students[1][0])   # Anu

3. Tuple
- Ordered and immutable (cannot be changed).
- Allows duplicate values.
- Syntax: ()

Example:
colors = ("red", "green", "blue")
print(colors)
print(colors[1])

4. Set
- Unordered and mutable.
- Does not allow duplicate values.
- Syntax: {}

Example:
numbers = {1, 2, 3, 2, 1}
numbers.add(4)
print(numbers)

5. Dictionary
- Stores data as key : value pairs.
- Mutable and keys are unique.
- Syntax: {}

Example:
student = {"name": "Raju", "age": 20, "course": "Python"}
print(student)
print(student["name"])

Difference:
------------------------------------------------------------
Type        Syntax   Ordered  Mutable  Duplicates
------------------------------------------------------------
List        []       Yes      Yes      Yes
Nested List [[]]     Yes      Yes      Yes
Tuple       ()       Yes      No       Yes
Set         {}       No       Yes      No
Dictionary  {k:v}    Yes      Yes      Keys: No
------------------------------------------------------------