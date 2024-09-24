class Suica:
    def __init__(self):
        self.__credit = 500
    
    def add(self, credit):
        if credit < 100:
            raise ValueError('100円からチャージできます。')
        self.__credit += credit
    
    @property
    def credit(self):
        return self.__credit
    
    def reduce_credit(self, credit):
        self.__credit -= credit