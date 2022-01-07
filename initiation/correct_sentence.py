"""

For the input of your function, you will be given one sentence. 
You have to return a corrected version, that starts with a capital letter and ends with a period (dot).

Input: A string
Output: A string

Precondition: No leading and trailing spaces, text contains only spaces, 'a-z', 'A-Z', ',' and '.'


>>> correct_sentence("greetings, friends")
'Greetings, friends.'

>>> correct_sentence("Greetings, friends")
'Greetings, friends.'

>>> correct_sentence("Greetings, friends.")
'Greetings, friends.'

>>> correct_sentence("hi")
'Hi.'

>>> correct_sentence("welcome to New York")
'Welcome to New York.'

"""


def correct_sentence(text):
    text_list = []
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for character in text:
        text_list.append(character)

    if text_list[0] not in upper:
        first_letter = text_list[0].upper()
        text_list.pop(0)
        text_list.insert(0, first_letter)

    if text_list[-1] != '.':
        text_list.append('.')

    answer = "".join(text_list)

    return answer




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')