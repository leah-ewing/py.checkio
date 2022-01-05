"""

Split the string into pairs of two characters. 

If the string contains an odd number of characters, then the missing second character of 
the final pair should be replaced with an underscore ('_').

Input: A string
Output: An iterable of strings

>>> split_pairs('abcd')
['ab', 'cd']

>>> split_pairs('abc')
['ab', 'c_']


"""

def split_pairs(a):
    
    pairs = []

    while len(a) > 1:
        pairs.append(a[0:2])
        a = a[2::]

    if len(a) > 0:
        pairs.append(f'{a[0]}_')

    print(pairs)



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')