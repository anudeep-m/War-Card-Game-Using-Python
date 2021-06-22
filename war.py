import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8,'Nine':9, 'Ten':10, 'Jack':11, 'Queen':12, 'King':13, 'Ace':14}

#********************************************************


#Card class which is used for creating the deck of cards
class Card:
    
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return f'{self.suit} {self.value}'


'''
Deck Class which is used for creating cards with the help of Card Class
Deck class is used for shuffling the cards and splitting between the two players
'''
class Deck:
    def __init__(self):
        self.deck_of_cards = []
        

        #this loop appends all the 52 unique cards into the list named dec_of_cards
        for suit in suits:
            for rank in ranks:
                self.deck_of_cards.append(Card(suit,rank))


    #funtion used for shuffling cards
    def shuffle(self):
        random.shuffle(self.deck_of_cards)
        

    #this function helps to pick a card from the deck_of_cards and return to players during splitting of cards    
    def pick_one(self):
        return self.deck_of_cards.pop()



#Player Class which is used for removing and adding cards to players hand(list)
class Player:
    
    def __init__(self,name,pl_cards):
        self.name=name
        self.pl_cards=pl_cards
        
    #funtion used for removing the top most card for playing    
    def remove_one(self):
        return self.pl_cards.pop(0)
    
    #funtion used for removing the top most card for playing      
    def add_cards(self,new_cards):
        self.pl_cards.extend(new_cards)

    #function to return a string during string operations for the objects created in Players class 
    #a meaningful string will be made using the attributes of that particular object   
    def __str__(self):
        return f'{self.name} has {len(self.pl_cards)} cards'



#********************************************************



#function used to check wether any player are left with no more cards
def check_lose(player1, player2):
    if len(player1) == 0 or len(player2)==0:
        return True
    return False


#function used to print the top bar which contains the players names
def printtopbar():
    print()
    print((f"{p1.name}'s Top Card".ljust(30) +  "vs" + f"{p2.name}'s Top Card".rjust(30)).center(100))
    print(("_"*70).center(100))
    print()


#function used for printing the card after every round of play
def printcard(x,y,m,n):
    print()
    print(((" "+"_"*10+" ").ljust(30) + (" "+"_"*10+" ").rjust(30)).center(100))
    print(("Cards Count:".ljust(20))+(("|          |").ljust(30) + ("|          |").rjust(30)).ljust(80))
    print((("|"+f"{x.suit}".center(10)+"|").ljust(30) + ("|"+f"{y.suit}".center(10)+"|").rjust(30)).center(100))
    print((f"{p1.name} - {m}".ljust(20))+(("|          |").ljust(30) + ("|          |").rjust(30)).ljust(80))
    print((("|"+f"{x.value}".center(10)+"|").ljust(29) +"vs"+ ("|"+f"{y.value}".center(10)+"|").rjust(29)).center(100))
    print((f"{p2.name} - {n}".ljust(20))+(("|          |").ljust(30) + ("|          |").rjust(30)).ljust(80))
    print((("|"+f"{x.rank}".center(10)+"|").ljust(30) + ("|"+f"{y.rank}".center(10)+"|").rjust(30)).center(100))
    print((("|"+"_"*10+"|").ljust(30) + ("|"+"_"*10+"|").rjust(30)).center(100))
    print()


#function used for printing the winner of the round after every round of play
def printroundwin(a,b):
    if a:
        print((("WON".center(12)).ljust(30) + ("LOST".center(12)).rjust(30)).center(100))
    else:
        print((("LOST".center(12)).ljust(30) + ("WON".center(12)).rjust(30)).center(100))
        



#the main logic of the war game
def wargame():
    z=1
    newcards=[]
    printtopbar()
    
    while not check_lose(player1,player2):
        #by giving any input from the user, the round starts. Each round will start with an user input
        #input can be anything, be it a number or a character or even space
        if input().lower() =="end":
            print("Game ended in between. DRAW")
            break
        else:       
            x=p1.remove_one()
            y=p2.remove_one()
            newcards.extend([x,y])
            print(f"Round : {z}".center(100))
            printcard(x,y,len(player1)+1,len(player2)+1)

            if x.value > y.value:
                p1.add_cards(newcards)
                newcards.clear()
                printroundwin(True ,False)
            
            elif y.value>x.value:
                p2.add_cards(newcards)
                printroundwin(False ,True)
                newcards.clear()
            
            else:
                print("Both have same ranked cards  \n")
                print("--------------WAR-------------- \n")
                print("Both players need to pick their top three cards and place them on the board  \n")

                
                for i in range(3):
                    if not check_lose(player1,player2):
                        newcards.extend([p1.remove_one(),p2.remove_one()])
                    else:
                        
                        if len(player2)>len(player1):
                            p2.add_cards(newcards)
                            print(f"Oops! {p1.name} have only {i} card(s)")
                            print(f"So {p2.name} takes all the cards on the board")
                        else:
                            p1.add_cards(newcards)
                            print(f"Oops! {p2.name} have only {i} card(s)")
                            print(f"So {p1.name} takes all the cards on the board")
                        
                        break
            z+=1
    
    else:
        print(("GAME OVER").center(100))
        print()
        if len(player2)>len(player1):
            print((f"{p1.name} have no more cards \n").center(100))
            print((f"{p2.name} is the WINNER").center(100))
        else:
            print((f"{p2.name} have no more cards \n").center(100))
            print((f"{p1.name} is the WINNER").center(100))


#********************************************************



if __name__ == "__main__":
    new_deck=Deck()
    new_deck.shuffle()
    player1=[]
    player2=[]

    for i in range(0,52,2):
        player1.append(new_deck.pick_one())
        player2.append(new_deck.pick_one())

    print("\nGame Instructions: \n")
    print("1)Please keep your names short - within 10 letters")       
    print("2)For each round, give any input...be it a number or a character or even space")
    print("3)Give an input of 'end' to end the game in between. Any other input will continue the game")
    print("4)Cards Count shown on left side are the number of cards before that round\n")
    

    p1=Player(input("Player 1 Name: "),player1)

    p2=Player(input("Player 2 Name: "), player2)

    wargame()