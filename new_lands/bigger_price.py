"""

Find the TOP most expensive item(s). 
The amount of top most expensive items to find is given as the first argument and the item's data is the second argument.

Input: an int and list of dicts - each dict has two keys: "name" and "price"
Output: a dict

>>> bigger_price(2, [{"name": "bread", "price": 100}, {'name': 'wine', 'price': 138}, {'name': 'meat', 'price': 15}, {'name': 'water', 'price': 1}])
[{'name': 'wine', 'price': 138}, {'name': 'bread', 'price': 100}]

>>> bigger_price(1, [{'name': 'pen', 'price': 5}, {'name': 'whiteboard', 'price': 170}])
[{'name': 'whiteboard', 'price': 170}]


"""


def bigger_price(limit, data):

    prices = []
    highest = []

    for i in range(len(data)):
        prices.append(data[i]["price"])

    prices = sorted(prices)[::-1][:limit]
    
    for price in prices:
        for i in range(len(data)):
            if data[i]["price"] == price:
                highest.append(data[i])
    


    print(highest)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print('\n🥳 ALL TESTS PASSED! YAY!\n')