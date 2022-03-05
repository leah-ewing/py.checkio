"""

Given an array with positive numbers and a number "n", find the n-th power of the element in the array with the index n. 
- If n is outside of the array, then return -1.

Input: An array as a list of integers and a number as a integer.
Output: An integer.


>>> index_power([1, 2, 3, 4], 2)
9

>>> index_power([1, 3, 10, 100], 3)
1000000

>>> index_power([0, 1], 0)
1

>>> index_power([1, 2], 3)
-1

>>> index_power([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 9)
1

>>> index_power([96, 92, 94], 3)
-1


"""


def index_power(array, n):

    if n < len(array):
        print(array[n]**n)
    else:
        print(-1)
        


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")