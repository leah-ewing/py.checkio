"""

In a given list the first element should become the last one. 

An empty list or list with only one element should stay the same.

Input: List
Output: Iterable

>>> replace_first([1, 2, 3, 4])
[2, 3, 4, 1]

>>> replace_first([1])
[1]

>>> replace_first([])
[]

"""


def replace_first(items):

    if len(items) > 0:
        items.append(items[0])
        items.pop(0)
        
    print(items)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')
