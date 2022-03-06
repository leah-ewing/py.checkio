"""

Given a list, return two values:
- The first one is a concatenation of all strings from the given list. 
- The second one is a sum of all integers from the given list.

Input: An array of strings and integers
Output: A list or tuple

>>> sum_by_types([])
['', 0]

>>> sum_by_types([1, 2, 3])
['', 6]

>>> sum_by_types(['1', 2, 3])
['1', 5]

>>> sum_by_types(['1', '2', 3])
['12', 3]

>>> sum_by_types(['1', '2', '3'])
['123', 0]

>>> sum_by_types(['size', 12, 'in', 45, 0])
['sizein', 57]

"""


def sum_by_types(items):
    
    string_list = []
    number_list = []
    new_list = []
    
    for item in items:
        if type(item) == str:
            string_list.append(item)
        elif type(item) == int or type(item) == float:
            number_list.append(item)
    
    new_list.append("".join(string_list))
    new_list.append(sum(number_list))
    
    print(new_list)
    
    
    
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")
        