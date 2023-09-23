class Tab:
    #class instance
    menu={
        'wine':5,
        'beer':3,
        'soft_drink':2,
        'chicken':10,
        'beef':15,
        'veggie':12,
        'dessert':6
    }
    pass

    def __init__(self):
        self.total=0
        self.items=[]
        pass

    def add(self,item):
        self.items.append(item)
        self.total+= self.menu[item]

    def print_bill(self,tax,service):
        tax=(tax/100)*self.total
        service=(service/100)*self.total
        total=self.total+tax+service

        for item in self.items:
            print (f'{item:15}: £{self.menu[item]}')
        
        print(f'{"Total":15}: £{total:.2f}')

table1=Tab()
table1.add('dessert')
table1.add('beer')
table1.add('veggie')
table1.print_bill(10,10)