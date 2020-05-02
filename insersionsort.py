#Sorts a sequence in ascending order using
# the insertion sort algorithm


def insertionSort(supermarket_list):
    n = len(supermarket_list)
    # Starts with the first item as the only sorted entry.
    for i in range(1, n):
        # Save the value to be positioned
        value = supermarket_list[i]

        # Find the position where value fits in the
        # ordered part of the list.
        pos = i
        while pos > 0 and value.get_item_sell_price() < supermarket_list[pos - 1].get_item_sell_price():
            # Shift the items to the right during the search
            supermarket_list[pos] = supermarket_list[pos-1]
            pos -= 1

            # Put the saved value into the open slot.
            supermarket_list[pos] = value
    return supermarket_list 

# list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]

# print("InsertionSort")
# print(list_of_numbers)
# insertionSort(list_of_numbers)
# print(list_of_numbers)
