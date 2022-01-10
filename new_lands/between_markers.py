"""

Given a string and two markers (the initial and final), find a substring enclosed between these two markers. 

Important conditions:
- The initial and final markers are always different.
- If there is no initial marker, then the first character should be considered the beginning of a string.
- If there is no final marker, then the last character should be considered the ending of a string.
- If the initial and final markers are missing then simply return the whole string.
- If the final marker comes before the initial marker, then return an empty string.

Input: Three arguments. All strings. The second and third arguments are the initial and final markers.
Output: A string.

Precondition: can't be more than one final marker and can't be more than one initial. Marker can't be an empty string


>>> between_markers('What is >apple<', '>', '<')
apple

>>> between_markers('No[/b] hi', '[b]', '[/b]')
No

>>> between_markers("<head><title>My new site</title></head>", "<title>", "</title>")
My new site

>>> between_markers('No [b]hi', '[b]', '[/b]')
hi

>>> between_markers('No hi', '[b]', '[/b]')
No hi

>>> between_markers('No <hi>', '>', '<')
''

"""


def between_markers(text, begin, end):

    new_begin = "["
    new_end = "]"
    original_text = text

    text = text.replace(begin, new_begin)
    text = text.replace(end, new_end)

    if new_begin in text and new_end in text:
        if text.index(new_begin) > text.index(new_end):
            answer = "''"
        else:
            answer = text[text.index(new_begin)+1:text.index(new_end)]
    else:
        if new_begin in text: 
            answer = text[text.index(new_begin)+1:]
        elif new_end in text:
            answer = text[:text.index(new_end)]
        else:
            answer = original_text


    print(answer)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')
