"""

Create a password verification function with the following verification conditions:
- Longer than 6 characters.
- Should contain at least one digit.

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

"""


def is_acceptable_password(password):
    digits = '1234567890'
    answer = False

    for letter in password:
        if letter in digits:
            answer = True
        if len(password) < 6:
            answer = False

    print(answer)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")