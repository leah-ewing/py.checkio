"""

Create a password verification function using these verification conditions:
- The length should be bigger than 6.
- Should contain at least one digit, but cannot consist of just digits.

Input: A string.
Output: A bool.

>>> is_acceptable_password('short')
False

>>> is_acceptable_password('muchlonger')
False

>>> is_acceptable_password('ashort')
False

>>> is_acceptable_password('muchlonger5')
True

>>> is_acceptable_password('sh5')
False

>>> is_acceptable_password('1234567')
False

"""

def is_acceptable_password(password):


    digits = '0123456789'

    if len(password) > 6:
        for letter in password:
            if letter in digits:
                digits = []
                for letter in digits:
                    digits.append(letter)
                if len(digits) == len(password):
                    acceptable = False
                else:
                    acceptable = True
            else:
                acceptable = False
    else:
        acceptable = False

    print(acceptable)
        


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")