from graphics import *
from random import *
from button3 import *
from MadLibClass import *
from RandomWord import *


def main():
    win=GraphWin("Mab Libs",1000,1000)
    
    intro=Text(Point(500,500),"Welcome to MAD LIBS!")
    intro.draw(win)
    
    win.getMouse()
    
    intro.undraw()
    instructions=Text(Point(500,100),"Please select the story you would like to create.")
    instructions.draw(win)
    
    story1=Button(win,Point(500,500),100,50,"Love Letter")
    story1.activate()

    Quit=Button(win,Point(900,100),50,50,"Quit")
    Quit.activate()
    
    pt=win.getMouse()


    if story1.clicked(pt)==True:
        instructions.undraw()
        Quit.undraw()
        story1.undraw()
        instructions2=Text(Point(500,300),"You can either enter what the field asks for and press Enter, or generate a random answer by pressing Random.\n Please click anywhere to continue.")
        instructions2.draw(win)
        pt=win.getMouse()
        instructions2.undraw()
        loveLetter=createMadLib(win,"LoveLetter.txt","LoveLetterWords.txt")
        loveLetter.getInput()
        loveLetter.makeStory()
    elif Quit.clicked(pt)==True:
        win.close()
    
    else:
        pt=win.getMouse()

main()
