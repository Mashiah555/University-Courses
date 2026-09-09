# Structure of Programming Languages - Assignment 3

This repository contains the solutions for **Assignment 3** in the "Structure of Programming Languages" course. 
The focus of this assignment is on advanced **Functional Programming** paradigms in Python, specifically emphasizing **Recursion** and **Lazy Evaluation**. 
All solutions adhere strictly to pure functional principles: no loops (`for`/`while`) and no mutable variables.

## 📝 Topics Covered
* **Pure Functions:** Implementing logic without state changes or mutable objects.
* **Regular Recursion:** Solving computational problems using standard recursive calls.
* **Tail Recursion:** Optimizing recursive functions to allow execution with lower space complexity, avoiding recursion depth limit issues.
* **Lazy Evaluation & Generators:** Utilizing generators (`yield`) to process data on-demand, minimizing memory footprint and enabling infinite sequences.

## 🗂️ Files Structure
The assignment is divided into two main subdirectories containing standalone Python scripts for each question:

### `recursions/`
* `q1.py`: Tuple generation (1 to 1000) using regular and tail recursion.
* `q2.py`: Array sum calculation operating on the generated tuple.
* `q3.py`: Finding the Least Common Multiple (LCM) purely via recursion.
* `q4.py`: Boolean recursive function to identify numeric palindromes.
* `q5.py`: Alphanumeric palindrome checker featuring string cleaning and Hebrew final letters support.
* `q6.py`: A recursive `sortedzip` function to sort and zip lists of lists.
* `q7.py`: RLE (Run-Length Encoding) compression implemented recursively.

### `generators/`
* `q1.py`: Eager vs. Lazy Evaluation comparison (measuring execution time and memory footprint).
* `q2.py`: An infinite prime number generator using pure recursion and `yield from`.
* `q3.py`: A Taylor series generator for approximating $e^x$.

## ⚙️ Installation & Setup
This assignment relies entirely on Python's built-in features (e.g., `sys`, `time`). No external libraries are needed, so you can skip installing dependencies.

## 🚀 How to Run
Each file is completely standalone. You can evaluate any question by executing its script directly from the terminal. 
Make sure you run them from the root of this folder.

For example, to evaluate Question 5 from the recursions part:

```bash
python recursions/q5.py
```
