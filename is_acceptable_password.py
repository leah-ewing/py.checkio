"""

Create a password verification function.

The verification condition is:

the length should be bigger than 6.
Input: A string.

Output: A bool.

>>> is_acceptable_password('short')
False

>>> is_acceptable_password('muchlonger')
True

>>> is_acceptable_password('ashort')
False

"""

def is_acceptable_password(password):
    
    if len(password) > 6:
        answer = True
    else:
        answer = False
    
    print(answer)
    

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')