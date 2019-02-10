from includes.gameRules import GameManadgement

class Main(GameManadgement):

   #INTRO
   def __init__(self):
      try:
         from random import randint
         myfile = "chess" + str(randint(1,3)) + ".txt"
         #opening the Chess ASCII Character files
         with open(myfile) as file:
            print(file.read())
      except:
         print("SAKK by Viktor Egedi")
   
   #PLAYERSETUP
   def playerSetup(self):
      #This dict holds the name of the players and their colors
      self.players = dict(player01="", color01="white", player02="", color02="black")
      try:
         while True:
            if (self.players['player01'] == "" or self.players['player02'] == ""):
               print("\n\nA játék megkezdéséhez regisztrálni kell a játékosokat!\n")
               self.players['player01'] = input("Kérem adja meg a fehér játékos nevét: ")
               self.players['player02'] = input("Kérem adja meg a fekete játékos nevét: ")
            else:
               break
      except:
         self.players['player01'] = "Játékos I."
         self.players['player02'] = "Játékos II."
      finally:
         print(f"\nA játékosok: [{self.players['player01']}] és [{self.players['player02']}]\n")

   #NEWGAME
   def newGame(self):
      ans = ""
      while True:
         if (ans != "igen" and ans != "nem"):
            ans = input("Szeretnének egy új játékot indítani? ([igen] vagy [nem]): ").lower()
         else:
            break
      
      if (ans == "nem"):
         print("\n\nRendben\nRemélem tetszett a kis játékom :)\nKészítette: Egedi Viktor, 2019")
      elif (ans == "igen"):
         nwGame = GameManadgement()

         #amig nincs matt