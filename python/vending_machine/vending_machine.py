from juice import Juice
from suica import Suica

class VendingMachine:
    def __init__(self):
        self.__sales_amount = 0
        self.__stocks = [
            Juice("ペプシ", 150, 5),
            Juice("モンスター", 230, 5),
            Juice("いろはす", 120, 5),
        ]
    
    def stock_items(self):
        return {stock.name: stock.stock for stock in self.__stocks}
    
    @property
    def sales_amount(self):
        return self.__sales_amount
    
    def availabled_purchace(self, suica, juice):
        return juice <= suica.credit and juice.stock != 0

    def buy(self, name, suica):
        select_juice = None
        for juice in self.__stocks:
            if name == juice.name:
                select_juice = juice
                break
        
        if select_juice is None or select_juice.stock == 0:
            raise ValueError(f'{name}は在庫がありません。')
        elif suica.credit < select_juice.price:
            raise ValueError(f'チャージ残高が不足しています。残高:{suica.credit}円')

        select_juice.subtract_stock()
        suica.reduce_credit(select_juice.price)
        self.__sales_amount += select_juice.price

    def replenishment(self, input_juice):
        replenishment_juice = None
        for juice in self.__stocks:
            if input_juice.name == juice.name:
                replenishment_juice = juice
                break
        if replenishment_juice is None:
            self.__stocks.append(input_juice)
        else:
            replenishment_juice.append_stock(input_juice.stock)