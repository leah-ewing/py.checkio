""" 

You have a string that consist only of digits. 

You need to find how many zero digits ("0") are at the beginning of the given string.

Input: A string, that consist of digits
Output: An Int


>>> beginning_zeros('100')
0

>>> beginning_zeros('001')
2

>>> beginning_zeros('100100')
0

>>> beginning_zeros('001001')
2

>>> beginning_zeros('012345679')
1

>>> beginning_zeros('0000')
4

"""

def beginning_zeros(number):
    zeros = 0
    i = 0

    while i < len(str(number)):
        if str(number[i]) == '0':
            zeros += 1
            i += 1
        else:
            break
    
    print(zeros)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')