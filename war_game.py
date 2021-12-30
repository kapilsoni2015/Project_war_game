import random

# Global variable suits and ranks
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two','Three', 'Four', 'Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

# Global variable values
values = {'Two':2,'Three':3, 'Four':4, 'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':11,'Queen':12,'King':13,'Ace':14}


# CARD
# SUIT, RANK, VALUE
class Card:
    
    def __init__(self,suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank] # to get numerical/integer values against ranks for later comparison operations

    def __str__(self):# prinitng out Card class instance
        return self.rank + " of " + self.suit

# two_of_clubs = Card('Clubs','Two')
# print(two_of_clubs)
# print(two_of_clubs.value)



'''
Institate a new deck
create all 52 cards objects

shuffle a deck of 52 cards

Deal (pop) cards from the deck objects
'''

class Deck:

    def __init__(self):
        # no user input is required or no arguments are reuiqred
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                #Crete the card object
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)

    def shuffle(self):
        #random.shuffle() does not return anything, it does operation in-place
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        # returning a card and removing it from deck.all_cards list
        return self.all_cards.pop()

# new_deck = Deck()
# print(new_deck.all_cards[-1])
# new_deck.shuffle()
# print(new_deck.all_cards[-1])
# print(len(new_deck.all_cards))
# my_card = new_deck.deal_one()
# print("my card is ")
# print(my_card)
# print("length of my deck is now:")
# print(len(new_deck.all_cards))




'''
Player class
'''

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def adding_cards(self, new_cards):
        if type(new_cards) == type([]):
            #adding List of multiple card objects
            self.all_cards.extend(new_cards)
        else:
            #For a single card object
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

# new_player = Player('Kapil')
# print(new_player)
# print(new_player.all_cards)
# two_of_clubs = Card('Clubs','Two')
# new_player.adding_cards(two_of_clubs)
# new_player.adding_cards([two_of_clubs, two_of_clubs,two_of_clubs])
# print(new_player)
# new_player.remove_one()
# print(new_player)





'''
Game logic
'''
# Game setup
# Creating computer players 
player_one = Player('One')
player_two = Player('two')

#creating and shuffling new deck
new_deck = Deck()
new_deck.shuffle()

# Splitting new_deck between these two players
for x in range(26):
    player_one.adding_cards(new_deck.deal_one())
    player_two.adding_cards(new_deck.deal_one())

#print(player_one.all_cards[2])

game_on = True # To have game continue

round_num = 0

while game_on:
    round_num += 1
    print(f"Currently round {round_num}")

    if len(player_one.all_cards) == 0:
        print('Player One, out of cards! Player Two wins!')
        game_on = False
        break #redundant as we already have game_on = False above, to break out of loop
    
    if len(player_two.all_cards) == 0:
        print('Player Two, out of cards! Player One wins!')
        game_on = False
        break #redundant as we already have game_on = False above, to break out of loop
    
    # Start a new round to place the cards on table
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())

    player_two_cards = []
    player_two_cards.append(player_two.remove_one())


    # At WAR
    at_war = True # for comparison still going on scenario

    while at_war:

        if player_one_cards[-1].value > player_two_cards[-1].value:

            player_one.adding_cards(player_one_cards)
            player_one.adding_cards(player_two_cards)

            at_war = False # Comparison ends here

        elif player_one_cards[-1].value < player_two_cards[-1].value:

            player_two.adding_cards(player_one_cards)
            player_two.adding_cards(player_two_cards)

            at_war = False # Comparison ends here

        else:
            print("WAR!")
            print(player_one_cards[-1].value, player_two_cards[-1].value)

            if len(player_one.all_cards) < 10:
                print("Player One unable to decalre war!")
                print("PLAYER TWO WINS!")
                game_on = False
                break
            
            elif len(player_two.all_cards) < 10:
                print("Player Two unable to decalre war!")
                print("PLAYER ONE WINS!")
                game_on = False
                break

            else:
                for num in range(10):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())

            


