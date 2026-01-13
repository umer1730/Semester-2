import pickle
class GameSave:
    def __init__(self,player_name,level,inventory):
        self.player_name = player_name
        self.level = level
        self.inventory = inventory
    
    def save_game(self,filename):
        try:
            with open(filename,"wb") as f:
                pickle.dump(self,f)
            print("Game saved successfully")

        except Exception as e:
            print(f"Save failed: {e}")
    
    @staticmethod
    def load_game(filename):
        try:
            with open(filename,"rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            print("No save file found")

p1 = GameSave("Ninja",10,["Sword","SHield"])
p1.save_game("save1.pkl")

loaded_player = GameSave.load_game("save1.pkl") 
print(f"Loaded Player: {loaded_player.player_name}, Level: {loaded_player.level}")   