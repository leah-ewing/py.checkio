"""

Sort a list by absolute value in ascending order.

Input: A list

Output: The list

>>> absolute_sort([-20, -5, 10, 15])
[-5, 10, 15, -20]

>>> absolute_sort([1, 2, 3, 0])
[0, 1, 2, 3]

>>> absolute_sort([-1, -2, -3, 0])
[0, -1, -2, -3]
 
"""

def absolute_sort(values):
    
    abs_pairs = []
    abs_values = []
    new_list = []
    
    for value in values:
        abs_values.append(abs(value))
        abs_pairs.append([value, abs(value)])
        
    abs_values = sorted(abs_values)
    
    for value in abs_values:
        for pair in abs_pairs:
            if value == pair[1]:
                new_list.append(pair[0])

    print(new_list)

    
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")