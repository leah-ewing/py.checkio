"""

You have a positive integer. Try to find out how many digits it has?

Input: A positive Int

Output: An Int.

>>> number_length(10)
2

>>> number_length(0)
1

>>> number_length(4)
1

>>> number_length(44)
2

"""

def number_length(a):

    answer = len(str(a))

    print(answer)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')