"""

You have to split a given array into two arrays. 
If it has an odd amount of elements, then the first array should have more elements. 
If it has no elements, then two empty arrays should be returned.


>>> split_list([1, 2, 3, 4, 5, 6])
[[1, 2, 3], [4, 5, 6]]

>>> split_list([1, 2, 3])
[[1, 2], [3]]

>>> split_list([])
([], [])

"""


def split_list(items):

    if len(items) == 0:
        print([[], []])
        
    else:
        new_list = []
        
        if len(items) % 2 == 0:
            first_half = items[:int(len(items) / 2)]
            last_half = items[int(len(items) / 2):]
            new_list.append(first_half)
            new_list.append(last_half)

        else:
            first_half = items[:int(len(items) / 2) + 1]
            last_half = items[int(len(items) / 2 + 1):]
            new_list.append(first_half)
            new_list.append(last_half)
            

        print(new_list)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')
