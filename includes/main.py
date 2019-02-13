from includes.gameRules import GameManadgement

class Main(GameManadgement):

   #INTRO
   """
   This method just prints the entry message
   """
   def __init__(self):
      try:
         myfile = "chess" + str(randint(1,3)) + ".txt"
         #opening the Chess ASCII Character files
         with open(myfile, "r", encoding="utf8") as file:
            print(file.read())
      except:
         print("SAKK by Viktor Egedi")
   
   #PLAYERSETUP
   """
   This method sets up the two players
   """
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
   """
   This method asks the players if they want to play, and starts one up if it is needed
   """
   def newGame(self):
      while True:
         while True:
            ans = input("Szeretnének egy új játékot indítani? ([igen] vagy [nem]): ").strip().lower()
            if (ans != "igen" and ans != "nem"):
               pass
            else:
               break
         
         #if the players don't want to play
         if (ans == "nem"):
            print("\n\nRendben\nRemélem tetszett a kis játékom :)\nKészítette: Egedi Viktor, 2019")
            break
         
         #if the players want to play
         elif (ans == "igen"):
            #Then the games starts
            nwGame = GameManadgement()

            #if the game is finished we delete the mwGame
            if nwGame:
               del nwGame