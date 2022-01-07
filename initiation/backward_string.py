"""

You should return a given string in reverse order.

Input: A string.

Output: A string.


>>> backward_string('val')
lav

>>> backward_string('ohho')
ohho

>>> backward_string('123456789')
987654321

"""

def backward_string(val):

    answer = str(val[::-1])
    
    print(answer)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')