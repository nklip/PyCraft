# Algorithms
<sub>[Back to PyCraft](../README.md#pycraft)</sub>

## Contents

1. [Overview](#overview)
2. [Project structure](#project-structure)
3. [Solutions](#solutions)
4. [Requirements](#requirements)
5. [Tests](#tests)
6. [Adding a solution](#adding-a-solution)

## Overview
<sub>[Back to top](#algorithms)</sub>

Python solutions to LeetCode exercises, mostly grouped by difficulty. Each
solution file includes the problem number, a link to the original task, and a short task
description before its solution class. `Time Complexity` and `Space Complexity`
comments above the entry method describe the implementation in that file and
define the input-size variables they use. Data structures document total storage
at the class level and time complexity above each public operation.

Space estimates account for the data the implementation allocates, including
returned collections where stated. Auxiliary space means memory used in addition
to the input and output. Tree solutions also account for stack depth and, when
building paths, the strings retained during recursion.

## Project structure
<sub>[Back to top](#algorithms)</sub>

```text
algs/
├── easy/
├── medium/
├── tests/
│   ├── easy/
│   ├── medium/
│   └── test_majority_element.py
├── list_node.py
├── majority_element.py
├── README.md
└── tree_node.py
```

Each exercise has its own module, with corresponding tests under `tests/`.
Most solutions live in difficulty folders; [Majority Element](majority_element.py)
currently lives at the collection root. [ListNode](list_node.py) and
[TreeNode](tree_node.py) provide the node types used by the linked-list and
binary-tree exercises.

## Solutions
<sub>[Back to top](#algorithms)</sub>

| Difficulty | LeetCode problem | Implementation | Tests |
| --- | --- | --- | --- |
| Easy | [455. Assign Cookies](https://leetcode.com/problems/assign-cookies/description/) | [assign_cookies.py](easy/assign_cookies.py) | [Tests](tests/easy/test_assign_cookies.py) |
| Easy | [844. Backspace String Compare](https://leetcode.com/problems/backspace-string-compare/description/) | [backspace_string_compare.py](easy/backspace_string_compare.py) | [Tests](tests/easy/test_backspace_string_compare.py) |
| Easy | [110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/) | [balanced_binary_tree.py](easy/balanced_binary_tree.py) | [Tests](tests/easy/test_balanced_binary_tree.py) |
| Easy | [121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/) | [best_time_to_buy_and_sell_stock.py](easy/best_time_to_buy_and_sell_stock.py) | [Tests](tests/easy/test_best_time_to_buy_and_sell_stock.py) |
| Easy | [704. Binary Search](https://leetcode.com/problems/binary-search/description/) | [binary_search.py](easy/binary_search.py) | [Tests](tests/easy/test_binary_search.py) |
| Easy | [94. Binary Tree Inorder Traversal](https://leetcode.com/problems/binary-tree-inorder-traversal/description/) | [binary_tree_inorder_traversal.py](easy/binary_tree_inorder_traversal.py) | [Tests](tests/easy/test_binary_tree_inorder_traversal.py) |
| Easy | [257. Binary Tree Paths](https://leetcode.com/problems/binary-tree-paths/description/) | [binary_tree_paths.py](easy/binary_tree_paths.py) | [Tests](tests/easy/test_binary_tree_paths.py) |
| Easy | [145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/description/) | [binary_tree_postorder_traversal.py](easy/binary_tree_postorder_traversal.py) | [Tests](tests/easy/test_binary_tree_postorder_traversal.py) |
| Easy | [144. Binary Tree Preorder Traversal](https://leetcode.com/problems/binary-tree-preorder-traversal/description/) | [binary_tree_preorder_traversal.py](easy/binary_tree_preorder_traversal.py) | [Tests](tests/easy/test_binary_tree_preorder_traversal.py) |
| Easy | [1346. Check If N and Its Double Exist](https://leetcode.com/problems/check-if-n-and-its-double-exist/description/) | [check_if_n_and_its_double_exist.py](easy/check_if_n_and_its_double_exist.py) | [Tests](tests/easy/test_check_if_n_and_its_double_exist.py) |
| Easy | [70. Climbing Stairs](https://leetcode.com/problems/climbing-stairs/description/) | [climbing_stairs.py](easy/climbing_stairs.py) | [Tests](tests/easy/test_climbing_stairs.py) |
| Easy | [217. Contains Duplicate](https://leetcode.com/problems/contains-duplicate/description/) | [contains_duplicate.py](easy/contains_duplicate.py) | [Tests](tests/easy/test_contains_duplicate.py) |
| Easy | [219. Contains Duplicate II](https://leetcode.com/problems/contains-duplicate-ii/description/) | [contains_duplicate_ii.py](easy/contains_duplicate_ii.py) | [Tests](tests/easy/test_contains_duplicate_ii.py) |
| Easy | [108. Convert Sorted Array to Binary Search Tree](https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/) | [convert_sorted_array_to_binary_search_tree.py](easy/convert_sorted_array_to_binary_search_tree.py) | [Tests](tests/easy/test_convert_sorted_array_to_binary_search_tree.py) |
| Easy | [2824. Count Pairs Whose Sum is Less than Target](https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/description/) | [count_pairs_whose_sum_is_less_than_target.py](easy/count_pairs_whose_sum_is_less_than_target.py) | [Tests](tests/easy/test_count_pairs_whose_sum_is_less_than_target.py) |
| Easy | [1652. Defuse the Bomb](https://leetcode.com/problems/defuse-the-bomb/description/) | [defuse_the_bomb.py](easy/defuse_the_bomb.py) | [Tests](tests/easy/test_defuse_the_bomb.py) |
| Easy | [1089. Duplicate Zeros](https://leetcode.com/problems/duplicate-zeros/description/) | [duplicate_zeros.py](easy/duplicate_zeros.py) | [Tests](tests/easy/test_duplicate_zeros.py) |
| Easy | [171. Excel Sheet Column Number](https://leetcode.com/problems/excel-sheet-column-number/description/) | [excel_sheet_column_number.py](easy/excel_sheet_column_number.py) | [Tests](tests/easy/test_excel_sheet_column_number.py) |
| Easy | [168. Excel Sheet Column Title](https://leetcode.com/problems/excel-sheet-column-title/description/) | [excel_sheet_column_title.py](easy/excel_sheet_column_title.py) | [Tests](tests/easy/test_excel_sheet_column_title.py) |
| Easy | [28. Find the Index of the First Occurrence in a String](https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/) | [find_first_occurence_in_string.py](easy/find_first_occurence_in_string.py) | [Tests](tests/easy/test_find_first_occurence_in_string.py) |
| Easy | [744. Find Smallest Letter Greater Than Target](https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/) | [find_smallest_letter_greater_than_target.py](easy/find_smallest_letter_greater_than_target.py) | [Tests](tests/easy/test_find_smallest_letter_greater_than_target.py) |
| Easy | [2269. Find the K-Beauty of a Number](https://leetcode.com/problems/find-the-k-beauty-of-a-number/description/) | [find_the_k_beauty_of_number.py](easy/find_the_k_beauty_of_number.py) | [Tests](tests/easy/test_find_the_k_beauty_of_number.py) |
| Easy | [278. First Bad Version](https://leetcode.com/problems/first-bad-version/description/) | [first_bad_version.py](easy/first_bad_version.py) | [Tests](tests/easy/test_first_bad_version.py) |
| Easy | [374. Guess Number Higher or Lower](https://leetcode.com/problems/guess-number-higher-or-lower/description/) | [guess_number_higher_or_lower.py](easy/guess_number_higher_or_lower.py) | [Tests](tests/easy/test_guess_number_higher_or_lower.py) |
| Easy | [202. Happy Number](https://leetcode.com/problems/happy-number/description/) | [happy_number.py](easy/happy_number.py) | [Tests](tests/easy/test_happy_number.py) |
| Easy | [232. Implement Queue using Stacks](https://leetcode.com/problems/implement-queue-using-stacks/description/) | [implement_queue_using_stacks.py](easy/implement_queue_using_stacks.py) | [Tests](tests/easy/test_implement_queue_using_stacks.py) |
| Easy | [225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/description/) | [implement_stack_using_queues.py](easy/implement_stack_using_queues.py) | [Tests](tests/easy/test_implement_stack_using_queues.py) |
| Easy | [160. Intersection of Two Linked Lists](https://leetcode.com/problems/intersection-of-two-linked-lists/description/) | [intersection_of_two_linked_lists.py](easy/intersection_of_two_linked_lists.py) | [Tests](tests/easy/test_intersection_of_two_linked_lists.py) |
| Easy | [226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/) | [invert_binary_tree.py](easy/invert_binary_tree.py) | [Tests](tests/easy/test_invert_binary_tree.py) |
| Easy | [392. Is Subsequence](https://leetcode.com/problems/is-subsequence/description/) | [is_subsequence.py](easy/is_subsequence.py) | [Tests](tests/easy/test_is_subsequence.py) |
| Easy | [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/description/) | [isomorphic_strings.py](easy/isomorphic_strings.py) | [Tests](tests/easy/test_isomorphic_strings.py) |
| Easy | [58. Length of Last Word](https://leetcode.com/problems/length-of-last-word/description/) | [length_of_last_word.py](easy/length_of_last_word.py) | [Tests](tests/easy/test_length_of_last_word.py) |
| Easy | [141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/) | [linked_list_cycle.py](easy/linked_list_cycle.py) | [Tests](tests/easy/test_linked_list_cycle.py) |
| Easy | [14. Longest Common Prefix](https://leetcode.com/problems/longest-common-prefix/description/) | [longest_common_prefix.py](easy/longest_common_prefix.py) | [Tests](tests/easy/test_longest_common_prefix.py) |
| Easy | [594. Longest Harmonious Subsequence](https://leetcode.com/problems/longest-harmonious-subsequence/description/) | [longest_harmonious_subsequence.py](easy/longest_harmonious_subsequence.py) | [Tests](tests/easy/test_longest_harmonious_subsequence.py) |
| Easy | [169. Majority Element](https://leetcode.com/problems/majority-element/description/) | [majority_element.py](majority_element.py) | [Tests](tests/test_majority_element.py) |
| Easy | [643. Maximum Average Subarray I](https://leetcode.com/problems/maximum-average-subarray-i/description/) | [maximum_average_subarray_i.py](easy/maximum_average_subarray_i.py) | [Tests](tests/easy/test_maximum_average_subarray_i.py) |
| Easy | [104. Maximum Depth of Binary Tree](https://leetcode.com/problems/maximum-depth-of-binary-tree/description/) | [maximum_depth_of_binary_tree.py](easy/maximum_depth_of_binary_tree.py) | [Tests](tests/easy/test_maximum_depth_of_binary_tree.py) |
| Easy | [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/) | [merge_sorted_array.py](easy/merge_sorted_array.py) | [Tests](tests/easy/test_merge_sorted_array.py) |
| Easy | [1768. Merge Strings Alternately](https://leetcode.com/problems/merge-strings-alternately/description/) | [merge_strings_alternately.py](easy/merge_strings_alternately.py) | [Tests](tests/easy/test_merge_strings_alternately.py) |
| Easy | [21. Merge Two Sorted Lists](https://leetcode.com/problems/merge-two-sorted-lists/description/) | [merge_two_sorted_lists.py](easy/merge_two_sorted_lists.py) | [Tests](tests/easy/test_merge_two_sorted_lists.py) |
| Easy | [876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/description/) | [middle_of_the_linked_list.py](easy/middle_of_the_linked_list.py) | [Tests](tests/easy/test_middle_of_the_linked_list.py) |
| Easy | [2540. Minimum Common Value](https://leetcode.com/problems/minimum-common-value/description/) | [minimum_common_value.py](easy/minimum_common_value.py) | [Tests](tests/easy/test_minimum_common_value.py) |
| Easy | [1. Two Sum](https://leetcode.com/problems/two-sum/description/) | [two_sum.py](easy/two_sum.py) | [Tests](tests/easy/test_two_sum.py) |
| Medium | [2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/description/) | [add_two_numbers.py](medium/add_two_numbers.py) | [Tests](tests/medium/test_two_numbers.py) |

## Requirements
<sub>[Back to top](#algorithms)</sub>

Install [uv](https://docs.astral.sh/uv/getting-started/installation/). The test
commands below request Python 3.14 and pytest through uv. The solutions themselves
use only Python's standard library and the local node helpers; no `.env` is needed.

This exercise collection currently has no `pyproject.toml`, `uv.lock`, or
`Makefile`. The commands use [uv's `--no-project` mode](https://docs.astral.sh/uv/reference/cli/#uv-run--no-project)
and request pytest with `--with`, so no manual environment setup is needed.
The pytest version is not locked here.

## Tests
<sub>[Back to top](#algorithms)</sub>

Run the full suite from the top-level `PyCraft` directory:

```bash
uv run --no-project --python 3.14 --with pytest python -m pytest algs/tests
```

Run one exercise's tests:

```bash
uv run --no-project --python 3.14 --with pytest python -m pytest algs/tests/easy/test_two_sum.py
```

The tests use `unittest.TestCase` and run through pytest. Using
[`python -m pytest`](https://docs.pytest.org/en/stable/how-to/usage.html#calling-pytest-through-python-m-pytest)
adds the current directory to Python's import path, allowing imports such as
`from algs.tree_node import TreeNode` when run from the repository root.

The root `make check` covers the four applications listed in the root `Makefile`;
run the command above to check this collection separately.

## Adding a solution
<sub>[Back to top](#algorithms)</sub>

1. Add a module named after the problem under the appropriate difficulty folder.
2. Put the LeetCode number, source link, and task summary before the solution class.
3. Add `Time Complexity` and `Space Complexity` comments above the entry method.
   Define the variables and account for sorting, temporary collections, recursion,
   and output allocation used by the implementation. For data structures, document
   total storage at the class level and time complexity above each public operation.
4. Add tests in the matching folder under `tests/`, including relevant edge cases.
   For a bug fix, verify that the regression test fails with the old behavior.
5. Add the problem, implementation, and test links to the table above, then run
   the test suite from the repository root.
