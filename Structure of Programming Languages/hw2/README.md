# Structure of Programming Languages - Assignment 2

This folder contains the solutions for **Assignment 2** in the "Structure of Programming Languages" course. 
The focus of this assignment is on **Functional Programming** paradigms in Python.

## 📝 Topics Covered
* **Lambda Expressions:** Anonymous functions for concise operations.
* **Higher-Order Functions:** Extensive use of `map`, `filter`, and `reduce`.
* **Closures:** Encapsulating state within inner functions (Task Manager).
* **Function Composition:** Building a functional pipeline without loops or recursion.

## 🗂️ Files Structure
The assignment is divided into standalone Python scripts for each question to avoid namespace collisions and make evaluation easier:
* `q1.py`: Lambda expressions and performance comparison (Higher-Order vs. Imperative).
* `q2.py`: Filtering and rolling computations (accumulate) on even/odd numbers.
* `q3.py`: Pure functions to calculate and filter Armstrong numbers.
* `q4.py`: Date generation using mapping (Gregorian and Hebrew dates).
* `q5.py`: Functions returning functions and Taylor approximation for $e^x$.
* `q6.py`: A Task Manager implemented entirely using a closure.
* `q7.py`: A text processing functional Pipeline.

## ⚙️ Installation & Setup
While most of the assignment uses Python's built-in functional libraries (`functools`, `itertools`), Question 4 (Hebrew dates) requires an external library.

To install the required dependencies for this specific assignment, run:
```bash
pip install -r requirements.txt
```

## 🚀 How to Run
Each file is completely standalone. You can evaluate any question by executing its script directly from the terminal.
For example, to evaluate Question 7:

```bash
python q7.py
```