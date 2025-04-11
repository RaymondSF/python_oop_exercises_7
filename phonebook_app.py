from phonebook import PhoneBook
from file_handler import FileHandler

class PhoneBookApplication:
    def __init__(self):
        self.__phonebook = PhoneBook()
        self.__filehandler = FileHandler("f.txt")

        # Load phonebook data from file
        phonebook_data = self.__filehandler.load_file()
        for name, numbers in phonebook_data.items():
            for number in numbers:
                self.__phonebook.add_number(name, number)

    def help(self):
        print("commands:")
        print("0 exit")
        print("1 add number")
        print("2 search")
        print("3 add address")

    def add_entry(self):
        name = input("name: ")
        number = input("number: (optional field): ")
        address = input("address: (optional field): ")

        if number:
            self.__phonebook.add_number(name, number)
        if address:
            self.__phonebook.add_address(name, address)

    def search(self):
        name = input("name: ")
        person = self.__phonebook.get_entry(name)

        if person is None:
            print(f"{name} address unknown") #updated print
            print(f"{name} number unknown")
            return
        
        # Print the person's data (address and phone numbers)
        print(f"{person.name()}")
        if person.address():
            print(f"address: {person.address()}")
        else:
            print("address: unknown")
        
        if person.numbers():
            print("phone numbers:")
            for number in person.numbers():
                print(number)
        else:
            print("number: unknown")

    def exit(self):
        # Save phonebook data to file
        phonebook_data = self.__phonebook.all_entries()
        self.__filehandler.save_file(phonebook_data)

    def execute(self):
        self.help()
        while True:
            command = input("command: ")
            if command == "0":
                self.exit()
                break
            elif command == "1":
                self.add_entry()
            elif command == "2":
                self.search()
            elif command == "3":
                self.add_address()

    def add_address(self):
        name = input("name: ")
        address = input("address: ")
        self.__phonebook.add_address(name, address)

application = PhoneBookApplication()
application.execute()
