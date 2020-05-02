from supermarket_model import SuperMarket

# Sorts a sequence in ascending order using
# the bubble sort algorithm


def bubbleSort(supermarket_list):
    arr = len(supermarket_list)
    print(range(supermarket_list - 1, 0, -1))
    # Perform n-1 bubble operations on the sequence
    for i in range(arr - 1, 0, -1):
        # Bubble the largest item to the end
        for j in range(i):
            if supermarket_list[j].get_item_sell_price() > supermarket_list[j + 1].get_item_sell_price():
                # Swap the j and j+1 items
                temp = supermarket_list[j]
                supermarket_list[j] = supermarket_list[j + 1]
                supermarket_list[j + 1] = temp
    return(supermarket_list)


# Test codes
# list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
# print("Bubble Sort")
# print(list_of_numbers)
# bubbleSort(list_of_numbers)
# print(list_of_numbers)
