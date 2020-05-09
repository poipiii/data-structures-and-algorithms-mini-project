#Sorts a sequence in ascending order using
# the insertion sort algorithm


def insertionSort(supermarket_list,order,key):
    n = len(supermarket_list)
    # Starts with the first item as the only sorted entry.
    if order.lower() == "d":
        for i in range(1, n):
            # Save the value to be positioned
            value = supermarket_list[i]

            # Find the position where value fits in the
            # ordered part of the list.
            pos = i
            if key == "price":
                while pos > 0 and value.get_item_sell_price() > supermarket_list[pos - 1].get_item_sell_price():
                    # Shift the items to the right during the search
                    supermarket_list[pos] = supermarket_list[pos-1]
                    pos -= 1

                    # Put the saved value into the open slot.
                    supermarket_list[pos] = value
            elif key == "stock":
                while pos > 0 and value.get_item_stock_lvl() > supermarket_list[pos - 1].get_item_stock_lvl():
                    # Shift the items to the right during the search
                    supermarket_list[pos] = supermarket_list[pos-1]
                    pos -= 1
                    # Put the saved value into the open slot.
                    supermarket_list[pos] = value
            elif key == "catergory":
                while pos > 0 and value.get_item_catergory() > supermarket_list[pos - 1].get_item_catergory():
                    # Shift the items to the right during the search
                    supermarket_list[pos] = supermarket_list[pos-1]
                    pos -= 1
                    # Put the saved value into the open slot.
                    supermarket_list[pos] = value
            elif key == "desc":
                while pos > 0 and value.get_item_desc() > supermarket_list[pos - 1].get_item_desc():
                    # Shift the items to the right during the search
                    supermarket_list[pos] = supermarket_list[pos-1]
                    pos -= 1
                    # Put the saved value into the open slot.
                    supermarket_list[pos] = value
            else:
                while pos > 0 and value.get_item_supplier() > supermarket_list[pos - 1].get_item_supplier():
                    # Shift the items to the right during the search
                    supermarket_list[pos] = supermarket_list[pos-1]
                    pos -= 1
                    # Put the saved value into the open slot.
                    supermarket_list[pos] = value
        return supermarket_list
    else:

        for i in range(1, n):
            # Save the value to be positioned
            value = supermarket_list[i]

            # Find the position where value fits in the
            # ordered part of the list.
            pos = i
            if key == "price":
                while pos > 0 and value.get_item_sell_price() < supermarket_list[pos - 1].get_item_sell_price():
                    # Shift the items to the right during the search
                    supermarket_list[pos] = supermarket_list[pos-1]
                    pos -= 1

                    # Put the saved value into the open slot.
                    supermarket_list[pos] = value
            elif key == "stock":
                while pos > 0 and value.get_item_stock_lvl() < supermarket_list[pos - 1].get_item_stock_lvl():
                    # Shift the items to the right during the search
                    supermarket_list[pos] = supermarket_list[pos-1]
                    pos -= 1    
                    # Put the saved value into the open slot.
                    supermarket_list[pos] = value
            elif key == "catergory":
                while pos > 0 and value.get_item_catergory() < supermarket_list[pos - 1].get_item_catergory():
                    # Shift the items to the right during the search
                    supermarket_list[pos] = supermarket_list[pos-1]
                    pos -= 1
                    # Put the saved value into the open slot.
                    supermarket_list[pos] = value
            elif key == "desc":
                while pos > 0 and value.get_item_desc() < supermarket_list[pos - 1].get_item_desc():
                    # Shift the items to the right during the search
                    supermarket_list[pos] = supermarket_list[pos-1]
                    pos -= 1
                    # Put the saved value into the open slot.
                    supermarket_list[pos] = value
            else:
                while pos > 0 and value.get_item_supplier() < supermarket_list[pos - 1].get_item_supplier():
                    # Shift the items to the right during the search
                    supermarket_list[pos] = supermarket_list[pos-1]
                    pos -= 1
                    # Put the saved value into the open slot.
                    supermarket_list[pos] = value
        return supermarket_list 


