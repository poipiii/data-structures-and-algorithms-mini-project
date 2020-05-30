from supermarket_model import SuperMarket

# Sorts a sequence in ascending order using
# the bubble sort algorithm
def bubbleSort(supermarket_list,order,key):
    arr = len(supermarket_list)
    if order.lower() == "d":
        # Perform n-1 bubble operations on the sequence
        for i in range(arr - 1, 0, -1):
            # Bubble the largest item to the end
            for j in range(i):
                if getattr(supermarket_list[j],key) <= getattr(supermarket_list[j + 1],key):
                    # Swap the j and j+1 items
                    temp = supermarket_list[j]
                    supermarket_list[j] = supermarket_list[j + 1]
                    supermarket_list[j + 1] = temp
        return supermarket_list
    else:
        for i in range(arr - 1, 0, -1):
            # Bubble the largest item to the end
            for j in range(i):
                if getattr(supermarket_list[j],key) > getattr(supermarket_list[j + 1],key):
                    # Swap the j and j+1 items
                    temp = supermarket_list[j]
                    supermarket_list[j] = supermarket_list[j + 1]
                    supermarket_list[j + 1] = temp
        return supermarket_list

# Test codes
# list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
# print("Bubble Sort")
# print(list_of_numbers)
# bubbleSort(list_of_numbers)
# print(list_of_numbers)
