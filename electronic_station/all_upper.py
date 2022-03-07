"""

Check if a given string has all symbols in upper case. 
If the string is empty or doesn't have any letter in it - function should return False.

Input: A string.
Output: a boolean.


>>> is_all_upper('ALL UPPER')
True

>>> is_all_upper('all lower')
False

>>> is_all_upper('mixed UPPER and lower')
False

>>> is_all_upper('')
False

"""


def is_all_upper(text):

    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    upper_letters = []

    if len(text) > 0:
        for letter in text:
            if letter in uppercase or letter == ' ':
                upper_letters.append(letter)
        
        if len(upper_letters) == len(text):
            print(True)
        else:
            print(False)
    else:
        print(False)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")