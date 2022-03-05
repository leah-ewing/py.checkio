"""

In a given list the last element should become the first one. 
An empty list or list with only one element should stay the same.

>>> replace_last([2, 3, 4, 1])
[1, 2, 3, 4]

>>> replace_last([1, 2, 3, 4])
[4, 1, 2, 3]

>>> replace_last([1])
[1]

>>> replace_last([])
[]

"""

def replace_last(line):
    
    if len(line) > 1:
        last_element = line.pop()
        line.insert(0, last_element)
    print(line)
    

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")