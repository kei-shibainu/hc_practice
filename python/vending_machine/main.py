from vending_machine import VendingMachine
from juice import Juice
from suica import Suica

def run():
    print('-----------')
    print('▫️スイカ100円チャージ')
    suica = Suica()
    suica.add(100)
    print(f'スイカ残高：{suica.credit}')

    print('-----------')
    print('▫️初期在庫の確認')
    vemding_machine = VendingMachine()
    print(vemding_machine.stock_items())

    print('-----------')
    print('▫️存在しないジュースを購入、もしくは在庫がない場合')
    try:
        vemding_machine.buy('おしるこ', suica)
    except ValueError as e:
        print(e)

    print('-----------')
    print('▫️ペプシを一つ購入')
    vemding_machine.buy('ペプシ', suica)
    print(vemding_machine.stock_items())
    print(f'スイカ残高：{suica.credit}')

    print('-----------')
    print('▫️サイダーを備蓄')
    cider = Juice('サイダー', 120, 2)
    vemding_machine.replenishment(cider)
    print(vemding_machine.stock_items())
    print('-----------')

    print('-----------')
    print('▫️いろはすを３つ購入')
    vemding_machine.buy('いろはす', suica)
    vemding_machine.buy('いろはす', suica)
    vemding_machine.buy('いろはす', suica)
    print(vemding_machine.stock_items())
    print(f'スイカ残高：{suica.credit}')

    print('-----------')
    print('▫️チャージ残高不足')
    try:
        vemding_machine.buy('モンスター', suica)
    except ValueError as e:
        print(e)
    print(vemding_machine.stock_items())

if __name__ == '__main__':
    run()