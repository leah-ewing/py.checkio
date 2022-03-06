"""

In a given word, check if one symbol goes right after another.
- If a symbol shows up more than once, count the first one
- If a symbol is not in the list, return False
- If the two symbols are the same, return False;
- The condition is case sensitive - 'a' and 'A' are different symbols.

Input: Three arguments. String, first symbol, second symbol.
Output: A bool.

>>> goes_after('world', 'w', 'o')
True

>>> goes_after('world', 'w', 'r')
False

>>> goes_after('world', 'l', 'o')
False

>>> goes_after('panorama', 'a', 'n')
True

>>> goes_after('list', 'l', 'o')
False

>>> goes_after('', 'l', 'o')
False

>>> goes_after('list', 'l', 'l')
False

>>> goes_after('world', 'd', 'w')
False

"""


def goes_after(word, first, second):
    
    if first in word and second in word:
        
        if first == second:
            print(False)
            
        else:
            for i in range(len(word)):
                if word[i] == first:
                    first_index = i
                    break
            for i in range(len(word)):
                if word[i] == second:
                    second_index = i
                    break
            
            if second_index - first_index == 1:
                print(True)
            else:
                print(False)
                
    else:
        print(False)
    
    
    
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")