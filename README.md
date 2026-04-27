
# Python Lists Assignment

Python Assignments from Aurora Robotics Workshop 2.0

## Overview

This repository contains a comprehensive series of Python exercises focused on mastering list operations, from basic creation to advanced memory concepts. Each task builds on the previous one to create a complete learning journey through Python lists.

## Tasks

### Task 1: Create Lists (`task1_create_lists.py`)
Learn how to create different types of lists with various data:
- Homogeneous lists (single data type): fruits, programming languages, numbers
- Heterogeneous lists (mixed data types): student details with name, age, height, and status

**Key Concepts:** List initialization, list printing

---

### Task 2: Indexing (`task2_indexing.py`)
Master positive indexing to access individual elements:
- Access elements using 0-based indexing
- Access multiple elements in a single print statement
- Extract specific items from a list of objects: Pen, Book, Laptop, Phone, Bag, Bottle

**Key Concepts:** Positive indexing, element access, zero-based indexing

---

### Task 3: Negative Indexing (`task3_negative%20indexing.py`)
Understand negative indexing for reverse access:
- Access elements from the end of a list
- Last element: `numbers[-1]`
- First element: `numbers[-9]` (from a 9-element list)
- Various middle elements using negative indices

**Key Concepts:** Negative indexing, reverse access, list length relationships

---

### Task 4: Slicing (`task4_slicing.py`)
Learn slice notation to extract multiple elements:
- Slice from the beginning: `nums[:3]` (elements 0-2)
- Slice from the end: `nums[-3:]` (last 3 elements)
- Slice a range: `nums[3:7]` (elements 3-6)

**Key Concepts:** Slice notation, range extraction, start/stop indices

---

### Task 5: Mutation (`task5_mutation.py`)
Modify list elements in place:
- Change elements by positive index: `colors[1] = "Purple"`
- Change elements by negative index: `colors[-2] = "White"`, `colors[-1] = "Silver"`
- Update multiple elements
- Demonstrate that changes persist in the list

**Key Concepts:** List mutability, in-place modification, element assignment

---

### Task 6: Memory Model (`task6_memory_model.py`)
Understand how Python handles list references and memory:
- Create list aliases: `b = a`
- Modify through alias: changes affect both variables
- Check object identity: `id()` function shows same memory address
- Learn that both variables point to the same list object in memory

**Key Concepts:** Reference semantics, object identity, memory model, aliasing

---

### Task 7: Mini Project (`task7_mini_project.py`)
Apply all concepts in a practical scenario:
- Work with a student record: name, age, major, GPA, country
- Modify student details using negative indexing
- Use list methods: `reverse()`
- Extract subsets using slicing

**Key Concepts:** List methods, practical application, compound operations

---

### Bonus Challenge (`bonus.py`)
Advanced slicing techniques:
- Extended slice with step: `nums[-1::-2]` (reverse with step of 2)
- Standard slicing: `nums[2:7]`

**Key Concepts:** Extended slicing, step parameter, reverse traversal
