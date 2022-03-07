"""

You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.
For example: The number given is 123405. The result will be 1*2*3*4*5=120.

Input: A positive integer.
Output: The product of the digits as an integer.


>>> digits_multiplication(123405)
120

>>> digits_multiplication(999)
729

>>> digits_multiplication(1000)
1

>>> digits_multiplication(1111)
1


"""


def digits_multiplication(number):

    minus_zeros = []
    number = str(number)

    for num in number:
        if num != '0':
            minus_zeros.append(int(num))
    number = minus_zeros

    product = number.pop(0)

    while len(number) > 0:
        product = product * number.pop(0)

    print(product)




if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")
