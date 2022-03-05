"""

Remove all of the elements after the given one from list.
- If a cutting element cannot be found, then the list shouldn't be changed
- If the list is empty, then it should remain empty.

Input: List and the border element.
Output: Iterable (tuple, list, iterator ...).

>>> remove_all_after([1, 2, 3, 4, 5], 3)
[1, 2, 3]

>>> remove_all_after([1, 1, 2, 2, 3, 3], 2)
[1, 1, 2]

>>> remove_all_after([1, 1, 2, 4, 2, 3, 4], 2)
[1, 1, 2]

>>> remove_all_after([1, 1, 5, 6, 7], 2)
[1, 1, 5, 6, 7]

>>> remove_all_after([], 0)
[]

>>> remove_all_after([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)
[7]

"""


def remove_all_after(items, border):

    if border in items:
        for i in range(len(items) - 1):
            if items[i] == border:
                if items[i] in items[i::]:
                    updated_list = items[:i + 1]
                    break
                else:
                    updated_list = items[:i + 1]
        print(updated_list)
    else:
        print(items)
    


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")
