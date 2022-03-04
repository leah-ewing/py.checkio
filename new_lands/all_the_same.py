"""

Check if all elements in the given list are equal.

Input: List.
Output: Bool.


>>> all_the_same([1, 1, 1])
True

>>> all_the_same([1, 2, 1])
False

>>> all_the_same(['a', 'a', 'a'])
True

>>> all_the_same([])
True

"""


def all_the_same(elements):
    
    if len(elements) > 0:
        elements = set(elements)
        if len(elements) == 1:
            print(True)
        else:
            print(False)
    else:
        print(True)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')
