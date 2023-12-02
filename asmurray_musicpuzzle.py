# -*- coding: utf-8 -*-
"""
Music Puzzle Game

Alexander Murray

background https://creator.nightcafe.studio/studio?open=creation&panelContext=%28jobId%3A3obwZPuQlAGD4ZVIlkUS%29
"""

import pygame, simpleGE, random

class Game(simpleGE.Scene):
    def __init__(self):
        simpleGE.Scene.__init__(self)
        self.background = pygame.image.load("organ1.jpg")
        self.background = pygame.transform.scale(self.background, (640, 480))
        self.setCaption("Music Puzzle")
        self.inputlen = 0
        
        self.addLabels()
        self.addButton()
        self.addMultiLabel()
        
        self.sprites = [self.lblTitle, self.multi, self.btnStart, self.btnKeyA, self.btnKeyB, self.btnKeyC, self.btnKeyD, self.btnKeyE, self.btnKeyF, self.btnKeyG, self.lblInput, self.lblHint, self.btnCheck, self.btnClear, self.lblAttempts, self.btnQuit]
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
        
    def addLabels(self):
        self.lblTitle = simpleGE.Label()
        self.lblTitle.text = "Music Puzzle"
        self.lblTitle.center = (320,40)
        self.lblTitle.size = (300, 30)
        
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
        self.btnStart.center = (320, 420)
        

        self.btnReset = simpleGE.Button()
        
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
        
        
        
    def update(self):
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
            self.lblAttempts.show ((540, 80))
            self.counter = 3
            self.lblAttempts.text = "Attempts: " + str(self.counter)
            #placePuzzle()
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
        if self.btnCheck.clicked:
            self.lblHint.show((320,130))
            if self.lblInput.text == placePuzzle.solutionKey:
                print("You win!")
                print(self.counter)
                print(self.lblInput.text)
                self.lblHint.text = "Congratulations! You win!"
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
            
            
class placePuzzle():
    keyList = ["A", "B", "C", "D", "E", "F", "G"]
    solution1 = random.sample(keyList, 4) 
    solutionKey = (f"{solution1[0]}{solution1[1]}{solution1[2]}{solution1[3]}")
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
    print(solutionKey)
    print(f"{solution1[1]} is not in last place.")
        
            
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
        
    
        
        
