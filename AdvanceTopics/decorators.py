class MyAwesomeClass:
    tax_rate = 0.1
    def __init__(self, income):
        self.income = income

    #it will accept only cls as first argument and it is necessary to pass it, helps to modify class data. you can call it by obj or class. it won't throw any error.
    @classmethod
    def change_tax_rate(cls, tax_rate):
        cls.tax_rate = tax_rate
    
    #no instance is required. this can't modidfy any sort of class data or instance data
    @staticmethod
    def compute_interest(money: int):
        if money >1000:
            return int(money*0.2)
        
        return money*0.1
    
    #this is used to use function like an attribute. First argument should be self only. And it can't take any other argument
    @property
    def awesome_function(self):
        cls = self.__class__

        return int(self.income*cls.tax_rate)
    
    #this is dunder fucntion which is called as double underscore function. And this is used to make objects feel like working with built in fucntion of python
    def __str__(self):
        return f"My Income Is {self.income}."



obj = MyAwesomeClass(2000)
print(obj)

print(MyAwesomeClass.compute_interest(obj.income))
obj.change_tax_rate(0.5)
print(obj.awesome_function)
MyAwesomeClass.change_tax_rate(0.3)
print(obj.awesome_function)

