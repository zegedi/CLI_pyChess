from includes.gameRules import GameManadgement #This one import the GameManadgement class
import re #This one imports the re package

class Figures(GameManadgement):

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
      col = self.checkTable(self, x=nextX, y=nextY, returnCol=True, useCopyTable=useCopyTable)

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
               if self.checkTable(self, x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != "":
                  return False
               else:
                  y += 1
                  x -= 1
            if self.checkTable(self, x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != color:
               return True
            else:
               return False
         
         #move down and right
         elif nextY > nowY and nextX > nowX:
            y = nowY + 1
            x = nowX + 1
            while y != nextY and x != nextX:
               if self.checkTable(self, x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != "":
                  return False
               else:
                  y += 1
                  x += 1
            if self.checkTable(self, x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != color:
               return True
            else:
               return False
         
         #move up and left
         elif nextY < nowY and nextX < nowX:
            y = nowY - 1
            x = nowX - 1
            while y != nextY and x != nextX:
               if self.checkTable(self, x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != "":
                  return False
               else:
                  y -= 1
                  x -= 1
            if self.checkTable(self, x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != color:
               return True
            else:
               return False
         
         #move up and right
         elif nextY < nowY and nextX > nowX:
            y = nowY - 1
            x = nowX + 1
            while y != nextY and x != nextX:
               if self.checkTable(self, x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != "":
                  return False
               else:
                  y -= 1
                  x += 1
            if self.checkTable(self, x=x, y=y, returnCol=True, useCopyTable=useCopyTable) != color:
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
            if self.checkTable(self, x=nextX, y=nextY, returnCol=True, useCopyTable=useCopyTable) != color:
               return True
            else:
               return False
         else:
            return False

      #if the king wants to move up or down
      elif nextX == nowX:
         if nextY == nowY - 1 or nextY == nowY + 1:
            if self.checkTable(self, x=nextX, y=nextY, returnCol=True, useCopyTable=useCopyTable) != color:
               return True
            else:
               return False
         else:
            return False
      
      #if the move is invalid
      else:
         return False