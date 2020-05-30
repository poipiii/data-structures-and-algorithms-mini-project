from supermarket_model import SuperMarket
from binarysearch import binarySearch
from bubblesort import bubbleSort
from insersionsort import insertionSort
#initalise a empty dictonary to store supermarket objects 
supermarket_obj_dict = {}

#creates a new supermarket object basewd on infom,ation prvided from user input and stor ot in the dictonary 
def create_new_product(item_desc, item_sell_price, item_stock_lvl, item_catergory, item_supplier):
    new_product = SuperMarket(
        item_desc, item_sell_price, item_stock_lvl, item_catergory, item_supplier)
    supermarket_obj_dict[item_desc] = new_product
    print("product has been created has been created ")

#takes in item desc and delete item from dictonary
def delete_product(item_desc):
    if item_desc in supermarket_obj_dict.keys():
        supermarket_obj_dict.pop(item_desc)
        print('{} has been deleted'.format(item_desc))
    else:
        return False

#take in item desc,option number and new infomation tonbe edited and sets the new infomation to object 
def edit_products(item_desc, edit, new_info):
    if item_desc in supermarket_obj_dict.keys():
        if edit == 1:
            product = supermarket_obj_dict.get(item_desc)
            product.set_item_desc(new_info)
            supermarket_obj_dict[item_desc] = product
        elif edit == 2:
            product = supermarket_obj_dict.get(item_desc)
            product.set_item_sell_price(new_info)
            supermarket_obj_dict[item_desc] = product
        elif edit == 3:
            product = supermarket_obj_dict.get(item_desc)
            product.set_item_stock_lvl(new_info)
            supermarket_obj_dict[item_desc] = product
        elif edit == 4:
            product = supermarket_obj_dict.get(item_desc)
            product.set_item_catergory(new_info)
            supermarket_obj_dict[item_desc] = product
        else:
            product = supermarket_obj_dict.get(item_desc)
            product.set_item_supplier(new_info)
            supermarket_obj_dict[item_desc] = product

        print("success")

    else:
        return False

#displays all products stored in he dictonary 
def display_all_products():
    print("product database")
    print("===========================================================================")
    print("descrption------sell_price------stock------catergory------supplier")
    for products in supermarket_obj_dict.values():
        print(products.get_item_desc(), " | ",
              products.get_item_sell_price(), " | ", products.get_item_stock_lvl(), " | ", products.get_item_catergory(), " | ", products.get_item_supplier(), " | ")

#takes in a list of objects and display all infomation in the list 
def display_products(results):
    print("product database")
    print("===========================================================================")
    print("descrption------sell_price------stock------catergory------supplier")
    for products in results:
        print(products.get_item_desc(), " | ",
              products.get_item_sell_price(), " | ", products.get_item_stock_lvl(), " | ", products.get_item_catergory(), " | ", products.get_item_supplier(), " | ")

def getattributename(option):
    option = option.lower()
    if option == "price":
        return "item_sell_price"
    elif option == "stock":
        return "item_stock_lvl"
    elif option == "catergory":
        return "item_catergory"
    elif option == "desc":
        return "item_desc"
    else:
        return "item_supplier"

#menu for adding new object to dictonary
def add_newitem_menu():
    while True:
        try:
            item_desc = input("input item description")
            if item_desc in supermarket_obj_dict.keys():
                print("item already in database please enter another item ")
                continue
            item_sell_price = int(input("input item price"))
            item_stk_lvl = int(input("input item stock"))
            item_catergory = input("input item catergory")
            item_supplier = input("input item supplier")


        except ValueError:
            print("please enter a valid value")
            continue
        else:
            create_new_product(item_desc, item_sell_price, item_stk_lvl, item_catergory, item_supplier)
            break

#menu to delete object from dictonary
def delete_item_menu():
    while True:
       
        item_desc = input("please input the name of the product you want to delete :")
        if item_desc in supermarket_obj_dict.keys():
            del_coniformation = input("are you sure you want to delete {} y/n :".format(item_desc))
            if del_coniformation.lower() == "y":
                delete_product(item_desc)
                
                break
            else:
                break
            
        else:
            print("item is not in database")
            continue

#takes in the entire supermarket object dictonary and compute the total stock level 
def compute_total(supermarket_list):
    stock_lvl_list = map(lambda product: product.get_item_stock_lvl(), supermarket_list)
    print(sum(stock_lvl_list))

#takes in the entire supermarket object dictonary and compute the average  stock level 
def compute_average(supermarket_list):
    stock_lvl_list = map(lambda product: product.get_item_stock_lvl(), supermarket_list)
    print(sum(stock_lvl_list) / len(supermarket_list))

#takes in a the list of supermarket objects and a key and pass to binarysearch function 
def searchBinary(key):
    result = binarySearch(list(supermarket_obj_dict.values()), key)
    #return a list of all objects that match key 
    return result

#takes in a the list of supermarket objects , a key and order of sort accending or decending and pass to bubbleSort function   
def sort_priceBubble(order,key):
    result = bubbleSort(list(supermarket_obj_dict.values()), order, key)
    #return a sorted list of objects 
    return result

#takes in a the list of supermarket objects , a key and order of sort accending or decending and pass to insertionSort function   
def sort_priceInsersion(order,key):
    result = insertionSort(list(supermarket_obj_dict.values()), order, key)
    #return a sorted list of objects 
    return result

create_new_product("apple", 2, 100, "fruit", "dole")
create_new_product("orange", 6, 100, "stuff", "dole")
create_new_product("pear", 4, 100, "fruit", "dole")
create_new_product("bannana", 3, 100, "stuff", "dole")

#menu for editing infomation of supermarketr objects 
def edit_item_menu():
    while True:

        item_desc = input()
        if item_desc in supermarket_obj_dict.keys():
            print("""what would you like to edit
            1.item description
            2.item sell price
            3. item stock 
            4. item catergory
            5.item supplier
            0. quit edit menu""")
            edit_choice = int(input("input your choice"))
            if edit_choice == 1:
                new_data = input("input new product description")
                edit_products(item_desc,edit_choice,new_data)
            elif edit_choice == 2:
                try:
                    new_data = int(input("input new product sell price"))
                except ValueError:
                    print("invalid data format please enter again")
                    continue
                else:
                    edit_products(item_desc, edit_choice, new_data)
            elif edit_choice == 3:
                try:
                    new_data = int(input("input new product stock"))
                except ValueError:
                    print("invalid data format please enter again")
                    continue
                else:
                    edit_products(item_desc, edit_choice, new_data)
            elif edit_choice == 4:
                new_data = input("input new product catergory")
                edit_products(item_desc, edit_choice, new_data)
            elif edit_choice == 5:
                new_data = input("input new product supplier")
                edit_products(item_desc, edit_choice, new_data)
            else:
                break
        else:
            print("item is not in database")
            break



#menu for displaying infomation on products
def display():
    while True:
            print("""what would you like to display
                1.display all products
                2.search product by price
                3.sort product using bubble sort
                4.sort product using insersion sort
                5.display total stock 
                6.display average stock
                0. quit display menu""")
            try:
                display_choice = int(input("please input a choice"))
            except ValueError:
                print("not a valid option")
                continue
            if display_choice == 1:
                display_all_products()
                continue
            elif display_choice == 2:
                key = int(input("input the price of item you want to search"))
                display_products(searchBinary(key))
                continue
            elif display_choice == 3:
                print("""sort options
                desc
                price
                stock 
                catergory
                supplier
                """ )
                key = input("input the sort option",)
                order = input("input A for (accending) or D for (decending)")
                display_products(sort_priceBubble(order, getattributename(key)))
            elif display_choice == 4:
                print("""sort options
                desc
                price
                stock 
                catergory
                supplier
                """ )
                key = input("input the sort option",)
                order = input("input A for (accending) or D for (decending)")
                display_products(sort_priceInsersion(order,getattributename(key)))
            elif display_choice == 5:
                compute_total(supermarket_obj_dict.values())
                continue
            elif display_choice == 6:
                compute_average(supermarket_obj_dict.values())
                continue

            else:
                break 
        




#the main menu 
while True:
    print('========================== Welcome to supermaket inventory manager ==========================')
    print(""" please choose an option
    1 Display inventory
    2 Add new item to inventory
    3 Edit item in inventory
    4 Delete item in inventory
    0 Quit application""" )
    try:
        main_option = int(input("please enter an option :"))
    except ValueError:
        print("invalid option please enter a valid option")
        continue
    if main_option == 1:
        display()
        continue
    elif main_option == 2:
        add_newitem_menu()
        continue
    elif main_option == 3:
        edit_item_menu()
        continue
    elif main_option == 4:
        delete_item_menu()
        continue
    elif main_option == 0:
        print("thank you for using goodbye")
        break
    else:
       continue


    
  
