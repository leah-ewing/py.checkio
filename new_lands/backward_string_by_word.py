"""

In a given string you should reverse every word, but the words should stay in their places.

Input: A string.
Output: A string.

Precondition: The line consists only from alphabetical symbols and spaces.


>>> backward_string_by_word('')
''

>>> backward_string_by_word('world')
'dlrow'

>>> backward_string_by_word('hello world')
'olleh dlrow'

>>> backward_string_by_word('hello   world')
'olleh   dlrow'


"""

def backward_string_by_word(text):
    text = text.split(' ')
    backwards_list = []

    for word in text:
        backwards_list.append(word[::-1])
    
    text = " ".join(backwards_list)

    return text



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')