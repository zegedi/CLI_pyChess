#!/usr/bin/env python3

from pathlib import Path
from languages.languages import *
from colorama import init, Fore, Back, Style
from random import randint
from copy import deepcopy
import sys
import os
import re

class GameManadgement():

   #PAWN
   """
   This method is for validating a pawn move
   """
   def pawn_move(self, nowX, nowY, nextX, nextY, color, useCopyTable=False):

      #this method check if a pawn could perform an en_passant kill
      def checkForEnPassant(self, nextX, nextY, color):
         for i in range(len(self.en_passant)):
            if nextY == self.en_passant[i]["realY"] and nextX == self.en_passant[i]["realX"] and color != self.en_passant[i]["col"]:
               return True
         else:
            return False
      
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
               #if it is a normal kill
               if self.checkTable(x=nextX, y=nextY, returnCol=True, useCopyTable=useCopyTable) == "white":
                  return True
               else:
                  #if it is an en_passnat kill
                  if checkForEnPassant(self=self, nextX=nextX, nextY=nextY, color=color):
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
               #if it is a normal kill
               if self.checkTable(x=nextX, y=nextY, returnCol=True, useCopyTable=useCopyTable) == "black":
                  return True
               else:
                  #if it is an en_passnat kill
                  if checkForEnPassant(self=self, nextX=nextX, nextY=nextY, color=color):
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

      #if the king wants to castle
      elif (nextX == nowX - 2 or nextX == nowX + 2) and nextY == nowY:

         #if the king is not in a check position
         if not self.checkForCheck(kingX=nowX, kingY=nowY, col=color):
            
            #if the king is white
            if color == "black":
               
               #if the king wants to go left (plus the king and the rook didn't moved yet)
               if nextX == nowX - 2 and not self.blackCastling["kingMoved"] and not self.blackCastling["leftRookMoved"]:

                  x = nowX - 1
                  while x != nextX - 2:
                     posCol = self.checkTable(x=x, y=nowY, returnCol=True)
                     if posCol != "":
                        return False
                     else:
                        if x == nextX - 1:
                           x += 1
                        
                        else:
                           #if the king is safe to go there
                           if not self.checkForCheck(kingX=x, kingY=nowY, col=color):
                              x += 1
                           #if the king could not go there due to check occurense
                           else:
                              return False

                  #finally if everything is right
                  return True

               #if the king wants go right (plus the king and the rook didn't moved yet)
               elif nextX == nowX + 2 and not self.blackCastling["kingMoved"] and not self.blackCastling["rightRookMoved"]:
                  
                  #checking if there is nothing between the figures
                  x = nowX + 1
                  while x != nextX + 1:
                     posCol = self.checkTable(x=x, y=nowY, returnCol=True)
                     if posCol != "":
                        return False
                     else:
                        #if the king is safe to go there
                        if not self.checkForCheck(kingX=x, kingY=nowY, col=color):
                           x += 1
                        #if the king could not go there due to check occurense
                        else:
                           return False

                  #finally if everything is right
                  return True

               #if the figures moved already
               else:
                  return False

            #if the king is black
            elif color == "white":

               #if the king wants to go left (plus the king and the rook didn't moved yet)
               if nextX == nowX - 2 and not self.whiteCastling["kingMoved"] and not self.whiteCastling["leftRookMoved"]:

                  x = nowX - 1
                  while x != nextX - 2:
                     posCol = self.checkTable(x=x, y=nowY, returnCol=True)
                     if posCol != "":
                        return False
                     else:
                        if x == nextX - 1:
                           x += 1
                        
                        else:
                           #if the king is safe to go there
                           if not self.checkForCheck(kingX=x, kingY=nowY, col=color):
                              x += 1
                           #if the king could not go there due to check occurense
                           else:
                              return False

                  #finally if everything is right
                  return True

               #if the king wants go right (plus the king and the rook didn't moved yet)
               elif nextX == nowX + 2 and not self.whiteCastling["kingMoved"] and not self.whiteCastling["rightRookMoved"]:
                  
                  #checking if there is nothing between the figures
                  x = nowX + 1
                  while x != nextX + 1:
                     posCol = self.checkTable(x=x, y=nowY, returnCol=True)
                     if posCol != "":
                        return False
                     else:
                        #if the king is safe to go there
                        if not self.checkForCheck(kingX=x, kingY=nowY, col=color):
                           x += 1
                        #if the king could not go there due to check occurense
                        else:
                           return False

                  #finally if everything is right
                  return True

               #if the figures moved already
               else:
                  return False

         #if the king is in a check position
         else:
            return False

      #if the move is invalid
      else:
         return False





   #These are the methods dealing with the game
   """
   #####################################################################################################################################
   """

   #This function creates a new game
   def __init__(self, player01, player02, color01, color02, lang):

      #This section sets up colorama
      init(autoreset=True)


      #Setting up the two player names and their colors
      self.players = dict(player01=player01, player02=player02, color01=color01, color02=color02)

      #Table
      """
      This is the table what the game uses to operate
       # Correct use of the table: self.table[y][x] ==> table[column][row]
       # The program also uses a variant of the table called copyTable is some methods
       * The table's elements are the columns [ Y ]
       * The elements's elements are the rows [ X ]
      """
      self.table = [
         ("A","B","C","D","E","F","G","H"), #These are the row names
         ["8", "black_rook","black_knight","black_bishop","black_queen","black_king","black_bishop","black_knight","black_rook"],
         ["7", "black_pawn","black_pawn","black_pawn","black_pawn","black_pawn","black_pawn","black_pawn","black_pawn"],
         ["6", "","","","","","","",""],
         ["5", "","","","","","","",""],
         ["4", "","","","","","","",""],
         ["3", "","","","","","","",""],
         ["2", "white_pawn","white_pawn","white_pawn","white_pawn","white_pawn","white_pawn","white_pawn","white_pawn"],
         ["1", "white_rook","white_knight","white_bishop","white_queen","white_king","white_bishop","white_knight","white_rook"],
         ("A","B","C","D","E","F","G","H")
      ]

      #This is the copy of the table
      self.copyTable = deepcopy(self.table)

      #These are the possible placeholders
      #These are on index 0 in the table's rows
      self.placeholders = ["1","2","3","4","5","6","7","8"]

      #This variable holds the number of the round since the start 
      self.roundCount = 1

      #This list holds the values of an en_passant position
      """
      This list holds additional dictionaries in itself which contain:
       # expire - in which round will the value expire
       # tableX - this is the pawn's X position on the table
       # tableY - this is the pawn's Y position on the table
       # realX  - this is the pawn's fictional X position
       # realY  - this is the pawn's fictional Y position
       # col    - this is the color of the pawn
      """
      self.en_passant = list()

      #This variable holds how much round went off to the 
      self.fifty_move = 1
      
      #Castling variables
      """
      These dicts are holding if the figures are moved or not
      """
      self.blackCastling = {"kingMoved": False, "leftRookMoved": False, "rightRookMoved": False}
      self.whiteCastling = {"kingMoved": False, "leftRookMoved": False, "rightRookMoved": False}
      self.copyBlackCastling = dict()
      self.copyWhiteCastling = dict()

      #King positions
      """
      These properties are holding the current positions of the kings
      # The program also uses two variants of these in some of the methods (copyBlackKing || copyWhiteKing)
      * These must be updated when the king moves
      * The type of the X and Y must be in an integer
      """
      self.blackKing = {"x": 5, "y": 1}
      self.whiteKing = {"x": 5, "y": 8}
      self.copyBlackKing = dict()
      self.copyWhiteKing = dict()


      #Setting up the language of the game
      #Hungarian
      if lang == "magyar":
         self.lang = Hungarian()

      #English (US)
      elif lang == "english":
         self.lang = English()

      #Default (English)
      else:
         self.lang = English()


      #These are kinds of error messages
      self.invalidInput = self.lang.invalidInput
      self.stepError = self.lang.stepError
      self.checkError = self.lang.checkError

      #finally invoking the playerMove method
      self.playerMove()



   #PlayerMove method
   """
   This method deals with the choise of the player
   """
   def playerMove(self):

      #This method prints a message when the game is finished
      def gameOver(self, player="", col="", otherPlayer="", otherCol=""):

         #first print 50 lines to make the previous steps disappear
         for i in range(60):
            print("")

         #then priniting the GAME OVER SIGN
         try:
            #creating the gameOver filename
            folder = os.path.dirname(os.path.abspath(__file__))
            fileName = "gg" + str(randint(1,3)) + ".txt"
            path = Path(folder, fileName)

            with open(path, "r", encoding="utf8") as f:
               print(f.read())
         except:
            print("GAME OVER!\n\n")

         #printing the final result and returning False to indicate this is the end of the game
         #if player01 won
         if player != "" and col != "" and otherPlayer == "" and otherCol == "":
            print(self.lang.checkmateMessage.format(player, col))
         
         #if player02 won
         elif player == "" and col == "" and otherPlayer != "" and otherCol != "":
            print(self.lang.checkmateMessage.format(otherPlayer, otherCol))

         #if it's a draw
         else:
            print(self.lang.drawMessage)



      #This method print out the current table
      def printTable(self):

         #This method creates the padding around the fig and col
         """
         This method creates the space around the elements
         """
         def addPadding(self, element):

            #specify the needed padding
            padding = 10 - len(element)

            pad = ""
            rest = ""

            for i in range(padding // 2):
               pad += " "

            element = pad + element + pad
            
            #if there should be more padding added
            if padding % 2 != 0:
               r = padding % 2
               for i in range(r):
                  rest += " "
            else:
               rest = ""

            return element + rest


         #first we print 40 lines the make the previos steps disappear
         for i in range(40):
            print("")

         #these variables hold spaces
         fiveSpace = "     "
         tenSpace = "          "

         whiteBg = Back.WHITE + Style.DIM
         blackBg = Back.BLACK

         #looping through the columns of the table
         for y in range(len(self.table)):

            #if it's not the first and last line
            if y != 0 and y != len(self.table) - 1:

               #printing the padding line on the top
               print(fiveSpace + "#",end="")
               for x in range(1, len(self.table[y])):
                  if y % 2 != 0:
                     if x % 2 != 0:
                        print(whiteBg + tenSpace, end="")
                     else:
                        print(blackBg + tenSpace, end="")
                  else:
                     if x % 2 != 0:
                        print(blackBg + tenSpace, end="")
                     else:
                        print(whiteBg + tenSpace, end="")
               else:
                  print("#")

               #looping through the table
               #first it prints the color of the figures
               for x in range(len(self.table[y])):

                  pos = self.table[y][x]

                  #if there's a figure on the position
                  if pos != "" and pos not in self.placeholders:
                     
                     position = re.split("_", pos)
                     col = position[0]

                     #setting the color to hungarian
                     if col == "black":
                        col = Fore.RED + Style.BRIGHT + addPadding(self=self, element=self.lang.black).upper()
                     elif col == "white":
                        col = Fore.GREEN + Style.BRIGHT + addPadding(self=self, element=self.lang.white).lower()

                     if y % 2 != 0:
                        if x % 2 != 0:
                           print(whiteBg + col, end="")
                        else:
                           print(blackBg + col, end="")
                     else:
                        if x % 2 != 0:
                           print(blackBg + col, end="")
                        else:
                           print(whiteBg + col, end="")

                  #if the table's position is empty
                  elif pos == "":
                     if y % 2 != 0:
                        if x % 2 != 0:
                           print(whiteBg + tenSpace, end="")
                        else:
                           print(blackBg + tenSpace, end="")
                     else:
                        if x % 2 != 0:
                           print(blackBg + tenSpace, end="")
                        else:
                           print(whiteBg + tenSpace, end="")

                  #if the position is a placeholder
                  elif pos in self.placeholders:
                     print(pos.center(5) + "#", end="")

               #if we reach the end of the line
               else:
                  print("#" + self.table[y][0].center(5))
               
               
               #then is prints the name of the figures
               for x in range(len(self.table[y])):

                  pos = self.table[y][x]

                  #if there's a figure on the position
                  if pos != "" and pos not in self.placeholders:
                     
                     position = re.split("_", pos)
                     col = position[0]
                     fig = position[1]

                     #setting the figure to hungarian
                     if fig == "pawn":
                        if col == "black":
                           fig = Fore.RED + Style.BRIGHT + addPadding(self=self, element=self.lang.pawn).upper()
                        else:
                           fig = Fore.GREEN + Style.BRIGHT + addPadding(self=self, element=self.lang.pawn).lower()
                     
                     elif fig == "rook":
                        if col == "black":
                           fig = Fore.RED + Style.BRIGHT + addPadding(self=self, element=self.lang.rook).upper()
                        else:
                           fig = Fore.GREEN + Style.BRIGHT + addPadding(self=self, element=self.lang.rook).lower()
                     
                     elif fig == "knight":
                        if col == "black":
                           fig = Fore.RED + Style.BRIGHT + addPadding(self=self, element=self.lang.knight).upper()
                        else:
                           fig = Fore.GREEN + Style.BRIGHT + addPadding(self=self, element=self.lang.knight).lower()
                     
                     elif fig == "bishop":
                        if col == "black":
                           fig = Fore.RED + Style.BRIGHT + addPadding(self=self, element=self.lang.bishop).upper()
                        else:
                           fig = Fore.GREEN + Style.BRIGHT + addPadding(self=self, element=self.lang.bishop).lower()
                     
                     elif fig == "queen":
                        if col == "black":
                           fig = Fore.RED + Style.BRIGHT + addPadding(self=self, element=self.lang.queen).upper()
                        else:
                           fig = Fore.GREEN + Style.BRIGHT + addPadding(self=self, element=self.lang.queen).lower()
                     
                     elif fig == "king":
                        if col == "black":
                           fig = Fore.RED + Style.BRIGHT + addPadding(self=self, element=self.lang.king).upper()
                        else:
                           fig = Fore.GREEN + Style.BRIGHT + addPadding(self=self, element=self.lang.king).lower()

                     #validating the position's background color
                     if y % 2 != 0:

                        if x % 2 != 0:
                           print(whiteBg + fig, end="")
                        else:
                           print(blackBg + fig, end="")
                     else:
                        if x % 2 != 0:
                           print(blackBg + fig, end="")
                        else:
                           print(whiteBg + fig, end="")

                  #if the table's position is empty
                  elif pos == "":
                     if y % 2 != 0:
                        if x % 2 != 0:
                           print(whiteBg + tenSpace, end="")
                        else:
                           print(blackBg + tenSpace, end="")
                     else:
                        if x % 2 != 0:
                           print(blackBg + tenSpace, end="")
                        else:
                           print(whiteBg + tenSpace, end="")

                  #if the position is a placeholder
                  elif pos in self.placeholders:
                     print(fiveSpace + "#", end="")

               #if we reach the end of the line
               else:
                  print("#")

                  
               #printing the padding line on the bottom
               print(fiveSpace + "#", end="")
               for x in range(1, len(self.table[y])):
                  if y % 2 != 0:
                     if x % 2 != 0:
                        print(whiteBg + tenSpace, end="")
                     else:
                        print(blackBg + tenSpace, end="")
                  else:
                     if x % 2 != 0:
                        print(blackBg + tenSpace, end="")
                     else:
                        print(whiteBg + tenSpace, end="")
               else:
                  print("#")
                  
                  #if it was the last line of the table
                  if y == len(self.table)-2:

                     #printing a row of #s
                     print(fiveSpace, end="")
                     for i in range(82):
                        print("#", end="")
                     else:
                        print("")


            #if it is the first and last line
            else:
               
               #printing the column number
               for x in range(len(self.table[y])):

                  #if it is the first item of the row
                  if x == 0:
                     print(fiveSpace, end="")

                  print(" " + self.table[y][x].center(9), end="")

               else:

                  #if it is the table's first column
                  if y == 0:

                     #printing a row of #s
                     print("\n" + fiveSpace, end="")
                     for i in range(82):
                        print("#", end="")
                     else:
                        print("")

      
      #This method asks for the input
      def askPlayer(self, playerName, playerColor, otherPlayer, otherColor, useCopy=False):
         while True:
            nowPos = input(self.lang.fromMessage).strip().lower()

            #Checking if the nowPos is a special command
            #if the player is given up
            if nowPos == "giveup":
               print("")
               while True:
                  ans = input(self.lang.giveupMessage).strip().lower()

                  #if the player wants to give up
                  if ans == self.lang.langYes or ans == self.lang.langYesShort:
                     gameOver(self=self, otherPlayer=otherPlayer, otherCol=otherColor)
                     return False

                  #if the player doesn't want to give up
                  elif ans == self.lang.langNo or ans == self.lang.langNoShort:
                     break


            #if the player offers a draw
            elif nowPos == "drawoffer":
               print("")
               while True:
                  ans = input(self.lang.drawOfferMessage.format(otherPlayer, playerName)).strip().lower()

                  #if the other player denise
                  if ans == self.lang.langNo or ans == self.lang.langNoShort:
                     break

                  #if the other player accepts the draw
                  elif ans == self.lang.langYes or ans == self.lang.langYesShort:
                     gameOver(self=self)
                     return False


            #if the player wants to use the Fifty-move rule
            elif nowPos == "50move":
               #if it is a valid Fifty-move rule
               if self.fifty_move >= 50:
                  gameOver(self=self)
                  return False

               #if it is not a valid Fifty-move rule
               else:
                  print("\n" + self.lang.fiftyMoveError)
               
            
            #if it is a normal move
            else:
               pass

               nextPos = input(self.lang.toMessage).strip().lower()

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
                        print("\n{}".format(result))

                     #if there is no error with the step
                     else:
                        #return True to indicate the game is not over yet
                        return True
                  
               else:
                  print("\n" + self.invalidInput)

                  
      #This method deals with the next player
      def nextPlayer(self, playerName, playerColor, otherPlayer, otherColor):

         #Validating the king's color and setting up the kingX and kingY for checking
         if playerColor == "white":
            kingX = self.whiteKing["x"]
            kingY = self.whiteKing["y"] 
            col = self.lang.white
            otherCol = self.lang.black

         elif playerColor == "black":
            kingX = self.blackKing["x"]
            kingY = self.blackKing["y"] 
            col = self.lang.black
            otherCol = self.lang.white

         #if there is a check on the user's king
         if self.checkForCheck(kingX=kingX, kingY=kingY, col=playerColor, useCopyTable=False):
            
            #if it is checkmate
            if self.checkForCheckmate(kingX=kingX, kingY=kingY, col=playerColor):
               
               #using the gameOver function and return False to indicate the end of the game
               gameOver(self=self, player=playerName, col=playerColor, otherPlayer=otherPlayer, otherCol=otherCol)
               return False

            #if it's a normal check
            else:
               
               while True:

                  #creating the copyTable
                  self.copyTable = deepcopy(self.table)

                  #creating the copy of the fifty_move
                  self.copyFifty_move = self.fifty_move

                  #Printing the table
                  printTable(self=self)

                  #printing who's next and the special commands
                  print(self.lang.roundMessage.format(self.roundCount ,playerName, col))
                  print(self.lang.commandMessage)
                  
                  #letting the user know that his king is in a check position
                  print(self.lang.checkMessage)
                  result = askPlayer(self=self, playerName=playerName, playerColor=playerColor, otherPlayer=otherPlayer, otherColor=otherCol, useCopy=True)

                  #if the user gives up or the players agreed to a draw
                  if not result:
                     #return False to indicate the game is over
                     return False

                  else:
                     #making the copies of the king's position
                     #it is used for updating the king's finaly position
                     if playerColor == "white":
                        self.copyWhiteKing = self.whiteKing
                        kingX = self.copyWhiteKing["x"]
                        kingY = self.copyWhiteKing["y"]

                     elif playerColor == "black":
                        self.copyBlackKing = self.blackKing
                        kingX = self.copyBlackKing["x"]
                        kingY = self.copyBlackKing["y"]

                     #if the check is over
                     if not self.checkForCheck(kingX=kingX, kingY=kingY, col=playerColor, useCopyTable=True):
                        
                        #updating the king's final position
                        if playerColor == "white":
                           self.whiteKing["x"] = self.copyWhiteKing["x"]
                           self.whiteKing["y"] = self.copyWhiteKing["y"]
                           
                        elif playerColor == "black":
                           self.blackKing["x"] = self.copyBlackKing["x"]
                           self.blackKing["y"] = self.copyBlackKing["y"]

                        #updating the fifty_move variable
                        self.fifty_move = self.copyFifty_move

                        #updating the castling variables
                        if playerColor == "white":
                           self.whiteCastling = deepcopy(self.copyWhiteCastling)

                        elif playerColor == "black":
                           self.blackCastling = deepcopy(self.copyBlackCastling)

                        #updating the self.table
                        self.table = deepcopy(self.copyTable)
                        break
                  

               #return True to indicate the game is not over yet
               return True

                  
         
         #if there is no check on the user's king
         else:

            #Printing the table
            printTable(self=self)

            #printing who's next and the special commands
            print(self.lang.roundMessage.format(self.roundCount ,playerName, col))
            print(self.lang.commandMessage)

            #asking the user for an input
            result = askPlayer(self=self, playerName=playerName, playerColor=playerColor, otherPlayer=otherPlayer, otherColor=otherColor, useCopy=False)
            return result

      
      #until the end of the game
      while True:

         #This holds the item's indexes of the en_passant list which needs to be poped
         indexesToPop = list()

         #This loop checks if there is any item in the self.en_passant which needs to be poped
         for i in range(len(self.en_passant)):
            if self.en_passant[i]["expire"] <= self.roundCount:
               indexesToPop.append(i)
         
         #poping the expired items from self.en_passant
         else:
            for i in indexesToPop:
               self.en_passant.pop(i)

         #WHITE PLAYER
         #if this is the end of the game
         if not nextPlayer(self=self, playerName=self.players['player01'], playerColor=self.players['color01'], otherPlayer=self.players['player02'], otherColor=self.players['color02']):
            break

         #BLACK PLAYER
         #if this is the end of the game
         if not nextPlayer(self=self, playerName=self.players['player02'], playerColor=self.players['color02'], otherPlayer=self.players['player01'], otherColor=self.players['color01']):
            break

         #adding one to the fifty_move variable
         self.fifty_move += 1

         #adding one to the roundCount variable
         self.roundCount += 1



   #CheckForCheck method
   """
   This method checks if the user's king got an attack. The method returns:
    # This method is also used to check if any of the user's figure could take the king's checker down
    # The otherX and otherY variables are the positions of a condicional figure move [ optional ]

    * True  - if the king is in check or could be
    * False - if the king is safe 
   """
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
      for p in range(len(possibleKingMove)):

         #creating the copyTable
         self.copyTable = deepcopy(self.table)
         
         #creating the next possible positions
         nextX = possibleKingMove[p]["x"]
         nextY = possibleKingMove[p]["y"]

         #if the possible position is on the table
         if (nextX >= 1 and nextX <= 8) and (nextY >= 1 and nextY <= 8):
            
            #if the king could go that position
            if self.king_move(nowX=kingX, nowY=kingY, nextX=nextX, nextY=nextY, color=col, useCopyTable=True):

               #making the change to the copyTable
               self.alterTable(nowX=kingX, nowY=kingY, nextX=nextX, nextY=nextY, col=col, fig="king", useCopyTable=True)
            
               #if the king is safe with that move ==> the game is not over yet
               if not self.checkForCheck(kingX=nextX, kingY=nextY, col=col, useCopyTable=True):
                  del self.copyTable
                  return False


      #if the king could not get out from the check by itself
      else:

         #creating the copyTable
         self.copyTable = deepcopy(self.table)

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
            self.copyTable = deepcopy(self.table)

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
         if len(pos) == 2:
            return pos[0]
         else:
            return ""

      #If we want to get the FIGURE
      elif returnFig:
         if len(pos) == 2:
            return pos[1]
         else:
            return ""


   #mapNumberToX
   """
   This method maps the letter form position input to numbers.
   """
   def mapNumberToX(self, letter):
      abc = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8}
      for x, value in abc.items():
         if letter == x:
            return int(value)

   #mapNumberToY
   """
   This method maps the letter form position input to numbers.
   """
   def mapNumberToY(self, number):
      str(number)
      abc = {"8": 1, "7": 2, "6": 3, "5": 4, "4": 5, "3": 6, "2": 7, "1": 8}
      for y, value in abc.items():
         if number == y:
            return int(value)



   #This function alters the table if a move could go down
   """
   This method makes the change to the table / copyTable
   """
   def alterTable(self, nowX, nowY, nextX, nextY, col, fig, thirdX=False, thirdY=False, thirdPos="", fourthX=False, fourthY=False, fourthPos="", useCopyTable=False):
      
      #This gets the color of the next position
      otherCol = self.checkTable(x=nextX, y=nextY, returnCol=True, useCopyTable=useCopyTable)
      
      #if we want to use the copyTable
      if useCopyTable:
         if bool(thirdX) and bool(thirdY):
            self.copyTable[thirdY][thirdX] = thirdPos
            if bool(fourthX) and bool(fourthY):
               self.copyTable[fourthY][fourthX] = fourthPos

         self.copyTable[nowY][nowX] = ""
         self.copyTable[nextY][nextX] = col + "_" + fig

         #if the move is a kill it resets the copyFifty_move variable
         if otherCol != "" and otherCol != col:
            self.copyFifty_move = 0
      
      #if we want to use the table
      else:
         if bool(thirdX) and bool(thirdY):
            self.table[thirdY][thirdX] = thirdPos
            if bool(fourthX) and bool(fourthY):
               self.table[fourthY][fourthX] = fourthPos

         self.table[nowY][nowX] = ""
         self.table[nextY][nextX] = col + "_" + fig
         
         #if the move is a kill it resets the fifty_move variable
         if otherCol != "" and otherCol != col:
            self.fifty_move = 0




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
         nowX = self.mapNumberToX(a.group())
         nowY = self.mapNumberToY(b.group())
         nextX = self.mapNumberToX(c.group())
         nextY = self.mapNumberToY(d.group())

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

                  #if it is a 2 step forward move
                  if col == "black" and nextY == nowY + 2:
                     self.en_passant.append(dict(expire=self.roundCount+2, tableX=nextX, tableY=nextY, realX=nextX, realY=nextY-1, col=col))
                  
                  elif col == "white" and nextY == nowY - 2:
                     self.en_passant.append(dict(expire=self.roundCount+1, tableX=nextX, tableY=nextY, realX=nextX, realY=nextY+1, col=col))
                  
                  
                  #if the pawn is in a figure-switch position
                  elif self.pawnSwitch(nextY=nextY, col=col):
                     while True:
                        ans = input(self.lang.pawnSwitchMessage).strip().lower()
                        #translating the input to figures
                        if ans == self.lang.queen:
                           fig = "queen"
                           break
                        elif ans == self.lang.rook:
                           fig = "rook"
                           break
                        elif ans == self.lang.bishop:
                           fig = "bishop"
                           break
                        elif ans == self.lang.knight:
                           fig = "knight"
                           break
                        else:
                           print(self.lang.wrongFigure)

                  
                  #if the user wants to perform an en_passant kill
                  for i in range(len(self.en_passant)):
                     if nextX == self.en_passant[i]["realX"] and nextY == self.en_passant[i]["realY"] and col != self.en_passant[i]["col"]:
                        self.alterTable(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, thirdX=self.en_passant[i]["tableX"], thirdY=self.en_passant[i]["tableY"], thirdPos="", useCopyTable=useCopyTable)
                        return False


                  #it makes the change to the table
                  self.alterTable(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, useCopyTable=useCopyTable)

                  #it makes the reset of the fifty_move variable
                  #if the move was on the copyTable
                  if useCopyTable:
                     self.copyFifty_move = 0

                  #if the move was performed on the table
                  else:
                     self.fifty_move = 0

                  return False
               
               else:
                  return self.stepError
            
            #This method deals with the rook
            elif fig == "rook" and playerColor == col:
               if self.rook_move(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, color=col, useCopyTable=useCopyTable):
                  
                  #altering the table
                  self.alterTable(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, useCopyTable=useCopyTable)

                  #altering the blackCastling dictionary
                  if playerColor == "black":
                     if nowY == 1 and nowX == 1 and not self.blackCastling["leftRookMoved"]:
                        self.blackCastling["leftRookMoved"] = True

                     elif nowY == 1 and nowX == 8 and not self.blackCastling["rightRookMoved"]:
                        self.blackCastling["rightRookMoved"] = True

                  #altering the whiteCastling dictionary
                  elif playerColor == "white":
                     if nowY == 8 and nowX == 1 and not self.whiteCastling["leftRookMoved"]:
                        self.whiteCastling["leftRookMoved"] = True

                     elif nowY == 8 and nowX == 8 and not self.whiteCastling["rightRookMoved"]:
                        self.whiteCastling["rightRookMoved"] = True
                  
                  
                  #Updating the king's move
                  #if we use the copyTable
                  if useCopyTable:
                     if col == "black":
                        
                        #creating a copy of the blackCastling
                        self.copyBlackCastling = deepcopy(self.blackCastling)

                        if nowY == 1 and nowX == 1 and not self.copyBlackCastling["leftRookMoved"]:
                           self.copyBlackCastling["leftRookMoved"] = True

                        elif nowY == 1 and nowX == 8 and not self.copyBlackCastling["rightRookMoved"]:
                           self.copyBlackCastling["rightRookMoved"] = True


                     elif col  == "white":

                        #creating a copy of the whiteCastling
                        self.copyWhiteCastling = deepcopy(self.whiteCastling)
                        
                        if nowY == 8 and nowX == 1 and not self.copyWhiteCastling["leftRookMoved"]:
                           self.copyWhiteCastling["leftRookMoved"] = True

                        elif nowY == 8 and nowX == 8 and not self.copyWhiteCastling["rightRookMoved"]:
                           self.copyWhiteCastling["rightRookMoved"] = True
                        
                  
                  #if the we used the table
                  else:

                     if playerColor == "black":
                        if nowY == 1 and nowX == 1 and not self.blackCastling["leftRookMoved"]:
                           self.blackCastling["leftRookMoved"] = True

                        elif nowY == 1 and nowX == 8 and not self.blackCastling["rightRookMoved"]:
                           self.blackCastling["rightRookMoved"] = True

                     #altering the whiteCastling dictionary
                     elif playerColor == "white":
                        if nowY == 8 and nowX == 1 and not self.whiteCastling["leftRookMoved"]:
                           self.whiteCastling["leftRookMoved"] = True

                        elif nowY == 8 and nowX == 8 and not self.whiteCastling["rightRookMoved"]:
                           self.whiteCastling["rightRookMoved"] = True
                  

                  #finally return False to indicate no errors
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
                  
                  #if the move is a castling
                  if nextY == nowY and (nextX == nowX - 2 or nextX == nowX + 2) and useCopyTable == False:

                     #setting up the rook
                     thirdPos = col + "_rook"

                     #if the user's king goes left
                     if nextX == nowX - 2:
                        self.alterTable(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, thirdX=nowX-1, thirdY=nowY, thirdPos=thirdPos, fourthX=1, fourthY=nowY, fourthPos="")

                     #if the user's king goes right
                     if nextX == nowX + 2:
                        self.alterTable(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, thirdX=nowX+1, thirdY=nowY, thirdPos=thirdPos, fourthX=8, fourthY=nowY, fourthPos="")

                  
                  #if it's a normal step and the king is safe to step there
                  elif not self.checkForCheck(kingX=nextX, kingY=nextY, col=col, useCopyTable=useCopyTable):
                     self.alterTable(nowX=nowX, nowY=nowY, nextX=nextX, nextY=nextY, col=col, fig=fig, useCopyTable=useCopyTable)
                  

                  #if the king can't get there due to check occurrence
                  else:
                     return self.stepError


                  """
                  If everything went alright
                  """

                  #Updating the king's move
                  #if we use the copyTable
                  if useCopyTable:
                     if col == "black":
                        self.copyBlackCastling = deepcopy(self.blackCastling)
                        self.copyBlackCastling["kingMoved"] = True
                     elif col  == "white":
                        self.copyWhiteCastling = deepcopy(self.whiteCastling)
                        self.copyWhiteCastling["kingMoved"] = True
                  
                  #if the we used the table
                  else:
                     if col == "black":
                        self.blackCastling["kingMoved"] = True
                     elif col  == "white":
                        self.whiteCastling["kingMoved"] = True


                  #Update the king's position
                  #if the we used the copyTable
                  if useCopyTable:
                     if col == "black":
                        self.copyBlackKing["x"] = nextX
                        self.copyBlackKing["y"] = nextY
                     elif col  == "white":
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
               
               #if the king can't get there
               else:
                  return self.stepError
            
            #if we can't make any move (if the position is empty or it's got the wrong color)
            else:
               return self.stepError