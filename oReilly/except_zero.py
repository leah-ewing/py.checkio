"""

Sort the numbers in an array. But the position of zeros should not be changed.

Input: A List.
Output: An Iterable (tuple, list, iterator ...).

>>> except_zero([5, 3, 0, 0, 4, 1, 4, 0, 7])
[1, 3, 0, 0, 4, 4, 5, 0, 7]

>>> except_zero([0, 2, 3, 1, 0, 4, 5])
[0, 1, 2, 3, 0, 4, 5]

>>> except_zero([0, 0, 0, 1, 0])
[0, 0, 0, 1, 0]

>>> except_zero([4, 5, 3, 1, 1])
[1, 1, 3, 4, 5]

>>> except_zero([0, 0])
[0, 0]

"""

def except_zero(items):

    zero_indexes = []
    new_list = []
    
    for i in range(len(items)):
        if items[i] == 0:
            zero_indexes.append(i)
        else:
            new_list.append(items[i])
            
    new_list = sorted(new_list)
    
    for index in zero_indexes:
        new_list.insert(index, 0)

    print(new_list)
    
   
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")