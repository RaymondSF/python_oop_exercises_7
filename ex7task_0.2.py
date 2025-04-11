# Part 1: Simple dice gameCreate multiple dices (at least three) and put them in a list. 
# See that your dice can be rolled,and the side can be shown. 
# Create a small game where the best sum of three rolls wins. 
# If the sum is a tie, tied dices are rolled until thewinner is found (best side wins). 
# Use functions and pass objects (or list of objects) as arguments. ¨
# Use informative and clear output prints.
# 
# Part 2: Add dicesChange your program now so that you can use any number of dices, e.g. number of dices. 
# The number of dices that is going to be usedis asked from the user.
# 
# part 3: Add PlayersCreate a class called Player. 
# Player has at least the following data attributes: name and a player id. 
# Remember to code accessor(getters)and mutator(setters)methods and str-method, use the Pythonic way, i.e.    
# use the property decorator. 
# 
# Create a dictionary so that the player id is thekey and each player has one dice. 
# Roll each player’s dice and print out each player’s dice’s side. 
# Use informative and clear output prints. 
# Create the dictionary in main function in this exercise. 
# If this is too difficult, start with creating 1 player. Then try to extend to multiple players if you can. 
# 
# part 4: Add MammalsCreate a mammal class. 
# It has the following data attributes: ID, species, name, size and weight.Part 
# 
# 5: Add pet to each playerAdd one data attribute to player (= add it to Player class), 
# attribute is called pet and it is always a mammal.
# Add also a method that helps to set the pet to the player.
# In the mainfunction,give every player one mammal and print out each player and their mammal’s information. 
# Use informative and clear output print. 
# If this is too difficult, start with 1 player and then extend to multiple players if you can. 
# 
# Part 6: Mammal based on dice game resultLet the player select theirpet mammal by rolling 2 dices and using their sum to indicate a mammal 
# (use here the dice game that you developed at the early part of this exercise). 
# The higher the number, the heavier mammal you get as your pet. 
# Remember to implement the selection logic in e.g.,main function (so not inside any class). 
# Thus, you are of course allowed to (and supposed to) call class’s methods from main (e.g. roll_dice, get_side etc
#
#
import random

# Part 1: Simple dice game
class Dice:
    def __init__(self):
        self.side = 1

    def roll(self):
        self.side = random.randint(1, 6)

    def get_side(self):
        return self.side

def roll_and_sum(dices):
    total = 0
    for dice in dices:
        dice.roll()
        total += dice.get_side()
    return total

def determine_winner(dices):
    total = roll_and_sum(dices)
    print(f"Dice rolls: {[dice.get_side() for dice in dices]}, Total: {total}")
    return total

def play_game(dices):
    print("Starting Dice Game!")
    player_score = determine_winner(dices)

    while True:
        opponent_score = determine_winner(dices)
        if player_score > opponent_score:
            print("Player wins!")
            break
        elif player_score < opponent_score:
            print("Opponent wins!")
            break
        else:
            print("It's a tie! Rolling again...")

if __name__ == "__main__":
    dices = [Dice() for _ in range(3)]
    play_game(dices)

# Part 2: Add dices
def play_game_user_dice():
    num_dices = int(input("Enter number of dices: "))
    dices = [Dice() for _ in range(num_dices)]
    play_game(dices)

if __name__ == "__main__":
    play_game_user_dice()  #run part 2

# Part 3: Add Players
class Player:
    def __init__(self, player_id, name):
        self._player_id = player_id
        self._name = name
        self._pet = None #added in part 5

    @property
    def player_id(self):
        return self._player_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def __str__(self):
        pet_info = f", Pet: {self._pet}" if self._pet else "" #added to include pet info, changed self.pet to self._pet
        return f"Player ID: {self.player_id}, Name: {self.name}{pet_info}"

    #added in part 5
    def set_pet(self, mammal):
        self._pet = mammal

def play_with_players():
    players = {}
    num_players = int(input("Enter number of players: "))
    for i in range(num_players):
        name = input(f"Enter name for player {i + 1}: ")
        players[i + 1] = Player(i + 1, name)

    player_dices = {player.player_id: Dice() for player in players.values()}

    for player_id, dice in player_dices.items():
        dice.roll()
        print(f"{players[player_id].name}'s dice roll: {dice.get_side()}")

if __name__ == "__main__":
    play_with_players() #run part 3

# Part 4: Add Mammals
class Mammal:
    def __init__(self, mammal_id, species, name, size, weight):
        self._mammal_id = mammal_id
        self._species = species
        self._name = name
        self._size = size
        self._weight = weight

    @property
    def mammal_id(self):
        return self._mammal_id

    @property
    def species(self):
        return self._species

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def size(self):
        return self._size

    @property
    def weight(self):
        return self._weight

    def __str__(self):
        return f"Mammal ID: {self.mammal_id}, Species: {self.species}, Name: {self.name}, Size: {self.size}, Weight: {self.weight}"

# Part 5: Add pet to each player
def assign_pets():
    players = {}
    num_players = int(input("Enter number of players: "))
    for i in range(num_players):
        name = input(f"Enter name for player {i + 1}: ")
        players[i + 1] = Player(i + 1, name)

    mammals = [
        Mammal(1, "Elephant", "Ellie", "Large", 6000),
        Mammal(2, "Lion", "Leo", "Medium", 190),
        Mammal(3, "Dog", "Buddy", "Small", 25),
        Mammal(4, "Bear", "Baloo", "Large", 400),
        Mammal(5, "Cat", "Mittens", "Small", 5),
        Mammal(6, "Whale", "Willy", "Huge", 150000),
        Mammal(7, "Giraffe", "Geoff", "Large", 1800),
        Mammal(8, "Tiger", "Tony", "Medium", 200),
        Mammal(9, "Rabbit", "Roger", "Small", 2),
        Mammal(10, "Hippopotamus", "Henry", "Large", 3500),
        Mammal(11, "Ferret", "Frank", "Small", 1),
        Mammal(12, "Dolphin", "Dave", "Medium", 200)
    ]

    for player in players.values():
        player.set_pet(random.choice(mammals))
        print(player)

if __name__ == "__main__":
    assign_pets() #run part 5

# Part 6: Mammal based on dice game result
def assign_pets_dice_game():
    players = {}
    num_players = int(input("Enter number of players: "))
    for i in range(num_players):
        name = input(f"Enter name for player {i + 1}: ")
        players[i + 1] = Player(i + 1, name)

    mammals = [
        Mammal(1, "Elephant", "Ellie", "Large", 6000),
        Mammal(2, "Lion", "Leo", "Medium", 190),
        Mammal(3, "Dog", "Buddy", "Small", 25),
        Mammal(4, "Bear", "Baloo", "Large", 400),
        Mammal(5, "Cat", "Mittens", "Small", 5),
        Mammal(6, "Whale", "Willy", "Huge", 150000),
        Mammal(7, "Giraffe", "Geoff", "Large", 1800),
        Mammal(8, "Tiger", "Tony", "Medium", 200),
        Mammal(9, "Rabbit", "Roger", "Small", 2),
        Mammal(10, "Hippopotamus", "Henry", "Large", 3500),
        Mammal(11, "Ferret", "Frank", "Small", 1),
        Mammal(12, "Dolphin", "Dave", "Medium", 200)
    ]

    for player in players.values():
        dice1 = Dice()
        dice2 = Dice()
        dice1.roll()
        dice2.roll()
        total_roll = dice1.get_side() + dice2.get_side()
        mammal_index = (total_roll - 2) % len(mammals)  # Adjust index to fit mammal list
        player.set_pet(mammals[mammal_index])
        print(player)

if __name__ == "__main__":
    assign_pets_dice_game() #run part 6
