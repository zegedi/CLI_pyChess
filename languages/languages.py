#!/usr/bin/env python3

#This class is for the Hungarian content
class Hungarian():

   #This function sets up all the language variables
   def __init__(self):

      #these are basic values which the program uses to operate
      self.langCode = "hu"
      self.langYes = "igen"
      self.langNo = "nem"

      #These values are used in the includes/main.py, playerSetup() function
      self.playerSetupMessage = "\n\n\nA játék megkezdéséhez regisztrálni kell a játékosokat!\n"
      self.playerSetupWhite = "Kérem adja meg a fehér játékos nevét: "
      self.playerSetupBlack = "Kérem adja meg a fekete játékos nevét: "
      self.playerSetupResult = "\nA játékosok: [{}] és [{}]\n\n"
      
      #These values are used in the includes/main.py, newGame0() function
      self.newGameMessage = "Szeretnének egy új játékot indítani? ([igen] vagy [nem]): "
      self.newGameNo = "\n\nRendben\nRemélem tetszett a kis játékom :)\nKészítette: Egedi Viktor © 2019"

      #These are the error messages used in includes/gameRules.py
      self.invalidInput = "  HIBA: érvénytelen pozíciót adott meg!"
      self.stepError = "  HIBA: nem lehet a megadott lépést elvégezni!"
      self.wrongFigure = "  HIBA: nincs ilyen figura az opciók között!"
      self.checkError = "  HIBA: királyod jelenleg sakkban van, meg kell szüntetned ezt az állapotot!"
      self.fiftyMoveError = "  HIBA: jelenleg nem tudsz élni az Ötven lépés szabállyal!"

      #These are the colors and the figure names for includes/gameRules.py
      self.white = "fehér"
      self.black = "fekete"
      self.pawn = "gyalog"
      self.rook = "bástya"
      self.bishop = "futó"
      self.knight = "huszár"
      self.queen = "vezér"
      self.king = "király"

      #These are the messages used in includes/gameRules.py
      self.checkmateMessage = "\nA győztes: {} (színe: {})\nGratulálunk a győzelemhez!\n"
      self.drawMessage = "\nA játszma eredménye döntetlen!\n"
      self.checkMessage = "\n Sakkot kaptál! Meg kell szüntetned ezt az állapotot!"
      self.roundMessage = "\n\n {}. KÖR:\n {} következik! ({}):"
      self.commandMessage = "\n Speciális parancsok: [giveup] - Játék feladása; [50move] - Ötven lépés szabálya; [drawoffer] - Döntetlen felajánlása"
      self.giveupMessage = " Biztos vagy benne, hogy feladod a játszmát? ([igen] vagy [nem]): "
      self.drawOfferMessage = " {}! {} felajánlotta a döntetlent. Elfogadod a azt? ([igen] vagy [nem]): "
      self.pawnSwitchMessage = " Mire cseréljem be a parasztot? [bástya, futó, huszár, vezér]: "
      self.fromMessage = "\n\n Te lépsz: "
      self.toMessage = " Hova: "



#This class is for the English content
class English():

   #This function sets up all the language variables
   def __init__(self):

      #these are basic values which the program uses to operate
      self.langCode = "en"
      self.langYes = "yes"
      self.langNo = "no"

      #These values are used in the includes/main.py, playerSetup() function
      self.playerSetupMessage = "\n\n\nBefore you start, you have to register the players!\n"
      self.playerSetupWhite = "Please, tell the name of the white player: "
      self.playerSetupBlack = "Please, tell the name of the black player: "
      self.playerSetupResult = "\nThe two players are: [{}] and [{}]\n\n"
      
      #These values are used in the includes/main.py, newGame0() function
      self.newGameMessage = "Would you like to start a new game? ([yes] or [no]): "
      self.newGameNo = "\n\nAll right.\nI hope you enjoyed my little creation :)\nCreator: Viktor Egedi © 2019"

      #These are the error messages used in includes/gameRules.py
      self.invalidInput = "  ERROR: you inserted an incorrect position!"
      self.stepError = "  ERROR: the given move could not be done!"
      self.wrongFigure = "  ERROR: there is no such figure in the options!"
      self.checkError = "  ERROR: your king is in a check position, you need to change this status!"
      self.fiftyMoveError = "  ERROR: your can not make use of the Fifty-move rule right now!"

      #These are the colors and the figure names for includes/gameRules.py
      self.white = "white"
      self.black = "black"
      self.pawn = "pawn"
      self.rook = "rook"
      self.bishop = "bishop"
      self.knight = "knight"
      self.queen = "queen"
      self.king = "king"

      #These are the messages used in includes/gameRules.py
      self.checkmateMessage = "\nWINNER: {} (color: {})\nCongratulations to your victory!\n"
      self.drawMessage = "\nThe final result is a draw!\n"
      self.checkMessage = "\n  Your king got checked! You need to change this status!"
      self.roundMessage = "\n\n {}. ROUND:\n {} is next! ({}):"
      self.commandMessage = "\n Special commands: [giveup] - To give up; [50move] - Fifty-move rule; [drawoffer] - Offer a draw"
      self.giveupMessage = " Are you sure you want to give up? ([yes] or [no]): "
      self.drawOfferMessage = " {}! {} offerd you a draw. Would you like ot accept it? ([yes] or [no]): "
      self.pawnSwitchMessage = " What figure should I replace the pawn with? [rook, bishop, knight, queen]: "
      self.fromMessage = "\n\n Your move: "
      self.toMessage = " Go to: "