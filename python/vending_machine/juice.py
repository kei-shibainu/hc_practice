class Juice:
    def __init__(self, name, price, stock):
        self.__name = name
        self.__price = price
        self.__stock = stock
    
    @property
    def name(self):
        return self.__name

    @property
    def price(self):
        return self.__price
    
    @property
    def stock(self):
        return self.__stock
    
    def append_stock(self, stock):
        self.__stock += stock

    def subtract_stock(self):
        self.__stock -= 1;