"""

Convert the name of a function (a string) from CamelCase ("MyFunctionName") 
into the Python format ("my_function_name") where all chars are in lowercase and 
all words are concatenated with an intervening underscore symbol "_".

Input: A function name as a CamelCase string.
Output: The same string, but in under_score.


>>> from_camel_case("MyFunctionName")
'my_function_name'

>>> from_camel_case("IPhone")
'i_phone'

>>> from_camel_case("ThisFunctionIsEmpty")
'this_function_is_empty'

>>> from_camel_case("Name")
'name'

"""


def from_camel_case(name):

    name_list = []
    indexes = []
    new_list = []
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    for letter in name:
        name_list.append(letter)
        
    name = name_list

    new_list.append(name[0])

    i = 1
    while i < len(name):
        if name[i] in uppercase:
            new_list.append('_')
        new_list.append(name[i])
        i += 1

    new_list = "".join(new_list).lower()

    return new_list
    
    


if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")