class MagicPotion:
    def __init__(self, name: str):
        self._name = name
        self._ingredients = []

    def add_ingredient(self, ingredient: str, amount: float):
        self._ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(self._name + ":")
        for ingredient in self._ingredients:
            print(f"{ingredient[0]} {ingredient[1]} grams")

class SecretMagicPotion(MagicPotion):
    def __init__(self,name :str, password: str):
        super().__init__(name)
        self._password = password

    def add_ingredient(self, ingredient: str, amount: float, password: str):
        if password == self._password:
            super().add_ingredient(ingredient, amount)
        else:
            print("Wrong password Ingredient is not added,")

    def print_recipe(self, password: str):
        if password == self._password:
            super().print_recipe()
        else:
            print("Wrong password. Acces denied")

diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus") 
diminuendo.add_ingredient("Toadstool", 1.5  , "hocuspocus") 
diminuendo.add_ingredient("Magic sand", 3.0  , "hocuspocus") 
diminuendo.add_ingredient("Frogspawn", 4.0  , "hocuspocus") 
diminuendo.print_recipe("hocuspocus") 
diminuendo.print_recipe("pocushocus") # WRONG password!

##Example output:
# Diminuendo maximus:
# Toadstool 1.5 grams
# Magic sand 3.0 grams
# Frogspawn 4.0 grams
# 2 Traceback (most recent call last):
# File "secret_magic_potion.py", line 98, in 
# raise ValueError("Wrong password!")
# ValueError: Wrong password!