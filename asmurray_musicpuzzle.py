# -*- coding: utf-8 -*-
"""
Music Puzzle Game

Alexander Murray

background https://creator.nightcafe.studio/studio?open=creation&panelContext=%28jobId%3A3obwZPuQlAGD4ZVIlkUS%29
"""

import pygame, simpleGE, random

class Game(simpleGE.Scene):
    solutionGuide = [""]
    solutionKey = ""
    simonKey = ""
    simonNum = 1
    def __init__(self):
        simpleGE.Scene.__init__(self)
        self.background = pygame.image.load("organ1.jpg")
        self.background = pygame.transform.scale(self.background, (640, 480))
        self.setCaption("Music Puzzle")
        self.inputlen = 0
        
        self.addLabels()
        self.addButton()
        self.addMultiLabel()
        
        self.sprites = [self.btnPuzzle, self.btnSimon, self.lblTitleSimon, self.multiSimon, self.lblTitle, self.multi, self.btnStart, self.btnStartSimon, self.btnKeyA, self.btnKeyB, self.btnKeyC, self.btnKeyD, self.btnKeyE, self.btnKeyF, self.btnKeyG, self.btnGreen, self.btnRed, self.btnYellow, self.btnBlue, self.lblInput, self.lblHint, self.btnCheck, self.btnSimonSolve, self.btnClear, self.btnClue, self.multiClue, self.btnClueHide, self.lblAttempts, self.btnReset, self.btnQuit]
        self.lblTitle.hide()
        self.btnStart.hide()
        self.multi.hide()
        self.lblInput.hide()
        self.btnKeyA.hide()
        self.btnKeyB.hide()
        self.btnKeyC.hide()
        self.btnKeyD.hide()
        self.btnKeyE.hide()
        self.btnKeyF.hide()
        self.btnKeyG.hide()
        self.btnQuit.hide()
        self.btnCheck.hide()
        self.btnClear.hide()
        self.lblHint.hide()
        self.lblAttempts.hide()
        self.btnClue.hide()
        self.multiClue.hide()
        self.btnClueHide.hide()
        self.btnReset.hide()
        self.btnStartSimon.hide()
        self.btnSimonSolve.hide()
        self.lblTitleSimon.hide()
        self.multiSimon.hide()
        self.btnGreen.hide()
        self.btnYellow.hide()
        self.btnBlue.hide()
        self.btnRed.hide()
    
        
    def addLabels(self):
        self.lblTitle = simpleGE.Label()
        self.lblTitle.text = "Music Puzzle"
        self.lblTitle.center = (320,40)
        self.lblTitle.size = (300, 30)
        
        self.lblTitleSimon = simpleGE.Label()
        self.lblTitleSimon.text = "Simon Says"
        self.lblTitleSimon.size = (300, 30)
        self.lblTitleSimon.center = (320, 40)
        
        self.lblInput = simpleGE.Label()
        self.lblInput.text = ""
        self.lblInput.center = (320,40)
        self.lblInput.size = (150,30)
        
        self.lblHint = simpleGE.Label()
        self.lblHint.text = ""
        self.lblHint.center = (320, 130)
        self.lblHint.size = (350, 30)
        
        self.lblAttempts = simpleGE.Label()
        self.lblAttempts.center = (500, 80)
        self.lblAttempts.size = (150, 30)
    
        
    def addButton(self):
        self.btnStart = simpleGE.Button()
        self.btnStart.text = "Start Game"
        self.btnStart.center = (320, 440)
        
        self.btnStartSimon = simpleGE.Button()
        self.btnStartSimon.text = "Start Game"
        self.btnStartSimon.center = (320,440)
        
        self.btnPuzzle = simpleGE.Button()
        self.btnPuzzle.text = "Puzzle Game"
        self.btnPuzzle.center = (320, 220)
        
        self.btnSimon = simpleGE.Button()
        self.btnSimon.text = "Simon Says"
        self.btnSimon.center = (320, 320)
        
        self.btnSimonSolve = simpleGE.Button()
        self.btnSimonSolve.text = "Solve"
        self.btnSimonSolve.center = (500, 30)
        

        self.btnReset = simpleGE.Button()
        self.btnReset.text = "New Game"
        self.btnReset.center = (320, 440)
        
        self.btnClue = simpleGE.Button()
        self.btnClue.text = "Clue"
        self.btnClue.center = (100, 440)
        
        self.btnClueHide = simpleGE.Button()
        self.btnClueHide.text = "Hide Clue"
        self.btnClue.center = (100, 440)
        
        self.btnClear = simpleGE.Button()
        self.btnClear.text = "Clear"
        self.btnClear.center = (100,30)

        self.btnCheck = simpleGE.Button()
        self.btnCheck.text = "Solve"
        self.btnCheck.center = (500,30)
        
        self.btnKeyA = simpleGE.Button()
        self.btnKeyA.text = "A"
        self.btnKeyA.center = (100, 240)
        self.btnKeyA.size = (50, 30)
        
        self.btnKeyB = simpleGE.Button()
        self.btnKeyB.text = "B"
        self.btnKeyB.center = (175, 240)
        self.btnKeyB.size = (50, 30)
        
        self.btnKeyC = simpleGE.Button()
        self.btnKeyC.text = "C"
        self.btnKeyC.center = (250, 240)
        self.btnKeyC.size = (50, 30)
        
        self.btnKeyD = simpleGE.Button()
        self.btnKeyD.text = "D"
        self.btnKeyD.center = (325, 240)
        self.btnKeyD.size = (50, 30)
        
        self.btnKeyE = simpleGE.Button()
        self.btnKeyE.text = "E"
        self.btnKeyE.center = (400, 240)
        self.btnKeyE.size = (50, 30)
        
        self.btnKeyF = simpleGE.Button()
        self.btnKeyF.text = "F"
        self.btnKeyF.center = (475, 240)
        self.btnKeyF.size = (50, 30)
        
        self.btnKeyG = simpleGE.Button()
        self.btnKeyG.text = "G"
        self.btnKeyG.center = (550, 240)
        self.btnKeyG.size = (50, 30)
        
        self.btnGreen = simpleGE.Button()
        self.btnGreen.text = "Green"
        self.btnGreen.size = (60, 40)
        self.btnGreen.center = (150 ,240)
        
        self.btnYellow = simpleGE.Button()
        self.btnYellow.text = "Yellow"
        self.btnYellow.size = (60, 40)
        self.btnYellow.center = (250, 240)
        
        self.btnBlue = simpleGE.Button()
        self.btnBlue.text = "Blue"
        self.btnBlue.size = (60, 40)
        self.btnBlue.center = (350, 240)
        
        self.btnRed = simpleGE.Button()
        self.btnRed.text = "Red"
        self.btnRed.size = (60, 40)
        self.btnRed.center = (450, 240)
        
        
        #self.btnKeys.itemSound = simpleGE.Sound("")
        
        self.btnQuit = simpleGE.Button()
        self.btnQuit.text = "Quit Game"
        self.btnQuit.center = (320, 420)
        
        
        
    def addMultiLabel(self):
        self.multi = simpleGE.MultiLabel()
        self.multi.textLines = [
            "Solve the music riddle",
            "Play the notes to add it to your answer",
            "Press the check button to compare it to the solution"
            ]
        self.multi.center = (325,245)
        self.multi.size = (550,300)
        
        self.multiSimon = simpleGE.MultiLabel()
        self.multiSimon.textLines = [
            "This is Simon Says",
            "Simon will play notes",
            "Match the notes",
            "See how long you can last"
            ]
        self.multiSimon.size = (550, 300)
        self.multiSimon.center = (325, 245)
        
        self.multiClue = simpleGE.MultiLabel()
        self.multiClue.center = (325, 245)
        self.multiClue.size = (550, 300)
        
    
    def createKey(self):
        keyList = ["A", "B", "C", "D", "E", "F", "G"]
        solution1 = random.sample(keyList, 4) 
        self.solutionKey = (f"{solution1[0]}{solution1[1]}{solution1[2]}{solution1[3]}")
        for i in range(len(solution1)):
            if solution1[i] == "A":
                solution1[i] = "Alex"
            if solution1[i] == "B":
                solution1[i] = "Beth"
            if solution1[i] == "C":
                solution1[i] = "Charlie"
            if solution1[i] == "D":
                solution1[i] = "Daniel"
            if solution1[i] == "E":
                solution1[i] = "Elaine"
            if solution1[i] == "F":
                solution1[i] = "Fred"
            if solution1[i] == "G":
                solution1[i] = "Gemma"
        print(solution1)
        print(self.solutionKey)
        self.solutionGuide = [
            f"{solution1[1]} is not in last place.",
            f"{solution1[2]} is beating {solution1[3]}",
            f"{solution1[2]} is losing to {solution1[0]}.",
            f"{solution1[0]} is beating {solution1[1]}.",
            f"{solution1[3]} is not winning."
            ]
        self.solutionGuide = random.sample(self.solutionGuide, 5)
        print(self.solutionGuide)
        
        
    def createSimon(self):
        simonList = ["G", "Y", "B", "R"]
        solution2 = random.choices(simonList, k = self.simonNum)
        self.simonKey = "".join(solution2)
        print(self.simonKey)
        
    

        
        
        
    def update(self):
        if self.btnPuzzle.clicked:
            self.lblTitle.show((320, 40))
            self.btnStart.show((320, 440))
            self.multi.show((325,245))
            self.btnPuzzle.hide()
            self.btnSimon.hide()
            
            
        if self.btnSimon.clicked:
            self.btnSimon.hide()
            self.btnPuzzle.hide()
            self.btnStartSimon.show((320, 440))
            self.lblTitleSimon.show((320, 40))
            self.multiSimon.show((325, 245))
            
        if self.btnStartSimon.clicked:
            self.btnSimon.hide()
            self.btnStartSimon.hide()
            self.multiSimon.hide()
            self.screen.blit(self.background, (0,0))
            self.btnQuit.show((540,440))
            self.lblInput.show((320,40))
            self.btnClear.show((100,40))
            self.btnSimonSolve.show((540,40))
            self.btnGreen.show((150 ,240))
            self.btnYellow.show((250 ,240))
            self.btnBlue.show((350 ,240))
            self.btnRed.show((450 ,240))
            self.createSimon()
            
        
        if self.btnStart.clicked:
            self.lblTitle.hide()
            self.btnStart.hide()
            self.multi.hide()
            self.screen.blit(self.background, (0,0))
            self.btnQuit.show((540,440))
            self.btnKeyA.show((100,240))
            self.btnKeyB.show((175,240))
            self.btnKeyC.show((250,240))
            self.btnKeyD.show((325,240))
            self.btnKeyE.show((400,240))
            self.btnKeyF.show((475,240))
            self.btnKeyG.show((550,240))
            self.lblInput.show((320,40))
            self.btnCheck.show((540,40))
            self.btnClear.show((100,40))
            self.lblAttempts.show((540, 80))
            self.btnClue.show((100, 440))
            self.counter = 3
            self.lblAttempts.text = "Attempts: " + str(self.counter)
            self.createKey()
            
            
            
        if self.inputlen < 4:
            if self.btnKeyA.clicked:
                #self.btnKeys.itemSound.play()
                self.lblInput.text += "A"
                self.inputlen += 1
            if self.btnKeyB.clicked:
                self.lblInput.text += "B"
                self.inputlen += 1
            if self.btnKeyC.clicked:
                self.lblInput.text += "C"
                self.inputlen += 1
            if self.btnKeyD.clicked:
                self.lblInput.text += "D"
                self.inputlen += 1
            if self.btnKeyE.clicked:
                self.lblInput.text += "E"
                self.inputlen += 1
            if self.btnKeyF.clicked:
                self.lblInput.text += "F"
                self.inputlen += 1
            if self.btnKeyG.clicked:
                self.lblInput.text += "G"
                self.inputlen += 1
                
        if self.btnReset.clicked:
            game = Game()
            game.start()
            
            
        if self.btnClear.clicked:
            self.lblHint.hide()
            self.lblInput.text = ""
            self.inputlen = 0
            
        if self.btnClue.clicked:
            self.multiClue.textLines = self.solutionGuide
            self.multiClue.show((325,245))
            self.btnClue.hide()
            self.btnClueHide.show((100, 440))
            
        if self.btnClueHide.clicked:
            self.multiClue.hide()
            self.btnClueHide.hide()
            self.btnClue.show((100,440))
            
        if self.btnSimonSolve.clicked:
            if self.lblInput.text == self.simonKey:
                self.simonNum += 1
                self.createKey()
            
        if self.btnCheck.clicked:
            self.lblHint.show((320,130))
            if self.lblInput.text == self.solutionKey:
                print("You win!")
                print(self.counter)
                print(self.lblInput.text)
                self.lblHint.text = "Congratulations! You win!"
                self.btnReset.show((320,440))
            elif self.counter == 0:
                print("You lose!")
                self.lblHint.text = "You lose. Try again."
            elif self.lblInput.text == "":
                self.lblHint.text = "No Input. Please try again"
            elif self.lblInput.text != "":
                self.counter -= 1
                self.lblAttempts.text = "Attempts: " + str(self.counter)
                self.inputlen = 0
                print(self.counter)
                print(self.lblInput.text)
                self.lblHint.text = "Incorrect Response. Try Again"
                
        if self.btnQuit.clicked:
            self.stop()
        

            
class PianoKeys(simpleGE.SuperSprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("")
        self.setSize()
        
        
        #self.setPosition(())
        #self.itemSound = simpleGE.Sound("")
        

def main():
    game = Game()
    game.start()
    
    
if __name__ == "__main__":
    main()
        
    
        
        

