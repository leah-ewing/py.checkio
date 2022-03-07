"""

Convert a string from the Python format (for example "my_function_name") into CamelCase ("MyFunctionName"), 
where the first char of every word is in uppercase and all words are concatenated without any intervening characters.

Input: A string.
Output: The same string, but in CamelCase.


>>> to_camel_case("my_function_name")
MyFunctionName

>>> to_camel_case("i_phone")
IPhone

>>> to_camel_case("this_function_is_empty")
ThisFunctionIsEmpty

>>> to_camel_case("name")
Name

"""


def to_camel_case(name):

    name_list = []
 
    for word in name:
        for letter in word:
            name_list.append(letter)

    name_list[0] = name_list[0].upper()

    i = 1
    while i < len(name_list):
        if name_list[i] == '_':
            name_list[i + 1] = name_list[i + 1].upper()
        i += 1
      
    name_list = "".join(name_list)
    name = "".join(name_list.split('_'))

    print(name)



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n🥳 ALL TESTS PASSED! YAY!\n")