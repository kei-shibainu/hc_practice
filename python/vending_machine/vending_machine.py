from juice import Juice
from suica import Suica

class VendingMachine:
    def __init__(self):
        self.__sales_amount = 0
        self.__stocks = [
            {'juice': (Juice("ペプシ", 150)), 'stock': 5},
            {'juice': (Juice("モンスター", 230)), 'stock': 5},
            {'juice': (Juice("いろはす", 120)), 'stock': 5},
        ]
    
    def stock_items(self):
        return {stock['juice'].name: stock['stock'] for stock in self.__stocks}

    @property
    def sales_amount(self):
        return self.__sales_amount
    
    def availabled_purchace(self, suica, juice, stock):
        return juice.price <= suica.credit and stock != 0
    
    def fetch_juice(self, name):
        return next((item for item in self.__stocks if item['juice'].name == name), None)


    def buy(self, name, suica):
        # 購入可能判定
        item = self.fetch_juice(name)
        if item is None or item['stock'] == 0:
            raise ValueError(f'{name}は在庫がありません。')
        elif suica.credit < item['juice'].price:
            raise ValueError(f'チャージ残高が不足しています。残高:{suica.credit}円')

        # 購入処理
        item['stock'] -= 1
        juice = item['juice']
        suica.reduce_credit(juice.price)
        self.__sales_amount += juice.price

    def replenishment(self, input_juice, stock):
        item = self.fetch_juice(input_juice.name)
        if item is None:
            self.__stocks.append({'juice': input_juice, 'stock': stock})
        else:
            item['stock'] -= stock