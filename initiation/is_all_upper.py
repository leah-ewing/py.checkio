"""

Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True.

Input: A string
Output: a boolean

Precondition: a-z, A-Z, 1-9 and spaces

>>> is_all_upper('ALL UPPER')
True

>>> is_all_upper('all lower')
False

>>> is_all_upper('mixed UPPER and lower')
False

>>> is_all_upper('')
True

>>> is_all_upper('444')
True

>>> is_all_upper('55 55 5')
True

"""

def is_all_upper(text):
    lowercase = 'abcdefghijklmnopqrstuvwxyz'

    if len(text) == 0:
        answer = True
    else:
        for letter in text:
            if letter in lowercase:
                answer = False
            else:
                answer = True

    print(answer)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')