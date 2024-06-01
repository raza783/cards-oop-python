class Player:
    def __init__(self,player_name,age,bet_amount):
        self.player_name=player_name
        if age<21:
            raise Exception("player age must be 21+")
        else:
            self.age=age
        if bet_amount<50:
            raise Exception("minimum bet amount is 50  us dollar")
        else:
            self.bet_amount=bet_amount
        self.games=[]
        self.my_money = self.bet_amount
    def add_win(self,amount):
        self.my_money+=amount
    def reduce_lost(self,amount):
        self.my_money-=amount
        if self.my_money==0:
            return "you lost all your money, try again"
    def add_game(self,game_name):
        self.games.append(game_name)
    def __repr__(self):
        result=""
        result+="player name: "+self.player_name+" age: "+str(self.age)+" bet amount: "+str(self.bet_amount)+" games: "
        result.join(self.games)
        return result



class Game:
    def __init__(self,name,players=4):
        self.name=name
        self.players=players
        self.deck = ["a", 2, 3, 4, 5, 6, 7, 8, 9, 10, "j", "q", "k"]
        self.wins=0
        self.losts=0
    def add_win(self,amount):
        self.wins+=amount
    def add_lost(self,amount):
        self.losts+=amount
        self.profits=self.wins-self.losts



class Casino:
    def __init__(self,name,capability,games):
        self.name=name
        self.capability=capability
        self.games={}
    def add_game(self,game): #game is am object
        self.games[game.name]=game.profits
    def my_profit(self):
        return sum(self.games.values())





