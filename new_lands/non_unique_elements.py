"""

Given a non-empty list of integers, return a list consisting of only the non-unique elements in this list. 
AKA: Remove all unique elements (elements which are contained in a given list only once). 
Do not change the order of the list. 

Input: A list of integers
Output: An iterable of integers

Precondition: 0 < len(data) < 1000


>>> checkio([1, 2, 3, 1, 3])
[1, 3, 1, 3]

>>> checkio([1, 2, 3, 4, 5])
[]

>>> checkio([5, 5, 5, 5, 5])
[5, 5, 5, 5, 5]

>>> checkio([10, 9, 10, 10, 9, 8])
[10, 9, 10, 10, 9]

>>> checkio([2])
[]

"""


def checkio(data):
    
    data_list = list(data)
    duplicate_nums = []
    unique_nums = []
    i = 0


    while len(data) > 0:
        data.pop(0)
        current_num = data_list[i]

        if current_num in data or current_num in duplicate_nums:
            duplicate_nums.append(current_num)

        i += 1


    print(duplicate_nums)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')