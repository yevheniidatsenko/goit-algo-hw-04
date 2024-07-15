# Sorting Algorithms

## Introduction

In this homework, we will explore the world of sorting algorithms, a fundamental concept in computer science. We will compare three different sorting algorithms, analyze their efficiency, and draw conclusions about their performance.

## Task Description

### Part 1: Comparing Sorting Algorithms

In this part, you will implement and compare three sorting algorithms: Merge Sort, Insertion Sort, and Timsort. You will use the `timeit` module to measure the execution time of each algorithm on different data sets. Your tasks include:

- Implementing the three sorting algorithms.
- Testing their efficiency on various data sets.
- Measuring the execution time of each algorithm using `timeit`.
- Analyzing the results and drawing conclusions about the performance of each algorithm.

### Part 2: Optional Task - Merging Sorted Lists

In this optional task, you will implement a function `merge_k_lists` that takes a list of sorted lists as input and returns a single sorted list. You can use the merge sorting algorithm as a reference.

#### Example Input and Output

Given:

```python
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Sorted list:", merged_list)
```

Expected Output:

```python
Sorted list: [1, 1, 2, 3, 4, 4, 5, 6]
```

## Goals and Objectives

- Understand the basics of sorting algorithms.
- Implement and compare different sorting algorithms.
- Analyze the efficiency of each algorithm.
- Draw conclusions about the performance of each algorithm.
- Implement a function to merge sorted lists.

# Results of code execution:

![alt text](assets/SCR-20240715-kiup.png)

# Conclusion:

Timsort (sorted and sort):

Timsort performed the best on all datasets. This proves its effectiveness due to its hybrid nature that combines merge and insertion sorting. Using the built-in sorted and sort functions is most appropriate for most sorting tasks in Python.

Merge Sort:

Merge Sort is effective for medium to large datasets, but is inferior to Timsort. This algorithm has stable performance, but its execution time increases with the size of the data.

Insertion Sort:

Insertion Sort works well on small data sets, but its performance drops off sharply as the data size increases. Due to its quadratic complexity, this algorithm is not suitable for large datasets.
