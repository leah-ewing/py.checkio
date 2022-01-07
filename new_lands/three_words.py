"""

Given a string with words and numbers separated by whitespaces (one space). 
The words contain only letters. Check if the string contains three words in succession. 
For example, the string "start 5 one two three 7 end" contains three words in succession.

Input: A string
Output: A boolean

Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined). 
0 < len(words) < 100

>>> checkio("Hello World hello")
True

>>> checkio("He is 123 man")
False

>>> checkio("1 2 3 4")
False

>>> checkio("bla bla bla bla")
True

>>> checkio("Hi")
False

>>> checkio("one two 3 four five six 7 eight 9 ten eleven 12")
True

>>> checkio("one two 3 four 5 six 7 eight 9 ten eleven 12")
False

>>> checkio("0 qwerty iddqd asdfg")
True

"""

def checkio(words):
    
    digits = '1234567890'
    words_list = words.split(' ')
    succession_list = []
    answer = False

    if len(words_list) > 3:
        while len(words_list) > 0:
            if len(succession_list) == 0:
                while len(succession_list) < 3:
                    succession_list.append(words_list.pop(0))
            else:
                succession_list.pop(0)
                succession_list.append(words_list.pop(0))
            
            digits_in_list = []

            for word in succession_list:
                for letter in word:
                    if letter in digits:
                        digits_in_list.append(letter)
            
            if len(digits_in_list) == 0:
                answer = True
                break

    else:
        if len(words_list) == 3:
            digits_in_list = []

            for word in words_list:
                for letter in word:
                    if letter in digits:
                        digits_in_list.append(letter)
            
            if len(digits_in_list) == 0:
                answer = True


    print(answer)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')