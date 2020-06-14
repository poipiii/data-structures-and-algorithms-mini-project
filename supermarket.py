#for details of asasingment please see README.md

from supermarket_model import SuperMarket
from binarysearch import binarySearch
from bubblesort import bubbleSort
from insersionsort import insertionSort
from shell_sort import shellsort
#initalise a empty dictonary to store supermarket objects 
supermarket_obj_list = []

#creates a new supermarket object basewd on infom,ation prvided from user input and stor ot in the dictonary 
def create_new_product(item_desc, item_sell_price, item_stock_lvl, item_catergory, item_supplier):
    new_product = SuperMarket(
        item_desc, item_sell_price, item_stock_lvl, item_catergory, item_supplier)
    supermarket_obj_list.append(new_product)
    print("product has been created has been created ")

#takes in item desc and delete item from dictonary
def delete_product(obj):
        supermarket_obj_list.remove(obj)
        print('{} has been deleted'.format(obj.get_item_desc()))
    

#take in item desc,option number and new infomation tonbe edited and sets the new infomation to object 
def edit_products(result,edit, new_info):
        old_product = supermarket_obj_list.index(result)
        if edit == 1:
            result.set_item_sell_price(float(new_info))
            supermarket_obj_list[old_product] = result
        elif edit == 2:
            result.set_item_stock_lvl(int(new_info))
            supermarket_obj_list[old_product] = result
        elif edit == 3:
            result.set_item_catergory(new_info)
            supermarket_obj_list[old_product] = result
        elif edit == 4:
            result.set_item_desc(new_info)
            supermarket_obj_list[old_product] = result
        else:
            result.set_item_supplier(new_info)
            supermarket_obj_list[old_product] = result

        print("success")

    
#displays all products stored in he dictonary 

def display_all_products(supermarket_obj_list):
    print("product database")
    print("===========================================================================")
    print("descrption------sell_price------stock------catergory------supplier")
    for products in supermarket_obj_list:
        print(products.get_item_desc(), " | ",
              products.get_item_sell_price(), " | ", products.get_item_stock_lvl(), " | ", products.get_item_catergory(), " | ", products.get_item_supplier(), " | ")

#takes in a list of objects and display all infomation in the list 
def display_products(results):
    if len(results) == 0:
        print("no results found")
    else:
        print("product database")
        print("===========================================================================")
        print("descrption------sell_price------stock------catergory------supplier")
        for products in results:
            print(products.get_item_desc(), " | ",
                products.get_item_sell_price(), " | ", products.get_item_stock_lvl(), " | ", products.get_item_catergory(), " | ", products.get_item_supplier(), " | ")
def getattributename(option):
    if option == 1:
        return "item_sell_price"
    elif option == 2 :
        return "item_stock_lvl"
    elif option == 3:
        return "item_catergory"
    elif option == 4:
        return "item_desc"
    else:
        return "item_supplier"

#menu for adding new object to list
def add_newitem_menu(condition):
    if condition == True:
        try:
            item_desc = input("input item description")
            result = searchBinary(item_desc, getattributename(4))
            if len(result) != 0:
                if item_desc == result[0].get_item_desc():
                    print("item already in database please enter another item ")
                    add_newitem_menu(True)
                
            item_sell_price = float(input("input item price"))
            item_stk_lvl = int(input("input item stock"))
            item_catergory = input("input item catergory")
            item_supplier = input("input item supplier")


        except ValueError:
            print("please enter a valid value")
            add_newitem_menu(True)

        else:
            create_new_product(item_desc, item_sell_price, item_stk_lvl, item_catergory, item_supplier)
            main(True)

#menu to delete object from dictonary
def delete_item_menu(condition):
    if condition == True:
       
        item_desc = input("please input the name of the product you want to delete :")
        result = searchBinary(item_desc, getattributename(4))
        if len(result) != 0:
            if result[0].get_item_desc() == item_desc:
                del_coniformation = input("are you sure you want to delete {} y/n :".format(item_desc))
                if del_coniformation.lower() == "y":
                    delete_product(result[0])
                    main(True)

                
                
                else:
                    main(True)
            
            
        else:
            print("item is not in database")
            delete_item_menu(True)

#takes in the entire supermarket object dictonary and compute the total stock level 
def compute_total(supermarket_list):
    stock_lvl_list = map(lambda product: int(product.get_item_stock_lvl()), supermarket_list)
    print("the total stock level is ",sum(stock_lvl_list))

#takes in the entire supermarket object dictonary and compute the average  stock level 
def compute_average(supermarket_list):
    stock_lvl_list = map(lambda product: int(product.get_item_stock_lvl()), supermarket_list)
    print("the average stock level is",sum(stock_lvl_list) / len(supermarket_list))

#takes in a the list of supermarket objects and a key and pass to binarysearch function 
def searchBinary(target,key):
    result = binarySearch(supermarket_obj_list, target, key)
    #return a list of all objects that match key 
    return result

#takes in a the list of supermarket objects , a key and order of sort accending or decending and pass to bubbleSort function   
def sort_Bubble(order,key):
    result = bubbleSort(supermarket_obj_list, order, key)
    #return a sorted list of objects 
    return result

#takes in a the list of supermarket objects , a key and order of sort accending or decending and pass to insertionSort function   
def sort_Insersion(order,key):
    result = insertionSort(supermarket_obj_list, order, key)
    #return a sorted list of objects 
    return result


def sort_shell(order, key):
    result = shellsort(supermarket_obj_list, order, key)
    #return a sorted list of objects
    return result

create_new_product("apple", 2, 100, "fruit", "dole")
create_new_product("orange", 6, 100, "stuff", "dole")
create_new_product("pear", 4, 100, "fruit", "dole")
create_new_product("bannana", 3, 100, "stuff", "test")

#menu for editing infomation of supermarketr objects 
def edit_item_menu(condition):
    if condition ==  True:

        item_desc = input("please enter the desc of the item you want to edit")
        result = searchBinary(item_desc, getattributename(4))
        if len(result) !=0 :
            print("""what would you like to edit
            1.item sell price
            2.item stock 
            3.item catergory
            4.item description
            5.item supplier
            0. quit edit menu""" )
            try:
                edit_choice = int(input("input your choice of data to edit"))
            except ValueError:
                print("please enter a number")
                edit_item_menu(True)
            if edit_choice == 4:
                new_data = input("input new product description")
                edit_products(result[0], edit_choice, new_data)
                main(True)

            elif edit_choice == 1:
                try:
                    new_data = int(input("input new product sell price"))
                except ValueError:
                    print("invalid data format please enter again")
                    edit_item_menu(True)
                else:
                    edit_products(result[0], edit_choice, new_data)
                    main(True)

            elif edit_choice == 2:
                try:
                    new_data = int(input("input new product stock"))
                except ValueError:
                    print("invalid data format please enter again")
                    edit_item_menu(True)

                else:
                    edit_products(result[0], edit_choice, new_data)
                    main(True)

            elif edit_choice == 3:
                new_data = input("input new product catergory")
                edit_products(result[0], edit_choice, new_data)
                main(True)

            elif edit_choice == 5:
                new_data = input("input new product supplier")
                edit_products(result[0], edit_choice, new_data)
                main(True)

            
        else:
            print("item is not in database")
            edit_item_menu(True)




#menu for displaying infomation on products
def display(condition):
    if condition == True:
            print("""what would you like to display
                1.display all products
                2.search product
                3.sort product using bubble sort
                4.sort product using insersion sort
                5.sort product using shell sort
                6.display total stock 
                7.display average stock
                0. quit display menu""")
            try:
                display_choice = int(input("please input a choice"))
            except ValueError:
                print("please enter a number")
                display(True)
                
            if display_choice == 1: 
                display_all_products(supermarket_obj_list)
                display(True)
            elif display_choice == 2:
                print("""serach options
                 1.item sell price
                 2.item stock 
                 3.item catergory
                 4.item description
                 5.item supplier
                """)
                key = int(input("input the search option"))
                target = input("input the data you want to search")
                if key == 1 or key ==  2:
                    target = int(target)
                display_products(searchBinary(target, getattributename(key)))
                display(True)
            elif display_choice == 3:
                print("""serach options
                 1.item sell price
                 2.item stock 
                 3.item catergory
                 4.item description
                 5.item supplier
                """)
                key = int(input("input the sort option"))
                order = input("input A for (accending) or D for (decending)")
                display_products(sort_Bubble(order, getattributename(key)))
                display(True)

            elif display_choice == 4:
                print("""sort options
                 1.item sell price
                 2.item stock 
                 3.item catergory
                 4.item description
                 5.item supplier
                """ )
                key = int(input("input the sort option"))
                order = input("input A for (accending) or D for (decending)")
                display_products(sort_Insersion(order, getattributename(key)))
                display(True)
            elif display_choice == 5:
                print("""sort options
                 1.item sell price
                 2.item stock 
                 3.item catergory
                 4.item description
                 5.item supplier
                """)
                key = int(input("input the sort option"))
                order = input("input A for (accending) or D for (decending)")
                display_products(sort_shell(order, getattributename(key)))
                display(True)

            elif display_choice == 6:
                compute_total(supermarket_obj_list)
                display(True)

            elif display_choice == 7:
                compute_average(supermarket_obj_list)
                display(True)

            elif display_choice == 0:
                main(True)
            else:
                print("please enter a valid number")
                display(True)

        




#the main menu 
def main(condition):
    if condition == True:
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
            print("please enter a number")
            main(True)
            
        if main_option == 1:
            display(True)
            
        elif main_option == 2:
            add_newitem_menu(True)
            
        elif main_option == 3:
            edit_item_menu(True)
            
        elif main_option == 4:
            delete_item_menu(True)
            
        elif main_option == 0:
            print("thank you for using goodbye")
            main(False)
        else:
            print("please enter a valid number")
            main(True)


        
main(True)
  
