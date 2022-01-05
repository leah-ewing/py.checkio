
"""

You have a number and you need to determine which digit in this number is the biggest.

Input: A positive int
Output: An Int (0-9)

>>> max_digit(0)
0

>>> max_digit(52)
5

>>> max_digit(634)
6

>>> max_digit(1)
1

>>> max_digit(10000)
1

"""

def max_digit(number):
    print(int(max(str(number))))




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')