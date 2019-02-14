from random import randint
import re

class GameManadgement():

   #PAWN
   """
   This method is for validating a pawn move
   """
   def pawn_move(self, nowX, nowY, nextX, nextY, color, useCopyTable=False):
      
      #if the pawn is BLACK
      if color == "black":

         #if the pawn moves 1 step forward
         if nextY == nowY + 1:

            #if it's a normal forward move
            if nextX == nowX:
               if self.checkTable(x=nextX, y=nextY, returnCol=True, useCopyTable=useCopyTable) == "":
                  return True
               else:
                  return False

            #if the pawn wants to kill
            elif (nextX == nowX -1) or (nextX == nowX + 1):
               if self.checkTable(x=nextX, y=nextY, returnCol=True, useCopyTable=useCopyTable) == "white":
                  return True
               else:
                  return False

         #if this is the first move of the (2 steps forward)
         elif nowY == 2 and nextY == nowY + 2 and nowX == nextX:
            if self.checkTable(x=nextX, y=nextY, returnCol=True, useCopyTable=useCopyTable) == "":
               return True
            else:
               return False
         
         #if the move is invalid
         else:
            return False

      
      #if the pawn is WHITE
      elif color == "white":

         #if the pawn moves 1 step forward
         if nextY == nowY - 1:
            
            #if it's a normal forward move
            if nextX == nowX:
               if self.checkTable(x=nextX, y=nextY, returnCol=True, useCopyTable=useCopyTable) == "":
                  return True
               else:
                  return False

            #if the pawn wants to kill
            elif (nextX == nowX -1) or (nextX == nowX + 1):
               if self.checkTable(x=nextX, y=nextY, returnCol=True, useCopyTable=useCopyTable) == "black":
                  return True
               else:
                  return False

         #if this is the first move of the (2 steps forward)
         elif nowY == 7 and nextY == nowY - 2 and nowX == nextX:
            if self.checkTable(x=nextX, y=nextY, returnCol=True, useCopyTable=useCopyTable) == "":
               return True
            else:
               return False
         
         #if the move is invalid
         else:
            return False


   
   #ROOK
   """
   This method is for validating the rook's move
   """
   def rook_move(self, nowX, nowY, nextX, nextY, color, useCopyTable=False):

      #rook moves up
      if nowX == nextX and nowY > nextY:
         y = nowY - 1
         while y != nextY:
            col = self.checkTable(x=nowX, y=y, returnCol=True, useCopyTable=useCopyTable)
            if bool(col):
               return False
            y -= 1
         col = self.checkTable(x=nowX, y=y, returnCol=True, useCopyTable=useCopyTable)
         if color != col:
            return True
         else:
            return False
      
      #rook moves down
      elif nowX == nextX and nowY < nextY:
         y = nowY + 1
         while y != nextY:
            col = self.checkTable(x=nowX, y=y, returnCol=True, useCopyTable=useCopyTable)
            if bool(col):
               return False
            y += 1
         col = self.checkTable(x=nowX, y=y, returnCol=True, useCopyTable=useCopyTable)
         if color != col:
            return True
         else:
            return False
      
      #rook moves right
      elif nowY == nextY and nowX < nextX:
         x = nowX + 1
         while x != nextY:
            col = self.checkTable(x=x, y=nowY, returnCol=True, useCopyTable=useCopyTable)
            if bool(col):
               return False
            x += 1
         col = self.checkTable(x=x, y=nowY, returnCol=True, useCopyTable=useCopyTable)
         if color != col:
            return True
         else:
            return False

      #rook moves left
      elif nowY == nextY and nowX > nextX:
         x = nowX - 1
         while x != nextY:
            col = self.checkTable(x=x, y=nowY, returnCol=True, useCopyTable=useCopyTable)
            if bool(col):
               return False
            x -= 1
         col = self.checkTable(x=x, y=nowY, returnCol=True, useCopyTable=useCopyTable)
         if color != col:
            return True
         else:
            return False

      #if the move is invalid
      else:
         return False
   

   #KNIGHT
   """
   This method is for validating the knight's move
   """
   def knight_move(self, nowX, nowY, nextX, nextY, color, useCopyTable=False):
      
      #gets the color ot the nextPosition field
      col = self.checkTable(x=nextX, y=nextY, returnCol=True, useCopyTable=useCopyTable)

      #validating the posible positions of the move
      #if it moves 1 up
      if nextY == nowY - 1:
         if nextX == nowX - 2 or nextX == nowX + 2:
            if col != color:
               return True
            else:
               return False
         else:
            return False

      #if it moves 2 up
      elif nextY == nowY - 2:
         if nextX == nowX - 1 or nextX == nowX + 1:
            if col != color:
               return True
            else:
               return False
         else:
            return False

      #if it moves 1 down
      elif nextY == nowY + 1:
         if nextX == nowX - 2 or nextX == nowX + 2:
            if col != color:
               return True
            else:
               return False
         else:
            return False

      #if it moves 2 down
      elif nextY == nowY + 2:
         if nextX == nowX - 1 or nextX == nowX + 1:
            if col != color:
               return True
            else:
               return False
         else:
            return False
      
      #if the move is invalid
      else:
         return False


   
   #BISHOP
   """
   This method is for validating the bishop's move
   """
   def bishop_move(self, nowX, nowY, nextX, nextY, color, useCopyTable=False):
      
      #getting the different between the Ys
      if nowY < nextY:
         y = nextY - nowY
      elif nowY > nextY:
         y = nowY - nextY
      else:
         return False

      #getting the different between the Xs
      if nowX < nextX:
         x = nextX - nowX
      elif nowX > nextX:
         x = nowX - nextX
      else:
         return False

      #if the move is valid
      if y == x:

         #move down and left
         if nextY > nowY and nextX < nowX:
            y = nowY + 1
            x = nowX - 1
            while y != nextY and x != nextX:
               if self.checkTable(x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != "":
                  return False
               else:
                  y += 1
                  x -= 1
            if self.checkTable(x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != color:
               return True
            else:
               return False
         
         #move down and right
         elif nextY > nowY and nextX > nowX:
            y = nowY + 1
            x = nowX + 1
            while y != nextY and x != nextX:
               if self.checkTable(x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != "":
                  return False
               else:
                  y += 1
                  x += 1
            if self.checkTable( x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != color:
               return True
            else:
               return False
         
         #move up and left
         elif nextY < nowY and nextX < nowX:
            y = nowY - 1
            x = nowX - 1
            while y != nextY and x != nextX:
               if self.checkTable(x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != "":
                  return False
               else:
                  y -= 1
                  x -= 1
            if self.checkTable(x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != color:
               return True
            else:
               return False
         
         #move up and right
         elif nextY < nowY and nextX > nowX:
            y = nowY - 1
            x = nowX + 1
            while y != nextY and x != nextX:
               if self.checkTable(x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != "":
                  return False
               else:
                  y -= 1
                  x += 1
            if self.checkTable(x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != color:
               return True
            else:
               return False
      
      #if the move is invalid
      else:
         return False

   
   #QUEEN
   """
   This method is for validating the queen's move
   """
   def queen_move(self, nowX, nowY, nextX, nextY, color, useCopyTable=False):

      #if the queen wants to move like a bishop
      if self.bishop_move(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, color=color, useCopyTable=useCopyTable):
         return True
      
      #if the queen wants to move like a rook
      elif self.rook_move(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, color=color, useCopyTable=useCopyTable):
         return True
      
      #if the move is invalid
      else:
         return False
         
   
   #KING
   """
   This method is for validating the king's move
   """
   def king_move(self, nowX, nowY, nextX, nextY, color, useCopyTable=False):
     
      # if the king moves left or right
      if (nextX == nowX - 1 or nextX == nowX + 1):
         if nextY == nowY or nextY == nowY + 1 or nextY == nowY + 1:
            if self.checkTable(x=nextX, y=nextY, returnCol=True, useCopyTable=useCopyTable) != color:
               return True
            else:
               return False
         else:
            return False

      #if the king wants to move up or down
      elif nextX == nowX:
         if nextY == nowY - 1 or nextY == nowY + 1:
            if self.checkTable(x=nextX, y=nextY, returnCol=True, useCopyTable=useCopyTable) != color:
               return True
            else:
               return False
         else:
            return False
      
      #if the move is invalid
      else:
         return False





   #These are the methods dealing with the game
   """
   #####################################################################################################################################
   """


   #These are kinds of error messages
   invalidInput = "HIBA: nem megfelelő paramétereket adott meg!"
   stepError = "HIBA: nem lehet a megadott lépést elvégezni!"
   checkError = "HIBA: királyod jelenleg sakkban van, meg kell szüntetned ezt az állapotot!"

   #This function creates a new game
   def __init__(self, player01, player02, color01, color02):

      #setting up the two player names and their colors
      self.players = dict(player01=player01, player02=player02, color01=color01, color02=color02)

      #Table
      """
      This is the table what the game uses to operate
       # Correct use of the table: self.table[y][x] ==> table[column][row]
       # The program also uses a variant of the table called copyTable is some methods
       * The table's elements are the columns [ Y ]
       * The elements's elements are the rows [ X ]
      """
      """
      self.table = [
         ("A","B","C","D","E","F","G","G"), #These are the row names
         ["1", "black_rook","black_knight","black_bishop","black_queen","black_king","black_bishop","black_knight","black_rook"],
         ["2", "black_pawn","black_pawn","black_pawn","black_pawn","black_pawn","black_pawn","black_pawn","black_pawn"],
         ["3", "","","","","","","",""],
         ["4", "","","","","","","",""],
         ["5", "","","","","","","",""],
         ["6", "","","","","","","",""],
         ["7", "white_pawn","white_pawn","white_pawn","white_pawn","white_pawn","white_pawn","white_pawn","white_pawn"],
         ["8", "white_rook","white_knight","white_bishop","white_queen","white_king","white_bishop","white_knight","white_rook"],
         ("A","B","C","D","E","F","G","G")
      ]
      """
      self.table = [
         ["A","B","C","D","E","F","G","G"], #These are the row names
         ["1", "black_rook","","","black_queen","black_king","black_bishop","black_knight","black_rook"],
         ["2", "black_pawn","black_pawn","black_pawn","","","black_pawn","black_pawn","black_pawn"],
         ["3", "","","black_knight","black_pawn","","","",""],
         ["4", "","","","","white_knight","","",""],
         ["5", "","","white_bishop","","white_pawn","","black_pawn",""],
         ["6", "","","white_knight","","","","",""],
         ["7", "white_pawn","white_pawn","white_pawn","white_pawn","","white_pawn","white_pawn","white_pawn"],
         ["8", "white_rook","","white_bishop","white_queen","white_king","","","white_rook"],
         ["A","B","C","D","E","F","G","G"]
      ]


      self.copyTable = self.table.copy()

      #These are the possible placeholders
      #These are on index 0 in the table's rows
      self.placeholders = ["1","2","3","4","5","6","7","8"]


      #King positions
      """
      These properties are holding the current positions of the kings
      # The program also uses two variants of these in some of the methods (copyBlackKingX && copyBlackKingY || copyWhiteKingX && copyWhiteKingY)
      * These must be updated when the king moves
      * The type of the X and Y must be in an integer
      """
      self.blackKing = {"x": 5, "y": 1}
      self.whiteKing = {"x": 5, "y": 8}


      #finally invoking the playerMove method
      #This will also return True is the game is over
      #return self.playerMove()
      self.playerMove()


   #PlayerMove method
   """
   This method deals with the choise of the player
   """
   def playerMove(self):

      #Printing the table
      """
      This code deals with the table printing
      """
      def printTable(self):
         #first we print 50 lines the make the previos steps disappear
         for i in range(50):
            print("")

         #these variables hold spaces
         fiveSpace = "     "
         twelveSpace = "            "

         #looping through the columns of the table
         for y in range(len(self.table)):

            #if it's not the first and last line
            if y != 0 and y != len(self.table) - 1:

               #printing the first two lines
               for i in range(1):
                  print(fiveSpace ,end="")
                  for j in range(8):
                     print("#" + twelveSpace, end="")
                  else:
                     print("#")

               #looping through the table
               #first it prints the color of the figures
               for i in range(1):
                  for x in range(len(self.table[y])):

                     pos = self.table[y][x]

                     #if there's a figure on the position
                     if pos != "" and pos not in self.placeholders:
                        
                        position = re.split("_", pos)
                        col = position[0]

                        #setting the color to hungarian
                        if col == "black":
                           col = "Fekete"
                        elif col == "white":
                           col = "Fehér"
                        
                        print("#" + col.center(12), end="")

                     #if the table's position is empty
                     elif pos == "":
                        print("#" + twelveSpace, end="")

                     #if the position is a placeholder
                     elif pos in self.placeholders:
                        print(pos.center(5), end="")

                  #if we reach the end of the line
                  else:
                     print("#" + self.table[y][0].center(5))
               
               #then is prints the name of the figures
               else:
                  for x in range(len(self.table[y])):

                     pos = self.table[y][x]

                     #if there's a figure on the position
                     if pos != "" and pos not in self.placeholders:
                        
                        position = re.split("_", pos)
                        fig = position[1]

                        #setting the figure to hungarian
                        if fig == "pawn":
                           fig = "Paraszt"
                        elif fig == "rook":
                           fig = "Bástya"
                        elif fig == "knight":
                           fig = "Ló"
                        elif fig == "bishop":
                           fig = "Futó"
                        elif fig == "queen":
                           fig = "Királynő"
                        elif fig == "king":
                           fig = "Király"
                        
                        print("#" + fig.center(12), end="")

                     #if the table's position is empty
                     elif pos == "":
                        print("#" + twelveSpace, end="")

                     #if the position is a placeholder
                     elif pos in self.placeholders:
                        print(fiveSpace, end="")

                  #if we reach the end of the line
                  else:
                     print("#")

                  
               #printing the last two lines
               for i in range(1):
                  print(fiveSpace ,end="")
                  for j in range(8):
                     print("#" + twelveSpace, end="")
                  else:
                     print("#")

               else:
                  print(fiveSpace, end="")
                  for i in range(105):
                     print("#", end="")
                  else:
                     print("")


            #if it is the first and last line
            else:
               
               #printing the column number
               for x in range(len(self.table[y])):

                  if x == 0:
                     print(fiveSpace, end="")

                  print(" " + self.table[y][x].center(12), end="")

               else:

                  #if it is the table's first column
                  if y == 0:

                     #printing a row of #s
                     print("\n" + fiveSpace, end="")
                     for i in range(105):
                        print("#", end="")
                     else:
                        print("")

      
      #This method asks for the input
      def askPlayer(self, playerColor, useCopy=False):
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
                  result = self.makeStep(nowPos=nowPos, nextPos=nextPos, playerColor=playerColor, useCopyTable=useCopy)
         
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

         #Printing the table
         printTable(self=self)

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
         print("\n\n{} következik (színe: {}):".format(playerName, col))
         
         #if there is a check on the user's king
         if self.checkForCheck(kingX=kingX, kingY=kingY, col=playerColor, useCopyTable=False):
            
            #if it is checkmate
            if self.checkForCheckmate(kingX=kingX, kingY=kingY, col=playerColor):
               
               #first print 50 lines to make the previous steps disappear
               for i in range(50):
                  print("")

               #creating the gameOver filename
               fileName = "gg" + str(randint(1,3)) + ".txt"

               #then priniting the GAME OVER SIGN
               with open(fileName, "r", encoding="utf8") as f:
                  print(f.read())

               #printing the final result and returning True to indicate this is the end of the game
               print("\nA győztes: {} (színe: {})\nGratulálunk a győzelemhez!\n".format(playerName, playerColor))
               return False

            #if it's a normal check
            else:
               
               while True:

                  #making the copyTable
                  self.copyTable.clear()
                  self.copyTable = self.table.copy()

                  #making the copies of the king's position
                  #it is used for updating the king's finaly position
                  if playerColor == "white":
                     self.copyWhiteKing = dict()
                     self.copyWhiteKing["x"] = kingX
                     self.copyWhiteKing["y"] = kingY

                  elif playerColor == "black":
                     self.copyBlackKing = dict()
                     self.copyBlackKing["x"] = kingX
                     self.copyBlackKing["y"] = kingY
                  
                  #letting the user know that his king is in a check position
                  print("\nSakkot kaptál! Meg kell szüntetned ezt az állapotot!")
                  askPlayer(self=self, playerColor=playerColor, useCopy=True)

                  #if the check is over
                  if not self.checkForCheck(kingX=kingX, kingY=kingY, col=playerColor, useCopyTable=True):
                     
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
                     return True
         
         #if there is no check on the user's king
         else:
            
            #asking the user for an input
            askPlayer(self=self, playerColor=playerColor, useCopy=False)
            return True

      
      #until the end of the game
      while True:

         #WHITE PLAYER
         #if this is the end of the game
         if not nextPlayer(self=self, playerName=self.players['player01'], playerColor=self.players['color01']):
            break

         #BLACK PLAYER
         #if this is the end of the game
         if not nextPlayer(self=self, playerName=self.players['player02'], playerColor=self.players['color02']):
            break


      #finally when the game finished we return True
      #return True




   #CheckForCheck method
   """
   This method checks if the user's king got an attack. The method returns:
    # This method is also used to check if any of the user's figure could take the king's checker down
    # The otherX and otherY variables are the positions of a condicional figure move [ optional ]

    * True  - if the king is in check or could be
    * False - if the king is safe 
   """
   #MÉG VAN MIT RAJTA JAVÍTANI
   def checkForCheck(self, kingX, kingY, col, returnCheckerPos=False, useCopyTable=False):

      #if we want to use the self.copyTable
      if useCopyTable:

         #looping through the self.copyTable
         for y in range(1,9):
            for x in range(1,9):

               #this one could change to self.copyTable
               #this one could change to self.table
               #this is the value of the position
               position = self.copyTable[y][x]

               #if the position is not empty and it is not a placeholder
               if position != "" and position not in self.placeholders:

                  #getting the value of the position
                  pos = re.split("_", position)

                  #This sets the color of the opponent
                  #if the king's color is white
                  if col == "white" and pos[0] == "black":
                     opponentColor = "black"
                  #if the king's color is black
                  elif col == "black" and pos[0] == "white":
                     opponentColor = "white"

                  #Checking the possible enemy moves againts the king
                  if pos[1] == "pawn" and pos[0] != col:
                     #if the pawn could take the king down
                     if self.pawn_move(nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=opponentColor, useCopyTable=useCopyTable):
                        #validating what to return
                        if returnCheckerPos:
                           checkerPos = {"x": int(x), "y": int(y)}
                           return checkerPos
                        else:
                           return True
               
                  elif pos[1] == "rook" and pos[0] != col:
                     #if the rook could take the king down
                     if self.rook_move(nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=opponentColor, useCopyTable=useCopyTable):
                        #validating what to return
                        if returnCheckerPos:
                           checkerPos = {"x": int(x), "y": int(y)}
                           return checkerPos
                        else:
                           return True
                  
                  elif pos[1] == "knight" and pos[0] != col:
                     #if the knight could take the king down
                     if self.knight_move(nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=opponentColor, useCopyTable=useCopyTable):
                        #validating what to return
                        if returnCheckerPos:
                           checkerPos = {"x": int(x), "y": int(y)}
                           return checkerPos
                        else:
                           return True
                  
                  elif pos[1] == "bishop" and pos[0] != col:
                     #if the bishop could take the king down
                     if self.bishop_move(nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=opponentColor, useCopyTable=useCopyTable):
                        #validating what to return
                        if returnCheckerPos:
                           checkerPos = {"x": int(x), "y": int(y)}
                           return checkerPos
                        else:
                           return True
                  
                  elif pos[1] == "queen" and pos[0] != col:
                     #if the queen could take the king down
                     if self.queen_move(nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=opponentColor, useCopyTable=useCopyTable):
                        #validating what to return
                        if returnCheckerPos:
                           checkerPos = {"x": int(x), "y": int(y)}
                           return checkerPos
                        else:
                           return True
                  
                  elif pos[1] == "king" and pos[0] != col:
                     #if the king could take the king down
                     if self.king_move(nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=opponentColor, useCopyTable=useCopyTable):
                        #validating what to return
                        if returnCheckerPos:
                           checkerPos = {"x": int(x), "y": int(y)}
                           return checkerPos
                        else:
                           return True
         
         #if the king isn't in a check position
         else:
            return False


      #if we want to use the table
      else:
         
         #looping through the self.table
         for y in range(1,9):
            for x in range(1,9):

               #this is the value of the position
               position = self.table[y][x]

               #if the position is not empty and it isn't a placeholder
               if position != "" and position not in self.placeholders:

                  #getting the value of the position
                  pos = re.split("_", position)

                  #This sets the color of the user
                  #if the king's color is white
                  if col == "white" and pos[0] == "black":
                     opponentColor = "black"
                  
                  #if the king's color is black
                  elif col == "black" and pos[0] == "white":
                     opponentColor = "white"

                  #Checking the possible enemy moves againts the king
                  if pos[1] == "pawn" and pos[0] != col:
                     #if the pawn could take the king down
                     if self.pawn_move(nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=opponentColor, useCopyTable=useCopyTable):
                        #validating what to return
                        if returnCheckerPos:
                           checkerPos = {"x": int(x), "y": int(y)}
                           return checkerPos
                        else:
                           return True
               
                  elif pos[1] == "rook" and pos[0] != col:
                     #if the rook could take the king down
                     if self.rook_move(nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=opponentColor, useCopyTable=useCopyTable):
                        #validating what to return
                        if returnCheckerPos:
                           checkerPos = {"x": int(x), "y": int(y)}
                           return checkerPos
                        else:
                           return True
                  
                  elif pos[1] == "knight" and pos[0] != col:
                     #if the knight could take the king down
                     if self.knight_move(nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=opponentColor, useCopyTable=useCopyTable):
                        #validating what to return
                        if returnCheckerPos:
                           checkerPos = {"x": int(x), "y": int(y)}
                           return checkerPos
                        else:
                           return True
                  
                  elif pos[1] == "bishop" and pos[0] != col:
                     #if the bishop could take the king down
                     if self.bishop_move(nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=opponentColor, useCopyTable=useCopyTable):
                        #validating what to return
                        if returnCheckerPos:
                           checkerPos = {"x": int(x), "y": int(y)}
                           return checkerPos
                        else:
                           return True
                  
                  elif pos[1] == "queen" and pos[0] != col:
                     #if the queen could take the king down
                     if self.queen_move(nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=opponentColor, useCopyTable=useCopyTable):
                        #validating what to return
                        if returnCheckerPos:
                           checkerPos = {"x": int(x), "y": int(y)}
                           return checkerPos
                        else:
                           return True
                  
                  elif pos[1] == "king" and pos[0] != col:
                     #if the king could take the king down
                     if self.king_move(nowX=int(x), nowY=int(y), nextX=kingX, nextY=kingY, color=opponentColor, useCopyTable=useCopyTable):
                        #validating what to return
                        if returnCheckerPos:
                           checkerPos = {"x": int(x), "y": int(y)}
                           return checkerPos
                        else:
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
            if self.king_move(nowX=kingX, nowY=kingY, nextX=nextX, nextY=nextY, color=col, useCopyTable=True):

               #making the change to the copyTable
               self.alterTable(nowX=kingX, nowY=kingY, nextX=nextX, nextY=nextY, col=col, fig="king", useCopyTable=True)
            
               #if the king is safe with that move ==> the game is not over yet
               if not self.checkForCheck(kingX=nextX, kingY=nextY, col=col, useCopyTable=True):
                  self.copyTable.clear()
                  return False


      #if the king could not get out from the check by itself
      else:

         #creating the copyTable
         self.copyTable = self.table.copy()

         #getting the checker's position (the figure who's checking our king) 
         pos = self.checkForCheck(kingX=kingX, kingY=kingY, col=col, returnCheckerPos=True, useCopyTable=True)

         #getting the color of the opponent
         if col == "white":
            enemyCol = "black"
         elif col == "black":
            enemyCol = "white"

         #checking if one of the user's figure could take the checker down
         if self.checkForCheck(kingX=pos["x"], kingY=pos["y"], col=enemyCol, useCopyTable=True):
            return False


         #if the user couldn't take down the checker
         else:

            #creating the copyTable
            self.copyTable = self.table.copy()

            #this will hold the positions from the checker to the king
            steps = []

            #if one of the user's figures could protect the king
            #if the opponent's figure is checking our king via a rook_move
            if self.rook_move(nowX=pos["x"], nowY=pos["y"], nextX=kingX, nextY=kingY, color=enemyCol, useCopyTable=True):

               #validating the steps
               #if the rook_move is horizontal
               if pos["y"] == kingY:
                  
                  #if it goes left 
                  if pos["x"] > kingX:
                     x = pos["x"] - 1
                     while x != kingX:
                        steps.append(dict(x=x, y=pos["y"]))
                        x -= 1

                  #if it goes right
                  elif pos["x"] < kingX:
                     x = pos["x"] + 1
                     while x != kingX:
                        steps.append(dict(x=x, y=pos["y"]))
                        x += 1

               #if the rook_move is vertical
               elif pos["x"] == kingX:

                  #if it goes up
                  if pos["y"] > kingY:
                     y = pos["y"] - 1
                     while x != kingX:
                        steps.append(dict(x=pos["x"], y=y))
                        y -= 1

                  #if it goes down
                  elif pos["y"] < kingY:
                     y = pos["y"] + 1
                     while x != kingX:
                        steps.append(dict(x=pos["x"], y=y))
                        y += 1


               #validating if any of the user's figures could get between it's king and the checker
               for i in range(len(steps)):
                  if self.checkForCheck(kingX=steps[i]["x"], kingY=steps[i]["y"], col=col, useCopyTable=True):
                     return False
               
               #else it is a checkmate (game over)
               else:
                  return True

            #if the opponent's figure is checking our king via a bishop_move
            elif self.bishop_move(nowX=pos["x"], nowY=pos["y"], nextX=kingX, nextY=kingY, color=enemyCol, useCopyTable=True):
                  
               nowY = pos["y"]
               nowX = pos["x"]
               nextY = kingY
               nextX = kingX

               #creating the steps
               #move down and left
               if nextY > nowY and nextX < nowX:
                  y = nowY + 1
                  x = nowX - 1
                  while y != nextY and x != nextX:
                     steps.append(dict(x=x, y=y))
                     y += 1
                     x -= 1
               
               #move down and right
               elif nextY > nowY and nextX > nowX:
                  y = nowY + 1
                  x = nowX + 1
                  while y != nextY and x != nextX:
                     steps.append(dict(x=x, y=y))
                     y += 1
                     x += 1
               
               #move up and left
               elif nextY < nowY and nextX < nowX:
                  y = nowY - 1
                  x = nowX - 1
                  while y != nextY and x != nextX:
                     steps.append(dict(x=x, y=y))
                     y -= 1
                     x -= 1
               
               #move up and right
               elif nextY < nowY and nextX > nowX:
                  y = nowY - 1
                  x = nowX + 1
                  while y != nextY and x != nextX:
                     steps.append(dict(x=x, y=y))
                     y -= 1
                     x += 1
               
               #validating if any of the user's figures could get between it's king and the checker
               for i in range(len(steps)):
                  if self.checkForCheck(kingX=steps[i]["x"], kingY=steps[i]["y"], col=col, useCopyTable=True):
                     return False

               #else it is a checkmate (game over)
               else:
                  return True
            
            #else it is a checkmate (game over)
            else:
               return True



   #FigureSwitch Method
   """
   This method is used for validating a pawn switch
    * True  - if the pawn is in switch position
    * False - if the pawn is not in switch position
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
    * The return value depends on the input parameters
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
            #print(pos)
            print("y: {}, x: {}".format(y, x))
            print(self.table[y+1][x])
            return pos[1]
         else:
            return ""


   #Mapping method
   """
   This method maps the letter form position input to numbers.
   """
   def mapNumberToX(self, letter):
      abc = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
      for y, value in abc.items():
         if letter == y:
            return value



   #This function alters the table if a move could go down
   """
   This method makes the change to the table / copyTable
   """
   def alterTable(self, nowX, nowY, nextX, nextY, col, fig, useCopyTable=False):
      if useCopyTable:
         self.copyTable[nowY][nowX] = ""
         self.copyTable[nextY][nextX] = col + "_" + fig
      else:
         self.table[nowY][nowX] = ""
         self.table[nextY][nextX] = col + "_" + fig



   #MakeStep method
   """
   This method validates the user input for the positions. This method returns:
    * False - if the move is made (this is because of how the player_move works)
    * else  - returns an error message
   """
   def makeStep(self, nowPos, nextPos, playerColor, useCopyTable=False):

      #Getting the user's input
      a = re.search("[a-h]", nowPos) #nowColumn
      b = re.search("[1-8]", nowPos) #nextRow
      c = re.search("[a-h]", nextPos) #nextColumn
      d = re.search("[1-8]", nextPos) #nextRow


      #Validating the user's input
      #If the user didn't give the correct input
      if a == None or b == None or c == None or d == None:
         return self.invalidInput
      
      #if the input is correct
      else:

         #Converting the user's input
         nowX = int(self.mapNumberToX(a.group()))
         nowY = int(b.group())
         nextX = int(self.mapNumberToX(c.group()))
         nextY = int(d.group())

         #If the starting and ending position is the same
         if nowX == nextX and nowY == nextY:
            return self.stepError
         
         else:
            #These variables would hold the user's figurename and the it's color
            fig = self.checkTable(x=nowX, y=nowY, returnFig=True, useCopyTable=useCopyTable)
            col = self.checkTable(x=nowX, y=nowY, returnCol=True, useCopyTable=useCopyTable)
            
            #This method deals with the pawn
            if fig == "pawn" and playerColor == col:
               if self.pawn_move(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, color=col, useCopyTable=useCopyTable):
                  
                  #if the pawn is in a figure-switch position
                  if self.pawnSwitch(nextY=nextY, col=col):
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
                  self.alterTable(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, useCopyTable=useCopyTable)
                  return False
               
               else:
                  return self.stepError
            
            #This method deals with the rook
            elif fig == "rook" and playerColor == col:
               if self.rook_move(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, color=col, useCopyTable=useCopyTable):
                  self.alterTable(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, useCopyTable=useCopyTable)
                  return False
               else:
                  return self.stepError
            
            #This method deals with the bishop
            elif fig == "bishop" and playerColor == col:
               if self.bishop_move(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, color=col, useCopyTable=useCopyTable):
                  self.alterTable(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, useCopyTable=useCopyTable)
                  return False
               else:
                  return self.stepError
            
            #This method deals with the knight
            elif fig == "knight" and playerColor == col:
               if self.knight_move(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, color=col, useCopyTable=useCopyTable):
                  self.alterTable(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, useCopyTable=useCopyTable)
                  return False
               else:
                  return self.stepError
            
            #This method deals with the queen
            elif fig == "queen" and playerColor == col:
               if self.queen_move(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, color=col, useCopyTable=useCopyTable):
                  self.alterTable( nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, useCopyTable=useCopyTable)
                  return False
               else:
                  return self.stepError
            
            #This method deals with the king
            elif fig == "king" and playerColor == col:
               if self.king_move(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, color=col, useCopyTable=useCopyTable):
                  #if the king is safe to step there
                  if not self.checkForCheck(kingX=nextX, kingY=nextY, col=col, useCopyTable=useCopyTable):
                     self.alterTable(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, useCopyTable=useCopyTable)
                     
                     #Update the king's position
                     #if the we used the copyTable
                     if useCopyTable:
                        if col == "black":
                           self.copyBlackKing = dict()
                           self.copyBlackKing["x"] = nextX
                           self.copyBlackKing["y"] = nextY
                        elif col  == "white":
                           self.copyWhiteKing = dict()
                           self.copyWhiteKing["x"] = nextX
                           self.copyWhiteKing["y"] = nextY
                     
                     #if the we used the table
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
               
               #if the king can't get there
               else:
                  return self.stepError
            
            #if we can't make any move (if the position is empty or it's got the wrong color)
            else:
               return self.stepError