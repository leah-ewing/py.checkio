"""

Given a string, find its first word.

Pay attention to the following points:
- There can be dots and commas in a string.
- A string can start with a letter or, for example, one/multiple dot(s) or space(s).
- A word can contain an apostrophe.
- The whole text can be represented with one word.

Input: A string
Output: A string

Precondition: the text can contain a-z A-Z, ',' and '.'


>>> first_word("Hello world")
Hello

>>> first_word("greetings, friends")
greetings

>>> first_word(" a word ")
a

>>> first_word("don't touch it")
don't

>>> first_word("... and so on ...")
and

>>> first_word("hi")
hi

>>> first_word("Hello.World")
Hello

"""

def first_word(text):

    text_list = text.rstrip('., ').strip(',. ').split(' ')

    if '.' in text_list[0] or ',' in text_list[0]:
        if '.' in text_list[0]:
            text_list = "".join(text_list)
            text_list = text_list.split('.')
        if ',' in text_list[0]:
            text_list = "".join(text_list)
            text_list = text_list.split(',')


    answer = str(text_list[0])


    print(answer)
  


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')
