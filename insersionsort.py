#Sorts a sequence in ascending order using
# the insertion sort algorithm
from supermarket_model import SuperMarket
def insertionSort(supermarket_list,order,key):
    n = len(supermarket_list)
    # Starts with the sort by asuming the first item is already sorted 
    if order.lower() == "d":
        #checks if order is d if it is sort list in decending order 
        for i in range(1, n):
            # Save the value to be swaped and compared 
            value = supermarket_list[i]

            # Find the position where value fits in the
            # ordered part of the list.
            pos = i
            while pos > 0 and getattr(value,key) > getattr(supermarket_list[pos - 1],key):
                # if pos id > 0 and Shift the items to the right during the search
                supermarket_list[pos] = supermarket_list[pos-1]
                pos -= 1
                # Put the saved value into the open slot in list .
                supermarket_list[pos] = value
        return supermarket_list
    else:
        for i in range(1, n):
            # Save the value to be positioned
            value = supermarket_list[i]

            # Find the position where value fits in the
            # ordered part of the list.
            pos = i
            while pos > 0 and getattr(value,key) < getattr(supermarket_list[pos - 1],key):
                # Shift the items to the right during the search
                supermarket_list[pos] = supermarket_list[pos-1]
                pos -= 1
                # Put the saved value into the open slot.
                supermarket_list[pos] = value
        return supermarket_list
        
