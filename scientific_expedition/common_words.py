"""

Given two strings with non-repeating words separated by commas, find all of the words that appear in both strings. 
The result must be represented as a string of words separated by commas in alphabetic order.

Input: Two arguments as strings.
Output: The common words as a string.


>>> common_words('hello,world', 'hello,earth')
'hello'

>>> common_words('one,two,three', 'four,five,six')
''

>>> common_words('one,two,three', 'four,five,one,two,six,three')
'one,three,two'


"""

def common_words(line1, line2):

    common = []
    
    line1 = line1.split(',')
    line2 = line2.split(',')
    
    for word in line1:
        if word in line2:
            common.append(word)
            
    common = ",".join(sorted(common))
    
    return common
            
    
    
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")