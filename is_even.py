"""

Check if the given number is even or not. Your function should return True if the number is even, and False if the number is odd.

Input: An int
Output: A bool

Precondition: both given ints should be between -1000 and 1000

>>> is_even(2)
True

>>> is_even(5)
False

>>> is_even(0)
True

"""


def is_even(num):
    
    if num%2 == 0:
        answer = True
    else:
        answer = False

    print(answer)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')

