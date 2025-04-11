from person import Person

class PhoneBook:
    def __init__(self):
        self.__persons = {}


        # updating classes to class Person

    def add_number(self, name: str, number: str):
        if name not in self.__persons:
            self.__persons[name] = Person(name) # each name has person object
        self.__persons[name].add_number(number)

    def add_address(self,name:str, address:str):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

    def get_number(self,name:str):
         if name not in self.__persons:
              return None
         return self.__persons[name].numbers() # access numbers of person object
    
    def search_by_number(self, number: str):
        for person in self.__persons.values():
            if number in person.numbers():
                return person
        return None
    
    def get_address(self, name: str):
        if name not in self.__persons:
            return None
        return self.__persons[name].address() # access afress of peroson object


    def get_entry(self, name: str):
            return self.__persons.get(name,None) # return Person object 
    
    def all_entries(self):
        return self.__persons   # return the whole dict of person objects
