"""

In a given text you need to sum the numbers while excluding any digits that form part of a word.

The text consists of numbers, spaces and letters from the English alphabet.

Input: A string
Output: An int

>>> sum_numbers('hi')
0

>>> sum_numbers('who is 1st here')
0

>>> sum_numbers('my number is 2')
2

>>> sum_numbers('This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year')
3755

>>> sum_numbers('5 plus 6 is')
11

>>> sum_numbers('')
0

>>> sum_numbers('I have 1 2 many cheese gr8ers')
3

>>> sum_numbers("i don't like the number 121")
121

"""


def sum_numbers(text):
    numbers = []
    current_number = []
    letters = 'abcdefghijklmnopqrstuvwxyz'
    digits = '1234567890'
    space = ' '
    i = 0
    j = -1

    if len(text) == 0:
        answer = 0

    else:
        if text[-1] in digits:
            while j > -(len(text)):
                if text[j] in digits:
                    current_number.append(text[j])
                    if text[j - 1] == space:
                        new_number = int("".join(current_number))
                        numbers.append(new_number)
                        current_number = []
                        break
                    if text[j - 1] in letters:
                        current_number = []
                        break
                    j -= 1
            text = text[:j]

        while i < len(text):
            if text[i] in digits:
                if text[i + 1] == space:
                    current_number.append(text[i])
                    new_number = int("".join(current_number))
                    numbers.append(new_number)
                    current_number = []
                    i += 1
                elif text[i + 1] in digits:
                    current_number.append(text[i])
                    i += 1
                else:
                    break
            else:
                i += 1

        answer = sum(numbers)
    
    print(answer)





if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')


