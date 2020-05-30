# supermarket class 
class SuperMarket():
    def __init__(self, item_desc, item_sell_price, item_stock_lvl,item_catergory,item_supplier):
        self.item_desc = item_desc
        self.item_sell_price = item_sell_price
        self.item_stock_lvl = item_stock_lvl
        self.item_catergory = item_catergory
        self.item_supplier = item_supplier
        #set sales of items to empty list 
        self.item_sales = []

    def set_item_desc(self, item_desc):
        self.item_desc = item_desc

    def set_item_sell_price(self, item_sell_price):
        self.item_sell_price = item_sell_price

    def set_item_stock_lvl(self, item_stock_lvl):
       self.item_stock_lvl = item_stock_lvl

    def set_item_catergory(self, item_catergory):
       self.item_catergory = item_catergory

    def set_item_supplier(self, item_supplier):
       self.item_supplier= item_supplier

    def set_item_sales(self, item_sales):
       self.item_sales = item_sales
    


    def get_item_desc(self):
        return self.item_desc
    
    def get_item_sell_price(self):
        return self.item_sell_price

    def get_item_stock_lvl(self):
        return self.item_stock_lvl

    def get_item_catergory(self):
        return self.item_catergory

    def get_item_supplier(self):
        return self.item_supplier

    def get_item_sales(self):
        return self.item_sales









