
## EX 7 task 1 part 1 (add Class person)
## 

class Person:

    def __init__(self,name):
        self.__name = name
        self.__numbers = []
        self.__address = None

    def name(self):
        return self.__name
    
    def numbers(self):
        return self.__numbers
    
    def address(self):
        return self.__address
    
    def add_number(self,number:str):
        self.__numbers.append(number)

    def add_address(self,address: str):
        self.__address = address
    



        