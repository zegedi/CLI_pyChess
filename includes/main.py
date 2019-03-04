#!/usr/bin/env python3

from includes.gameRules import GameManadgement
from languages.languages import *
from random import randint
from pathlib import Path
import os

class Main(GameManadgement):

   #INTRO
   """
   This method prints the entry message and asks the player for a language
   """
   def __init__(self):

      #Printing the chess logo
      try:
         #creating tha path
         folder = os.path.dirname(os.path.abspath(__file__))
         myfile = "chess" + str(randint(1,5)) + ".txt"
         path = Path(folder, myfile)

         #opening the Chess ASCII Character files
         with open(path, "r", encoding="utf8") as f:
            print(f.read())
      except:
         print("\nCHESS by Viktor Egedi\n")


      #This list holds the available languages for the game
      availableLangs = ['magyar', 'english']

      #This will print all the available languages
      for i in availableLangs:
         print(" - {}".format(i.capitalize()))

      #This will set up the language of the program
      print("\nPlease select a language to use, from the list above!")
      while True:
         langChoise = input(" My choise: ").strip().lower()

         #if the user gave an input
         if langChoise != "":

            #if that input is in availableLangs
            if langChoise in availableLangs:
               self.langChoise = langChoise
               break

      #setting the language
      if langChoise == "magyar":
         self.lang = Hungarian()

      elif langChoise == "english":
         self.lang = English()
   

   #PLAYERSETUP
   """
   This method sets up the two players
   """
   def playerSetup(self):

      #This prints out the setup message
      print("\n\n")
      try:
         folder = os.path.dirname(os.path.abspath(__file__))
         path = Path(folder, "setup.txt")
         with open(path, "r", encoding="utf8") as f:
            print(f.read())
      except:
         print("PLAYER SETUP!")

      #This dict holds the name of the players and their colors
      self.players = dict(player01="", color01="white", player02="", color02="black")
      while True:
         if (self.players['player01'] == "" or self.players['player02'] == ""):
            print(self.lang.playerSetupMessage)
            self.players['player01'] = input(self.lang.playerSetupWhite).strip()
            self.players['player02'] = input(self.lang.playerSetupBlack).strip()
         else:
            break
      print(self.lang.playerSetupResult.format(self.players['player01'], self.players['player02']))

   #NEWGAME
   """
   This method asks the players if they want to play, and starts one up if it is needed
   """
   def newGame(self):

      #Printing the new game logo
      try:
         folder = os.path.dirname(os.path.abspath(__file__))
         path = Path(folder, "newgame.txt")
         with open(path, "r", encoding="utf8") as f:
            print(f.read())
      except:
         print("\nNEW GAME")

      print("\n\n")

      #Asking for a new game
      while True:
         while True:
            ans = input(self.lang.newGameMessage).strip().lower()
            if (ans != self.lang.langYes and ans != self.lang.langNo and ans != self.lang.langYesShort and ans != self.lang.langNoShort):
               pass
            else:
               break
         
         #if the players don't want to play
         if (ans == self.lang.langNo or ans == self.lang.langNoShort):
            print(self.lang.newGameNo)
            break
         
         #if the players want to play
         elif (ans == self.lang.langYes or ans == self.lang.langYesShort):
            #Then the games starts
            nwGame = GameManadgement(player01=self.players['player01'], player02=self.players['player02'], color01=self.players['color01'], color02=self.players['color02'], lang=self.langChoise)

            #if the game is finished we delete the mwGame
            del nwGame