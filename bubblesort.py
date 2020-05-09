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
                if key == "price":
                    if supermarket_list[j].get_item_sell_price() <= supermarket_list[j + 1].get_item_sell_price():
                        # Swap the j and j+1 items
                        temp = supermarket_list[j]
                        supermarket_list[j] = supermarket_list[j + 1]
                        supermarket_list[j + 1] = temp
                elif key == "stock":
                    if supermarket_list[j].get_item_stock_lvl() <= supermarket_list[j + 1].get_item_stock_lvl():
                        # Swap the j and j+1 items
                        temp = supermarket_list[j]
                        supermarket_list[j] = supermarket_list[j + 1]
                        supermarket_list[j + 1] = temp
                elif key == "catergory":
                    if supermarket_list[j].get_item_catergory() <= supermarket_list[j + 1].get_item_catergory():
                        # Swap the j and j+1 items
                        temp = supermarket_list[j]
                        supermarket_list[j] = supermarket_list[j + 1]
                        supermarket_list[j + 1] = temp
                elif key == "desc":
                    if supermarket_list[j].get_item_desc() <= supermarket_list[j + 1].get_item_desc():
                        # Swap the j and j+1 items
                        temp = supermarket_list[j]
                        supermarket_list[j] = supermarket_list[j + 1]
                        supermarket_list[j + 1] = temp
                else:
                    if supermarket_list[j].get_item_supplier() <= supermarket_list[j + 1].get_item_supplier():
                        # Swap the j and j+1 items
                        temp = supermarket_list[j]
                        supermarket_list[j] = supermarket_list[j + 1]
                        supermarket_list[j + 1] = temp
        return (supermarket_list)
    else:
        for i in range(arr - 1, 0, -1):
            # Bubble the largest item to the end
            for j in range(i):
                 if key == "price":
                    if supermarket_list[j].get_item_sell_price() > supermarket_list[j + 1].get_item_sell_price():
                        # Swap the j and j+1 items
                        temp = supermarket_list[j]
                        supermarket_list[j] = supermarket_list[j + 1]
                        supermarket_list[j + 1] = temp
                 elif key == "stock":
                     if supermarket_list[j].get_item_stock_lvl() > supermarket_list[j + 1].get_item_stock_lvl():
                         # Swap the j and j+1 items
                         temp = supermarket_list[j]
                         supermarket_list[j] = supermarket_list[j + 1]
                         supermarket_list[j + 1] = temp
                 elif key == "catergory":
                     if supermarket_list[j].get_item_catergory() > supermarket_list[j + 1].get_item_catergory():
                         # Swap the j and j+1 items
                         temp = supermarket_list[j]
                         supermarket_list[j] = supermarket_list[j + 1]
                         supermarket_list[j + 1] = temp
                 elif key == "desc":
                     if supermarket_list[j].get_item_desc() > supermarket_list[j + 1].get_item_desc():
                         # Swap the j and j+1 items
                         temp = supermarket_list[j]
                         supermarket_list[j] = supermarket_list[j + 1]
                         supermarket_list[j + 1] = temp
                 else:
                     if supermarket_list[j].get_item_supplier() > supermarket_list[j + 1].get_item_supplier():
                         # Swap the j and j+1 items
                         temp = supermarket_list[j]
                         supermarket_list[j] = supermarket_list[j + 1]
                         supermarket_list[j + 1] = temp
        return (supermarket_list)
    


# Test codes
# list_of_numbers = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
# print("Bubble Sort")
# print(list_of_numbers)
# bubbleSort(list_of_numbers)
# print(list_of_numbers)
