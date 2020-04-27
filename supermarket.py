from supermarket_model import SuperMarket

supermarket_obj_dict = {}

def create_new_product(item_desc, item_sell_price, item_stock_lvl, item_catergory, item_supplier):
    new_product = SuperMarket(
        item_desc, item_sell_price, item_stock_lvl, item_catergory, item_supplier)
    supermarket_obj_dict[item_desc] = new_product


def delete_product(item_desc):
    if item_desc in supermarket_obj_dict.keys():
        supermarket_obj_dict.pop(item_desc)
        return '{} has been deleted'.format(item_desc)
    else:
        return False


def edit_products(item_desc, edit, new_info):
    if item_desc in supermarket_obj_dict.keys():
        if edit == "descrption":
            product = supermarket_obj_dict.get(item_desc)
            product.set_item_desc(new_info)
            supermarket_obj_dict[item_desc] = product
        elif edit == "price":
            product = supermarket_obj_dict.get(item_desc)
            product.set_item_sell_price(new_info)
            supermarket_obj_dict[item_desc] = product
        elif edit == "stock":
            product = supermarket_obj_dict.get(item_desc)
            product.set_item_stock_lvl(new_info)
            supermarket_obj_dict[item_desc] = product
        elif edit == "catergory":
            product = supermarket_obj_dict.get(item_desc)
            product.set_item_catergory(new_info)
            supermarket_obj_dict[item_desc] = product
        else:
            product = supermarket_obj_dict.get(item_desc)
            product.set_item_supplier(new_info)
            supermarket_obj_dict[item_desc] = product

        return "success"

    else:
        return False


def display_all_products():
    print("product database")
    print("===========================================================================")
    print("descrption------sell_price------stock------catergory------supplier")
    for products in supermarket_obj_dict.items():
        print(products.get_item_desc(), " | ",
              products.get_item_sell_price(), " | ", products.get_item_stock_lvl, " | ", products.get_item_catergory(), " | ", products.get_item_supplier(), " | ")
