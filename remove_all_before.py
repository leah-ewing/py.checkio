"""

Remove from the list all of the elements before the given one.

Input: List and the border element.
Output: Iterable (tuple, list, iterator ...).


>>> remove_all_before([1, 2, 3, 4, 5], 3)
[3, 4, 5]

>>> remove_all_before([1, 1, 2, 2, 3, 3], 2)
[2, 2, 3, 3]

>>> remove_all_before([1, 2, 3, 4, 5], 3)
[3, 4, 5]

>>> remove_all_before([1, 1, 2, 2, 3, 3], 2)
[2, 2, 3, 3]

>>> remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)
[2, 4, 2, 3, 4]

>>> remove_all_before([1, 1, 5, 6, 7], 2)
[1, 1, 5, 6, 7]

>>> remove_all_before([], 0)
[]

>>> remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)
[7, 7, 7, 7, 7, 7, 7, 7, 7]



"""



def remove_all_before(items, border):

    i = 0

    if len(items) > 0:
        if border in items:
            while i < len(items) - 1:
                if items[i] == border:
                    index = i
                    answer = items[index::]
                    break
                else:
                    i += 1
        else:
            answer = items
    else:
        answer = []

    print(answer)

   


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')