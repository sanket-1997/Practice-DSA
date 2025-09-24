class Person:
    def __init__(self, name = None):
        self.__name = name if name is not None else 'Unknown'
    

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, new_name : str ):
        if isinstance(new_name, str) and new_name.strip():
            self.__name = new_name
        else:
            raise ValueError("Invalid Name")
        

p = Person()
print(p.name)