"""

Compress a list so that if two or more elements in a row are the same, only return one element.

Input: List.
Output: "Compressed" Iterable (list, tuple, iterator ...).

>>> compress([5, 5, 5, 4, 5, 6, 6, 5, 5, 7, 8, 0, 0])
[5, 4, 5, 6, 5, 7, 8, 0]

>>> compress([1, 1, 1, 1, 2, 2, 2, 1, 1, 1])
[1, 2, 1]

>>> compress([7, 7])
[7]

>>> compress([])
[]

>>> compress([1, 2, 3, 4])
[1, 2, 3, 4]

>>> compress([9, 9, 9, 9, 9, 9, 9])
[9]

"""

def compress(items):
    
    if len(items) > 0:

        new_list = []
        new_list.append(items.pop(0))
        
        for item in items:
            if item != new_list[-1]:
                new_list.append(item)
        
        print(new_list)
                 
    else:
        print(items)
    


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')