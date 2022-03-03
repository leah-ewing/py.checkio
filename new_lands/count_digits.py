"""

Count the number of digits in a given string.

Input: A string
Output: An integer


>>> count_digits('hi')
0

>>> count_digits('who is 1st here')
1

>>> count_digits('my number is 2')
1
>>> count_digits('This picture is an oil on canvas painting by Danish artist Anna Petersen between years 1845 and 1910')
8

>>> count_digits('5 plus 6 is')
2

>>> count_digits('')
0

"""

def count_digits(text):
    numbers_in_text = []
    digits = '1234567890'

    for letter in text:
        if letter in digits:
            numbers_in_text.append(letter)
    
    answer = len(numbers_in_text)

    print(answer)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')
