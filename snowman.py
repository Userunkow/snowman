#---------------------------------------------------------
# Program: snowmanStarter.py
# Author: Atillah
# Date: Jan 6, 2022
# Description: This program allows the user to selec
#   from three different categories of puzzles.
#   Each puzzle incldes a clue to the answer.
#   denmination of change to be given
# Input: User try to guess the puzzle.
#---------------------------------------------------------
import pygame
pygame.init()
import random


##---------------------------------------
## initialize global variables/constants 
##---------------------------------------
BLACK = (0,0, 0)
WHITE = (255,255,255)
RED   = (255,0, 0)
GREEN = (0,255,0)
BLUE  = (0,0,255)
LIGHT_BLUE = (102,255,255)



btn_font = pygame.font.SysFont("arial", 20)
guess_font = pygame.font.SysFont("monospace", 24)
clue_font = pygame.font.SysFont("monospace", 16)


def spacedOut(afterstring):
    beforestring = ""
    for i in afterstring:
        beforestring += i+' '
    return beforestring
    
    
def clickBtn(mp,buttons):
    for i,xy in enumerate(buttons):
        a = mp[0] - xy[0]
        b = mp[1] - xy[1]
        c = (a**2 + b**2)**.5
        if c <=15:
            return i
    return -1


def loadSnowmanImages():
    smImages = []
    for imgNum in range(9):
        fileName = 'snowman' + str(imgNum) + '.png'
        smImages.append(pygame.image.load(fileName))
    return smImages


def loadPuzzles():
    puzzles = [[],[],[]]
    fi = open('puzzles.txt','r')
    for p in fi:
        puz=p.strip().split(',')
        catIndex = int(puz[0])-1
        puzzles[catIndex].append(puz[1:])
    fi.close()
    return puzzles


def getRandomPuzzle(cat,puzzles):
    print (len(puzzles[cat]))
    pIndex = random.randrange(0,len(puzzles[cat]))
    randomPuz = puzzles[cat][pIndex]
    return randomPuz


def initializeGuess(puzzle):
    guess = ''
    for c in puzzle:
        if c == ' ':
            guess += ' '
        else:
            guess += '_'
    return guess


def drawGuess():
    guessSurface = guess_font.render(spacedOut(guess),True,BLACK)
    x = (win.get_width() - guessSurface.get_width())//2
    win.blit(guessSurface, (x,270))
    clueSurface = clue_font.render(clue,True,BLACK)
    x = (win.get_width() - clueSurface.get_width())//2
    win.blit(clueSurface, (x,320))

    
def creatButtons():
    x = 98
    y = 400
    buttons = []
    for btn in range (26):
        buttons.append((x,y))
        x +=42
        if btn == 12:
            x = 98
            y +=42
    print (buttons)
    return buttons


def updateGuess(ltrGuess,guess,puzzle):
    newGuess = ''
    for i,ltr in enumerate(puzzle):
        if ltrGuess == ltr:
            newGuess += ltr
        else:
            newGuess += guess[i]
    return newGuess


catButons = [[(56,200,190,80), 'T.V. Shows'],
             [(271,200,190,80),'Famous Landmarks'],
             [(486,200,190,80),'Famous Canadians']]


def drawCatagoryButtons(catButtons):
    for b in catButtons:
        bRec = b[0]
        bText = b[1]
        pygame.draw.rect(win,BLUE,b[0],0)
        pygame.draw.rect(win,RED,b[0],3)
        bTextSurface = btn_font.render(bText,True,WHITE)
        x = bRec[0] + (bRec[2]-bTextSurface.get_width())//2
        y = bRec[1] + (bRec[3]-bTextSurface.get_height())//2
        win.blit(bTextSurface,(x,y))  


def catBtnClick (mp,buttons):
    for i,b in enumerate (buttons):
        if pygame.Rect (b[0]).collidepoint(mp):
            return i
    return -l


def drawButtons(buttons):
    for i,xy in enumerate (buttons):
        pygame.draw.circle(win,LIGHT_BLUE,xy,15,0)
        pygame.draw.circle(win,BLACK,xy,15,1)
        ltrToRender = chr(i+65)
        ltrSurface = btn_font.render(ltrToRender,True,BLACK)
        win.blit(ltrSurface,(xy[0]-ltrSurface.get_width()//2,xy[1]-ltrSurface.get_height()//2))



#---------------------------------------#
# function that redraws all objects     #
#---------------------------------------#
def redraw_game_window():
    win.fill(GREEN)
    if currentScreen == CATEGORY_SCREEN:
        drawCatagoryButtons(catButons)
    else:
         
        # code to draw things goes here
        drawButtons(buttons)
        win.blit(smImages[wrongCount],(175,15))
        drawGuess()
        if won:
            win.blit(wonSurface,(25,130))
        elif lost:
            win.blit(lostSurface,(25,140))
    pygame.display.update()

    

    
#---------------------------------------#
# the main program begins here          #
#---------------------------------------#
wonSurface = guess_font.render("YOU WIN", True,BLACK)
lostSurface = guess_font.render("YOU LOST!", True,BLACK)
won = False
lost = False
CATEGORY_SCREEN = 0
GAME_SCREEN = 1
currentScreen = CATEGORY_SCREEN
win=pygame.display.set_mode((700,480))
buttons = creatButtons()
wrongCount = 0
smImages = loadSnowmanImages()
puzzles = loadPuzzles()
##cat = int(input('Enter category: '))
##randompuzz = getRandomPuzzle(cat, puzzles)
##puzzle = randompuzz[0]
##clue = randompuzz[1]
##guess = initializeGuess(puzzle)
##print (puzzle)
##print (clue)
inPlay = True
while inPlay:
    redraw_game_window()                           # window must be constantly redrawn - animation
    pygame.time.delay(10)                          # pause for 10 miliseconds
    
    for event in pygame.event.get():               # check for any events
        if event.type == pygame.QUIT:              # if user clicks on the window's 'X' button
            inPlay = False                         # exit from the game
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                inPlay = False                     # exit from the game
        if event.type == pygame.MOUSEBUTTONDOWN:   # if user clicks anywhere on win
            clickPos = pygame.mouse.get_pos()
            bIndex = clickBtn(clickPos,
                              buttons)
            print('You clicked on :', chr(bIndex+65))
            if bIndex!=-1:
                letterguess = chr(bIndex+65)
                if letterguess in puzzle:
                    guess = updateGuess(letterguess, guess,puzzle)
                    if guess == puzzle:
                        won = True
                else:
                    wrongCount +=1

                    if wrongCount == 8:

                      lost = True
                     
                    
                    
                       

                    
                    

while True:
    pCat = int(input('Enter Category:' ))
    rndIndex = random.randrange(0,2)
    rndPuzzle = puzzles[pCat][rndIndex]
    print('Puzzle:', rndPuzzle[0])
    print('Clue:', rndPuzzle[1])




#---------------------------------------#                                        
pygame.quit()   # always quit pygame when done!



