"""

Given a list of booleans, check if the majority of elements are true.
- An empty list should return false
- If trues and falses have an equal amount, return false

Input: A list of booleans
Output: A Boolean


>>> is_majority([True, True, False, True, False])
True

>>> is_majority([True, True, False])
True

>>> is_majority([True, True, False, False])
False

>>> is_majority([])
False

"""


def is_majority(items):
    true_count = 0
    false_count = 0
    
    for item in items:
        if item == True:
            true_count += 1
        elif item == False:
            false_count += 1
    
    if true_count > false_count:
        print(True)
    else:
        print(False)
        
        

if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")