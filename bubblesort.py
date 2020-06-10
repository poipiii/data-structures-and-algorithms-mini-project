from supermarket_model import SuperMarket

# Sorts a sequence in ascending order using
# the bubble sort algorithm
def bubbleSort(supermarket_list,order,key):
    arr = len(supermarket_list)
    #check if order id d if yes sort list in decending order 
    if order.lower() == "d":
        #start the sort from the end of the list 
        for i in range(arr - 1, 0, -1):
            for j in range(i):
                if getattr(supermarket_list[j],key) <= getattr(supermarket_list[j + 1],key):
                    # if number at index if lesser than number at index + 1 Swap the numbers
                    temp = supermarket_list[j]
                    supermarket_list[j] = supermarket_list[j + 1]
                    supermarket_list[j + 1] = temp
        #return the sortes list 
        return supermarket_list
    else:
        for i in range(arr - 1, 0, -1):
            # Bubble the largest item to the end
            for j in range(i):
                if getattr(supermarket_list[j], key) > getattr(supermarket_list[j + 1], key):
                    # if number at index if lesser than number at index + 1 Swap the numbers
                    temp = supermarket_list[j]
                    supermarket_list[j] = supermarket_list[j + 1]
                    supermarket_list[j + 1] = temp
        #return the sortes list 
        return supermarket_list


