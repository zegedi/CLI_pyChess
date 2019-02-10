import includes.figures as figs #This is the figure.py wich contains Figures() class
import includes.main as main #This is the main.py wich Main() class
import re

class GameManadgement(main.Main, figs.Figures):

   #These are kinds of error messages
   invalidInput = "HIBA: nem megfelelő paramétereket adott meg!"
   stepError = "HIBA: nem lehet a megadott lépést elvégezni!"
   checkError = "HIBA: királyod jelenleg sakkban van, meg kell szüntetned ezt az állapotot!"

   #King positions
   """
   These properties are holding the current positions of the kings
    * These must be updated when the king moves
    * The type of the X and Y must be in an integer
   """
   blackKing = {"x": 1, "y": 5}
   whiteKing = {"x": 8, "y": 5}

   #This function creates a new game
   def __init__(self):

      #Table
      """
      This is the table what the game uses to operate
       # Correct use of the table: self.table[y][x] ==> table[column][row]
       * The table's elements are the columns [ Y ]
       * The elements's elements are the rows [ X ]
      """
      self.table = [
         ("1","2","3","4","5","6","7","8"), #These are the row names
         ["A", "black_rook","black_knight","black_bishop","black_queen","black_king","black_bishop","black_knight","black_rook"],
         ["B", "black_pawn","black_pawn","black_pawn","black_pawn","black_pawn","black_pawn","black_pawn","black_pawn"],
         ["C", "","","","","","","",""],
         ["D", "","","","","","","",""],
         ["E", "","","","","","","",""],
         ["F", "","","","","","","",""],
         ["G", "white_pawn","white_pawn","white_pawn","white_pawn","white_pawn","white_pawn","white_pawn","white_pawn"],
         ["H", "white_rook","white_knight","white_bishop","white_queen","white_king","white_bishop","white_knight","white_rook"]
      ]

      #CopyTable
      """
      The copyTable is used to test if a move is valid or not
       * It is used in the checkForCheck() method
      """
      #self.copyTable = self.table.copy()


   #PlayerMove method
   """
   This method deals with the choise of the player
   """
   def playerMove(self):
      
      #This method asks for the input
      def askPlayer(self, useCopy=False):
         while True:
            nowPos = input("\nHonnan: ").strip().lower()
            nextPos = input("Hova: ").strip().lower()

            #if input's lenght is 2
            if len(nowPos) == 2 and len(nextPos) == 2:

               #if the input doesn't contain a number (1-8)
               if len(re.findall("[a-h][a-h]", nowPos)) != 0 or len(re.findall("[a-h][a-h]", nowPos)) != 0:
                  print("\n" + self.invalidInput)

               #if the input doesn't contain a letter (a-h)
               elif len(re.findall("[1-8][1-8]", nowPos)) != 0 or len(re.findall("[1-8][1-8]", nowPos)) != 0:
                  print("\n" + self.invalidInput)

               #if the input is correct
               else:

                  #Checking the result of the move
                  result = self.makeStep(self=self, nowPos=nowPos, nextPos=nextPos, playerColor=playerColor, useCopyTable=useCopy)
         
                  #if an error occurs with the step
                  if bool(result):
                     print("\n {}".format(result))

                  #if there is no error with the step
                  else:
                     break
                  
            else:
               print("\n" + self.invalidInput)



      #This method deals with the next player
      def nextPlayer(self, playerName, playerColor):
         """
         PRINT TABLE
         """
         #Validating the king's color
         if playerColor == "white":
            kingX = self.whiteKing["x"]
            kingY = self.whiteKing["y"] 
            col = "fehér"
         elif playerColor == "black":
            kingX = self.blackKing["x"]
            kingY = self.blackKing["y"] 
            col = "fekete"

         #printing who's next
         print("\n{} következik (színe: {}):".format(playerName, col))
         
         #if there is a check on the user's king
         if self.checkForCheck(self=self, kingX=kingX, kingY=kingY, col=playerColor, useCopyTable=False):
            
            #if it is checkmate
            if self.checkForCheckmate(self=self, kingX=kingX, kingY=kingY, col=playerColor):
               """ GAME OVER! """
               pass
            
            #if it's a normal check
            else:

               #making the copyTable
               self.copyTable = self.table.copy()
               while True:

                  #making the copies of the king's position
                  #it is used for updating the king's finaly position
                  if playerColor == "white":
                     self.copyWhiteKing["x"] = kingX
                     self.copyWhiteKing["y"] = kingY

                  elif playerColor == "black":
                     self.copyBlackKing["x"] = kingX
                     self.copyBlackKing["y"] = kingY
                  
                  #letting the user know that his king is in a check position
                  print("Sakkot kaptál! Meg kell szüntetned ezt az állapotot!")
                  askPlayer(self=self, useCopy=useCopy)

                  #if the check is over
                  if not self.checkForCheck(self=self, kingX=kingX, kingY=kingY, col=playerColor, useCopyTable=True):
                     #updating the king's final position
                     if playerColor == "white":
                        self.whiteKing["x"] = self.copyWhiteKing["x"]
                        self.whiteKing["y"] = self.copyWhiteKing["y"]
                        del self.copyWhiteKing
                     elif playerColor == "black":
                        self.blackKing["x"] = self.copyBlackKing["x"]
                        self.blackKing["y"] = self.copyBlackKing["y"]
                        del self.copyBlackKing

                     #updating the self.table
                     self.table.clear()
                     self.table = self.copyTable.copy()
                     del self.copyTable
                     break
         
         #if there is no check on the user's king
         else:
            
            #asking the user for an input
            askPlayer(self=self, useCopy=False)

      
      #WHITE PLAYER
      nextPlayer(self=self, playerName=self.players['player01'], playerColor=self.players['color01'])

      #BLACK PLAYER
      nextPlayer(self=self, playerName=self.players['player02'], playerColor=self.players['color02'])




   #CheckForCheck method
   """
   This method checks if the user's king got an attack. The method returns:
    # The otherX and otherY variables are the positions of a condicional figure move [ optional ]
    * True  - if the king is in check or could be
    * False - if the king is safe 
   """
   #MÉG VAN MIT RAJTA JAVÍTANI
   def checkForCheck(self, kingX, kingY, col, useCopyTable=False):
      
      #These are the possible placeholders
      placeholders = ["A","B","C","D","E","F","G","H"]

      #if we want to use the self.copyTable
      if useCopyTable:

         #looping through the self.copyTable
         for y in range(1,9):
            for x in self.copyTable[y]:

               #if the position is not empty
               if x != "":

                  #if the position is not a placeholder
                  if x not in placeholders:

                     #getting the value of the position
                     pos = re.split("_", x)

                     #This sets the color of the user
                     #if the king's color is white
                     if col == "white" and pos[0] == "black":
                        userColor = "black"
                     #if the king's color is black
                     elif col == "black" and pos[0] == "white":
                        userColor = "white"

                     #Checking the possible enemy moves againts the king
                     if pos[1] == "pawn" and pos[0] != col:
                        #if the pawn could take the king down
                        if self.pawn_move(self=self, nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=userColor, useCopyTable=useCopyTable):
                           return True
                  
                     elif pos[1] == "rook" and pos[0] != col:
                        #if the rook could take the king down
                        if self.rook_move(self=self, nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=userColor, useCopyTable=useCopyTable):
                           return True
                     
                     elif pos[1] == "knight" and pos[0] != col:
                        #if the knight could take the king down
                        if self.knight_move(self=self, nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=userColor, useCopyTable=useCopyTable):
                           return True
                     
                     elif pos[1] == "bishop" and pos[0] != col:
                        #if the bishop could take the king down
                        if self.bishop_move(self=self, nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=userColor, useCopyTable=useCopyTable):
                           return True
                     
                     elif pos[1] == "queen" and pos[0] != col:
                        #if the queen could take the king down
                        if self.queen_move(self=self, nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=userColor, useCopyTable=useCopyTable):
                           return True
                     
                     elif pos[1] == "king" and pos[0] != col:
                        #if the king could take the king down
                        if self.king_move(self=self, nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=userColor, useCopyTable=useCopyTable):
                           return True
         
         #if the king isn't in a check position
         else:
            return False


      #if we want to use the table
      else:
         
         #looping through the self.table
         for y in range(1,9):
            for x in self.table[y]:

               #if the position is not empty
               if x != "":

                  #if the position is not a placeholder
                  if x not in placeholders:

                     #getting the value of the position
                     pos = re.split("_", x)

                     #This sets the color of the user
                     #if the king's color is white
                     if col == "white" and pos[0] == "black":
                        userColor = "black"
                     #if the king's color is black
                     elif col == "black" and pos[0] == "white":
                        userColor = "white"

                     #Checking the possible enemy moves againts the king
                     if pos[1] == "pawn" and pos[0] != col:
                        #if the pawn could take the king down
                        if self.pawn_move(self=self, nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=userColor, useCopyTable=useCopyTable):
                           return True
                  
                     elif pos[1] == "rook" and pos[0] != col:
                        #if the rook could take the king down
                        if self.rook_move(self=self, nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=userColor, useCopyTable=useCopyTable):
                           return True
                     
                     elif pos[1] == "knight" and pos[0] != col:
                        #if the knight could take the king down
                        if self.knight_move(self=self, nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=userColor, useCopyTable=useCopyTable):
                           return True
                     
                     elif pos[1] == "bishop" and pos[0] != col:
                        #if the bishop could take the king down
                        if self.bishop_move(self=self, nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=userColor, useCopyTable=useCopyTable):
                           return True
                     
                     elif pos[1] == "queen" and pos[0] != col:
                        #if the queen could take the king down
                        if self.queen_move(self=self, nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=userColor, useCopyTable=useCopyTable):
                           return True
                     
                     elif pos[1] == "king" and pos[0] != col:
                        #if the king could take the king down
                        if self.king_move(self=self, nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=userColor, useCopyTable=useCopyTable):
                           return True
         
         #if noone can take the king down
         else:
            return False



   #CheckForCheckmate
   """
   This method checks if the user is lost or not
    * True  - if the user lost the game
    * False - if the user didn't lose the game
   """
   #meg kell nézni hogy a király elléphet-e a sakkból
   #ha nem tud ellépni akkor tudja valami blokkolni a sakkot vagy megölni a támadót
   #
   def checkForCheckmate(self, kingX, kingY, col):

      #making the possible steps with the king
      #The possible's first list is the column ==> Y
      #The possible's second list is the row ==> X
      possibleKingMove = [
         {"x": kingX-1, "y": kingY},
         {"x": kingX-1, "y": kingY+1},
         {"x": kingX-1, "y": kingY-1},
         {"x": kingX+1, "y": kingY},
         {"x": kingX+1, "y": kingY+1},
         {"x": kingX+1, "y": kingY-1},
         {"x": kingX, "y": kingY+1},
         {"x": kingX, "y": kingY-1}
      ]

      #looping through the possible columns
      for p in possibleKingMove:

         #creating the copyTable
         self.copyTable = self.table.copy()
         
         #creating the next possible positions
         nextX = p["x"]
         nextY = p["y"]

         #if the possible position is on the table
         if (nextX >= 1 and nextX <= 8) and (nextY >= 1 and nextY <= 8):
            
            #if the king could go that position
            if self.king_move(self=self, nowX=kingX, nowY=kingY, nextX=nextX, nextY=nextY, color=col, useCopyTable=True):
               
               #making the change to the copyTable
               self.alterTable(self=self, nowX=kingX, nowY=kingY, nextX=nextX, nextY=nextY, col=col, fig="king", useCopyTable=True)
            
         #if the king is safe with that move ==> the game is not over yet
         if not self.checkForCheck(self=self, kingX=nextX, kingY=nextY, col=col, useCopyTable=True):
            return False


      #if the king could not get out from the check by itself
      else:

         #if one of the user's figures could take down the attacker
         

         #if one of tehr user's figures could protect the king


   #FigureSwitch Method
   """
   This method is used for validating a pawn switch
   """
   def pawnSwitch(self, nextY, col):
      
      #if the pawn is white
      if col == "white":
         if nextY == 1:
            return True
         else:
            return False
         
      #if the pawn is black
      elif col == "black":
         if nextY == 8:
            return True
         else:
            return False



   #CheckTable method
   """
   This method is used to check if there is any figure in the specified position where the player wants to go.
   """
   def checkTable(self, x, y, returnCol=False, returnFig=False, useCopyTable=False):

      #if we want to use the copyTable
      if useCopyTable:
         pos = re.split("[_]", self.copyTable[y][x])
      else:
         pos = re.split("[_]", self.table[y][x])

      #If we want ot get the COLOR
      if returnCol:
         if len(pos) > 0:
            return pos[0]
         else:
            return ""

      #If we want to get the FIGURE
      elif returnFig:
         if len(pos) > 0:
            return pos[1]
         else:
            return ""
      
      """
      else:
         return False
         #IT COULD CHANGE
      """


   #Mapping method
   """
   This method maps the letter form position input to numbers.
   """
   def mapNumberToY(self, letter):
      abc = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
      for y, value in abc.items():
         if letter == y:
            return value


   #This function alters the table if a move could go down
   """
   This method makes the change to the table / copyTable
   """
   def alterTable(self, nowX, nowY, nextX, nextY, col, fig, useCopyTable=False):
      nowX = str(nowX)
      nowY = str(nowY)
      nextX = str(nextX)
      nextY = str(nextY)
      if useCopyTable:
         self.copyTable[nowY][nowX] = ""
         self.copyTable[nextY][nextX] = col + "_" + fig
      else:
         self.table[nowY][nowX] = ""
         self.table[nextY][nextX] = col + "_" + fig



   #MakeStep method
   """
   This method validates the user input for the positions. This method returns:
    * False - if the move is made
    * else  - returns an error message
   """
   def makeStep(self, nowPos, nextPos, playerColor, useCopyTable=False):

      #Getting the user's input
      a = re.search("[a-h]", nowPos) #Column
      b = re.search("[1-8]", nowPos) #Row
      c = re.search("[a-h]", nextPos) #Column
      d = re.search("[1-8]", nextPos) #Row


      #Validating the user's input
      #If the user didn't give the correct input
      if a == None or b == None or c == None or d == None:
         return self.invalidInput
      
      #if the input is correct
      else:

         #Converting the user's input
         nowY = int(self.mapNumberToY(a.group()))
         nowX = int(b.group())
         nextY = int(self.mapNumberToY(c.group()))
         nextX = int(d.group())

         #If the starting and ending position is the same
         if nowX == nextX and nowY == nextY:
            return self.stepError
         
         else:
            #These variables would hold the user's figurename and the it's color
            fig = self.checkTable(x=nowX, y=nowY, returnFig=True)
            col = self.checkTable(x=nowX, y=nowY, returnCol=True)
            
            #This method deals with the pawn
            if fig == "pawn" and playerColor == col:
               if self.pawn_move(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, color=col, useCopyTable=useCopyTable):
                  
                  #if the pawn is in a figure-switch position
                  if self.pawnSwitch(self=self, nextY=nextY, col=col):
                     while True:
                        ans = input("Mire cseréljem be a parasztot? [bástya, futó, ló, királynő]: ").strip().lower()
                        #translating the input to figures
                        if ans == "királynő":
                           fig == "queen"
                           break
                        elif ans == "bástya":
                           fig == "rook"
                           break
                        elif ans == "futó":
                           fig == "bishop"
                           break
                        elif ans == "ló":
                           fig == "knight"
                           break
                        else:
                           print("HIBA: nincs ilyen figura az opciók között!")

                  #it makes the change to the table
                  self.alterTable(self=self, nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, useCopyTable=useCopyTable)
                  return False
               
               else:
                  return self.stepError
            
            #This method deals with the rook
            elif fig == "rook" and playerColor == col:
               if self.rook_move(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, color=col, useCopyTable=useCopyTable):
                  self.alterTable(self=self, nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, useCopyTable=useCopyTable)
                  return False
               else:
                  return self.stepError
            
            #This method deals with the bishop
            elif fig == "bishop" and playerColor == col:
               if self.bishop_move(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, color=col, useCopyTable=useCopyTable):
                  self.alterTable(self=self, nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, useCopyTable=useCopyTable)
                  return False
               else:
                  return self.stepError
            
            #This method deals with the knight
            elif fig == "knight" and playerColor == col:
               if self.knight_move(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, color=col, useCopyTable=useCopyTable):
                  self.alterTable(self=self, nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, useCopyTable=useCopyTable)
                  return False
               else:
                  return self.stepError
            
            #This method deals with the queen
            elif fig == "queen" and playerColor == col:
               if self.queen_move(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, color=col, useCopyTable=useCopyTable):
                  self.alterTable(self=self, nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, useCopyTable=useCopyTable)
                  return False
               else:
                  return self.stepError
            
            #This method deals with the king
            elif fig == "king" and playerColor == col:
               if self.king_move(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, color=col, useCopyTable=useCopyTable):
                  #if the king is safe to step there
                  if not self.checkForCheck(self=self, x=nextX, y=nextY, col=col, useCopyTable=useCopyTable):
                     self.alterTable(self=self, nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, useCopyTable=useCopyTable)
                     
                     #Update the king's position
                     if useCopyTable:
                        if col == "black":
                           self.copyBlackKing["x"] = nextX
                           self.copyBlackKing["y"] = nextY
                        elif col  == "white":
                           self.copyWhiteKing["x"] = nextX
                           self.copyWhiteKing["y"] = nextY
                     
                     #if the we used the copyTable
                     else:
                        if col == "black":
                           self.blackKing["x"] = nextX
                           self.blackKing["y"] = nextY
                        elif col  == "white":
                           self.whiteKing["x"] = nextX
                           self.whiteKing["y"] = nextY
                     
                     #finally return False for no errors
                     return False
                  
                  #if the king can't get there due to check occurrence
                  else:
                     return self.stepError
               else:
                  return self.stepError
            
            #else
            else:
               return "Rossz színnel akarsz lépni"