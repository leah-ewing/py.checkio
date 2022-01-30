"""

Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. 
If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

Input: Iterable
Output: Iterable


>>> frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])
[4, 4, 4, 4, 6, 6, 2, 2]

>>> frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])
['bob', 'bob', 'bob', 'carl', 'alex']

"""


def frequency_sort(items):
    pass
   

frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]) # => [4, 4, 4, 4, 6, 6, 2, 2]
# frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob']) # => ['bob', 'bob', 'bob', 'carl', 'alex']


# if __name__ == '__main__':
#     import doctest
#     if doctest.testmod().failed == 0:
#         print('\n🥳 ALL TESTS PASSED! YAY!\n')