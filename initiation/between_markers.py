"""

Given a string and two markers (the initial one and final), find a substring enclosed between these two markers.

- The initial and final markers are always different.
- The initial and final markers are always 1 char size.
- The initial and final markers always exist in a string and go one after another.

Input: Three arguments. All of them are strings. The second and third arguments are the initial and final markers.
Output: A string.

Precondition: There can't be more than one final and one initial markers.


>>> between_markers('What is >apple<', '>', '<')
'apple'

>>> between_markers('What is [apple]', '[', ']')
'apple'

>>> between_markers('What is ><', '>', '<')
''

>>> between_markers('>apple<', '>', '<')
'apple'

>>> between_markers("[an apple]","[","]")
'an apple'

"""


def between_markers(text, begin, end):

    words = []

    split_text = text.split(" ")
    
    for i in range(len(split_text)):
        if begin in split_text[i] and end in split_text[i]:
            words.append(split_text[i][1:-1])
        elif begin in split_text[i] and end in split_text[i + 1]:
            words.append(split_text[i][1::])
            words.append(split_text[i + 1][:-1])


    answer = ' '.join(words)


    return answer




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')