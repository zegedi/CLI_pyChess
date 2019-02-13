from includes import main

#GAME BEGINING
"""
This is where the program all begins
"""

#This prints the entry message
mgGame = main.Main()

#This sets up the two players
mgGame.playerSetup()

#This method asks if the players want to start a new game
mgGame.newGame()