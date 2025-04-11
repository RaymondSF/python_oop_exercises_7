# In this exercise you will create another version of the PhoneBookApplication. 
# You will add addresses to the data which can be attached to a name.
# For simplicity's sake the functionality for saving to file has been removed, 
# and some other methods have been renamed to better accommodate the change.


# Part 1: A separate class for person’s data:
# Please change the way the data of a person is handled. 
# Implement a class named Person, which takes care of the phone numbers and addresses of persons. 
# The class should work as follows:
# person = Person("Eric") 
# print(person.name())   
# print(person.numbers())   
# print(person.address())   
# person.add_number("040-123456") 
# person.add_address("Mannerheimintie 10 Helsinki") 
# print(person.numbers())   
# print(person.address())   
# Output should be the following:
# Eric[]  
# None
# ['040-123456']
# Mannerheimintie 10 Helsinki
# 
# 
# Part 2: PhoneBook uses the class Person
# Please change the internal implementation of the original application 
# so that your PhoneBook class uses objects of class Person to store the data in the phone book. 
# That is, the attribute __persons should still contain a dictionary, but the values should be Person-objects and not lists. 
# The user of your application should notice no difference; 
# the changes must not affect the user interface.

# WARNING: whenever you make structural changes to your code, as described in this exercise, always take baby steps and test at every possible stage. 
# Do not try and make all the changes at once. 
# That is a sure way of running into serious problems with your code.
# A suitable first step might be to write some code for checking the functionality of the PhoneBookclass directly. 
# For example, the following should at least not cause any errors:
# phonebook = PhoneBook()  
# phonebook.add_number("Eric", "02  -123456") 
# print(phonebook.get_entry("Eric")) 
# print(phonebook.get_entry("Emily"))  
# When you've made the necessary changes in your program and have absolutely verified the functionality within the PhoneBook class, 
# you can move on to the user interface, and see if everything still works as expected.
# 
# Part 3: Adding an address
# Please implement the functionality for adding an address to an entry in your phone book. 
# The program should work as follows:

# commands:
# 0 exit
# 1 add number
# 2 search
# 3 add address
# command: 1

# name: Eric
# number: 02-123456
# command: 3
# name: Emily
# address:Viherlaaksontie 7, Espoo

# command: 2
# name: Eric02-123456
# address unknown
# 
# command: 2
# name: Emily
# number unknown
# Viherlaaksontie 7, Espoo

# command: 3
# name: Eric
# address: Linnankatu 75, Turku

# command: 2
# name: Eric
# 02-123456
# Linnankatu 75, Turku

# command: 2
# name: Wilhelm
# address unknown 
# number unknown 
# command: 0
# 
# WARNING and hint: as stated above in the previous exercise, do not try and make all the changes at once. 
# That is a sure way of running into serious problems with your code.
# First make sure youcan reliably add addresses using the PhoneBook class directly. 
# Once you have verified this, you can move on to the necessary changes in the user interface