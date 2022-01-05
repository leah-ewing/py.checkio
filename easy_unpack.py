"""

Create a function that gets a tuple and returns a tuple with 3 elements, the first, third and second element from the last for the given array

>>> easy_unpack((6, 2, 9, 4, 3, 9))
(6, 9, 3)

>>> easy_unpack((1, 2, 3, 4, 5, 6, 7, 9))
(1, 3, 7)

>>> easy_unpack((1, 1, 1, 1))
(1, 1, 1)

>>> easy_unpack((6, 3, 7))
(6, 7, 3)

"""



def easy_unpack(elements):

    answer = (elements[0], elements[2], elements[-2])

    print(answer)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')
