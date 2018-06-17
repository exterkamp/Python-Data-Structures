<p>
    <img src="https://img.shields.io/badge/coverage-100%25-brightgreen.svg"/>
    <img src="https://img.shields.io/badge/python-%3E%3D3.6.4-blue.svg"/>
</p>

# Python Data Structures

This project is a repository of common computer science data
structures, sorting algorithms, and functions.  Comments have 
been provided to explain the classes' implementation and underlying
logic.

### Testing

Running the test suite with [unittest](https://docs.python.org/3/library/unittest.html).
```Bash
$ python -m unittest discover tests
```

Running the test suite with coverage report with [coverage](http://coverage.readthedocs.io/en/latest/).
```Bash
$ coverage run -m unittest discover tests
$ coverage report -m
```

### Sorting Algorithms
* [Quicksort](sorts/quicksort.py)
* [Mergesort](sorts/mergesort.py)
* [Radixsort](sorts/radixsort.py)
* [Heapsort](sorts/heapsort.py)
* [Topological Sort](structures/graph.py)

### Searching Algorithms
* [BinarySearch](searches/binary_search.py)
* [Breadth First Search](searches/breadth_first_search.py)
  * [2D Grid BFS](searches/breadth_first_search.py)
  * [Graph BFS](searches/breadth_first_search.py)

### Data Structures
* [LRU Cache](structures/lru_cache.py)
* [Naïve Tree](structures/naive_tree.py)
  * [In-Order Traversal](structures/naive_tree.py)
  * [Pre-Order Traversal](structures/naive_tree.py)
  * [Post-Order Traversal](structures/naive_tree.py)
* [Binary Search Tree](structures/binary_search_tree.py)
* [Hash Map](structures/hash_map.py)
  * [DJB2 Hash Function](structures/hash_map.py)
  * [SDBM Hash Function](structures/hash_map.py)
  * [Lose/Lose Hash Function](structures/hash_map.py)
* [Heap](structures/heap.py)
* [Trie](structures/trie.py)
* [Priority Queue](structures/priority_queue.py)
* [Linked List](structures/linked_list.py)
  * [Contains Cycles](structures/linked_list.py)
  * [Find Start of Cycle](structures/linked_list.py)
* [Graph](structures/graph.py)
  * [Detect Cycle](structures/graph.py)

### Algorithms

Different algorithmic programs.  Grouped by general topic.

#### Bitwise Algorithms
* [Hamming Distance](algorithms/bitwise/hamming_ops.py)
* [Hamming Weight](algorithms/bitwise/hamming_ops.py)
* [Binary Complement](algorithms/bitwise/complement.py)

#### Mathematical Algorithms
* [Fibonacci](algorithms/math/fibonacci.py)
* [Factorial](algorithms/math/factorial.py)

#### String Based Algorithms
* [Fizz Buzz](algorithms/string/fizz_buzz.py)
* [Permutations](algorithms/string/permutations.py)
* [Combinations](algorithms/string/combinations.py)
  * [Letters in Word](algorithms/string/combinations.py)
  * [Letters from Phone](algorithms/string/combinations.py)
* [Longest Common Prefix](algorithms/string/longest_common_prefix.py)
  * [Trie](algorithms/string/longest_common_prefix.py)
  * [Reduce](algorithms/string/longest_common_prefix.py)
* [Finding Substring](algorithms/string/rabin_karp_substring_search.py)
  * [Rabin-Karp](algorithms/string/rabin_karp_substring_search.py)